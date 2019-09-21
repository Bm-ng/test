import os
import json

files = []
ds_id = []
def load_id_sp(id):
    files = os.listdir('../DB')
    if "san_pham.csv" not in files:
        return
    with open('../DB/san_pham.csv', 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) > 1:
                if int(datas[0]) == id:
                    #id#tensp#giaban#phan_loai_ID '\n'
                    hang_hoa = {}
                    hang_hoa["id"] = datas[0]
                    hang_hoa["ten_sp"] = datas[1]
                    hang_hoa["gia_ban"] = datas[2]
                    hang_hoa["phan_loai_ID"] = datas[3]
                    if hang_hoa["phan_loai_ID"].endswith('\n'):
                        hang_hoa["phan_loai_ID"] = hang_hoa["phan_loai_ID"][0:len(datas["phan_loai_ID" ])-1]
                line = f.readline()

    return hang_hoa["ten_sp"], hang_hoa["gia_ban"]

def xem_ds_sp():
    files = os.listdir("../DB")
    if "san_pham.csv" not in files:
        return
    with open ('../DB/san_pham.csv', 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) > 1: 
                hang_hoa ={}
                hang_hoa["id"] = datas[0]
                hang_hoa["ten_sp"] = datas[1]
                hang_hoa["gia_ban"] = datas[2]
                hang_hoa["phan_loai_ID"] =datas[3]
                if hang_hoa["phan_loai_ID"].endswith('\n'):
                        hang_hoa["phan_loai_ID"] = hang_hoa["phan_loai_ID"][0:len(datas["phan_loai_ID" ])-1]
                line = f.readline()
    return xem_ds_sp

def kiem_tra_id(id):
     with open ('../DB/san_pham.csv', 'r') as f:
        line = f.readline()
        while line:
            datas = line.split("#")
            if len(datas) > 1: 
                hang_hoa ={}
                hang_hoa["id"] = datas[0]
                if int(hang_hoa["id"]) == int(id):
                    return hang_hoa["id"]
                line =f.readline()
########


def tao_id(path):
    id_dict = {}
    if os.stat(path).st_size == 0:
        id_dict["id"] = '0'
        ds_id.append(id_dict)
        return id_dict
    else:
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                datas = line.split("#")
                id_dict["id"] = datas[0]
                line = f.readline()
            ds_id.append(id_dict)
        return id_dict






def load_all(path):
    files.clear()
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.json' in file:
                files.append(os.path.join(r, file))
    print("load_all_file", files)
    return files

list_sale_product = []
def count_sale_product(product_name,total_sale):
    for f in files:
        with open(f, 'r') as line:
            invoice = json.load(line)
            for hanghoa in invoice["ds_hh"]:
                if hanghoa['ten_sp'] == product_name:
                    total_sale = total_sale + hanghoa['so_luong']
    count_sale_product1 = {}
    count_sale_product1['product_name'] = product_name
    count_sale_product1['total_sale'] = total_sale
    list_sale_product.append(count_sale_product1)
    # return list_sale_product


def total_sale_for_products():
    load_all_file('../HoaDon/')
    with open('../Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                products = {}
                products["ten"] = str_to_reads[1]
                total_sale = 0
                count_sale_product(products["ten"],total_sale)
            line = f.readline()



def top_sale_products():
    total_sale_for_products()
    print ("max",max(list_sale_product, key=lambda x:x['total_sale'])) 
    print ("min",min(list_sale_product, key=lambda x:x['total_sale'])) 
    list_sale_product.clear()

#top_sale_products()

list_money_product = []
def count_money_product(product_name,total_money):
    for f in files:
        with open(f, 'r') as line:
            invoice = json.load(line)
            for hanghoa in invoice["danhsachhanghoa"]:
                if hanghoa['ten'] == product_name:
                    total_money = total_money + hanghoa['thanhtien']
    count_money_product1 = {}
    count_money_product1['product_name'] = product_name
    count_money_product1['total_money'] = total_money
    list_money_product.append(count_money_product1)


def total_money_for_products():
    load_all_file('../HoaDon/')
    with open('../Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                products = {}
                products["ten"] = str_to_reads[1]
                total_money = 0
                count_money_product(products["ten"],total_money)
            line = f.readline()




def top_revenue():
    total_money_for_products()
    print(list_money_product)
    print ("max",max(list_money_product, key=lambda x:x['total_money'])) 
    print ("min",min(list_money_product, key=lambda x:x['total_money']))
    list_money_product.clear()               