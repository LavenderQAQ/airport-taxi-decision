import numpy as np
import seaborn as sns

f=open('C++np/cmake-build-debug/new_data.txt')
val=[]
for line in f.readlines():
    line=line.strip('\n').split(' ')
    a=[]
    for i in line:
        a.append(int(i))
    val.append(a)
index=[]
for i in range(60):
    index.append(i)
p=sns.barplot(x=index,y=val[13])
print(p)