'''list_1 =['aabbc', 'abcabc', "abdddccc"]
list_2 = ['bbaad', 'abbaccd', "abdddcee"]
aabbc and bbaad has 2as, 2bs and diff is only one that is c,d
Output:
['c', 'd']
aabbc bbaad
'''
def one_diff_list(list_1,list_2):
    '''There are two lists having string elements, \
    I wanted the elements which are having\
    only one difference to the corresponding element in another list.'''
    for i in list_1:
        dict_i = sorted_l(list(i))
        for j in list_2:
            dict_j = sorted_l(list(j))
            for k,v in dict_i.items():
                if k in dict_j.keys() and v==dict_j[k]:
                    pass
                elif k not in dict_j.keys() and v==1:
                    l1 = list(set(i) - set(j))
                    l2 = list(set(j) - set(i))
                    if len(l1) == 1 and len(l2) == 1:
                        print(l1 + l2)
                        print(i, j)
one_diff_list(list_1,list_2)
