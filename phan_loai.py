import os
#category

ds_phan_loai = []
def load_phan_loai():
    files = os.listdir('../DB')
    if "phan_loai.csv" not in files:
        return
    with open ('../DB/phan_loai.csv', 'r') as f:
        line = f.readline()
        while line:
            lines = line.split("#")
            #  GK#Nuoc giai khat  \n
            #  TP#Thuc pham  \n
            if len(lines) > 1:
                phan_loai_hh = {}
                phan_loai_hh["id"] = lines[0]
                loai_hang = lines[1]
                if loai_hang.endswith('\n'):
                    loai_hang = loai_hang[0:len(loai_hang)-1]
                phan_loai_hh["loai_hang"] = loai_hang
                ds_phan_loai.append(phan_loai_hh)
            line = f.readline()
    
def tao_phan_loai():
    data = {}
    id = input ("Nhap vao ID loai hang hoa: ")
    ids = xem_phan_loai(id)
    if ids is not None:
        print("ID da ton tai!")
        return
    data["id"] = id
    data["loai_hang"] = input("Xin moi nhap loai hang: ")
    ds_phan_loai.append(data)
    datas = data["id"] + "#" + data["loai_hang"] + '\n'
    with open('../DB/phan_loai.csv' , 'a') as f:
        data = f.write(datas)

def xem_phan_loai(id = None):
    if id is None:
        id = input("Nhap vao ID loai hang hoa: ")
    for loai_hh in ds_phan_loai:
        if loai_hh["id"] == id :
            print ("ID loai hang hoa: ", id)
            return loai_hh

def danh_sach_phan_loai():
    return ds_phan_loai