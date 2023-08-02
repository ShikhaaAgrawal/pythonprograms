#list
#1.LIST
#a. IS the given list divisible by 3 or not
noof_days = [2,5,8,7,4,6,15,4,7,9,2]
for x in noof_days:
    if x%3==0:
        print (x," in list is divisible by 3 ")
    else:
        print(x," in list is not divisible by 3") 
#b.square of even numbers in the list
print ("\n\nthe sum of even numbers are")
sum=0
for x in noof_days:
    if x%2==0:
        print(" the square of ", x," is ", x**2)
        sum=sum+x # c.sum of digits of all even munbers
print("\n\nsum of even numbers in the list is",sum)
# d.removing the duplicate elements of the list 
# (by converting the list into set because set automatically removes the duplicate elements )
rem= list(set(noof_days)) 
print("\n\nthe list with the duplicate elements removed is :", rem)

#dictionary
#a function to display the starting date of events 
event_date={ "holi":"25 march 2023","diwali": " 15 november 2023",
            " sunday brunch ": " every sunday", " christmas ": "24 december 2023" }
ev_name=input(" enter event name : ")
def func(ev_name):
    print(event_date[ev_name])
    
    
      
                  