from lxml import etree

tree = etree.parse('warcraft_shorten.xml')
root = tree.getroot()
clear = tree
for link in clear.findall('//a'):
    if link.tail != None: link.getparent().text += link.tail
    link.getparent().remove(link)
for section in clear.getroot()[0]:
    print section[0][0].text, section[0][1].text
    for subsection in section[1:]:
        print subsection[0][0].text
        for each in subsection[1:]:
            print each.text
print etree.tostring(clear, pretty_print = 'True', encoding = 'utf-8')