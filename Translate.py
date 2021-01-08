import csv
from datetime import datetime
start_time = datetime.now()
file = "french_dictionary.csv"
rep = {} 
rows = {}
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      rows[row[0]]=row[1]
with open("t8.shakespeare.txt", "r") as f:
  lines=[]
  for i in f:
    for w in i.split():
      lines.append(w)
for i in lines:
  if(i in rows.keys()):
    if(i not in rep):
      print(str(i)+"->"+str(rows[i]))
      rep[i]=0
    else:
      rep[i]+=1
print(rep)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)import csv
from datetime import datetime
start_time = datetime.now()
file = "french_dictionary.csv"
rep = {} 
rows = {}
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      rows[row[0]]=row[1]
with open("t8.shakespeare.txt", "r") as f:
  lines=[]
  for i in f:
    for w in i.split():
      lines.append(w)
for i in lines:
  if(i in rows.keys()):
    if(i not in rep):
      print(str(i)+"->"+str(rows[i]))
      rep[i]=0
    else:
      rep[i]+=1
print(rep)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)