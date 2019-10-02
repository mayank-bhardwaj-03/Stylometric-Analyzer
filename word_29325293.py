# Author: Mayank Bhardwaj
# Start date: 18 may 2018
# Last modified date: 26 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This code is use for analysing the number of occurrences for each word from a
# given tokenised list. This class should also have one instance variable.

import pandas as pd
import numpy as np
import urllib.request
import urllib.error


class WordAnalyser:

    # ------------------------initialise the word dataframe----------------------
    def __init__(self):
        self.word_df = pd.DataFrame(columns=['data', 'frequency'])

    # ---------------------uses to print each word occurrences-------------------
    def __str__(self):
        string_to_print = 'Total number of occurences for each word :' + '\n'
        for key, values in self.word_df.iterrows():
            string_to_print = string_to_print + str(
                values['data']) + ' : ' + str(values['frequency']) + '\n'
        return string_to_print

    # -----------------Analyse the word from the tokenise list-------------------
    def analyse_words(self, tokenised_list):
        append_list = []
        for word in tokenised_list:
            if not word.isdigit() and not word.isalpha():  # check if digit/ alpha
                if len(word) > 1:
                    append_list.append(word.lower())
            else:
                append_list.append(word.lower())
        # append in the word dataframe
        self.word_df['data'] = append_list
        self.word_df['frequency'] = self.word_df.groupby('data')[
            'data'].transform('count')
        self.word_df = self.word_df.drop_duplicates('data')
        # calculate the frequency of the each word.
        self.word_df['frequency'] = \
            self.word_df['frequency'] / (self.word_df['frequency'].agg(np.sum))
        self.word_df = self.word_df.sort_values('data')

    # ------------------Analyse the stop word frequency--------------------------
    def get_stopword_frequency(self):
        stopword_df = pd.DataFrame(columns=['data', 'frequency'])  # Stop word
        # dataframe
        file = 'context.txt'
        # get the contents
        try:
            urllib.request.urlretrieve(
                'http://www.lextek.com/manuals/onix/stopwords1.html', file)

            # read the input html file from the website.
            file_handle = open('context.txt', 'r')

            html = file_handle.readlines()

            list = []

            for each in html:
                each = str(each)
                each = each.replace("\n\n", "")
                list.append(each)
            i = list.index(
                'about\n')  # find the index of the first word'about\n'

            file_stop = open('stop.txt', 'w')

            while i != list.index('yours\n'):  # find the index of the
                if list[i] != '\n':  # last word 'yours\n'
                    file_stop.write(list[i])
                i += 1

            file_stop.close()  # close the file.

            file_stop = open('stop.txt', 'r')
            # read the input stop word file and append the data in the stopword
            # dataframe from the word dataframe.
            for line in file_stop:
                line = line.strip('\n')
                for key, values in self.word_df.iterrows():

                    if values['data'] == line:
                        stopword_df.loc[len(stopword_df)] = \
                            [values['data'], values['frequency']]
            stopword_df = stopword_df.drop_duplicates('data')
            stopword_df = stopword_df.sort_values('data')

            return stopword_df

        except (urllib.error.URLError, urllib.error.HTTPError):
            print("The URL is not working")
            return None

    # -----------------Analyse the length of the word frequency------------------
    def get_word_length_frequency(self):

        # wordlength dataframe has been created.
        wordlength_df = pd.DataFrame(columns=['data1', 'data', 'frequency'])
        for key, values in self.word_df.iterrows():
            wordlength_df.loc[len(wordlength_df)] = \
                [values['data'], str(len(values['data'])), values['frequency']]
        wordlength_df['frequency'] = \
            wordlength_df.groupby('data')['frequency'].transform('sum')

        # deleted the word length extra column data1.
        del wordlength_df['data1']

        wordlength_df = wordlength_df.drop_duplicates('data')

        wordlength_df = wordlength_df.sort_values('data')

        return wordlength_df
