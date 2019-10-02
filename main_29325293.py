# Author: Mayank Bhardwaj
# Start date: 18 may 2018
# Last modified date: 26 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# the main program that enables you to compare the different stylistic features
# analysed from the six selected texts authored by Shakespeare and Marlowe.

import pandas as pd
from preprocessor_29325293 import Preprocessor
from character_29325293 import CharacterAnalyser
from word_29325293 import WordAnalyser
from visualiser_29325293 import AnalysisVisualiser


def read(file):
    # ----------Read the input files and store in the input sequence-------------

    string = ''
    try:
        input_sequence = open(file, 'r')
        if not input_sequence.read(1):
            # to verify if the file has any data or not
            print(file, 'does not contain any data')
            return None
        else:
            input_sequence.close()
            input_sequence = open(file, 'r')
            for line in input_sequence:
                string += line

            return string
    except IOError:
        print('One of the file does no exist, please check')
        return None


# Main function calls the all four task & pass the .tok files as the input files.


def main():
    # below are the input files.
    file_list = ['Edward_II_Marlowe.tok',
                 'Hamlet_Shakespeare.tok',
                 'Henry_VI_Part1_Shakespeare.tok',
                 'Henry_VI_Part2_Shakespeare.tok',
                 'Jew_of_Malta_Marlowe.tok',
                 'Richard_II_Shakespeare.tok'
                 ]

    print("The below are the list:")
    print('1. Edward_II_Marlowe.tok\n'
          '2. Hamlet_Shakespeare.tok\n'
          '3. Henry_VI_Part1_Shakespeare.tok\n'
          '4. Henry_VI_Part2_Shakespeare.tok\n'
          '5. Jew_of_Malta_Marlowe.tok\n'
          '6. Richard_II_Shakespeare.tok'
          )

    count = 0

    for file in file_list:
        input_sequence = read(file)

        if input_sequence is not None:
            token_list = Preprocessor()  # class object
            token_list.tokenise(input_sequence)
            character_analyser = CharacterAnalyser()
            character_df = character_analyser.analyse_character(
                token_list.get_tokenised_list())
            puntuation_df = character_analyser.get_puntuation_frequency()

            word_analyser = WordAnalyser()  # class object
            word_analyser.analyse_words(
                token_list.get_tokenised_list())
            wordlength_df = word_analyser.get_word_length_frequency()
            stopword_df = word_analyser.get_stopword_frequency()

            # rename the column name from frequency to file name.
            character_df.columns = ['data', file]
            puntuation_df.columns = ['data', file]
            wordlength_df.columns = ['data', file]
            if stopword_df is not None:
                stopword_df.columns = ['data', file]

                if count == 0:
                    all_character_dataframes = character_df
                    all_punctuation_dataframes = puntuation_df
                    all_wordlength_dataframes = wordlength_df
                    all_stopword_dataframes = stopword_df

                else:
                    all_character_dataframes = \
                        all_character_dataframes.merge(character_df,
                                                       on='data', how='outer')
                    all_punctuation_dataframes = \
                        all_punctuation_dataframes.merge(puntuation_df,
                                                         on='data', how='outer')
                    all_wordlength_dataframes = \
                        all_wordlength_dataframes.merge(wordlength_df,
                                                        on='data', how='outer')
                    all_stopword_dataframes = \
                        all_stopword_dataframes.merge(stopword_df,
                                                      on='data', how='outer')
                count += 1

                character_dataframes = \
                    pd.concat([all_character_dataframes], keys='character')

                punctuation_dataframes = pd.concat([all_punctuation_dataframes],
                                                   keys='punctuation')
                wordlength_dataframes = pd.concat([all_wordlength_dataframes],
                                                  keys='length')
                stopword_dataframes = pd.concat([all_stopword_dataframes],
                                                keys='stopword')

            else:
                print("The stop word frequency is not calculated")
                if count == 0:
                    all_character_dataframes = character_df
                    all_punctuation_dataframes = puntuation_df
                    all_wordlength_dataframes = wordlength_df

                else:
                    all_character_dataframes = \
                        all_character_dataframes.merge(character_df,
                                                       on='data', how='outer')
                    all_punctuation_dataframes = \
                        all_punctuation_dataframes.merge(puntuation_df,
                                                         on='data', how='outer')
                    all_wordlength_dataframes = \
                        all_wordlength_dataframes.merge(wordlength_df,
                                                        on='data', how='outer')

                count += 1
                character_dataframes = \
                    pd.concat([all_character_dataframes], keys='character')

                punctuation_dataframes = pd.concat([all_punctuation_dataframes],
                                                   keys='punctuation')
                wordlength_dataframes = pd.concat([all_wordlength_dataframes],
                                                  keys='length')

        else:
            exit()

    if stopword_df is not None:

        old_dataframes = \
            pd.concat([character_dataframes, punctuation_dataframes,
                       wordlength_dataframes, stopword_dataframes])
        old_dataframes.to_csv('final.csv')

        # below in the code, i have called the class analyser visualiser.

        visualiser = AnalysisVisualiser(old_dataframes)  # class object

        visualiser.visualise_character_frequency()
        visualiser.visualise_punctuation_frequency()
        visualiser.visualise_stopword_frequency()
        visualiser.visualise_word_length_frequency()

    else:
        old_dataframes = \
            pd.concat([character_dataframes, punctuation_dataframes,
                       wordlength_dataframes])
        old_dataframes.to_csv('final.csv')

        # below in the code, i have called the class analyser visualiser.

        visualiser = AnalysisVisualiser(old_dataframes)  # class object

        visualiser.visualise_character_frequency()
        visualiser.visualise_punctuation_frequency()
        visualiser.visualise_word_length_frequency()


# ---------------------------main function call----------------------------------


if __name__ == "__main__":
    main()
