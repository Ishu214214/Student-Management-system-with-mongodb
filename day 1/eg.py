# import rsa

# publicKey, privateKey = rsa.newkeys(512)

# # this is the string that we will be encrypting
# message = "hello geeks"

# encMessage = rsa.encrypt(message.encode(), 
# 						publicKey)

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# decMessage = rsa.decrypt(encMessage, privateKey).decode()

# print("decrypted string: ", decMessage)
import hashlib
key="hello"

key = hashlib.md5(key.encode('utf-8')).hexdigest()

print(key)


















# from pymongo import MongoClient
# import pandas as pd


# CONNECTION_STRING = "mongodb+srv://praveenmalav09:Praveen123@cluster0.pwmxmn5.mongodb.net"
# # Create a connection using MongoClient. 
# client = MongoClient(CONNECTION_STRING)
# mydatabase = client['student'] 
# # table ha
# mycollection=mydatabase['std_pannel'] 


# dataset = pd.read_excel('//home//chinmay//Desktop//ishu//day 1//dummy.xls')

# for i in range(0,len(dataset)):
#     mylist = [
#    { "name": dataset['name'][i], "mobile": str(dataset['mobile'][i]), "email": dataset['email'][i] ,"password":dataset['password'][i],"User_Ids": str(dataset['User_Ids'][i]),"user_dob":dataset['user_dob'][i] }


#     ]
#     mycollection.insert_many(mylist)



# from cryptography.fernet import Fernet


# message = "hello geeks"



# key = Fernet.generate_key()



# fernet = Fernet(key)

# encMessage = fernet.encrypt(message.encode())

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# decMessage = fernet.decrypt(encMessage).decode()

# print("decrypted string: ", decMessage)




# import bcrypt 

# # example password 
# password = 'password123'

# # converting password to array of bytes 
# # bytes = password.encode('utf-8') 

# # # generating the salt 
# # salt = bcrypt.gensalt() 

# # # Hashing the password 
# # hash = bcrypt.hashpw(bytes, salt) 

# # print(hash)


# Password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# print(Password)



