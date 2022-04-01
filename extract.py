from xml.dom.minidom import parse
import xml.dom.minidom

xml_file = r'sitemap.xml'

DOMTree = xml.dom.minidom.parse(xml_file)
root_node = DOMTree.documentElement
loc_nodes = root_node.getElementsByTagName("loc")
for loc in loc_nodes:
	print(loc.childNodes[0].data)
