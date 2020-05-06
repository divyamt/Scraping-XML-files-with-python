import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Aditya</name>
  <phone type = 'intl'>3445432223</phone>
  <email hide = "yes"/>
  <name>
</person>
'''
tree = ET.fromstring(data)


print("Name: ",tree.find('name').text)
print("Number:",tree.find('phone').text)
print("Attr: ",tree.find('email').get('hide'))
