import pandas as pd
import re
from collections import defaultdict


def read_file(name):
  data = pd.read_csv(name)
  return(data)

def process_degrees(data):
  print("DEGREE NAMES")
  degree = data[[1]]
  degrees = defaultdict(int)
  for i in range(len(data)):
    deg = degree.ix[i][0]
    deg = deg.replace(".","")
    deg_l = re.findall(r"\w*",deg)
    for el in deg_l:
      if el != '' and el != '0':
        if el in degrees:
          degrees[el]= degrees[el]+1
        else:
          degrees[el] =1

  total=0
  for key in degrees.keys():
    print("%s:\t%s"%(key,degrees[key]))
    total+=1
  print("Total Degrees: %s\n"%total)

def process_titles(data):
  title = data[[2]]
  titles = defaultdict(int)
  for i in range(len(data)):
    tit = title.ix[i][0]
    tit_l = re.findall(r"[\w|\s]*ssor",tit)
    for el in tit_l:
      if el != '' and el != '0':
        if el in titles:
          titles[el]= titles[el]+1
        else:
          titles[el] =1

  total=0
  print("TITLES:")
  for key in titles.keys():
    print("%s:\t%s"%(key,titles[key]))
    total+=1

  print("Total Titles: %s"%total)

def process_emails(data):

  email = data[[3]]
  emails = defaultdict(int)
  em_l=[]
  for i in range(len(data)):
    em = email.ix[i][0]
    em_l = em_l+ re.findall(r"[\w|\s|\.|@]*\.edu",em)
    em_d = re.findall(r"[\w|\s|\.]*\.edu",em)
    for el in em_d:
      if el != '' and el != '0':
        if el in emails:
          emails[el]= emails[el]+1
        else:
          emails[el] =1

  e_names = emails.keys()
  print("\nEMAILS:")
  print(em_l)

  total=0
  print("\nEMAIL DOMAINS:")
  for key in emails.keys():

    print("%s:\t%s"%(key,emails[key]))
    total+=1

  

def main():
  data = read_file('faculty.csv')
  process_degrees(data)
  process_titles(data)
  process_emails(data)

if __name__ == '__main__':
  main()
