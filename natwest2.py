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
