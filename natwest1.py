
#NatWest Code Test  
#We appreciate you taking the time to complete this test, hopefully you'll find it interesting too. You can 
#choose the coding language of your choice to provide the solution between JavaScript and Python. 
 
#Problem Statement 
#You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for 
#each year of their total age. They will only be able to blow out the tallest of the candles. Count how many 
#candles are tallest. 
 
#Example 
#candles = [4, 4, 1, 3] 
#The maximum height candles are 4 units high. There are 2 of them, so return 2. 
 
#Function Description 
#Create the function birthdayCakeCandles in the editor below. 
#birthdayCakeCandles has the following parameter(s): 
#• int candles[n]: the candle heights 
#Returns 
#• int: the number of candles that are tallest 
#Input Format 
#The first line contains a single integer, n, the size of candles[]. 
#The second line contains n space-separated integers, where each integer i describes the height of 
#candles[i]. 
#Sample Input 
 
#4  
#3 2 1 3 
 
#Sample Output 
 
#2 
 
#Explanation 
#Candle heights are [3, 2, 1, 3]. The tallest candles are 3 units, and there are 2 of them. 
  
 
#Deliverables  
#• Project containing source code for your solution.  
#• Any instructions to run the solution.  
#• A short description of what you have implemented. 
 
#Please check-in your code to a GitHub repository, add a detailed readme file and provide details and 
#access. 
 
print("Welcome to the Birthday Party")
age=int(input("enter the age of children:"))
n=int(input("length of number of candles:"))
if age==n:
    candle_height=[]
    for i in range (n):
        element=int(input("enter the candles:"))
        candle_height.append(element)
    print('height of candles are:',candle_height)
    max=0
    i=0
    while i<len(candle_height):
            c=0
            if candle_height[i]>max :
                max=candle_height[i]
            i+=1
            for num in candle_height:
                if num==max:
                    c=c+1
    print( "highest candle:",max,'\n',"number of highest candles:",c)
else:
    print(" It is not execute,because age and candles are not equal")