from  datetime import datetime
from datetime import date

def find_distance():
  ####a) 
  form = '%m-%d-%Y'
  date_start = datetime.strptime('01-02-2013',form)
  date_stop = datetime.strptime('07-28-2015',form)   
  delt =date_stop-date_start
  print(delt)

  ####b)  
  form = '%m%d%Y'
  date_start = datetime.strptime('12312013',form) 
  date_stop = datetime.strptime('05282015',form) 
  delta = date_stop-date_start
  print(delta)

  ####c)  
  form = '%d-%b-%Y'
  date_start = datetime.strptime('15-Jan-1994',form)
  date_stop = datetime.strptime('14-Jul-2015',form) 
  delt = date_stop-date_start
  print(delt)

def main():
  find_distance()

if __name__ == '__main__':
  main()
