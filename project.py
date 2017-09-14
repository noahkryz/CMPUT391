#CMPUT 391 - Project #1
#Due Date: October 9, 2017
#Noah Kryzanowski


#Different Cases for storing the values in the database
#Case #1: Node Extraction
#---node (id integer, lat float, lon float)---
#	From <node , extract:
#		id=""
#		lat=""
#		lon=""
#	Each node begins with <node, followed by the data, ending with />
#---WE NEED TO STORE THE <tag/> DATA AS WELL. SEE CASE #3.

#
#
#
#
#
#
#

#Case #3: Tag Extraction (Node and Way)
#---nodetag (id integer, k text, v text)
#---waytag  (id integer, k text, v text)
#	From <tag , extract:
#		id=""
#		k=""
#		v=""
#	Each tag is nested in either <node (CASE #1) or <way (CASE #2)
#	Each tag begins with <tag, followed by the data, ending with />


import xml.etree.ElementTree as ET
#tree = ET.parse('edmonton.osm')
#root = tree.getroot()

#for node in root.iter('node'):
	



def main():
	#---HARDCODED FILE NAME---		
	inputFile = 'edmonton.osm'
	tree = ET.parse(inputFile)
	root = tree.getroot()

	for node in root.iter('node'):
		print(node.id)

#	print('\nThe file "' + inputFile + '" was opened successfully\n')

	
main()