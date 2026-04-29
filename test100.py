import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

if "vote_dialog_requested" not in st.session_state:
    st.session_state.vote_dialog_requested = False
if "vote_reason" not in st.session_state:
    st.session_state.vote_reason = ""
if "vote_choice" not in st.session_state:
    st.session_state.vote_choice = ""
if "selected_genre" not in st.session_state:
    st.session_state.selected_genre = "멜로"

def open_vote_dialog(choice: str) -> None:
    st.session_state.vote_choice = choice
    st.session_state.vote_dialog_requested = True

st.markdown(
    """
    <style>
    body { background: #f8fafc; }
    .outer-box { border: 1px solid #e5e7eb; border-radius: 24px; padding: 32px; background: #ffffff; box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08); margin-bottom: 24px; }
    .section-title { font-size: 32px; font-weight: 800; margin-bottom: 24px; color: #111827; }
    .metrics-grid { display: flex; gap: 20px; }
    .metric-card { border: 1px solid #e5e7eb; border-radius: 22px; padding: 24px; background: #fff; min-height: 170px; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05); }
    .metric-label { color: #6b7280; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.08em; text-transform: uppercase; }
    .metric-value { font-size: 35px; font-weight: 800; color: #111827; margin-bottom: 18px; line-height: 1; }
    .trend { display: inline-flex; align-items: center; gap: 0.5rem; padding: 8px 14px; border-radius: 999px; font-size: 14px; font-weight: 600; }
    .trend.up { background: #d1fae5; color: #166534; }
    .trend.down { background: #fee2e2; color: #991b1b; }
    .trend span.icon { font-size: 16px; line-height: 1; }
    .choice-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; margin-bottom: 24px; }
    .choice-card { border: 1px solid #e5e7eb; border-radius: 24px; padding: 24px; background: #ffffff; box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06); }
    .choice-title { font-size: 24px; font-weight: 700; margin-bottom: 8px; color: #111827; }
    .choice-subtitle { color: #6b7280; margin-bottom: 18px; line-height: 1.5; }
    .radio-hint { color: #9ca3af; margin-left: 26px; margin-top: -8px; margin-bottom: 12px; display: block; font-size: 13px; }
    .payment-note { margin-top: 20px; padding: 14px 18px; border-radius: 16px; background: #e0f2fe; color: #075985; font-weight: 600; }
    .vote-row { display: flex; gap: 14px; margin-top: 16px; }
    .vote-button { width: 100%; border: 1px solid #e5e7eb; border-radius: 14px; padding: 12px 0; background: #ffffff; color: #111827; font-size: 16px; font-weight: 600; }
    .vote-button:hover { background: #f8fafc; }
    .bottom-alert { border: 1px solid #fde68a; border-radius: 18px; padding: 18px 22px; background: #fef3c7; color: #92400e; margin-bottom: 18px; }
    .bottom-alert strong { display: block; font-size: 17px; margin-bottom: 8px; }
    .selected-genre { margin: 18px 0 12px; font-size: 18px; font-weight: 700; color: #111827; }
    .genre-video { border-radius: 24px; overflow: hidden; }
    .transaction-table { width: 100%; border-collapse: collapse; }
    .transaction-table th, .transaction-table td { padding: 14px 16px; border-bottom: 1px solid #e5e7eb; }
    .transaction-table thead th { background: #f8fafc; color: #111827; font-weight: 700; border-bottom: 2px solid #d1d5db; }
    .transaction-card { border: 1px solid #e5e7eb; border-radius: 24px; padding: 24px; background: #ffffff; box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06); }
    .transaction-heading { font-size: 26px; font-weight: 700; margin-bottom: 20px; color: #111827; }
    @media (max-width: 768px) { .metrics-grid { flex-direction: column; } .metric-card { margin-bottom: 18px; } }
    </style>
    """,
    unsafe_allow_html=True,
)

metrics = [
    {"label": "매출 합계", "value": "45,231", "trend": "20.1%", "direction": "up"},
    {"label": "회원 가입", "value": "+235", "trend": "-1.21%", "direction": "down"},
    {"label": "판매 수익", "value": "+12,234", "trend": "19%", "direction": "up"},
]
# 운영 현황
with st.container():
    st.markdown('<div class="section-title">운영 현황</div>', unsafe_allow_html=True)

    cols = st.columns(3, gap="large")
    for col, metric in zip(cols, metrics):
        with col:
            direction_class = "up" if metric["direction"] == "up" else "down"
            icon = "▲" if metric["direction"] == "up" else "▼"
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{metric["label"]}</div>
                    <div class="metric-value">{metric["value"]}</div>
                    <div class="trend {direction_class}">
                        <span class="icon">{icon}</span>
                        {metric["trend"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# 매출 현황
month_order = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
chart_df = pd.DataFrame({
    "Month": month_order,
    "Sales": [4300, 4500, 2800, 3600, 3750, 2700, 1800, 2650, 1850, 1300, 4900, 2050]
})
chart_df["Month"] = pd.Categorical(chart_df["Month"], categories=month_order, ordered=True)
chart_df = chart_df.sort_values("Month")

with st.container():
    st.markdown('<div class="section-title">매출 현황</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Bar Chart", "📈 Line Chart", "📉 Area Chart"])
    
    with tab1:
        st.bar_chart(chart_df.set_index('Month')['Sales'])
    
    with tab2:
        st.line_chart(chart_df.set_index('Month')['Sales'])
    
    with tab3:
        st.area_chart(chart_df.set_index('Month')['Sales'])

# 거래 내역(Read Only)
transaction_df = pd.DataFrame([
    {"거래내역": "INV001", "결제": "수금", "총액": 500, "지불방법": "신용카드"},
    {"거래내역": "INV002", "결제": "미수금", "총액": 200, "지불방법": "현금"},
    {"거래내역": "INV003", "결제": "수금", "총액": 150, "지불방법": "체크카드"},
    {"거래내역": "INV004", "결제": "미수금", "총액": 350, "지불방법": "신용카드"},
    {"거래내역": "INV005", "결제": "수금", "총액": 400, "지불방법": "무통장입금"},
])

st.markdown('<div class="section-title">거래 내역(Read Only)</div>', unsafe_allow_html=True)

with st.container(border=True):
    st.dataframe(transaction_df, use_container_width=True)

st.write("")  # 간격

# 거래내역 (Editable)
st.markdown('<div class="section-title">✏️ 거래 내역 (Editable)</div>', unsafe_allow_html=True)

with st.container(border=True):
    st.data_editor(
        transaction_df,
        use_container_width=True,
        num_rows="fixed",
        disabled=False,
    )
    
# 선택 UI
with st.container():
    left_col, right_col = st.columns([2, 1], gap=None, border=True,)
    with left_col:
        st.markdown('<div class="choice-title">지불 방법 선택</div>', unsafe_allow_html=True)
        st.markdown('<div class="choice-subtitle">지불 방법을 선택하세요</div>', unsafe_allow_html=True)
        
        payment = st.radio(
            "",
            ["신용카드", "현금", "체크카드"],
            index=1,
        )
        if payment == "신용카드":
            st.markdown('<span class="radio-hint">국민/신한/우리</span>', unsafe_allow_html=True)
        elif payment == "현금":
            st.markdown('<span class="radio-hint">현금영수증</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="radio-hint">농협/신협</span>', unsafe_allow_html=True)
        st.markdown('<div class="payment-note">현금 영수증</div>', unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="choice-title">찬/반 투표</div>', unsafe_allow_html=True)
        st.markdown('<div class="choice-subtitle">찬/반 투표에 참여해주세요.</div>', unsafe_allow_html=True)
        with st.container(horizontal=True):
            st.button('찬성', on_click=open_vote_dialog, args=('찬성',))
            st.button('반대', on_click=open_vote_dialog, args=('반대',))
        


    if st.session_state.vote_dialog_requested:
        @st.dialog('의견을 말씀해주세요.')
        def vote_dialog():
            if st.session_state.vote_choice == '찬성':
                st.markdown('찬성하는 이유를 말씀해주세요.')
            else:
                st.markdown('반대하는 이유를 말씀해주세요.')
            st.session_state.vote_reason = st.text_area(
                '그 이유는...',
                value=st.session_state.vote_reason,
                placeholder='의견을 입력해 주세요.',
            )
            if st.button('제출'):
                if st.session_state.vote_reason.strip():
                    st.success(f"{st.session_state.vote_choice} 의견이 제출되었습니다.")
                    st.session_state.vote_dialog_requested = False
                    st.session_state.vote_choice = ''
                else:
                    st.error('의견을 입력해주세요.')

        vote_dialog()

# 이미지 참고용 하단 추천 UI
with st.container():
    st.markdown(
        '<div class="bottom-alert"><strong>⚠️ 서두르세요!</strong>주말 넷플릭스 주도권을 룸메에게 뺏겨서야 되겠습니까?</div>',
        unsafe_allow_html=True,
    )

    videos = {
        "멜로": "https://www.youtube.com/watch?v=0pdqf4P9MB8",
        "미스터리": "https://www.youtube.com/watch?v=YoHD9XEInc0",
        "스릴러": "https://www.youtube.com/watch?v=6hB3S9bIaco",
        "액션": "https://www.youtube.com/watch?v=TcMBFSGVi1c",
    }

    genres = list(videos.keys())
    selected = st.radio(
        "",
        genres,
        index=genres.index(st.session_state.selected_genre),
        horizontal=True,
    )
    st.session_state.selected_genre = selected

    st.markdown(
        f'<div class="selected-genre">현재 선택된 장르: {st.session_state.selected_genre}</div>',
        unsafe_allow_html=True,
    )

    st.video(videos[st.session_state.selected_genre])
