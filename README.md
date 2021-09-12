# Election-Analysis
### Overview of the project
#### The goal of this project was to perform an election audit to provide to the Colorado Board of Elections. Through the use of python, we were able to use a csv file and perform an analysis on it and save results to a text file. Information that was requested for the audit:
 - total votes
 - list of all candidates who received votes
 - votes per canididate received
 - percentage of votes each candidiate received
 - winner of the election
 
 ### Election-Audit Results
#### 
- Total Votes = 369,711
- Total votes and percentage by county:
  - Jefferson county had 38,855 votes, held by 10.51%
  - Denver county had 306,055 votes, held by 82.78%
  - Arapahoe had 24,801 votes, held by 6.71%
- Largest number of votes was Denver
- Total number of votes and percentage by candidate:
  - Charles Casper Stockham had 85,213 of the votes, 23%
  - Diana DeGette had 272,892, 73.8%
  - Raymon Anthony Doane had 11,606, 3.1%
- Winner of the election = Diana Degette
  - 272,892 total votes, 73.8% of the popular vote
  - 
### Election-Audit Summary:
#### Though this inital intent of this anaylsis was to provide voting information on the election, we could also use this to analyze a spending report per candidate. By adding another column of total cost, we could understand the candidate's total cost as well as a trend in dollars spent per county. This could help the election commission prepapre an election budget per candidate and potentially result in a cost savings over time.
  - adding a total cost variable to 0
  - adding the cost to the dictionary with the values of dollars spent (as seen below)
  - we associate the dollars to the candidates name instead of the candidate votes for this example
  - the end result: the "winner" would actually be "If candidate planned cost < candidate actual cost 
  <img width="503" alt="Screen Shot 2021-09-12 at 4 39 37 PM" src="https://user-images.githubusercontent.com/88811084/133003628-b8258dae-b8d3-4b34-9ba7-e723678aa400.png">
Another way we can re-use this scipt would be an age factor. To better understand the voters in the countys, we would neeed to an age for each ballot. 
  - best way would be to group the ages first ( 18-25, 26-35, etc.)
  - add a varriable to the age group
  - associate the candiates name with the votes, percentage of votes, and most popular age count by ballot
  - example below:
  <img width="565" alt="Screen Shot 2021-09-12 at 4 50 34 PM" src="https://user-images.githubusercontent.com/88811084/133003857-cd1b5a44-1e62-424b-98be-792c6c364dd8.png">
