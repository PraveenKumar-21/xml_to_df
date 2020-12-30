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

category |	lang |	title |	author |	year |	price |	language |	cricketer1 |	cricketer2 |	country
-------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
COOKING |	en |	Everyday Italian |	Giada De Laurentiis |	2005 |	30.00 |	NaN |	NaN |	NaN |	NaN
CHILDREN |	en |	Harry Potter |	J K. Rowling |	2005 |	29.99 |	hello	| Praveen |	Pathan |	[india, india1]
WEB |	en |	Learning XML |	Erik T. Ray |	2003 |	39.95 |	NaN |	NaN |	NaN |	NaN
