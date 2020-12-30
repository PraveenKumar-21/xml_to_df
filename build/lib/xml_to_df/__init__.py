__version__ = "0.0.3"

import xml.etree.ElementTree as ET
import pandas as pd


def attribute_add(el, temp2):
    attrib_l = list(el.attrib)
    for att in attrib_l:
        temp2[att] = el.attrib[att]
    return


def element_loop(element_l, temp1):
    """Input:
            element_list
            sample_dictionary_variable to write the output to
        Output:
            dictionary"""
    for el in element_l:
        el_tag = []
        nested_l = list(el)
        attribute_add(el, temp1)

        if len(nested_l) == 0:
            if el.tag in temp1.keys():
                if isinstance(temp1[el.tag], list):
                    temp1[el.tag].append(el.text)
                else:
                    el_tag = []
                    el_tag.extend([temp1[el.tag], el.text])
                    temp1[el.tag] = el_tag
            else:
                temp1[el.tag] = el.text
        elif len(nested_l) > 0:
            element_loop(el, temp1)

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
        attribute_add(ri, temp)
        element_l = list(ri)
        full_data.append(element_loop(element_l, temp))
    df = pd.DataFrame(full_data)
    return df
