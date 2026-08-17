items=int(input("Enter the numnber of items you would like to include in the list"))
i=0
total=0.00
expenses=[]


while(i<items):
  expenses.append(float(input("Enter expense: ")))
  i+=1

i=0
while(i<items):
  total+=expenses[i]
  i+=1
  
print(f"total is {total:.2f}")
  
