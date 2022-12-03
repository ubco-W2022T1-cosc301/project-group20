# COSC 301 - Data Analytics
### Group 20
### Team Members
- Zach Kelly 41637836
- Gerren Hunter
- Sarah Q
# UFC Fighter Statistics

## Introduction

This report considers a Ulitimate Fighting Championship (UFC) dataset. The data was scraped from the ufcstats website March 21st, 2021 and contains a list of statistics for every UFC fight in the history of the organization. Every row contains information about each fighter, fight details, and the winner. Provided this data the following research questions are considered:

- Which fighters have the most submission victories in the UFC?
- Does reach have a significant affect on fighter success in the UFC?
- What is the average fighter height amoung different UFC weight divisions?

These topics were motivated by our groups interest in mixed martial arts and the UFC. Answering research questions of these type help differentiate fighters and highlight their strengths or weaknesses.

## Exploratory Data Analysis

- overall stats of the dataset
- add gained information about the submmission column (column includes values of type int, where the value is how many submission wins the fighter has to date)
- mention there are multiple instances of a fighter within the rows. The total submission count will be the first instance of the fighter in descending order.
- add a figure for the number of fights under each division. This points out potential bias in the dataset (i.e. more fights in lw than wfw)
- mention the number of fights each fighter has in descending order
- data type of height column what units of measurement. 
- show the plot of the height distribution across all divisions


The raw dataset is stored in the form of a two dimensional dataframe and contains 6012 rows and 144 column entries. 106 columns have entries of type float, 28 columns have entries of type integer, 9 columns have entries of type object and 1 column has entries of type boolean. The competitors for each fight are classified as either Red or Blue. The information about the fighters will have a prefix "R" or "B" to clarify value assignment. For instance, column R_win_by_submission references the red fighter.

<img src ="images/raw_data_head.png" width="1000px">

Figure 1: first 5 rows of the raw dataset.

Further investigation of the win_by_submission columns using the .unique() function reveals the columns only contains integer values in the range 0 to 14. This tells us we likely don't have to change any entry types or drop any rows in the submission columns.

