def palindrome(w):
    return "w is palindrome" if w == w[::-1] else "not a palindrome"
  #  return ["w is not palindrome", "w is palindrome"][w == w[::-1]]

def palindrome_core(w):
    count=0
    for i in range(len(w)):
        if w[i] == w[len(w)-1-i]:
            count+=1
    print(count)
    if count == len(w):
        return (f"{w} is palindrome")
    else:
        return (f"{w} is not palindrome")
