import os
import phan_loai

#product

ds_sp = []

def load_sp():
    files = os.listdir("../DB")
    if "san_pham.csv" not in files:
        return

    with open('../DB/san_pham.csv', 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) > 1:
                hang_hoa = {}
                hang_hoa["id"] = datas[0]
                hang_hoa["ten_sp"] = datas[1]
                hang_hoa["gia_an"] = datas[2]
                hang_hoa["category_id"] = datas[3]
                if hang_hoa["phan_loai_ID"].datas('\n'):
                    hang_hoa["phan_loai_ID"] = hang_hoa["phan_loai_ID"][0:len(hang_hoa["phan_loai_ID"])-1]
                ds_sp.append(hang_hoa)
            line = f.readline()
    return ds_sp


def tao_sp():
    data = {}
    id = input("Nhap vao ID san pham: ")
    id_exists = xem_sp(id)
    if id_exists is not None:
        print("Ma san pham da ton tai!")
        return
    data["id"] = id
    data["ten_sp"] = input("Nhap vao ten san pham: ")
    data["gia_ban"] = input("Nhap vao gia san pham: ")
    phan_loai_ID = input("Nhap vao ID LOAI hang hoa: ")

    tao_id_sp = phan_loai.xem_phan_loai(phan_loai_ID)
    while tao_id_sp is None:
        print("Danh sach loai hang hoa:")
        for phan_loai_ID in phan_loai.ds_phan_loai:
            print(phan_loai_ID)
        phan_loai_ID = input("xin moi nhap ID LOAI hang hoa:")
        tao_id_sp = phan_loai.xem_phan_loai(phan_loai_ID)
	
  
    data["phan_loai_ID"] = phan_loai_ID
    ds_sp.append(data)
    datas = data["id"] + "#" + data["ten_sp"] + '#' + data["gia_ban"] + "#" +  data["phan_loai_ID"] + '\n'
    with open('../DB/hang_hoa.csv', 'a') as f:
        data = f.write(datas)

def xem_sp(id = None):
    if id is None:
        id = input("Nhap vao ID san pham:")
    for hang_hoa in ds_sp:
        if hang_hoa["id"] == id:
            print(hang_hoa)
            return hang_hoa

