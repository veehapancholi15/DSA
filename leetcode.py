# #2185
# def prefixCount(words: list[str], pref: str) -> int:
#     count = 0
#     for i in range(len(words)):
#         if words[i][:len(pref):] == pref:
#             count += 1
#     return count
    
# words = ["pay","attention","practice","attend"]
# pref = "at"
# print(prefixCount(words,pref))

#771


# #3110
# def scoreOfString(s: str) -> int:
#     for i in range(len(s-1)):
#         res += abs(ord(s[i]-ord(s[i+1])))
#     return res 
# s = "hello"
# print(scoreOfString,s)
 
# #9
# def isPalindrome(self, x: int, rev: int) -> bool:
#     str1 = 
# # print(isPalindrome(rev))


#916
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]

split_results = [list(word) for word in words1]

for split_word in split_results:
    print(split_word)
