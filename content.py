import csv
f=open ("/home/ancil/E Drive/Program/PythonPro/employe.csv")
f.readline()
fr=csv.reader(f)
minsal,maxsal=[],[]
for row in fr:
    print(row[1],row[2])
    minsal.append(row[1])
    maxsal.append(row[2])
print("MAX SALARY = ",max(maxsal))
print("MIN SALARY = ",min(minsal))