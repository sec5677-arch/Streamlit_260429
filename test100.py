import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="centered")

# 샘플 데이터
chart_data = pd.DataFrame({
    "Month": ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
    "Sales": [4300, 4500, 2800, 3600, 3750, 2700, 1800, 2650, 1850, 1300, 4900, 2050]
})

table_data = pd.DataFrame({
    "거래내역": ["INV001", "INV002", "INV003", "INV004", "INV005"],
    "결제": ["수금", "미수금", "수금", "미수금", "수금"],
    "총액": [500, 200, 150, 350, 400],
    "지불방법": ["신용카드", "현금", "체크카드", "신용카드", "무통장입금"]
})

with st.container(border=True):
    
    # 타이틀
    st.title("운영 현황")

    st.write("")  # 간격

    # 내부 카드 3개
    col1, col2, col3 = st.columns(3, gap="large")

    # 카드 1
    with col1:
        with st.container(border=True):
            st.caption("매출 합계")
            st.metric(
                label=" ",
                value="45,231",
                delta="+20.1%"
            )

    # 카드 2
    with col2:
        with st.container(border=True):
            st.caption("회원 가입")
            st.metric(
                label=" ",
                value="+235",
                delta="-1.21%"
            )

    # 카드 3
    with col3:
        with st.container(border=True):
            st.caption("판매 수익")
            st.metric(
                label=" ",
                value="+12,234",
                delta="+19%"
            )
