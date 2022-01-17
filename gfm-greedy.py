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
t=150
sum=0
times=100
nod=100
ans=0

for z in range(0,nod):
    u=rand(t,0,7557)
    nx=[[] for a in range(80)]
    adad=[0]*80
    x=[]
    y=[]
    for i in range(t):
      #  print(len(nx))
        x.append(df.iloc[i][0])
       # print(df.iloc[i][0])
        nx[df.iloc[i][0]].append(i)
        adad[df.iloc[i][0]]+=1
        y.append((df.iloc[i][0],df.iloc[i][1]))
    x.sort()
    matches=[0]*t
#cnt=0
    for p in range(0,times):
        l = [0] * t
        ted=[0]*80
       # passen=[]
        for i in range(0,t):
       #     print(1)
            r=random.randint(0,t-1)
        #    passen.append(y[r][0])
            if(ted[y[r][0]]>=adad[y[r][0]]):
                continue
            j=random.randint(1,adad[y[r][0]]-ted[y[r][0]])
            o=0
            for g in range(0,t):

                if((x[g]==y[r][0]) and (l[g]==0)):
                    o+=1
                    if(o==j):
                        l[g]+=1
                        ted[y[r][0]]+=1
                        break

     #   print(l)
        matches=np.add(matches,l)
  #  print(matches)
  #  sum+=min(matches)
    maxi=1000*1000*1000
    best=0
   # print('salam')
    for i in range(len(nx)):
        jam=0
        if(len(nx[i])>0):
            for j in range(len(nx[i])):
                jam+=matches[nx[i][j]]
            if(maxi>(jam/len(nx[i]))):
                maxi=jam/(len(nx[i]))
                best=i
   # sum+=maxi/times
    #     print(i, nx[i], jam / len(nx[i]))
   # print(best,maxi)
    sum += maxi / (times * nod)  # opt.x[sz*sz])
    avg += 0.6321
    oo=0
    if oo==1:
        sz=len(x)
        obj=[0]*(sz*sz+1)
        obj[sz*sz]=-1
        lhs_ineq=()
        rhs_ineq=[]
        ok=[]*sz
        check = [[0] * sz for l in range(sz)]
        for i in range(0,sz):
           #     print(check[0][0])
            for j in range(0,sz):
                if x[i]==y[j][0]:
                    check[i][j]=1
                    arr = [0] * (sz * sz + 1)
                    arr[i*sz+j]=1
                    lhs_ineq=lhs_ineq+(arr,)
                    rhs_ineq.append((math.exp(1)-1)/math.exp(1))
             #   else:
              #      print(i,j,check[i][j])
     #   print("hello")
        for i in range(0,sz):
             arr = [0] * (sz * sz + 1)
             for j in range(i*sz,i*sz+sz):
                arr[j]=1
             lhs_ineq=lhs_ineq+(arr,)
             rhs_ineq.append(1)
        for i in range(len(nx)):
             arr = [0] * (sz * sz + 1)
             for j in range(len(nx[i])):
                  for f in range(nx[i][j]*sz,nx[i][j]*sz+sz):
                    arr[f]=-1
             arr[sz*sz]=len(nx[i])
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
     #   print("hi")
        for i in range(0,sz):
            for j in range(0,sz):
                if(check[i][j]==1):
                    bnd.append((0,1))
                else:
                    bnd.append((0,0))
        bnd.append([0,sz])
    #    print("topol")
        opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,  bounds=bnd, method="revised simplex")
    #    print(opt.x[sz*sz])
    #    print(z)
    #   sum+=maxi/(times*nod)#opt.x[sz*sz])
    #    avg+=0.6321#opt.x[sz*sz]

   # ans+=maxi/(times*opt.x[sz*sz])
  #  print(maxi/times,opt.x[sz*sz])
  #  print(maxi/times,opt.x[sz*sz],maxi/(times*opt.x[sz*sz]))
print((sum*nod)/avg,avg/(nod),time.time()-start_time)
#50 0.97 86.833
#75 0.933 190.725  0.632
#100 0.923 363.500 0.632
#125 0.914 978.942 0.632
#150 0.922 2446.671 0.632

#with fixed point
#50 0.958 5.898
#75 0.943 9.796
#100 0.925 13.872
#125 0.920 16.920
#150 0.912 23.632






