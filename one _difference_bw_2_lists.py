'''list_1 =['aabbc', 'abcabc', "abdddccc"]
list_2 = ['bbaad', 'abbaccd', "abdddcee"]
aabbc and bbaad has 2as, 2bs and diff is only one that is c,d
Output:
['c', 'd']
aabbc bbaad
'''
def sorted_l(l1):
    d1={}
    for j in l1:
            d1[j]=d1.get(j,0)+1
    return dict(sorted(d1.items(),key=lambda kv:kv[0]))
def one_diff_list(list_1,list_2):
    '''There are two lists having string elements, \
    I wanted the elements which are having\
    only one difference to the corresponding element in another list.'''
    for i in list_1: #iterate each element in list aabbc
        dict_i = sorted_l(list(i)) #convert to dict {'a': 2, 'b': 2, 'c': 1}
        for j in list_2:
            dict_j = sorted_l(list(j)) #convert to dict {'a': 2, 'b': 2, 'd': 1}
            for k,v in dict_i.items():#compare every key of dict i in dict j and ignore if same key,value 
                if k in dict_j.keys() and v==dict_j[k]:
                    pass
                elif k not in dict_j.keys() and v==1:#else k of i is not  in dictj and  v==1, take the diff of dict i and dict j keys,if len of diff is one print 
                    l1 = list(set(i) - set(j))
                    l2 = list(set(j) - set(i))
                    if len(l1) == 1 and len(l2) == 1:
                        print(l1 + l2)
                        print(i, j)
one_diff_list(list_1,list_2)
