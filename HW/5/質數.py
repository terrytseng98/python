num = int(input("請輸入一個數值: "))

# 質數大於 1
if num > 1:
   # 檢視因子
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是質數")
           print(i,"乘於",num//i,"是",num)
           break
   else:
       print(num,"是質數")

# 如果輸入的數值小於或等於 1，不是質數
else:
   print(num,"不是質數")