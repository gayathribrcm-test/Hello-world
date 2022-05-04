def dup_letter_remove(wrd):
    print("".join(dict.fromkeys(list(wrd))))
def dup_letter(wrd):
    l={}
    l1=[]
    for i in range(0,len(wrd)):
        l[wrd[i]]=l.get(wrd[i],[])+[i]
    for k,v in l.items():
            l1.append(wrd[v[0]])
    return "".join(l1)

def dup_let(wrd):
    s=''
    for i in wrd:
        if (i in s):
            continue
        else:
            s=s+i
    print(s)
