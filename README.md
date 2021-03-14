# Election Analysis

## Project Overview

Tom, a Colorado Board of Elections employess has been tasked with completing the election audit of a recent local congressional election. In addition to the electino audit, the Election Commission has requested the addition of the following information: 
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

Using python, I assisted tom with analyzing the data and adding the additional information to the audit. 

## Election Audit Results

**Total Votes**:
- Total of 369,711 votes. 

**County Votes**:
- **Denver**: Denver had the largest voter turnout with 306,055 votes which accounts for 82.8% of all votes.
- **Jeffferson**: Jefferson had 38,855 votes which accounts for 10.5% of all votes
- **Arapahoe**: Arapahoe had 24,801 votes which accounts for 6.7% of all votes

**Candidate Results**:
- **Diana Degette**: Diana won the election by receieving a total of 272,892 votes, which is 73.8% of all votes received.
- **Charles Casper Stockham**: Charles received 85,213 votes, which is 23% of all votes.
- **Ryan Anthony Doane**: Raymon recieve 11,606 votes which is 3.1% of all votes.

All data on the election results can be found in election_analysis.txt located in the Analysis folder.

## Election Audit Summary

In summary, using python to analyze the election data and determine a winner is effective and can be extended to other elections in other parts of the nation or world. 
- First, this script can be used to determine election outcomes based on city polling instead of counties. In order to do this, voter data from multiple cities will need to be either put into the election_results.csv file or a new dataset will need to be created. 
- Second, we could also include the age of voters to determine how age influecnes election results. To do this we would simply initializing a new variable and naming it vote_age = 0. This variable will hold the data of the voters age. 
