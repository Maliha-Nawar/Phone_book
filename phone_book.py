phone_book={'gilly':+880197,'bil':+88014,'jenny':+88011}
x=1
while x<6:
    name=input("Attempt "+str(x)+"/5) whose phone no. would you like to collect?(Press enter to exit): ")
    if name in phone_book.keys():
        print(name+"'s phone no. is: "+str(phone_book[name]))
    elif name == '':
        break
    else:
        ans=input("sorry, we don't have any record by this name...would you like to add this here? ")
        if ans=="yes":
            no=input('please insert the no. : ')
            phone_book[name]=no
            print("phone_book has been updated")
    x=x+1
