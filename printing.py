import functionality
import string
import json
from json import JSONDecodeError

print("Welcome to Food Ordering App")
c=1
while c!=0:
    print("Press:")
    print("0: Exit")
    print("1: Register as Admin")
    print("2: Register as User")
    print("3: Login as Admin")
    print("4: Login as User")
    c=int(input())
    if c==1:
        print("Enter Full Name:")
        F=input()
        print("Enter Email:")
        E=input()
        print("Enter Password:")
        P=input()
        print("Enter Address:")
        A=input()
        print("enter phone number")
        N=input()
        if '@' in E and '.com' in E and len(P)!=0 and len(E)!=0 and len(A)!=0 and len(F)!=0:
            functionality.Register('admin','Food Ordering App\\user.json','Food Ordering App\\admin.json',F,A,E,P,N)
            print("Registered Successfully as Admin !!")
        else:
            print("Please Enter Valid Data")
    elif c==2:
        print("Enter Full Name:")
        F=input()
        print("Enter Email:")
        E=input()
        print("Enter Password:")
        P=input()
        print("Enter Address:")
        A=input()
        print("Enter the phone number:")
        N=input()
        if '@' in E and '.com' in E and len(P)!=0 and len(E)!=0 and len(A)!=0 and len(F)!=0 and len(N)!=0:
            ch=functionality.Register('user','Food Ordering App\\user.json','Food Ordering App\\admin.json',F,A,E,P,N)
            if ch==True:
                print("Registered Successfully as Member !!")
            else:
                print("Registration Unsuccessful")
        else:
            print("Please Enter Valid Data")
    elif c==3:
        print("Enter Email")
        E=input()
        print("Enter Password")
        P=input()
        success=functionality.Login('admin','Food Ordering App\\user.json','Food Ordering App\\admin.json',E,P)
        if success==True:
        
            temp=open('Food Ordering App\\admin.json','r')
            adms=json.load(temp)
            owner_details=[]
            for i in range(len(adms)):
                if adms[i]["Email"]==E and adms[i]["Password"]==P:
                    owner_details.append(adms[i])
                    break
            while True:
                print("Press: ")
                print("1: Create New Food items")
                print("2: View food items list")
                print("3: Update food items")
                print("4: Delete food items")
                print("0: Logout")
                in1=int(input())
                if in1==1:
                    p_id=functionality.AutoGenerate_ProductID()
                    print("Food ID generated is "+str(p_id))
                    print("Enter Item Name: ")
                    Item_Name=input()
                    print("Enter Quantity of item: ")
                    Quantity_item=input()
                    print("Enter Price: ")
                    Item_Price=input()
                    print("Enter Discount: ")
                    Item_Discount=input()
                    if '%' not in Item_Discount:
                        Item_Discount+="%"
                    print("Enter Available Stock: ")
                    Item_Stock=input()
                    try:
                        int(Item_Price)
                    except ValueError:
                        Item_Price=""
                    try:
                        int(Item_Stock)
                    except ValueError:
                        Item_Stock=""
                    if len(p_id)!=0 and len(Item_Name)!=0 and len(Item_Price)!=0 and len(Item_Discount)!=0 and len(Item_Discount)!=0 and len(Item_Stock)!=0:
                        ch=functionality.Create_Product(owner_details[0]["Full Name"],'Food Ordering App\\item.json',p_id,Item_Name,Quantity_item,int(Item_Price),Item_Discount,int(Item_Stock))
                        if ch==True:
                            print("Item successfully created !!")
                        else:
                            print("Item creation unsuccessful, Please Enter Valid Data")
                    else:
                        print("Item creation unsuccessful, Please Enter Valid Data")
                elif in1==2:
                    print("Press :")
                    print("1: View All Items")
                    print("2: View Items by Product ID")
                    in2=int(input())
                    if in2==1:
                        l=functionality.Read_Products(owner_details[0]["Full Name"],'Food Ordering App\\item.json')
                        if len(l)==0:
                            print("No items created till now!!")
                        else:
                            for i in range(len(l)):
                                print("Product ID: "+str(l[i]['Product ID']))
                                print("Item Name: "+str(l[i]['Item Name']))
                                print("Quantity_Item: "+str(l[i]['Quantity Item']))
                                print("Price: "+str(l[i]['Price']))
                                print("Discount: "+str(l[i]['Discount']))
                                print("Stock Available:"+str(l[i]['Total Stock Available']))
                    elif in2==2:
                        print("Enter Product ID :")
                        pr_id=input()
                        dtls=[]
                        functionality.Read_Product_By_ID('Food Ordering App\\item.json',pr_id,dtls)
                        if len(dtls)==0:
                            print("Invalid ID")
                        else:
                            print("Item Name: "+str(dtls[i]["Item Name"]))
                            print("Quantity: "+str(dtls[i]["Quantity"]))
                            print("Price: "+str(dtls[i]["Price"]))
                            print("Discount: "+str(dtls[i]["Discount"]))
                            print("Stock Available: "+str(dtls[i]["Total Stock Available"]))
                    else:
                        print("Invalid  Choice")
                elif in1==3:
                    print("Enter Product ID: ")
                    prd_id=input()
                    print("Enter Detail to be udpdated: ")
                    detail_tbu=input()
                    print("Enter Updated detail: ")
                    u_detail=input()
                    dn=functionality.Update_Product('Food Ordering App\\item.json',prd_id,detail_tbu,u_detail)
                    if dn==True:
                        print("Item Edit Successfully")
                    else:
                        print("Invalid Item Detail")
                elif in1==4:
                    print("Enter Product ID: ")
                    pr_id=input()
                    dn=functionality.Delete_Product('Food Ordering App\\item.json',pr_id)
                    if dn==True:
                        print("Item Deleted Successfully")
                    else:
                        print("Invalid Product ID")
                elif in1==0:
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Credentials")
    elif c==4:
        print("Enter Email")
        E=input()
        print("Enter Password")
        P=input()
        success=functionality.Login('user','Food Ordering App\\user.json','Food Ordering App\\admin.json',E,P)
        if success==True:
            temp=open('Food Ordering App\\user.json','r')
            mems=json.load(temp)
            user_details=[]
            for i in range(len(mems)):
                if mems[i]["Email"]==E and mems[i]["Password"]==P:
                    user_details.append(mems[i])
                    break
            while True:
                print("Press: ")
                print("1: Create New Order")
                print("2: View Order History")
                print("3: Update Profile")
                print("4: Logout")
                in3=int(input())
                if in3==1:
                    temp=open('Food Ordering App\\item.json','r')
                    try:
                        content=json.load(temp)
                        temp.close()
                        print("Products Available:")
                        for i in range(len(content)):
                            print(content[i]['Product ID'],content[i]['Item Name'],str(content[i]['Price'])+"INR")
                        print("Enter Product ID")
                        id_pr=input()
                        print("Enter Quantity")
                        q=int(input())
                        o_id=functionality.AutoGenerate_OrderID()
                        ch=functionality.Place_Order('Food Ordering App\\order.json',user_details[0]['Full Name'],user_details[0]["Address"],'Food Ordering App\\item.json',id_pr,q,o_id)
        
                        if ch==True:
                            print("Order Successfully Placed with order id: "+str(o_id))
                        else:
                            print("Order Unsuccessful")
                    except JSONDecodeError:
                        print("No Products Available")
                elif in3==2:
                    l=[]
                    functionality.Order_History('Food Ordering App\\order.json',user_details[0]['Full Name'],l)
                    if len(l)==0:
                        print("No orders Placed Yet !!")
                    else:
                        for i in range(len(l)):
                            print("Order ID: "+str(l[i]['Order ID']))
                            print("Item Name: "+str(l[i]['Item Name']))
                            print("MRP: "+str(l[i]['Price']))
                            print("Discount: "+str(l[i]['Discount']))
                            print("Price after Discount: "+str(l[i]['Price after Discount']))
                            print("Quantity: "+str(l[i]['Quantity']))
                            print("Grand Total: "+str(l[i]['Total Cost']))
                            print("Delivering to: "+str(l[i]['Delivering to']))
                elif in3==3:
                    print("Enter Detail to be updated: ")
                    dtl_tbu=input()
                    print("Enter Update Detail: ")
                    up_dtl=input()
                    ch=functionality.Update_Member('Food Ordering App\\user.json',user_details[0]['Full Name'],dtl_tbu,up_dtl)
                    if ch==True:
                        print("Detail Updated Successfully !!")
                    else:
                        print("Invalid Detail")
                elif in3==4:
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Credentials")
    elif c==0:
        break
    else:
        print("Invalid Choice")

