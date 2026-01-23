import streamlit as it
import time
meh = 0
it.title("Đăng kí tài khoảng")
t = it.text_input("Tên tài khoảng :")
mk = it.text_input("Mật khẩu :")
mk2 = it.text_input("Nhập lại mật khẩu :")
tnd = it.text_input("Tên người dùng :")
e = it.text_input("Email :")
if it.button("submit"):
    if not t or not mk or not mk2 or not tnd or not e:
        it.write("Đừng điền thiếu thông tin !")
    else:
        pro = 0
        bar = it.progress(pro)
        idk = it.empty()
        for i in range(100):
            time.sleep(0.05)
            pro += 1
            bar.progress(pro)
            idk.text(f"progress {pro} %")
        it.write(f"cảm ơn bạn đã đăng kí :3")
        it.balloons()