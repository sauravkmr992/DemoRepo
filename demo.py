from collections import Counter

x=[1,2,2,3,3,3,4,4,4,4]

count=Counter(x)

print(count)

count_dic={}
for ele in x:
    if ele not in count_dic:
        count_dic[ele] = 0
        count_dic[ele] += 1
    else:
        count_dic[ele]+=1

print(count_dic)    