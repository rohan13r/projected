import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_prodID():
    #generate a random prod ID
    Prod_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Prod_ID

def Register(type,gamer_json_file,seller_json_file,Full_Name,Email,Password):
    '''Register the gamer/ogranizer based on the type with the given details'''
    if type.lower()=='seller':
        f=open(seller_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(gamer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password,
            'Wishlist' : [],
            'Cart':[],
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,gamer_json_file,seller_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='seller':
        f=open(seller_json_file,'r+')
    else:
        f=open(gamer_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Product(org,prod_json_file,prodId, prodtitle, prodtype,prodprice,available):
    '''Create an prod with the details entered by seller'''
    d = {
        'ProductID' : prodId,
        'Product Title': prodtitle,
        'Product Type' : prodtype,
        'Price Per Day' : prodprice,
        'Total Stock Available' : available,
    }
    f = open(prod_json_file,'r+')
    content=json.load(f)
    try:
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
    f.close()

def Update_product(org,prod_json_file,prod_id,detail_to_be_updated,updated_detail):
    '''Update prod by ID || Take the key name to be updated from gamer, then update the value entered by user for that key for the selected prod
    || Return True if successful else False'''
    f = open(prod_json_file,'w')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["ProductID"]==prod_id :
            content[i][detail_to_be_updated] = updated_detail
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
    f.close()
    return False

def View_all_products(prod_json_file):
    '''Read all the prods created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(prod_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
    


def View_prod_ByID(prod_json_file,prod_id):
    '''Return details of the prod for the prod ID entered by user'''
    f = open(prod_json_file,'r+')
    prod = {}
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return {}
    for i in range(len(content)):
        if content[i]["ID"]==prod_id:
            return content[i]
            
    f.close()
    return {}
def Register_for_prod(prod_json_file,prod_id,Full_Name):
    '''#Register the logged in gamer in the prod with the prod ID entered by gamer. 
    #(append Full Name inside the "Users Registered" list of the selected prod)) 
    #Return True if successful else return False
'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''#Write your code below this line
'''
    f = open(prod_json_file,'w')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["prod ID"]==prod_id and content[i]['Seats Available']>0:
            if content[i]["End Date"]>=date_today and content[i]["End Time"]>=current_time:           
                content[i]["Users Registered"].append(Full_Name)
                content[i]['Seats Available'] -=1
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                return True
    f.close()
    return False    
       

def fetch_all_prods(prod_json_file,Full_Name,prod_details,upcoming_ongoing):
    '''#View Registered prods | Fetch a list of all prods of the logged in memeber
'''
    '''#Append the details of all upcoming and ongoing prods list based on the today's date/time and prod's date/time
'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''#Write your code below this line
'''
    f = open(prod_json_file,'w')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return upcoming_ongoing
    for i in range(len(content)):
        if Full_Name in content[i]["Users Registered"]:
            if content[i]["End Date"]>=date_today and content[i]["End Time"]>=current_time:           
                upcoming_ongoing.append(content[i])
            
    f.close()
    return upcoming_ongoing    
    
    

def Update_Password(gamers_json_file,Full_Name,new_password):
    f=open(gamers_json_file,'w')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name :
            content[i]["Password"]== new_password
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
    f.close()
    return False
            
       
    '''#$Update the password of the gamer by taking a new passowrd || Return True if successful else return False
'''
    

def View_all_products(prod_json_file):
    '''#Read all the prods created | DO NOT change this function
'''
    '''#Already Implemented Helper Function
'''
    details=[]
    f=open(prod_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details

