empty_list = []
print(empty_list)
numbers = [1, 2, 3, 4, 5] * 3
print("numbers")
triples = [1, 2, 3]
print("triples")
alist = [100, 200, 300, 400, 500]
alist = alist[::-1]
print(alist,"\n")
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
            if len(word) > 1 and word[0]== word[-1]:
                    ctr +=1
                    lst.append(word)
    print("list of words with first and last character same\n",lst)
    return ctr
count = match_words(['abc','cfc','xyz','aba','1221'])
print("number of words having first and last character same:",count)
l = [4,5,12,9,7,10,8]
print("original list :", l)
count = 0
for i in l:
    count += i
    avg = count/len(l)
    print("sum = ", count)
    print("average = ", avg)
    l.sort()
    print("smallest element is:", l[0])
    print("largest element is:",[-1])