# Author: Mayank Bhardwaj
# Start date: 18 may 2018
# Last modified date: 26 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This code for analysing the number of occurrences for each character from a
# given tokenised list, including any letters (‘A’ to ‘Z’), numerals (‘0’ to
# ‘9’), and punctuations.

import pandas as pd
import numpy as np


class CharacterAnalyser:

    # -------------------------initialize the character dataframe----------------
    def __init__(self):
        self.character_df = pd.DataFrame(
            columns=['data', 'frequency'])  # df1=character_df

    # ---------------------use to print each character occurrences---------------
    def __str__(self):
        string_to_print = 'Total number of occurences for each character :' + '\n'
        for key, values in self.character_df.iterrows():
            string_to_print = string_to_print + str(
                values['data']) + ' : ' + str(values['frequency']) + '\n'
        return string_to_print

    # --------Analyse the tokenise list and put in the character dataframe-------
    def analyse_character(self, tokenised_list):

        append_list = []
        for word in tokenised_list:
            for character in word:
                character = character.strip(' ')
                append_list.append(character.strip('\n').lower())
        self.character_df['data'] = append_list  # appended data in dataframe
        self.character_df['frequency'] = self.character_df.groupby('data')[
            'data'].transform('count')  # count the total character
        self.character_df = self.character_df.drop_duplicates()  # drop duplicates

        self.character_df['frequency'] = \
            self.character_df['frequency'] / (
                self.character_df['frequency'].agg(np.sum))

        self.character_df = self.character_df.drop_duplicates('data')
        self.character_df = self.character_df.sort_values('data')
        return self.character_df

    # ---------------------Analyse the puntuation frequency----------------------
    def get_puntuation_frequency(self):
        puntuation_df = pd.DataFrame(columns=['data', 'frequency'])
        for key, values in self.character_df.iterrows():  # uses the character
            character = values['data']  # dataframe to create
            character = character.strip(' ')  # puntuation dataframe
            character = character.strip('\n')
            if not character.isdigit() and not character.isalpha():
                puntuation_df.loc[len(puntuation_df)] = [values['data'],
                                                         values['frequency']]

        puntuation_df = puntuation_df.drop_duplicates('data')
        puntuation_df = puntuation_df.sort_values('data')
        return puntuation_df
