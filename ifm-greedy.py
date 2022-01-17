import math

import pandas as pd
import numpy as np
import random
from scipy.optimize import linprog
import time
start_time = time.time()


# Function to generate a sorted list
# of random numbers in a given
# range with unique elements
avg=0
def rand(num, start=1, end=100):
    arr = []
    tmp = random.randint(start, end)

    for x in range(num):

        while tmp in arr:
            tmp = random.randint(start, end)

        arr.append(tmp)

    arr.sort()

    return arr

df = pd.read_excel (r'write_data.xlsx',usecols=[1,2])
t=75
sum=0
times=100
nod=100
for z in range(0,nod):
    u=rand(t,0,7557)
    nx=[0]*80
    x=[]
    y=[]
    for i in u:
        x.append(df.iloc[i][0])
        nx[df.iloc[i][0]]+=1
        y.append([df.iloc[i][0],df.iloc[i][1]])
#table = [[0 for p in range(80)] for q in range(80)]
#print(table[77][77])
#print(x)
#print(table)
    x.sort()
    matches=[0]*t
#cnt=0
    for p in range(0,times):
        l = [0] * t
        ted=[0]*80
        passen=[]
        for i in range(0,t):
            r=random.randint(0,t-1)
            passen.append(y[r][0])
            if(ted[y[r][0]]>=nx[y[r][0]]):
                continue
            j=1#random.randint(1,nx[y[r][0]]-ted[y[r][0]])
          #  o=0;
            for g in range(0,t):
             #   ok=0
                if((x[g]==y[r][0]) and (l[g]==0)):
  #                  o+=1
       #             if(o==j):
                        l[g]+=1
                        ted[y[r][0]]+=1
                 #       ok=1
                        break

        matches=np.add(matches,l)
  #  print(matches)
    sum+=min(matches)
    sz=len(x)
    obj=[0]*(sz*sz+1)
    obj[sz*sz]=-1
    lhs_ineq=()
    rhs_ineq=[]
    ok=[]*sz
    check = [[0] * sz for l in range(sz)]
    for i in range(0,sz):
          # print(check[0][0])
            for j in range(0,sz):
               if x[i]==y[j][0]:
             #  ok[i].append(j)
             #   print(iii,jj,1)
                check[i][j]=1
                arr = [0] * (sz * sz + 1)
                arr[i*sz+j]=1
                lhs_ineq=lhs_ineq+(arr,)
                rhs_ineq.append((math.exp(1)-1)/math.exp(1))
           # else:
            #    print(i,j,check[i][j])
    for i in range(0,sz):
        arr = [0] * (sz * sz + 1)
        for j in range(i*sz,i*sz+sz):
            arr[j]=1
        lhs_ineq=lhs_ineq+(arr,)
        rhs_ineq.append(1)
    for i in range(0,sz):
        arr = [0] * (sz * sz + 1)
        for j in range(i*sz,i*sz+sz):
            arr[j]=-1
        arr[sz*sz]=1
        lhs_ineq=lhs_ineq+(arr,)
        rhs_ineq.append(0)
    for j in range(0,sz):
        arr = [0] * (sz * sz + 1)
        for i in range(0,sz):
            arr[i*sz+j]=1
        lhs_ineq=lhs_ineq+(arr,)
        rhs_ineq.append(1)
    
    bnd=[]
  #  print(y)
  #  print(y)
   # print(check[0][0])
    for i in range(0,sz):
        for j in range(sz):
            if(check[i][j]==1):
                bnd.append((0,1))
            else:
                bnd.append((0,0))
    bnd.append([0,sz])
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,  bounds=bnd, method="revised simplex")
 #   print(z)
    avg += opt.x[sz*sz]#0.632

  #  print(sum)


print(sum/(nod*times),avg/(nod),sum/(avg*times),time.time()-start_time)
# 50  0.790  34.655
# 75  0.775  111.297
# 100 0.760  366.136
# 125 0.747  968.151
# 150 0.731  13316.339

# with fixed opt
# 50 0.786 3.344
# 75 0.765 7.186
# 100 0.759 10.220
# 125 0.752 13.073
# 150 0.741 19.544


