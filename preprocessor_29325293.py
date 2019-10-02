# Author: Mayank Bhardwaj
# Start date: 18 may 2018
# Last modified date: 26 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This have one instance variable which is a list that holds the individual
# tokens of the entire text as a result of applying the tokenise() method defined
# in this class.


class Preprocessor:
    # ---------------------Initialize the tokenised list-------------------------
    def __init__(self):
        self.tokenised_list = []

    # ---------------------Prints the tokenised list----------------------
    def __str__(self):
        string_to_print = 'The tokenize list as below:' + '\n'
        for each in self.tokenised_list:
            string_to_print = string_to_print + str(each) + '\n'
        return string_to_print

    # ------Analyse the line from the .tok file and make a tokenize file---------
    def tokenise(self, input_sequence):

        input_sequence = input_sequence.replace('\n', ' ')
        space_token = input_sequence.split(' ')
        for word in space_token:
            space_token = word.strip('\n')
            self.tokenised_list.append(space_token)

    # --------------------Get the tokenize value in main class-======------------
    def get_tokenised_list(self):
        return self.tokenised_list
