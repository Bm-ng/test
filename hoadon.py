import json
import os
import sanpham
import base
import datetime

now = datetime.datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
date_dir = now.strftime("%d_%m_%Y")


def max_id():
    with open('../hoa_don/ma_hoa_don.txt', 'r') as string:
        line = string.readline()
        while line:
            datas = line.lstrip("HD")
            line = string.readline()
        return datas
    

ds_hoa_don=[]
sp_ban_ra = {}


def tao_hd():
    ma_hd = int(max_id()) + 1
    ma_hd = str(format(ma_hd, '03d'))
    print("Hoa don: HD" + ma_hd)
    hoa_don={}
    hoa_don["ma_hd"] = "IN" + ma_hd
    hoa_don["ngay_hd"]= date_time
    hoa_don["khach_hang"]= input("Ten khach hang :")
    hoa_don["tien_truoc_thue"] = 0
    hoa_don["thue"] = 0.10
    hoa_don["tong_tien"] = 0
    hoa_don["ds_sp"] = []
    stt = 1
    nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
    while nhaphanghoa.upper() == 'Y':
        base.xem_ds_sp()
        hanghoa = {}
        hanghoa["stt"] = stt
        id_hang_hoa = base.kiem_tra_id(int(input("nhap id hang hoa: ")))
        while id_hang_hoa is None:
            id_hang_hoa = base.kiem_tra_id(int(input("ID hang hoa sai. Hay nhap lai, : ")))
            base.xem_ds_sp()
        while id_hang_hoa is not None:
            data = base.load_id_sp(int(id_hang_hoa))
            hanghoa["ten"] = data[0]
            hanghoa["so_luong"] = int(input("Nhap vao so luong: "))
            hanghoa["don_gia"] = int(data[1])
            hanghoa["thanh_tien"] = hanghoa["so_luong"] * hanghoa["don_gia"]
                
            if hanghoa["ten"] in sp_ban_ra:
                sp_ban_ra[hanghoa["ten"]]["tongso"] = sp_ban_ra[hanghoa["ten"]]["tongso"] + hanghoa["so_luong"]
                sp_ban_ra[hanghoa["ten"]]["doanhthu"] = sp_ban_ra[hanghoa["ten"]]["doanhthu"] + hanghoa["thanh_tien"]
            else:
                sp_ban_ra[hanghoa["ten"]] = {
                "tongso": hanghoa["so_luong"],
                "doanhthu": hanghoa["thanh_tien"]
                }

            hoa_don["ds_sp"].append(hanghoa)
            hoa_don["tien_truoc_thue"] = hoa_don["tien_truoc_thue"] + (hanghoa["thanh_tien"])
            break 
        nhaphanghoa = input("=> Ban co muon nhap tiep hang hoa khong (y/n): ")
        stt += 1
    hoa_don["tong_tien"] = hoa_don["tien_truoc_thue"] + hoa_don["tien_truoc_thue"] * hoa_don["thue"]
    #ds_hoa_don.append(hoa_don)
    print("Kiemtra:", hoa_don)
    filename = "IN" + ma_hd +".json"
    with open('../hoa_don/' + filename, 'w') as f:
        json.dump(hoa_don, f)
    data = open("../hoa_don/ma_hoa_don.txt", "a")
    data.write("IN" + ma_hd +"\n")
        

def file_name_exists():
    ma_hd_can_xem = ''
    while not os.path.isfile('../hoa_don/'+ ma_hd_can_xem +'.json'):
        ma_hd_can_xem = input("nhap so hoa don can xem:")  
    return ma_hd_can_xem

def view_invoice():
    ma_hd_canxem = file_name_exists()
    with open('../hoa_don/' + ma_hd_canxem + '.json', 'r') as f:
        invoice = json.load(f)
        
        print("==========================HOA DON MUA HANG==========================")
        print("So hoa don:",invoice["ma_hd"].rjust(15))
        print("Ngay xuat:",invoice["ngay_hd"].rjust(31))
        print("Ten khach hang:",invoice["khach_hang"].rjust(13))
        print("Tong tien truoc thue",str(invoice["tien_truoc_thue"]).rjust(6))
        print("Tong tien sau thue ",str('%.2f' % invoice["tong_tien"]).rjust(10))
        print("_________________________________thong tin hoa don_________________________________")
        print("+-------+-------------------------+----------+---------------+------------------+")
        print("|  STT  |         hang hoa        | so luong |    don gia    |    thanh tien    |")
        print("+-------+-------------------------+----------+---------------+------------------+")
                    
        for hanghoa in invoice["ds_sp"]:
        #print("In dong hang hoa o day")
            print("|",str((hanghoa['stt'])).center(5),"|" ,hanghoa['ten'].rjust(23), "|",str(hanghoa['so_luong']).center(8),"|",str(hanghoa['don_gia']).center(13),"|",str(hanghoa['thanh_tien']).center(16),"|")
        print("+-------+-------------------------+----------+---------------+------------------+")
        #end of Hoa don se in o day



