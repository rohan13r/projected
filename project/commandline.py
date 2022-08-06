from json.decoder import JSONDecodeError
import operations
import json
from json import JSONDecodeError

print("Welcome to Meet app")
tp=open('sellers.json','r+')
try:
    cp=json.load(tp)
    if 'admin@edyoda.com' not in str(cp):
        operations.Register('seller','gamers.json','sellers.json','admin','admin@edyoda.com','admin')
    tp.close()
except JSONDecodeError:
    operations.Register('seller','gamers.json','sellers.json','admin','admin@edyoda.com','admin')
c=1
while True:
    print("Press:")
    print("1: Register")
    print("2: Login")
    print("0: Exit")
    try:
        c=int(input())
    except ValueError:
        print("Please enter valid choice")
        continue
    if c==1:
        print("Press :")
        print("1: Register as seller")
        print("2: Register as gamer")
        try:
            in1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1==1:
            print("Enter Full Name:")
            F=input()
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                operations.Register('seller','gamers.json','sellers.json',F,E,P)
                print("Registered successfully as seller")
        elif in1==2:
            print("Enter Full Name:")
            F=input()
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                operations.Register('gamer','gamers.json','sellers.json',F,E,P)
                print("Registered successfully as Gamer")
        else:
            print("Please enter valid choice!")
    elif c==2:
        print("Press: ")
        print("1: Login as Seller")
        print("2: Login as Gamer")
        try:
            in1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1==1:
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            s=operations.Login('seller','gamers.json','sellers.json',E,P)
            if s==False:
                print("Invalid Credentials")
                continue
            else:
                t=open('sellers.json','r')
                cnt=json.load(t)
                t.close()
                n=""
                for i in range(len(cnt)):
                    if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
                        n=cnt[i]["Full Name"]
                        break
                print("Welcome "+str(n))
                while True:
                    print("Press :")
                    print("1: Create Products")
                    print("2: View all Products created")
                    print("3: View Product Details by ID")
                    print("4: Update Product")
                    print("0: Logout")
                    try:
                        i1=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if i1==1:
                        Ev_ID=operations.AutoGenerate_prodID()
                        print("prod ID Generated - "+str(Ev_ID))
                        print("Enter prod Name:")
                        Ev_Name=input()
                        print("Enter Start Date (YYYY-MM-DD):")
                        try:
                            Cap=int(input())
                        except ValueError:
                            print("Please enter valid data")
                            continue
                        else:
                            operations.Create_Product(n,'prod.json',Ev_ID,Ev_Name,[],Cap,Cap)
                            print("prod created successfully")
                    elif i1==2:
                        ev_details=operations.View_all_products(n,'prod.json')
                        if len(ev_details)==0:
                            print("No prods created yet! \n")
                        else:
                            for i in range(len(ev_details)):
                                print("Product ID: "+str(ev_details[i]['ID']))
                                print("Product Name: " +str(ev_details[i]['Name']))
                                print("Seller: " +str(ev_details[i]['seller']))
                                print("Seats Available: "+str(ev_details[i]['Seats Available']))
                                print('\n')
                    elif i1==3:
                        print("Enter Product ID")
                        ev_id=input()
                        f14=open('prod.json','r')
                        try:
                            c14=str(json.load(f14))
                            if ev_id not in c14:
                                print("Invalid prod ID")
                                continue
                        except JSONDecodeError:
                            print("prods not available")
                            continue
                        d=operations.View_prod_ByID('prod.json',ev_id)
                        print("prod Name: " +str(d[0]['Name']))
                        print("seller: " +str(d[0]['seller']))
                        print("Seats Available: "+str(d[0]['Seats Available']))
                        print('\n')
                    elif i1==4:
                        print("Enter prod ID:")
                        ev_id=input()
                        print("Enter detail to be Updated ( Name || Start Date || Start Time || End Time || End Date ): ")
                        dtl=input()
                        print("Enter new value:")
                        updtl=input()
                        f11=open('prod.json','r')
                        try:
                            c11=str(json.load(f11))
                            f11.close()
                        except JSONDecodeError:
                            print("No prods created")
                            f11.close()
                            continue
                        if ev_id not in c11:
                            print("Invalid prod ID")
                            continue
                        if (len(ev_id)*len(dtl)*len(updtl))==0:
                            print("Please enter valid data")
                            continue
                        else:
                            ch=operations.Update_product(n,'prod.json',ev_id,dtl,updtl)
                        if ch==False:
                            print("Cannot update prod")
                        else:
                            print("prod updated successfully")
                    elif i1==0:
                        break
                    else:
                        print("Ivalid Option")
        elif in1==2:
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            s=operations.Login('gamer','gamers.json','sellers.json',E,P)
            if s==False:
                print("Invalid Credentials")
                continue
            else:
                t=open('gamers.json','r')
                cnt=json.load(t)
                t.close()
                n=""
                for i in range(len(cnt)):
                    if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
                        n=cnt[i]["Full Name"]
                        break
                print("Welcome "+str(n))
                while True:
                    print("Press:")
                    print("1: View Registered prods")
                    print("2: Register for an prod")
                    print("3: Update Password")
                    print("4: View prod Details by ID")
                    print("0: Logout")
                    try:
                        i=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if i==1:
                        all_prods=[]
                        upcoming_ongoing=[]
                        operations.fetch_all_prods('prod.json',n,all_prods,upcoming_ongoing)
                        print("All Upcoming/Ongoing prods: ")
                        for i in range(len(upcoming_ongoing)):
                            print("prod Name: " +str(upcoming_ongoing[i]['Name']))
                            print("seller: " +str(upcoming_ongoing[i]['seller']))
                            print('\n')
                    elif i==2:
                        l=operations.View_all_products('prod.json')
                        if len(l)==0:
                            print("No prods available")
                        else:
                            print("All prods: ")
                            for i in range(len(l)):
                                t=l[i]
                                print("prod ID: "+str(t['ID']))
                                print("prod Name: " +str(t['Name']))
                                print("Seller: "+str(t['seller']))
                                print("Seats Available: "+str(t['Seats Available']))
                                print("Total Seats: "+str(t['Capacity']))
                                print('\n')
                        print("Enter prod ID: ")
                        prod_id=input()
                        ch=operations.Register_for_prod('prod.json',prod_id,n)
                        f44=open('prod.json','r')
                        c44=str(json.load(f44))
                        if prod_id not in c44:
                            print("Invalid prod ID")
                        if ch==True:
                            print("Successfully Registered")
                        else:
                            print("prod seats are full! \n")
                    elif i==3:
                        print("Enter new password")
                        pswd=input()
                        if(len(pswd))<4:
                            print("Please enter valid data")
                            continue
                        op=operations.Update_Password('gamers.json',n,pswd)
                        if op==True:
                            print("Password updated successfully")
                        else:
                            print("Cannot update password")
                    elif i==4:
                        print("Enter prod ID")
                        ev_id=input()
                        f14=open('prod.json','r')
                        try:
                            c14=str(json.load(f14))
                            if ev_id not in c14:
                                print("Invalid prod ID")
                                continue
                        except JSONDecodeError:
                            print("prods not available")
                            continue
                        d=operations.View_prod_ByID('prod.json',ev_id)
                        print("prod Name: " +str(d[0]['Name']))
                        print("Seller: "+str(d[0]["seller"]))
                        print("Seats Available: "+str(d[0]['Seats Available']))
                        print('\n')
                    elif i==0:
                        break
                    else:
                        print("Invalid Choice, Please enter again")
                        continue
    elif c==0:
        break
    else:
        print("Invalid Choice, Please enter again")
        continue

