class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix): 
        # Check if any word starts with the given prefix

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def suggest(self, prefix):
        suggestions = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return suggestions  # No suggestions if prefix not found
            node = node.children[char]
        self._find_words(node, prefix, suggestions)
        return suggestions

    def _find_words(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._find_words(child_node, prefix + char, suggestions)
