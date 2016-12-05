from lxml import etree
import json

tree = etree.parse('warcraft_shorten.xml')
root = tree.getroot()
clear = tree
for link in clear.findall('//a'):
    if link.tail != None: link.getparent().text += link.tail
    link.getparent().remove(link)


#print etree.tostring(clear, pretty_print = 'True', encoding = 'utf-8')

dumpdata = []
pk = 1
for section in clear.getroot()[0]:
    chapter = section[0][0].text #section[0][1].text
    for subsection in section[1:]:
        stringNum = subsection[0][0].text
        stringText = ''
        for each in subsection[1:]:
            stringText += each.text
        dumpdata.append({
            "model":"inliner.Quote",
            "pk":pk,
            "fields":
                {
                    "text":stringText,
                    "chapternum":chapter[:-1],
                    "stringnum":stringNum[:-1],
                }
        })
        pk += 1

target = open('fixtures/datata.json', 'w')
target.write(json.dumps(dumpdata))
target.close()