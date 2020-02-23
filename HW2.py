# Some code below was taken from:
# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/

class treeNode():
	def __init__(self): 
		
		# Initialising one node for tree 
		self.children = {} 
		self.last = False

class tree(): 
	def __init__(self): 
		
		# Initialising the tree structure. 
		self.root = treeNode() 
		self.word_list = [] 

	def formtree(self, keys): 
		
		# Forms a tree structure with the given set of strings 
		# if it does not exists already else it merges the key 
		# into it by extending the structure as required 
		for key in keys: 
			self.insert(key) # inserting one key to the tree. 

	def insert(self, key): 
		
		# Inserts a key into tree if it does not exist already. 
		# And if the key is a prefix of the tree node, just 
		# marks it as leaf node. 
		node = self.root 

		for a in list(key): 
			if not node.children.get(a): 
				node.children[a] = treeNode() 

			node = node.children[a] 

		node.last = True

	def search(self, key): 
		
		# Searches the given key in tree for a full match 
		# and returns True on success else returns False. 
		node = self.root 
		found = True

		for a in list(key): 
			if not node.children.get(a): 
				found = False
				break

			node = node.children[a] 

		return node and node.last and found 

	def suggestionsRec(self, node, word): 
		
		#recursively traverse the tree and return whole word
		if node.last: 
			self.word_list.append(word) 

		for a,n in node.children.items(): 
			self.suggestionsRec(n, word + a)

	def printAutoSuggestions(self, key): 
		
		# Returns all the words in the tree whose common 
		# prefix is the given key thus listing out all 
		# the suggestions for autocomplete. 
		node = self.root 
		not_found = False
		temp_word = '' 

		for a in list(key): 
			if not node.children.get(a): 
				not_found = True
				break

			temp_word += a 
			node = node.children[a] 

		if not_found: 
			return 0
		elif node.last and not node.children: 
			return -1

		self.suggestionsRec(node, temp_word) 

		for s in self.word_list: 
			if s.length == key.length() + 1:
				print(s)
		return 1

# Driver Code 
# keys = ["hel", "hell", "hi", "he", "cat", "ca", "hello", "high"]
filename = open("words.txt", "r")
keys = []
for line in filename:
	keys.append(line)
filename.close()

key = input("Search word: ") # key for autocomplete suggestions. 

# creating tree 
t = tree() 

# creating the tree structure 
t.formtree(keys) 

# autocompleting the given key using tree structure. 
comp = t.printAutoSuggestions(key) 

if comp == -1: 
	print("No other strings found with this prefix\n") 
elif comp == 0: 
	print("No string found with this prefix\n") 

