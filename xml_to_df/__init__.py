__version__ = "0.0.6"

import xml.etree.ElementTree as ET
import pandas as pd


def attribute_add(el, temp2, tag):
    attrib_l = list(el.attrib)
    for att in attrib_l:
        cur_tag_att = tag + '_' + att
        if cur_tag_att in temp2.keys():
            if isinstance(temp2[cur_tag_att], list):
                temp2[cur_tag_att].append(el.attrib[att])
            else:
                el_att_list = []
                el_att_list.extend([temp2[cur_tag_att], el.attrib[att]])
                temp2[cur_tag_att] = el_att_list
        else:
            temp2[cur_tag_att] = el.attrib[att]
    return


def element_loop(element_l, temp1, tag):
    """Input:
            element_list
            sample_dictionary_variable to write the output to
            current xml element tag
        Output:
            dictionary"""
    for el in element_l:
        el_tag = []
        nested_l = list(el)
        new_tag = tag + '_' + el.tag

        attribute_add(el, temp1, new_tag)
        if len(nested_l) == 0:
            if el.text is not None:
                if new_tag in temp1.keys():
                    if isinstance(temp1[new_tag], list):
                        temp1[new_tag].append(el.text)
                    else:
                        el_tag_list = []
                        el_tag_list.extend([temp1[new_tag], el.text])
                        temp1[new_tag] = el_tag_list
                else:
                    temp1[new_tag] = el.text
        elif len(nested_l) > 0:
            element_loop(el, temp1, new_tag)

    return temp1


def convert_xml_to_df(xml_file):
    """Input: XML file
        Output:
        A pandas dataframe with nested xml elements flattened out to individual columns"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    full_data = []
    for ri in root:
        temp = {}
        attribute_add(ri, temp, ri.tag)
        element_l = list(ri)
        full_data.append(element_loop(element_l, temp, ri.tag))
    df = pd.DataFrame(full_data)
    return df
