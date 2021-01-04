# import pickle
# import numpy as np
#
# filename='F:/datasets/IFETEL/fetel-data/Wiki/enwiki20151002anchor-fetwiki-0_1-dev.pkl'
# with open(filename, 'rb') as f:
#     a=pickle.load(f)
#     b=np.array(a)
#     print("*****************")
#     print (len(b[-2][6]))
#     print(a[1])
    # for i in range(7):
    #     print(i)
    #     print(b[-1][i])
import collections

# 两种方法来给 namedtuple 定义方法名
#User = collections.namedtuple('User', ['name', 'age', 'id'])
Uaser = collections.namedtuple('User', 'name age id')
user = Uaser('tester', '22', '464643123')

print(user._fields)