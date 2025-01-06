#1. Reverse a String
# str="hello"
# print(str[::-1])


# 2. Count Vowels in a String
# str="hello"
# vowels="aeiou"
# count=0
# for i in str:
    # if i in vowels:
        # count+=1
# print(count)


# 3. Check Palindrome
# str="madam"
# if str==str[::-1]:
    # print("Palindrome")
# else:
    # print("Not Palindrome")

# 4. Count words in a String
# str="hello world"
# print(len(str.split()))

# 5. Removes duplicates in a String
# str="hello"
# print(set(str)) #converts str to set and set method removes duplicates elements


# 6. Count consonants in a String
# str="hello"
# vowels="aeiou"
# count=0
# for i in str:
    # if i not in vowels:
        # count+=1
# print(count)

# 7. Check for anagram
# str1="listen"
# str2="silent"
# print(sorted(str1))
# if sorted(str1)==sorted(str2):
    # print("Anagram")


# 8. Check Subsequence
# str1="hello"
# str2="hello world"
# i=j=0
# while i<len(str1) and j<len(str2):
    # if str1[i]==str2[j]:
        # i+=1
    # j+=1
# if i==len(str1):
    # print("Subsequence")
# else:
    # print("Not Subsequence")

# 9. Check Substring
# str1="hello"
# str2="hello world"
# if str1 in str2:
    # print("Substring")
# else:
    # print("Not Substring")


# 10. Length of the Longest Word
str="hello world"
print(max(len(i) for i in str.split()))
