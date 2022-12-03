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

-  The total submission count will be the first instance of the fighter in descending order.


The raw dataset is stored in the form of a two dimensional dataframe and contains 6012 rows and 144 column entries. The rows descend in order according to most recent date. 106 columns have entries of type float, 28 columns have entries of type integer, 9 columns have entries of type object and 1 column has entries of type boolean. The competitors for each fight are classified as either Red or Blue. The information about the fighters will have a prefix "R" or "B" to clarify value assignment. For instance, column R_win_by_submission references the red fighter.

<p align="center">
    <img src ="images/raw_data_head.png" width="1000px">
    Figure 1: first 5 rows of the raw dataset.
<p\>

Investigation of the win_by_submission columns using the .unique() function reveals the columns only contains integer values in the range 0 to 14. This tells us we likely don't have to change any entry types or drop any rows in the submission columns. However, the .unique() function also revealed we have missing values in the height columns suggesting we will have to drop those corresponding rows if the analysis we're doing includes the height columns.

To assess potential bais in the dataset, the distribution of data should be considered. For instance, some weight divisions fight more frequently than others. To observe the number of fights in each weight divison a distribution was plotted.

<p align="center">
    <img src ="images/fight_dist.png" width="500px">
    <p align="center">Figure 2: barplot of the number of fights per weight division for the ufc dataset<p\>
<p\>

The above figure shows that the most number of recorded fights occur in the lightweight and welterweight divisions (>1000) and the least number of fights occur in the catchweight and womens featherweight divisions (<100).

To observe the values of fighter height in the ufc a distribution plot was created.

<p align="center">
    <img src ="images/height_dist.png" width="500px">
    <p align="center">Figure 3: distribution plot of fighter height in centimeters for the ufc dataset<p\>
<p\>

The above figure shows that the average fighter height is approximately 183 centimeters across all weight divsions. It is important to note that the plot contains duplicate values of the same fighter (i.e. Donald Cerone has 36 fights meaning his height is accounted for 36 times). This introduces a bias to the height distributions in the more active divisions. 

## Research Question 1: Which fighters have the most submission victories in the UFC?

To assess which fighter in the ufc has the largest count of submission wins it is most convient to create a new dataframe and vertically stack the red and blue instances of the fighter and submission columns. To get the most number of submissions for each fighter, the first instance (most recent fight) of the fighter is kept and the remaining duplicates are removed. The resulting table is shown belown.

<p align="center">
    <img src ="images/sub_wins.png" width="250px">
    <p align="center">Figure 4: ranking of fighters with the most submission wins in the ufc as of march 2021 <p\>
<p\>
