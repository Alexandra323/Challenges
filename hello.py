#CHALLENGES TO PRACTICE

#list reverse, string reverse
# l=[1,2,3]
# l.reverse()
# print(l)
# string = "Hello"
# string = string[::-1]
# print(string)

  
#FUzzBUZZ
# l = []
# count1=0
# count2=0
# count3=0
# for num in range(100):
#     l.append(num)
#     if num%3 ==0 and num%5 ==0:
#         count1+=1
#         print("BloombergLP")

#     elif num%3 ==0:
#         count2+=1
#         print("bloomberg")
#     elif num%5 == 0:
#         count3+=1
#         print("LP")
#     else: print(num)    

# print(count1, count2, count3)


# count how many of each vowels in a string
vowels = 'aeiouy'
string = 'alexandra'
count = 0
dic = {}
for i in string:
    if i in vowels:
        if i not in dic:    
            dic[i] = 1
        else: 
            dic[i] += 1
print(count) 
print(dic)

#BL2 indentify if the 2 given strings has the same letters
string = 'acbd'
s = 'abdc'
# if sorted(string) == sorted(s):
#     print("It is ")
# else:print("It is not")

#get the duplicate values in the list

# r = [1,22,1,3,3,4,5,6,7,8,]
# duplicate =[] #
# unique= [] # 
# for i in r:
#     if i not in unique:
#         unique.append(i)
#     else:
#         duplicate.append(i)
# print(duplicate)
# print(unique)


# l= [1,1,3,2]
# l2 = set(l)
# print(l2)
    
# n = [2,3,4,5] #4
# # for i in range(len(n)): 
# #     print(n[i])
# print('len->',len(n))
# j = 0
# while ( j < len(n) ): 
#     print(n[j], j)
#     j+=1

#####END



