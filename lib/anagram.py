# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted([letter for letter in word])
    def match(self, available_anagram):
        match_available_anagram=[]     

        for word in available_anagram:
            if sorted([letter for letter in word]) ==self.word:
               match_available_anagram.append(word)
        return match_available_anagram       