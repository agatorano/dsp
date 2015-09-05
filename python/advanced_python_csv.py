import pandas as pd
import re

def get_data(name):
  data = pd.read_csv(name)
  return data
  
def process_emails(data):

  email = data[[3]]
  em_l=[]
  for i in range(len(data)):
    em = email.ix[i][0]
    em_l = em_l+ re.findall(r"[\w|\s|\.|@]*\.edu",em)

  write_csv(em_l)

def write_csv(e_mail):
  f = open('emails.csv','w')
  for el in e_mail:
    f.write(el+'\n')

def main():
  data = get_data('faculty.csv')
  process_emails(data)

if __name__ == '__main__':
  main()
