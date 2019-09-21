import os
import phan_loai
import hoadon
import base
import user
import sanpham



          
def menu1():
    print("+--------------MENU-----------------+")
    print("|Chon 1 de tao account seller       |")
    print("|Chon 2 de update thông tin seller  |")
    print("|Chon 3 de deactive account seller  |")
    print("|Chon 4 list danh sách SELLER       |")
    print("|Chon 5 list danh sách BUYER        |")
    print("|Chon 6 de vao QUAN LY HOA DON      |")
    print("|Chon E de logout                   |")
    print("+-----------------------------------+")

    while True:
        x=input("=> chon chuc nang:")
        print("=> ban da chon chuc nang:",x)
        if x == '1':
            user.tao_nguoi_dung_moi()
        if x == '2':
            user.sua_nguoi_dung()
        if x == '3':
            user.xoa_nguoi_dung()
        if x == '4':
            user.xem_nguoi_dung()
        #if x == '5':
            #user.xe()
        if x == '6':
            menu2()
        if x.upper() == 'E':
            print("Tam biet! Hen gap lai")
            break


def menu2():
    print("+--------------MENU-----------------+")
    print("|Chon THH de tao hang hoa           |")
    print("|Chon XHH de xem hang hoa           |")
    print("|Chon TLH de tao loai hang hoa      |")
    print("|Chon XLH de xem loai hang hoa      |")
    print("|Chon C de tao hoa don              |")
    print("|Chon R de xem thong tin hoa don    |")
    print("|Chon T de tinh tong doanh thu      |")
    print("|Chon A de tinh tong hang hoa ban ra|")
    print("|Chon E de thoat                    |")
    print("+-----------------------------------+")


    sanpham.load_sp()
    phan_loai.load_phan_loai()

    while True:
        x=input("=> chon chuc nang:")
        print("=> ban da chon chuc nang:",x)
        if x.upper() == 'TLH':
            phan_loai.tao_phan_loai()
        if x.upper() == 'XLH':
            phan_loai.xem_phan_loai()
        if x.upper() == 'THH':
            sanpham.tao_sp()
        if x.upper() == 'XHH':
            sanpham.xem_sp()
        if x.upper() == 'C':
            hoadon.tao_hd()
        if x.upper() == 'R':
            hoadon.view_invoice()
        if x.upper() == 'T':
            base.top_revenue()
        if x.upper() == 'A':
            base.top_sale_products()
        if x.upper() == 'E':
            print("Tam biet! Hen gap lai")
            break
            