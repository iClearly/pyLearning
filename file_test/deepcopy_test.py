#! /usr/bin/env python
# _*_ coding:UTF-8 _*_

d = [4, ['a', ['b', 'c'], 'test'], 5, ['string', 'iterator']]
v =['string list', 'control']
deepcopy_list = d[:]
lv = ['name', 'age', v]
print(d)
print(deepcopy_list)
deepcopy_list[0] = 0
deepcopy_list[1][1][0] = 'b_string'
print(d)
print(deepcopy_list)
print(lv)
ldd = ['string', 'test', 'last']
lcc = ldd
ldd = ['string', lcc, lcc, 'last']
print('lcc; ', ldd)


#jiu
