class SS_functions(object):
    def __init__(self, word=0, second=0, wpm=130):
        self.word = word # number of words
        self.second = second # length of presentation in second
        self.wpm = wpm # wpm = word per minute

    def wordToSecond(self):
        pass
        # Return intager
        # Convert the number of words to length of presentation in second
        # Use wpm to calculate the number

    def secondToWord(self):
        pass
        # Return intager
        # Convert length of presentation in second to the number of words
        # Use wpm to calculate the number

if __name__ == "__main__":
    functions_test1 = SS_functions(520)
    functions_test2 = SS_functions(0, 180)
    functions_test3 = SS_functions(520, 0, 160)
    print(functions_test1.second)
    print(functions_test2.word)
    print(functions_test3.second)
