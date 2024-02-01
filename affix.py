num=int(input("Enter num:"))
result=str(num)
if num>=1000:
  result=str(num//1000)+'k'+str(num%1000)
  print(result)