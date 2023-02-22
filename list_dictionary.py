import time
from typing import List
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        global word_list, freq_list
        word_list = []
        freq_list = []
        for i in range(len(words_frequencies)):
           word_list.append(words_frequencies[i].word)
           freq_list.append(words_frequencies[i].frequency)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # place holder for return

        if word in word_list:
            return freq_list[word_list.index(word)]
        else:
            return 0
        

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        if word_frequency.word not in word_list:
            word_list.append(word_frequency.word)
            freq_list.append(word_frequency.frequency)
            return True
        else:
            return False

        
    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return

        if word in word_list:
            freq_list.remove(freq_list[word_list.index(word)])
            word_list.remove(word)
            return True
        else:
            return False
        

    def autocomplete(self, prefix_word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        # words = list(dic.keys())
        # freq = list(dic.values())
        suggestions = []
        suggestions_frequency = []
        top3_suggestions = []
        for i in range(len(word_list)):
            if word_list[i].startswith(prefix_word):
                suggestions.append(WordFrequency(word_list[i],freq_list[i]))
                suggestions_frequency.append(freq_list[i])

        if suggestions_frequency == []:
            pass

        else:
            sorted_frequency = sorted(suggestions_frequency, reverse=True)
            if len(sorted_frequency) < 3 :
                for i in range(len(sorted_frequency)):
                    top3_suggestions.append(suggestions[suggestions_frequency.index(sorted_frequency[i])]) 
            
            else:
                for i in range(3):
                    top3_suggestions.append(suggestions[suggestions_frequency.index(sorted_frequency[i])]) 
        
        return top3_suggestions  

            
