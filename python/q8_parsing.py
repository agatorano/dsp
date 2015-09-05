# -*- coding: utf-8 -*-
#The football.csv file contains the results from the English Premier League 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import pandas as pd

def read_data(data):
  data = pd.read_csv(data)
  return(data)

def get_min_score_difference(parsed_data):

  min_=100
  team = ''
  for i,row in parsed_data.iterrows():
    tea = row['Team']
    print(tea)
    goals = row['Goals']
    allowed = row['Goals Allowed']
    diff = abs(goals-allowed)
    print("\t%s\n\t%s\n\t%s"%(goals,allowed,diff))
    if diff<min_:
      min_ = diff
      team = tea

  return(team)

def main():
  data = read_data('football.csv')
  team = get_min_score_difference(data)
  print(team)  

if __name__ == '__main__':
  main()
