import jsontree


def getType(node):
	if node['type'] == 'folder':
		return 'folder'
	elif node['type'] == 'url':
		return 'url'
	else:	
		return -1

def getInfo(node, *arg):
	info = []
	
	if len(arg) > 1:
		for i in arg:
			info.append(node[i])
	elif len(arg) == 1:	
		return node[arg[0]]
	return info

		
def getChildren(node):
	for items in node["children"]:
		if getType(items) == 'url':
			print "URL- ", getInfo(items, 'url', 'date_added')
		elif getType(items) == 'folder':
			print "Folder Found: ",getInfo(items, 'name')
			for each in items["children"]:
				getChildren(each)
	

		
if __name__ == "__main__":
	path = '/home/abhishek/Misc/Abhishek/scripts/BookMarkX/testBookmarks'
	f = open(path)
	data = jsontree.loads(f.read())
	testdata1 = data["roots"]["bookmark_bar"]
	
	getChildren(testdata1)