a=int(raw_input())
if a%4==0 and a%100==0 and a%400==0:
  print("leap year")
else:
  print("not a leap year")
