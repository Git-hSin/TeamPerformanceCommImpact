# TeamPerformanceCommImpact

How do different sports teams performances impact the communities that surround the cities they are in?


## Introduction

Sports teams in a city provide historic data in various categories related to those teams performances over time. The impact of those performances can be measured alongside datasets of: the economies and demographics; of the communities that surround them, during that same period. 

## Hypothesis

A team's performance will benefit economies of production and real estate, in the communities that surround them, and affect demographic groups differently across those sets. 

## Sources & Method

Independent variables, primary of which is time, studied across all datasets are consistent in these categories:
- Geographic location & the demographics within
  - Income, real estate value, ethnicity, 
  
- Sport Organizations

    
### Sports Organizations
-20 years of data (1998 - 2018) regarding the win/loss records, playoff/championship data, and attendance figures for each team in Major League Baseball, the National Football League, and the National Basketball Association. 
  - Sources: 
    - MLB Data: https://www.baseball-reference.com/
    - NFL Data: https://www.pro-football-reference.com/
    - NBA Data: https://www.basketball-reference.com/
 - The above sources provide tables that can be manipulated and exported as CSV files. Once the data was gathered and cleaned, Tim organized them into analysis-ready DataFrames via the Python Pandas library.
 - The visualizations were done using matplotlib and seaborn
 -Cleveland Browns 1998 issue: The city of Cleveland agreed to demolish Cleveland Stadium and build a new stadium on the same site, and the NFL agreed to reactivate the Browns by the 1999 season through either an expansion draft or a relocated franchise. The Browns were officially reactivated in 1998 through the expansion process and resumed play in 1999. Therefore, the Browns plotting in the Bottom 3 NFL Teams plot begins on 1999 instead of 1998. 
 
### Zillow

### US Census
- US Census information provides the largest demographic population size to sample datasets for analysis against other variables. 
  - Sources:
    - API: https://www.census.gov/data/developers/guidance/api-user-guide.Overview.html
   
  
