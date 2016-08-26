from lxml import etree as ET
tree = ET.parse('xml.txt')
root = tree.getroot()
print root.tag
print([ c.tag for c in root ])
# print [c.tag for c in questions]
# print(ET.tostring(questions, pretty_print=True))
print (ET.tostring(root.find("QUESTIONLIST"),pretty_print=True))
questionList = root.find("QUESTIONLIST")
print [c.attrib for c in questionList]

print (ET.tostring(root.xpath("//QUESTION_MULTIPLECHOICE[@id='q1']")[0]
,pretty_print=True))
print root.xpath("//QUESTION_MULTIPLECHOICE[@id='q1']")