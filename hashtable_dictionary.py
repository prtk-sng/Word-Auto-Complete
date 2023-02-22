from typing import List
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        global dic
        dic = {}
        for i in range(len(words_frequencies)):
           dic[words_frequencies[i].word] =  words_frequencies[i].frequency

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        if word in dic.keys():
            return dic[word]
        else:
            return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        if word_frequency.word not in dic.keys():
            dic[word_frequency.word] =  word_frequency.frequency
            return True
        else:
            return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        if word in dic.keys():
            del dic[word]
            return True
        else:
            return False

    def autocomplete(self, word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        words = list(dic.keys())
        freq = list(dic.values())
        suggestions = []
        suggestions_frequency = []
        top3_suggestions = []
        for i in range(len(words)):
            if words[i].startswith(word):
                suggestions.append(WordFrequency(words[i],freq[i]))
                suggestions_frequency.append(freq[i])

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
