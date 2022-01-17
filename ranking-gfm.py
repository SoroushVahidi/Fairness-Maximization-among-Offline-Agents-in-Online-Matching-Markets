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
def rand(num, start, end):
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

for z in range(0,nod):
    u=rand(t,0,7557)
    nx=[[] for a in range(80)]
    adad=[0]*80
    x=[]
    y=[]
    rp=np.random.permutation(t)
    for i in range(len(u)):
      #  print(len(nx))
        x.append(df.iloc[i][0])
       # print(df.iloc[i][0])
        nx[df.iloc[i][0]].append(i)
        adad[df.iloc[i][0]]+=1
        y.append((df.iloc[i][0],df.iloc[i][1]))
#table = [[0 for p in range(80)] for q in range(80)]
#print(table[77][77])
#print(x)
#print(table)
    x.sort()
    matches=[0]*t
#cnt=0
    for p in range(0,times):
    #    rp = np.random.permutation(t)
        l = [0] * t
        ted=[0]*80
        for i in range(0,t):
       #     print(1)
            r=random.randint(0,t-1)
            if(ted[y[r][0]]>=adad[y[r][0]]):
                continue
    #        j=random.randint(1,adad[y[r][0]]-ted[y[r][0]])
       #     o=0
            for g in range(0,t):

                if((x[rp[g]]==y[r][0]) and (l[rp[g]]==0)):
                #    o+=1
                 #   if(o==j):
                        l[rp[g]]+=1
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
         for j in nx[i]:
           jam+=matches[j]

         if(maxi>(jam/len(nx[i]))):
            maxi=jam/(len(nx[i]))
            best=i
    #     print(i, nx[i], jam / len(nx[i]))
   # print(best,maxi)
    oo=0
    if oo==1:
        sz=len(x)
        obj=[0]*(sz*sz+1)
        obj[sz*sz]=-1
        lhs_ineq=[]
        rhs_ineq=[]
        ok=[]*sz
        check = [[0] * sz for l in range(sz)]
        for i in range(0,sz):
       #     print(check[0][0])
            for j in range(0,sz):
                if x[i]==y[j][0]:
             #   ok[i].append(j)
             #   print(iii,jj,1)
                    check[i][j]=1
                    arr = [0] * (sz * sz + 1)
                    arr[i*sz+j]=1
                    lhs_ineq.append(arr)
                    rhs_ineq.append((math.exp(1)-1)/math.exp(1))
         #   else:
          #      print(i,j,check[i][j])
        for i in range(0,sz):
            arr = [0] * (sz * sz + 1)
            for j in range(i*sz,i*sz+sz):
                arr[j]=1
            lhs_ineq.append(arr)
            rhs_ineq.append(1)
        for i in range(len(nx)):
            arr = [0] * (sz * sz + 1)
            for j in range(len(nx[i])):
                for f in range(nx[i][j]*sz,nx[i][j]*sz+sz):
                    arr[f]=-1
            arr[sz*sz]=len(nx[i])
            lhs_ineq.append(arr)
            rhs_ineq.append(0)
        for j in range(0,sz):
            arr = [0] * (sz * sz + 1)
            for i in range(0,sz):
                arr[i*sz+j]=1
            lhs_ineq.append(arr)
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
        for i in range(1, 78):
            if (len(nx[i]) > 0):
                s = 0
                for j in range(len(nx[i])):
                    #  print(len(x),nx[i][j]*sz+sz)
                    for g in range(nx[i][j] * sz, nx[i][j] * sz + sz):
                        s += opt.x[g]
    sum+=maxi/times
    avg=0.6321*nod
   # avg+=opt.x[sz*sz]
   # print(opt.x[sz*sz])

       #     print(i,s/len(nx[i]))
  #  print(opt.x)

  #  print(min(matches)/(times*opt.x[sz*sz]))
    #print(opt.x[sz*sz])
   # print(opt.x)
  #  print(rhs_ineq)
 #   for i in range(0,sz):
  #    for j in range(0,sz):
   #        if(check[i][j]==1):
    #             print(opt.x[i*sz+j])
   # for j in range(0,sz):
    #  sum=0
     # for i in range(0,sz):
      #     sum+=opt.x[i*sz+j]
      #print(sum)
print(sum/avg,avg/nod,time.time()-start_time)

#50 0.859 37.710 0.632
#75 0.861 149.081 0.632
#100 0.847 412.306 0.632

#fixed opt
#50 0.865 5.587
#75 0.850 11.090
#100 0.844 14.937
#125 0.825 17.591
#150 0.826 35.334




