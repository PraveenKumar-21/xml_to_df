# XML to Pandas Dataframe
## Flattens out nested xml to individual columns in dataframe

###### Sample input.xml
```
<bookstore>
<book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
    <values>
      <value id="300">1</value>
      <value id="100">5</value>
      <value id="200">2</value>
    </values>
  </book>
  <book category="CHILDREN">
    <title lang="en" language="hello">Harry Potter</title>
    <author>J K. Rowling</author>
    <cricketers>
        <cricketer1>Praveen</cricketer1>
        <cricketer2>Pathan</cricketer2>
        <country>india</country>
        <country>india1</country>
      </cricketers>
    <year>2005</year>
    <price>29.99</price>
    <values>
      <value></value>
      <value></value>
    </values>
  </book>
  <book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>

```
### df = xml_to_df.convert_xml_to_df("input.xml")
### df.head()
###### Output dataframe

book_category | book_title_lang | book_title | book_author | book_year | book_price | book_values_value_id | book_values_value | book_title_language | book_cricketers_cricketer1 | book_cricketers_cricketer2 | book_cricketers_country
-------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |-------- | --------
COOKING | en | Everyday Italian | Giada De Laurentiis | 2005 | 30.00 | [300, 100, 200] | [1, 5, 2] | NaN | NaN | NaN | NaN
CHILDREN | en | Harry Potter | J K. Rowling | 2005 | 29.99 | NaN | NaN | hello | Praveen | Pathan | [india, india1]
WEB | en | Learning XML | Erik T. Ray | 2003 | 39.95 | NaN | NaN | NaN | NaN | NaN | NaN