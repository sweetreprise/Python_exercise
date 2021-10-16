from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("/words.txt")
    235886 words read
    
    
    """

    def __init__(self, path):
        """reads file and prints out number of words read"""
        my_file = open(path)
        self.words = self.read_file(my_file)

        print(f"{len(self.words)} words read")

    def read_file(self, my_file):
        """reads all the words in the file"""
        return [word.strip() for word in my_file]

    def random(self):
        """returns random word from file"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """a subclass of WordFinder that reads files but excludes blank lines and comments"""
    def read_file(self, my_file):
        return [word.strip() for word in my_file if not word.startswith("#")]

