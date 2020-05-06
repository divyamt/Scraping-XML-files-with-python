import xml.etree.ElementTree as ET

data = '''<stuff>
<persons>
    <person>
      <name>Divyam</name>
      <phone>8923440123</phone>
      <email hide = "yes"/>
    </person>
    <person>  
      <name>Ujju</name>
      <phone>8932222142</phone>
      <email hide = "no"/>
    </person>
    <person> 
    <name>Shanky</name>
      <phone>9938987642</phone>
      <email hide = "no"/>
    </person>
    <person>
      <name>smith</name>
      <phone>032330033000</phone>
      <email hide = "no"/>
    </person>
    <person>
      <name>Sheldon</name>
      <phone>1323233234323</phone>
      <email hide = "no"/>
    </person>
  </persons>
</stuff>
'''

tree = ET.fromstring(data)
lst = tree.findall('persons/person')
for item in lst:
  print("Name:",item.find('name').text)
  print("Phone:",item.find('phone').text)
  print("Attribute",item.find('email').get('hide'))
  print("\n")
