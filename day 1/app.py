from flask import Flask, request, render_template ,redirect,session ,flash
from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename
import pandas as pd

#for encription and decription
import hashlib

#hash_object = hashlib.sha256()


CONNECTION_STRING = "mongodb+srv://praveenmalav09:Praveen123@cluster0.pwmxmn5.mongodb.net"
# Create a connection using MongoClient. 
client = MongoClient(CONNECTION_STRING)
mydatabase = client['student'] 
# table ha
mycollection=mydatabase['std_pannel'] 



app = Flask(__name__)

# this session key for passing the varibal one router to another , it make secure and unike
app.secret_key = 'the random string'

# image ka leya ha ya 
upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder


#main code
@app.route('/')
def home():  
    return render_template("index.html")

  


# @app.route('/login' , methods = ['GET', 'POST'])
# def login():
#     if request.method == 'POST':

#         email_cheak = (request.form['email'])
#         password_cheak= (request.form['password'])


#         password = hashlib.md5(password_cheak.encode('utf-8')).hexdigest()
#         print(password)

#         session["email_cheak"] = email_cheak
#         session["password_cheak"] = password


#         # yo data base sa koi particular ak value ko uutha raha ha
#         user_password_encrip=mycollection.find_one(  { 'email': email_cheak} )
#         user_password_encrip_mess=user_password_encrip['password']
#         print(user_password_encrip_mess)




#         if password  == user_password_encrip_mess:
#             #return redirect('/my_profile')
#             return redirect('/my_profile')
        
#         else:
#             return render_template("login.html"  , prediction_text="incorrect User Id or Password")
#         #return password_cheak


#     return render_template("login.html" ) 
  





@app.route('/login' , methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':

        email_cheak = (request.form['email'])
        password_cheak= (request.form['password'])


        password = hashlib.md5(password_cheak.encode('utf-8')).hexdigest()
        print(password)

        session["email_cheak"] = email_cheak
        session["password_cheak"] = password


        # yo data base sa koi particular ak value ko uutha raha ha
        user_password_encrip=mycollection.find_one(  { 'email': email_cheak} )

        user_password_encrip_mess=user_password_encrip['password']
        print(user_password_encrip_mess)




        if password  == user_password_encrip_mess:

            if len(user_password_encrip['mobile']) >= 10:
                
       
                return redirect('/my_profile')   # it redirect url
            else:
                flash('Mobile No shoud be change')
                return redirect('/my_profile')
        
        else:
            return render_template("login.html"  , prediction_text="incorrect User Id or Password")
        #return password_cheak


    return render_template("login.html" ) 
  




@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method == "POST":
        # be encoded to byte string before encryption
        
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        User_Ids = request.form['User_Ids']
        password =  request.form['password']
        user_dob =  request.form['user_dob']

        # be encoded to byte string before encryption

        password = hashlib.md5(password.encode('utf-8')).hexdigest()
          # dictionary to be added in the database 
        rec={ 
                    "name": name, 
                    "mobile": mobile, 
                    "email": email ,
                    "password":password,
                    "User_Ids": User_Ids,
                    "user_dob":user_dob
                    } 

                # inserting the data in the database 
        rec = mycollection.insert_one(rec)

        return redirect('/login')
            
    return render_template("registration.html")








@app.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    user_email=session.get("email_cheak",None)
    user_password=session.get("password_cheak",None)
    user_detail=mycollection.find_one(  { 'email': user_email, 'password': user_password} )

# printing keys and values separately
    values = user_detail.values()    
    user_detail_all_info= list(values)
    #display_img_user=user_detail_all_info[7]
    

   
    # for image display
    if request.method == 'POST':
        #(Update_Password)
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)

         
        #add image detail in data base
        mycollection.update_one({ 'email': user_email, 'password': user_password} ,{ '$set' : {'user_img':filename}} )

        # update the detail the data base

        # it is not run properly becouse it cheake image file also thats why

        # Update_Password = (request.args.get('Update_Password'))
        # print(Update_Password)
        # mycollection.update_one({ 'email': user_email, 'password': user_password} ,{ '$set' : {'User_Ids':Update_Password }} )

        return render_template('my_profile.html', img=img , user_name=user_detail_all_info[1] , user_mobile= user_detail_all_info[2],user_email=user_detail_all_info[3],user_User_Ids=user_detail_all_info[5], User_date=user_detail_all_info[6])
   

    if len(user_detail_all_info) == 8:
        return render_template('my_profile.html' , display_img=user_detail_all_info[7] , user_name=user_detail_all_info[1],user_mobile= user_detail_all_info[2],user_email=user_detail_all_info[3],user_User_Ids=user_detail_all_info[5], User_date=user_detail_all_info[6])

    else:
        return render_template('my_profile.html' , user_name=user_detail_all_info[1],user_mobile= user_detail_all_info[2],user_email=user_detail_all_info[3],user_User_Ids=user_detail_all_info[5], User_date=user_detail_all_info[6])




# for update the student detail bt the student
@app.route('/std_updates' ,methods=['POST','GET'])
def std_updates():

    user_email=session.get("email_cheak",None)
    user_password=session.get("password_cheak",None)
    user_detail=mycollection.find_one(  { 'email': user_email, 'password': user_password} )

    values = user_detail.values()    
    user_detail_all_info= list(values)

    Update_Password = (request.args.get('Update_Password'))
    #print(Update_Password)
    mycollection.update_one({ 'email': user_email, 'password': user_password} ,{ '$set' : {'User_Ids':Update_Password }} )

    return render_template("std_updates.html" ,display_img=user_detail_all_info[7],user_name=user_detail_all_info[1],user_mobile= user_detail_all_info[2],user_email=user_detail_all_info[3],user_User_Ids=user_detail_all_info[5], User_date=user_detail_all_info[6])


# logine by the admine

@app.route('/dashboad')# ,methods=['POST','GET'])
def dashboad():
    # decMessage = fernet.decrypt(name).decode() 
    # print("decrypted string: ", decMessage)
        

    a=list(mycollection.find({}))
    
    #decMessage = fernet.decrypt(a).decode() 
    print("decrypted string: ", a)
  
   
    return render_template("dashboad.html" , all_data=a )#,decript=fernet.decrypt(name).decode())




@app.route('/admine_update')# ,methods=['POST','GET'])
def admine_update():

    #a=list(mycollection.find({}))
   
    return render_template("admine_update.html" )#, all_data=a )



#fill_by_exel

@app.route('/fill_by_exel')
def fill_by_exel():


    dataset = pd.read_excel('//home//chinmay//Desktop//ishu//day 1//dummy.xls')
    

    for i in range(0,len(dataset)):

        # hash_object.update(dataset['password'][i].encode())
        # password = hash_object.hexdigest()
        password = hashlib.md5(dataset['password'][i].encode('utf-8')).hexdigest()

        mylist = [
                { 
                    "name": dataset['name'][i], "mobile": str(dataset['mobile'][i]), "email": dataset['email'][i] ,
                 "password":password,"User_Ids": str(dataset['User_Ids'][i]),"user_dob":dataset['user_dob'][i] 
                 }
        ]
        mycollection.insert_many(mylist)
    return render_template("fill_by_exel.html")


if __name__=="__main__":
  app.run(debug=True)