#!/usr/bin/python3
from getpass import getpass
import base64
import hashlib
import menu
import user

print("+----------------------------------------------+")
print("|                    LOGIN                     |")
print("+----------------------------------------------+")

def Login():
    loginlist = []
    logindict = {}
    ds_nguoi_dung = user.load_nguoi_dung()
    # print("ds_nguoi_dung:", ds_nguoi_dung)
    logindict["status"] = '1'
    logindict["email"] = input("Nhap tai khoan: ")
    password_txt = getpass("Nhap vao password: ")
    logindict["password"] = hashlib.md5(password_txt.encode()).hexdigest()
    loginlist.append(logindict)
    
    sellerCount = 0
    adminCount = 0
    count = 0
    for sellerUser in ds_nguoi_dung:
        if logindict["status"] == sellerUser["status"]  and logindict["email"] == sellerUser["email"] and logindict["password"] == sellerUser["password"]:
            sellerCount = 1
            # print("log so mot", sellerCount)
            if logindict["status"] == sellerUser["status"]  and logindict["email"] == sellerUser["email"] and logindict["password"] == sellerUser["password"] and logindict["email"] == 'admin@gmail.com':
                adminCount = 1
                # print("log so hai",adminCount)
        else:
            count = 3
                # print("log so ba",count)
    if sellerCount > 0 and adminCount > 0:
        print("Xin chao ",logindict["email"]," ban da dang nhap thanh cong voi quyen ADMIN")
        menu.menu1()
    if sellerCount > 0 and adminCount == 0:
        print("Xin chao ",logindict["email"]," ban da dang nhap thanh cong voi quyen SELLER")
        menu.menu2()
    if count >  1:
        print("Sai thao tac")
        return         
Login()