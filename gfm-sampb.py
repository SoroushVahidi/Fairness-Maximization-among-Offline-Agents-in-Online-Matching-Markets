import math
import bisect
import pandas as pd
import numpy as np
import random
from scipy.optimize import linprog

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

df = pd.read_excel(r'write_data.xlsx', usecols=[1, 2])
t = 50
sum = 0
times = 100
nod = 100
for z in range(0, nod):
    u = rand(t, 0, 7557)
    nx=[[] for a in range(80)]
    x = []
    y = []
    for i in range(t):
        x.append(df.iloc[i][0])
        nx[df.iloc[i][0]] .append(i)
        y.append((df.iloc[i][0], df.iloc[i][1]))
    # table = [[0 for p in range(80)] for q in range(80)]
    # print(table[77][77])
    # print(x)
    # print(table)
    x.sort()
    matches = [0] * t
    # cnt=0
    sz = len(x)
    obj = [0] * (sz * sz + 1)
    obj[sz * sz] = -1
    lhs_ineq = []
    rhs_ineq = []
    ok = [] * sz
    check = [[0] * sz for l in range(sz)]
    for i in range(0, sz):
        #     print(check[0][0])
        for j in range(0, sz):
            if x[i] == y[j][0]:
                #   ok[i].append(j)
                #   print(iii,jj,1)
                check[i][j] = 1
                arr = [0] * (sz * sz + 1)
                arr[i * sz + j] = 1
                lhs_ineq.append(arr)
                rhs_ineq.append((math.exp(1) - 1) / math.exp(1))
        #   else:
        #      print(i,j,check[i][j])
    for i in range(0, sz):
        arr = [0] * (sz * sz + 1)
        for j in range(i * sz, i * sz + sz):
            arr[j] = 1
        lhs_ineq.append(arr)
        rhs_ineq.append(1)
    for i in range(len(nx)):
        arr = [0] * (sz * sz + 1)
        for j in range(len(nx[i])):
            for f in range(nx[i][j] * sz, nx[i][j] * sz + sz):
                arr[f] = -1
        arr[sz * sz] = len(nx[i])
        lhs_ineq.append(arr)
        rhs_ineq.append(0)
    for j in range(0, sz):
        arr = [0] * (sz * sz + 1)
        for i in range(0, sz):
            arr[i * sz + j] = 1
        lhs_ineq.append(arr)
        rhs_ineq.append(1)

    bnd = []
    #  print(y)
    #  print(y)
    # print(check[0][0])
    for i in range(0, sz):
        for j in range(sz):
            if (check[i][j] == 1):
                bnd.append((0, 1))
            else:
                bnd.append((0, 0))
    bnd.append([0, sz])
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
 #   print(opt.x[sz*sz])
    for p in range(0, times):
        l = [0] * t
        ted = [0] * 80
        for i in range(0, t):
            r = random.randint(0, t - 1)
            if (ted[y[r][0]] >= len(nx[y[r][0]])):
                continue
            avai = []
            prob = []
            p = 0
            for u in range(len(x)):
                if ((l[u] == 0) and (check[u][r] == 1)):
                    avai.append(u)
                    prob.append(p + opt.x[u * sz + r])
                    p += opt.x[u * sz + r]

            c = random.uniform(0, 1)
            #   for ind in range(len(prob)):
            #      if(prob[ind]>=c*p):
            #         break
            #       print(prob,c)
            ind = bisect.bisect(prob, c * p - 0.0001)
            #      print(c*p,prob)
            l[avai[ind]] = 1
            ted[y[r][0]] += 1
        matches = np.add(matches, l)
    maxi = 1000 * 1000 * 1000
    best = 0
    # print('salam')
    for i in range(len(nx)):
        jam = 0
        if (len(nx[i]) > 0):
            for j in nx[i]:
                jam += matches[j]
            if (maxi > (jam / len(nx[i]))):
                maxi = jam / (len(nx[i]))
                best = i
    sum += (maxi/opt.x[sz*sz])
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
# print(opt.x[sz*sz])
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
# print(sum)
print(sum / (times*nod))


