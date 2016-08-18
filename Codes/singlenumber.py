class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        a=A[0]
        for i in range(1,len(A)):
            a=a^A[i]
        return a
