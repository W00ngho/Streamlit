import streamlit as st
import pandas as pd
import numpy as np

# 타이틀 적용 예시
st.title('My first streamlit page')

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :sunglasses:')

# Header 적용
st.header('헤더를 입력할 수 있어요! :sparkles:')

# Subheader 적용
st.subheader('이것은 subheader 입니다')

# 캡션 적용
st.caption('캡션을 한 번 넣어 봤습니다')

# 코드 표시
sample_code = '''
나의 첫 스트림릿 페이지
'''
st.code(sample_code, language="python")

# 일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')

# 마크다운 문법 지원
# st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 컬러코드: blue, green, orange, red, violet
# st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

# LaTex 수식 지원
# st.latex(r'\sqrt{x^2+y^2}=1')

# --------------------

import streamlit as st
import pandas as pd
import numpy as np


st.title('데이터프레임')

# DataFrame 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
st.dataframe(dataframe, use_container_width=False)


# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(dataframe)


# # 메트릭
st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")


# --------------------------------

import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')


# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='sample.csv', 
    mime='text/csv'
)

# 체크 박스
agree = st.checkbox('동의 하십니까?')

if agree:
    st.write('동의 해주셔서 감사합니다 :100:')

# 라디오 선택 버튼
mbti = st.radio(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'))

if mbti == 'ISFJ':
    st.write('당신은 :Salmon[전략가] 이시네요')
elif mbti == 'ISFJ':
    st.write('당신은 :blue[수호자] 이시네요')
elif mbti == 'INFJ':
    st.write('당신은 :green[옹호자] 이시네요')
elif mbti == 'INTJ':
    st.write('당신은 :pink[전략가] 이시네요')
elif mbti == 'ISTP':
    st.write('당신은 :yellow[장인] 이시네요')
elif mbti == 'ISFP':
    st.write('당신은 :yellow[모험가] 이시네요')
elif mbti == 'INFP':
    st.write('당신은 :green[중재자] 이시네요')
elif mbti == 'INTP':
    st.write('당신은 :pink[논리술사] 이시네요')
elif mbti == 'ESTP':
    st.write('당신은 :yellow[사업가] 이시네요')
elif mbti == 'ESFP':
    st.write('당신은 :yellow[연예인] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
elif mbti == 'ENTP':
    st.write('당신은 :pink[변론가] 이시네요')
elif mbti == 'ESTJ':
    st.write('당신은 :pink[통솔자] 이시네요')
elif mbti == 'ESFJ':
    st.write('당신은 :blue[집정관] 이시네요')
elif mbti == 'ENTJ':
    st.write('당신은 :pink[통솔자] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")



# if mbti == 'ISTJ':
#     st.write('당신은 :blue[현실주의자] 이시네요')
# elif mbti == 'ENFP':
#     st.write('당신은 :green[활동가] 이시네요')
# else:
#     st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP',
     'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'), 
    index=2
)
 
if mbti == 'INTJ':
    st.write('당신은 :[전략가] 이시네요')
elif mbti == 'ISFJ':
    st.write('당신은 :blue [수호자] 이시네요')
elif mbti == 'INFJ':
    st.write('당신은 :green[옹호자] 이시네요')
elif mbti == 'ISTP':
    st.write('당신은 :yellow[장인] 이시네요')
elif mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ISFP':
    st.write('당신은 :yellow[모험가] 이시네요')
elif mbti == 'INFP':
    st.write('당신은 :green[중재자] 이시네요')
elif mbti == 'INTP':
    st.write('당신은 :pink[논리술사] 이시네요')    
elif mbti == 'ESTP':
    st.write('당신은 :blue사업가] 이시네요')
elif mbti == 'ENFJ':
    st.write('당신은 :blue[선도자] 이시네요')
elif mbti == 'ESFP':
    st.write('당신은 :yellow[연예인] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
elif mbti == 'ENTP':
    st.write('당신은 :pink[변론가] 이시네요')
elif mbti == 'ESTJ':
    st.write('당신은 :pink[경영자] 이시네요')
elif mbti == 'ESFJ':
    st.write('당신은 :blue[집정관] 이시네요')
elif mbti == 'ENTJ':
    st.write('당신은 :pink[통솔자] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 다중 선택 박스
options = st.multiselect(
    '당신이 좋아하는 과일은 뭔가요?',
    ['망고', '오렌지', '사과', '바나나'],
    ['망고', '오렌지'])

st.write(f'당신의 선택은: :red[{options}] 입니다.')


# 슬라이더
values = st.slider(
    '범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
    0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)

start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2020, 1, 1, 0, 0), 
    max_value=dt(2020, 1, 7, 23, 0),
    value=dt(2020, 1, 3, 12, 0),
    step=datetime.timedelta(hours=1),
    format="MM/DD/YY - HH:mm")
st.write("선택한 약속 시간:", start_time)


# 텍스트 입력
title = st.text_input(
    label='가고 싶은 여행지가 있나요?', 
    placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지: :violet[{title}]')

# 숫자 입력
number = st.number_input(
    label='나이를 입력해 주세요.', 
    min_value=10, 
    max_value=100, 
    value=30,
    step=5
)
st.write('당신이 입력하신 나이는:  ', number)
