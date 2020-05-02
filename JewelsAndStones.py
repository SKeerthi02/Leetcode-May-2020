

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        counter = collections.Counter(S)
        for ele in J:
            count += counter[ele]
        return count
        
  *********************************Another Solution ***************************************
  
  class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        count = 0
        for char in S:
            if char in J:
                count += 1
        return count 
