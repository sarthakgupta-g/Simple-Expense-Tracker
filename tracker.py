items=int(input("Enter the numnber of items you would like to include in the list"))
i=0
total=0.00

while(i<items):
  expense=float(input("Enter expense: "))
  total=total+expense
  i+=1
  
print(f"total is {total:.2f}")
