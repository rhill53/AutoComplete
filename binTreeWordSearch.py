# Some code below was taken from:
# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/


class TreeNode:
	def __init__(self): 
		
		# Initialising one node for tree 
		self.children = {} 
		self.last = False


class Tree:
	def __init__(self): 
		
		# Initialising the tree structure. 
		self.root = TreeNode()
		self.word_list = [] 

	def form_tree(self, keys):
		
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
				node.children[a] = TreeNode()

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

	def suggestions_rec(self, node, word):
		
		# recursively traverse the tree and return whole word
		if node.last: 
			self.word_list.append(word) 

		for a, n in node.children.items():
			self.suggestions_rec(n, word + a)

	def auto_suggestions(self, key):

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

		self.suggestions_rec(node, temp_word)

		return 1
