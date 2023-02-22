from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node
from typing import List


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    def __init__(self):
        self.root = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for x in words_frequencies:
            self.add_word_frequency(x)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        return_value = self.search_node(word, self.root)
        if return_value:
            return return_value.frequency
        else:
            return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        return_value = False
        self.root = self.add_node(word_frequency.word,word_frequency.frequency, self.root)
        if(self.root):
            return_value = True
        return return_value

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        self.root = self.delete_node(word, self.root)
        if self.delete_node(word, self.root):
            return True
        else:
            return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        num_of_output = 3
        return_list: WordFrequency = []
        initial_list = self.autocomplete_node(word)
        word_list = []

        if initial_list:
            for x in initial_list:
                word_list.append(word + x)
            for y in word_list:
                temp_word = self.search_node(y, self.root)
                temp_freq = temp_word.frequency
                return_list.append(WordFrequency(y, temp_freq))

            return_list.sort(key = lambda x: x.frequency, reverse = True)

            if len(return_list) < 3:
                num_of_output = len(return_list)
            return_list = return_list[:num_of_output]
        return return_list

    def add_node(self, word: str, freq: int, node: Node) -> Node:
        if not node:
            node = Node(word[0])

        if word[0] == node.letter:
            if len(word[1:]) == 0:
                node.frequency = freq
                node.end_word = True
            else:
                node.middle = self.add_node(word[1:], freq, node.middle)
        elif word[0] < node.letter:
            node.left = self.add_node(word, freq, node.left)
        elif word[0] > node.letter:
            node.right = self.add_node(word, freq, node.right)
        #print(node.letter)
        return node

    # recursively traverses through the tree and returns the found node
    def search_node(self, word: str, node: Node) -> Node:
        if not node:
            return None

        # if word's first letter is found, it traverses down the middle to search for the rest of the word
        if word[0] == node.letter:
            if len(word[1:]) == 0:
                return node
            else:
                return self.search_node(word[1:] , node.middle)
        # traverse left tree
        elif word[0] < node.letter:
            return self.search_node(word, node.left)
        # traverse right tree
        elif word[0] > node.letter:
            return self.search_node(word, node.right)

    # returns 0 if no, 1 if yes
    def num_of_node_child(self, node: Node) -> int:
        count = 0
        if node.middle:
            count += 1
        if node.left:
            count += 1
        if node.right:
            count += 1
        # print(count)
        return count

    # returns the nodes of the word with no frequency/end_word
    def delete_node(self, word: str, node: Node) -> Node:
        if node:
            num_child_nodes = self.num_of_node_child(node)

            if word[0] == node.letter:
                if len(word[1:]) == 0:
                    if num_child_nodes > 0:
                        node.frequency = None
                        node.end_word = False
                    else:
                        return None
                else:
                    node.middle = self.delete_node(word[1:], node.middle)
            elif word[0] < node.letter:
                node.left = self.delete_node(word, node.left)
            elif word[0] > node.letter:
                node.right = self.delete_node(word, node.right)

            remaining_child_nodes = self.num_of_node_child(node)

            if not node.end_word and num_child_nodes == 1 and num_child_nodes != remaining_child_nodes:
                return None
            else:
                return node
        else:
            return None

    # note: 'yield' is like 'return' but returns a generator object instead of just a value
    def get_auto_complete_words(self, node: Node):
        if node:
            if node.middle:
                for letters in self.get_auto_complete_words(node.middle):
                    #print(letters)
                    yield(node.letter + letters)
            if node.left:
                for letters in self.get_auto_complete_words(node.left):
                    # print(letters)
                    yield(letters)
            if node.right:
                for letters in self.get_auto_complete_words(node.right):
                    # print(letters)
                    yield(letters)

            if node.end_word:
                # print('end')
                yield(node.letter)

    # uses the search function to get to the end node of the word
    def autocomplete_node(self, word: str) -> []:
        searched_node = self.search_node(word, self.root)
        if searched_node:
            return self.get_auto_complete_words(searched_node.middle)
        else:
            return []