# Stylometric-Analyzer
Style analysis for 2 different authors and 6 books.
Stylometry is an application of statistical methods for linguistic style analysis. It is often used to 
attribute authorship to anonymous or disputed works (often in written language) based on the 
linguistic behaviours or characteristics manifested in the texts. One of the classic authorship 
attribution studies was whether William Shakespeare wrote all his works, in particular one of his popular plays — Henry VI Trilogy — was highly disputed to have been written or co-authored by Christopher Marlowe. 
In this, I have implement the stylometric analyser and represent the character, stop word, punctuation and word length frequency by the visualisation.

Total 6 books are analysed.

1.	Implementation of tasks

1.1 Task-1: Setting up the preprocessor

In this task, the preprocessor accepts the input from the file and make token file in form of word and punctuation. I have seperated it by ‘/n’ and space ’ ‘.

1.2 Task-2: Building character analyzer class

In this task, I have passed the tokenized list (from task 1) and pass as the input  and the output will consist of the frequency of individual characters. The output is stored in a readable format using pandas data frame in form of two columns data and frequency.

1.3 Task-3: Building Word analyzer class

In this task, I have performed the frequency analysis on a given tokenized list at the word level, extracts the stop word frequency from(
http://www.lextek.com/manuals/onix/stopwords1.html) and word length frequency of files. The output is stored as pandas data frame with data and frequency columns.

1.4 Task-4: Building a class for visualizing the analysis

In this task, each statistic of character, punctuation, stop-word and word length is displayed using plots and helps user to understand the graph in a simple manner.

1.5 Task-5: Main method

In this task, I have called all the functions and run the program after passing the input from here. Steps are taken to read the input files 

2.	Output screenshot

When the main file is run, the statistic data and visualizations are automatically displayed and stored in required directory. Refer the folders for output
