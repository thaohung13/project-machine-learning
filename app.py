import streamlit as st
import math
st.title("TTĐ: Giải phương trình bậc hai")
with st.form(key = 'my-form'):
    a = st.number_input('Nhập a:')
    b = st.number_input('Nhập b:')
    c = st.number_input('Nhập c:')
    submit_button_giai = st.form_submit_button(label='Giải')

if submit_button_giai:
    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                ket_qua = 'PTB1 vô số nghiệm'
            else:
                ket_qua = 'PTB1 vô nghiệm'
        else:
            x = -c/b
            ket_qua = 'PTB1 có nghiệm x = %.2f' % x
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            ket_qua = 'PTB2 vô nghiệm'
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            ket_qua = 'PTB2 có nghiệm x1 = %.2f và x2 = %.2f' % (x1, x2)
        st.write(f'{ket_qua}')
