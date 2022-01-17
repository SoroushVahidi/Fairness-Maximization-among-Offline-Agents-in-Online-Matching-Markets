import math
import bisect
import pandas as pd
import numpy as np
import random
from scipy.optimize import linprog
import time
start_time = time.time()


# Function to generate a sorted list
# of random numbers in a given
# range with unique elements
avg = 0
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
t = 125
sum = 0
times = 100
nod=100
for z in range(0,nod):
    u=rand(t, 0, 7557)
    nx=[0]*80
    x=[]
    y=[]
    for i in u:
        x.append(df.iloc[i][0])
        nx[df.iloc[i][0]] += 1
        y.append((df.iloc[i][0], df.iloc[i][1]))
#table = [[0 for p in range(80)] for q in range(80)]
#print(table[77][77])
#print(x)
#print(table)
    x.sort()
    matches=[0]*t
#cnt=0
    sz = t
    obj = [0] * (sz * sz + 1)
    obj[sz * sz] = -1
    lhs_ineq = []
    rhs_ineq = []
    ok = [] * sz


    check = [[0] * sz for l in range(sz)]
    for q in range(0, t):
        #     print(check[0][0])
        for j in range(0, t):
            if x[q] == y[j][0]:
                #   ok[i].append(j)
                #   print(iii,jj,1)
                check[q][j] = 1
                arr = [0] * (sz * sz + 1)
                arr[q * sz + j] = 1
                lhs_ineq.append(arr)
                rhs_ineq.append((math.exp(1) - 1) / math.exp(1))
    for l in range(0, sz):
        arr = [0] * (sz * sz + 1)
        for j in range(l * sz, l * sz + sz):
            arr[j] = 1
        lhs_ineq.append(arr)
        rhs_ineq.append(1)
    for l in range(0, sz):
        arr = [0] * (sz * sz + 1)
        for j in range(l * sz, l * sz + sz):
            arr[j] = -1
        arr[sz * sz] = 1
        lhs_ineq.append(arr)
        rhs_ineq.append(0)
    for j in range(0, sz):
        arr = [0] * (sz * sz + 1)
        for l in range(0, sz):
            arr[l * sz + j] = 1
        lhs_ineq.append(arr)
        rhs_ineq.append(1)
    bnd = []
    for l in range(0, sz):
        for j in range(sz):
            if (check[l][j] == 1):
                bnd.append((0, 1))
            else:
                bnd.append((0, 0))
    bnd.append([0, sz])
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
    #print(opt.x)
    for p in range(0,times):
        l = [0] * t
        ted = [0] * 80
        for i in range(0,t):
            r = random.randint(0, t - 1)
            if(ted[y[r][0]]>=nx[y[r][0]]):
                continue
            avai=[]
            prob=[]
            p=0
            for u in range(len(x)):
                if((l[u]==0) and (check[u][r]==1)):
                    avai.append(u)
                    prob.append(p+opt.x[u*sz+r])
                    p += opt.x[u*sz+r]


            c=random.uniform(0, 1)
           
         #   for ind in range(len(prob)):
          #      if(prob[ind]>=c*p):
           #         break
     #       print(prob,c)
            ind=bisect.bisect(prob,c*p-0.0001)
      #      print(c*p,prob)
            l[avai[ind]]=1
            ted[y[r][0]]+=1
        matches = np.add(matches, l)
    sum += (min(matches)/(times*opt.x[sz*sz]))
    avg += opt.x[sz*sz]
  #  print(matches)



      #      j=1#random.randint(1,nx[y[r][0]]-ted[y[r][0]])
          #  o=0;
       #     for g in range(0,t):
             #   ok=0
        #        if((x[g]==y[r][0]) and (l[g]==0)):
  #                  o+=1
       #             if(o==j):
         #               l[g]+=1
          #              ted[y[r][0]]+=1
                 #       ok=1
           #             break
              #  if(ok==1):
                #    break
     #   print(l)
        #
  #  print(matches)
  #  sum+=min(matches)



         #   else:
          #      print(i,j,check[i][j])



    

  #  sum+=min(matches)/times
  #  avg+=opt.x[sz*sz]
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
print(sum/nod, avg/nod, time.time()-start_time)

#50 0.870 39.123 0.632
#75 0.867 123.276 0.632
#100 0.855 397.577 0.632
#125 0.852 4885.310 0.632
#150 0.854 13853.541 0.632





