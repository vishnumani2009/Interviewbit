'''
ven a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

import re
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A=re.sub('[^A-Za-z0-9]+', '', A)
        a=list(A)
        a="".join(a[::-1])
        #print a
        return a.upper()==A.upper()


'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
'''

import re
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        A=re.sub("[ +]"," ",A)
        A=A.split()
        #print A
        if len(A)>0:
            if A[len(A)-1].isalpha():
                return len(A[len(A)-1])
            else:
                return 0
        else:
            return 0

'''
STR-STR
'''
class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle=="" and haystack=="":
            return -1
        if needle=="" or haystack=="":
            return -1
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

