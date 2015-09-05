from collections import OrderedDict
import pandas as pd
import re

def read_file(name):
  data = pd.read_csv(name)
  return(data)

def create_bad_dict(data):

  faculty_dict = {}
  for i,row in data.iterrows():
    last_name = re.findall(r"\w*$",row[0])[0] 
    if last_name in faculty_dict:
      faculty_dict[re.findall(r"\w*$",row[0])[0]].append(list(row.values[1:]))
    else: 
      faculty_dict[last_name] = [list(row.values[1:])]

  for key,value in faculty_dict.iteritems():
    print("%s\n\t%s"%(key,value))


def create_dict(data):

  faculty_dict = {(re.findall(r"\w*",row[0])[0],re.findall(r"\w*",row[0])[-2]):list(row[1:]) for i,row in data.iterrows()}

  #for key,value in faculty_dict.iteritems():
  #  print("%s\n\t%s"%(key,value))
  
  return faculty_dict

def ordered_dict(faculty):
  
  el = OrderedDict(sorted(faculty.items(),key=lambda x: x[0][1]))
  for key,value in el.iteritems():
    print("%s\n\t%s"%(key,value))

  

def main():
  data = read_file('faculty.csv')
  #create_bad_dict(data)
  dicts = create_dict(data)
  ordered_dict(dicts)

if __name__ == '__main__':
  main()
