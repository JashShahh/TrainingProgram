def isSubsetSum(set, n, sum) :
    
    if (sum == 0) :
        return True
    if (n == 0 and sum != 0) :
        return False
   
   
    if (set[n - 1] > sum) :
        return isSubsetSum(set, n - 1, sum);
   
    
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
      

n = int(input("Enter the number of elements:")) 
print("Enter the elements:") 
set = [] 
for i in range(0, n): 
  set.append(int(input("")))
sum = int(input("The Sum is: "))
if (isSubsetSum(set, n, sum) == True) :
    print("Found a subset with given sum")
else :
    print("No subset with given sum")
