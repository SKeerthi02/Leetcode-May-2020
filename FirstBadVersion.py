
******************Jugad method :P *********************
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1                             # 2 , 2
        low, high, mid = 1, n, n//2 
        while True:
            if not isBadVersion(mid):   
                low = mid 
                mid = (low + high) //2 + 1
            elif isBadVersion(mid-1):
                high = mid     
                mid = (low + high) //2
            else:
                return mid

********************************************************************************************************************
Optimized*****

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        #my code begins here
        low, high = 1 , n
        while low < high:
            mid = (low + high)//2
            if not isBadVersion(mid):   
                low = mid + 1
            else:
                high = mid -1      
        return low if isBadVersion(low) else low + 1
