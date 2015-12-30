_end = '_end_'

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            if letter not in current_dict:
            	current_dict[letter] = {}
            current_dict = current_dict[letter]
        current_dict[_end] = _end
    return root

def print_trie(root, current_word, lex):
	if _end in root:
		print current_word
	for letter in lex:
		if letter in root:
			print_trie(root[letter], current_word+letter, lex)

def lex_sorting(words, lex):
	root = make_trie(words)
	print_trie(root, "", lex)

lex_sorting(["aaa","aa",""], "a")
