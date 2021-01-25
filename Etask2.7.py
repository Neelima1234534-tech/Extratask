def findPairs(lst, K):  
    res = [] 
    while lst: 
        num = lst.pop() 
        diff = K - num 
        if diff in lst: 
            res.append((diff, num)) 
          
    res.reverse() 
    return res 
      
# Driver code 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1] 
K = 8
print(findPairs(lst, K)) 