
#NatWest Code Test  
#Thank you for taking the time to complete this code test. We appreciate you taking the time to complete 
#this test, hopefully you'll find it interesting too. You can choose the coding language of your choice to 
#provide the solution between JavaScript and Python. 
 
#Problem Statement 
#Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers 
#in S is not evenly divisible by k. 
 
#Example 
 #S = [19, 10, 12, 10, 24, 25, 22]     k = 4 
#One of the arrays that can be created is S[0] = [10, 12, 25]. Another is S[1] = [19, 22, 24]. After testing all 
#permutations, the maximum length solution array has 3 elements. 
 
#Function Description 
#Complete the nonDivisibleSubset function in the editor below. 
#nonDivisibleSubset has the following parameter(s): 
#• int S[n]: an array of integers 
#• int k: the divisor 
#Returns 
#• int: the length of the longest subset of S meeting the criteria 
#Input Format 
#The first line contains 2 space-separated integers, n and k, the number of values in S and the non factor. 
#The second line contains n space-separated integers, each an S[i], the unique 
#values of the set. 
 
#Constraints 
#• All of the given numbers are distinct. 
#Sample Input 
#STDIN 
#---------- 
#Function 
#-------------------- 
#4 3 
#1 7 2 4 
#S[ ] size n = 4, k = 3  
#S = [1, 7, 2, 4] 
 
#Sample Output 
 
#3 
 
#Explanation 
#The sums of all permutations of two elements from S = {1, 7, 2, 4} are: 
 
#1 + 7 = 8 
#1 + 2 = 3 
#1 + 4 = 5 
#7 + 2 = 9 
#7 + 4 = 11 
#2 + 4 = 6  
 
#Only S = {1, 7, 4} will not ever sum to a multiple of k = 3. 
 
#Deliverables  
#• Project containing source code for your solution.  
#• Any instructions to run the solution.  
#• A short description of what you have implemented. 
 
#Please check-in your code to a GitHub repository, add a detailed readme file and provide details and 
#access. 
 
n=int(input("enter the length of list:"))
k=int(input("enter the divsible value:"))
a=[]
sum_list=[]
for i in range(n):
    val=int(input("enter the numbers:"))
    a.append(val)
    print("element in list:",a)
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        sum=a[i]+a[j]
        sum_list.append(sum)
        j=j+1
    i=i+1
print(' total subset are:',sum_list)
s=0
count=0
while s<len(sum_list):
    if sum_list[s]%k!=0:
        count+=1
    s=s+1
print("number of  non divisible subsets are:",count)
    


