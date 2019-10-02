# Author: Mayank Bhardwaj
# Start date: 18 may 2018
# Last modified date: 26 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# • character frequency: the relative frequency of each different character —
#   the frequency of each character is based on the length of a given text;
# • punctuation frequency: the relative frequency of each different punctuation -
#   the frequency of each punctuation is based on the length of a given text;
# • stop_word frequency: the relative frequency of each different stopword—
#   the frequency of each stopword is based on the length of a given text;
# • word length frequency: the relative frequency of each different word length -
#   the frequency of each word length is based on the length of a given text.

import matplotlib.pyplot as plt


class AnalysisVisualiser:

    # ------------------assign all text stats in the all dataframe---------------
    def __init__(self, all_text_stats):
        self.all_dataframes = all_text_stats

    # ------------------------character visualisation----------------------------
    def visualise_character_frequency(self):
        self.all_dataframes.loc['c'][0:].plot(title='characters Frequency',
                                              kind='bar', x='data',
                                              y=['Edward_II_Marlowe.tok',
                                                 'Hamlet_Shakespeare.tok',
                                                 'Henry_VI_Part1_Shakespeare.tok',
                                                 'Henry_VI_Part2_Shakespeare.tok',
                                                 'Jew_of_Malta_Marlowe.tok',
                                                 'Richard_II_Shakespeare.tok'
                                                 ], figsize=(17, 10))
        plt.show()

    # -----------------------Puntuation visualisation----------------------------
    def visualise_punctuation_frequency(self):
        self.all_dataframes.loc['p'][0:].plot(title='Puntuation Frequency',
                                              kind='bar', x='data',
                                              y=['Edward_II_Marlowe.tok',
                                                 'Hamlet_Shakespeare.tok',
                                                 'Henry_VI_Part1_Shakespeare.tok',
                                                 'Henry_VI_Part2_Shakespeare.tok',
                                                 'Jew_of_Malta_Marlowe.tok',
                                                 'Richard_II_Shakespeare.tok'
                                                 ], figsize=(17, 10))
        plt.show()

    # ------------------------Stop word visualisation----------------------------
    def visualise_stopword_frequency(self):
        self.all_dataframes.loc['s'][0:].plot(title='Stop_Word Frequency',
                                              kind='bar', x='data',
                                              y=['Edward_II_Marlowe.tok',
                                                 'Hamlet_Shakespeare.tok',
                                                 'Henry_VI_Part1_Shakespeare.tok',
                                                 'Henry_VI_Part2_Shakespeare.tok',
                                                 'Jew_of_Malta_Marlowe.tok',
                                                 'Richard_II_Shakespeare.tok'
                                                 ], figsize=(17, 10))

        self.all_dataframes.loc['s'][0:].sort_values(['Edward_II_Marlowe.tok',
                                                      'Hamlet_Shakespeare.tok',
                                                      'Henry_VI_Part1_Shakespeare.tok',
                                                      'Henry_VI_Part2_Shakespeare.tok',
                                                      'Jew_of_Malta_Marlowe.tok',
                                                      'Richard_II_Shakespeare.tok'
                                                      ],
                                                     ascending=False).head(
            10).plot(
            title='Highest 10 Stop_Word Frequency',
            kind='bar', x='data',
            y=['Edward_II_Marlowe.tok',
               'Hamlet_Shakespeare.tok',
               'Henry_VI_Part1_Shakespeare.tok',
               'Henry_VI_Part2_Shakespeare.tok',
               'Jew_of_Malta_Marlowe.tok',
               'Richard_II_Shakespeare.tok'
               ], figsize=(17, 10))

        plt.show()

    # ----------------------Word length visualisation----------------------------
    def visualise_word_length_frequency(self):
        self.all_dataframes.loc['l'][0:].plot(title='Word Length Frequency',
                                              kind='bar', x='data',
                                              y=['Edward_II_Marlowe.tok',
                                                 'Hamlet_Shakespeare.tok',
                                                 'Henry_VI_Part1_Shakespeare.tok',
                                                 'Henry_VI_Part2_Shakespeare.tok',
                                                 'Jew_of_Malta_Marlowe.tok',
                                                 'Richard_II_Shakespeare.tok'
                                                 ], figsize=(17, 10))
        plt.show()
