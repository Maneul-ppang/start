import streamlit as st

st.title('두 수의 합 계산기')

a = st.number_input('첫번째 숫자를 입력하세요', value=0)
b = st.number_input('두번째 숫자를 입력하세요', value=0)

st.write(f'두 수의 합은 {a + b} 입니다')
