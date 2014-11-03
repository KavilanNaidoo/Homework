#Kavilan Naidoo
#29-10-2014
#times table

table = int(input("Please enter the times table you would like to display: "))
count = 0
total = 0
while count <13:
    total = table * count
    print("{0:<0} x {1:^1} = {2:>2}".format(count,table,total))
    count = count + 1
    
    
