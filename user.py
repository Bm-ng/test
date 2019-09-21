import base
import sys
import json
import hashlib
import shutil

#### Tham khao code cua anh Khien - phan status hay.
class user():
    id = None
    status = None
    email = None
    name = None

    def __init__(self,id, status, name):
        self.id = id
        #self.email = email
        self.status = status
        self.name = name
        datas = str(self.id) + "#" + str(self.status)+ "#" + str(self.name) + '\n'
        print (datas)
    def tao_nguoi_dung(self,email,password):
        self.password = password
        self.email = email
        datas = str(self.id)+ "#" + str(self.status) + "#" + str(self.email) + "#" + str(self.password) + "#" + str(self.name) +'\n'
        #print (datas)
        with open ('../DB/nguoi_dung.csv', 'a') as f:
            datas = f.write(datas)
    
    def tao_khach_hang(self, phone):
        self.phone = phone
        datas = str(self.id) + "#" + str(self.status) +"#" + str(self.phone) + "#" + str(self.name) + '\n'
        #print (datas)
        with open('../DB/khac_hang.csv', 'a') as f:
            datas = f.write(datas)

ds_nguoi_dung = []
ds_khach_hang = []

####################__Nguoi_dung__##################
def load_nguoi_dung():  
    with open('../DB/nguoi_dung.csv', 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) > 1:
                danhsach_nguoi_dung = {}
                # id#status#email#password#name \n
                danhsach_nguoi_dung["status"]= datas[1]
                danhsach_nguoi_dung["email"] = datas [2]
                danhsach_nguoi_dung["password"] = datas [3]
                ds_nguoi_dung.append(danhsach_nguoi_dung)
            line = f.readline()
    #print (ds_nguoi_dung)
    return ds_nguoi_dung

def xem_nguoi_dung():
    danhsach_nguoi_dung = []
    with open('../DB/nguoi_dung.csv' , 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) >1:
                danhsach_nguoi_dung = {}
                # #id#status#email#password#name \n
                danhsach_nguoi_dung["id"] = datas[0]
                danhsach_nguoi_dung["status"] = datas[1]
                danhsach_nguoi_dung["email"] = datas[2]
                danhsach_nguoi_dung["name"] = datas[3]
                if danhsach_nguoi_dung["name"].endswith('\n'):
                    danhsach_nguoi_dung["name"] = danhsach_nguoi_dung["name"][0:len(danhsach_nguoi_dung["name"]) -1]
                if int(datas["status"]) == 1 :
                    danhsach_nguoi_dung["status"] = 'active'
                else:
                    danhsach_nguoi_dung["status"] = 'inactive'
                datas = f.readline()
    print("+----------------------Nguoi dung--------------------+")
    print("+------+---------+------------------+----------------+")
    print("| STT  |  Status |      Email       |      Name      |")
    print("+------+---------+------------------+----------------+")
    print("|" +str(danhsach_nguoi_dung[id]).rjust(6,' ')+"|"+str(danhsach_nguoi_dung['status']).rjust(9,' ')+"|"+ str(danhsach_nguoi_dung['email']).rjust(18,' ')+"|"+str(danhsach_nguoi_dung['name']).rjust(16,' ')+"|")
    print("+------+---------+------------------+----------------+")

def tao_nguoi_dung_moi():
    load_nguoi_dung()
    email = input("Xin moi nhap vao email: ")
    i = 0
    for ten in ds_nguoi_dung:
        if email == ten["email"]:
            i +=1
    if i >0:
        print("Email da ton tai, vui long nhap email moi!")
        print(email)
    else:
        ds_id = base.tao_id('../DB/nguoi_dung.csv')
        id_new = int(ds_id["id"]) + 1
        name = input("Nhap vao ten cua ban: ") 
        password_txt = getpass("Xin moi nhap password moi: ")
        password_encode = hashlib.md5(password_txt.encode()).hexdigest()
        #print password_encode
        tk_nguoi_dung = user(id_new,'1',name,'')
        tk_nguoi_dung.tao_nguoi_dung(email,password_encode)

def sua_nguoi_dung():
    pass

def xoa_nguoi_dung():
    shutil.copy('../DB/nguoi_dung.csv','../DB.nguoi_dung_backup.csv')
    email = input("Nhap Email nguoi dung muon xoa: ")
    with open ('../DB/nguoi_dung_backup.csv', 'r') as f:
        with open ('../DB/nguoi_dung.csv', 'w') as wfile:
            line = f.readline()
            while line:
                datas = line.split("#")
                if len(datas) > 1: 
                    if emaill == datas[2]:
                        email = datas[2]
                        lines = line.replace("#1#", "#0#")
                        lines = wfile.write(lines)
                    else:
                        line = wfile.write(line)
                    line = f.readline()
                wfile.closed

    

##########################__khach_hang__###########################
def load_khach_hang():
    with open('../DB/khach_hang.csv', 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) > 1:
                danhsach_khach_hang ={}
                # stt#sdt#name \n
                danhsach_khach_hang["phone"] = datas[2]
                ds_khach_hang.append(danhsach_khach_hang)
            line = f.readline()
    #print (danhsach_khach_hang)
    return ds_khach_hang

