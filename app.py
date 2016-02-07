import jsontree
path = 'testBookmarks'

f = open(path)

data = jsontree.loads(f.read())

testdata1 = data["roots"]["bookmark_bar"]

print type(testdata1["children"])
'''
for item in testdata1["children"]:
	#print type(item)
	type = item['type']
	if type == 'folder':
		print "its a folder with name : ",item['name']
		print "the folder contents are - \n"
		for each in item["children"]:
			print each['type']
'''
#print testdata1

#print dir(testdata1["children"][0])

#print jsontree.dumps(testdata1, indent=4)

def parser(data, depth, path):
	print "CURRENT PATH = ", path
	for item in data["children"]:	# check for all the item in booknark bar
		type = item['type']
		if type == 'folder':      # if a folder is found do folder job
			depth = depth + 1
			path = path + item['name'] + '\\'
			print depth*'-'+"Found a sub-folder with name : ",item['name']
			print depth*' '+"-------------------------------"
			size = len(item["children"])
			print depth*'-'+"the size of folder is - ", size
			for each in range(0,size):
				if item["children"][each]["type"] == 'folder':
					path = path + item["children"][each]["name"] + '\\'
					
					#parser(item["children"][each],depth, path)
					parser(item["children"][each],depth, path)
					print depth*'-'+"Name of Folder :- " , item["children"][each]["name"]
					
				elif item["children"][each]["type"] == 'url':
					print depth*'-'+"URL :- " , item["children"][each]["url"]
			
		elif type == 'url':
			depth = depth - 1
			path = path + item['name'] + '\\'
			print depth*'-'+"URL :- ", item['url']

depth = 1	
path = u'\\'		
parser(testdata1, depth, path)
