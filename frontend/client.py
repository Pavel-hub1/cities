import sys
import requests
import json
import streamlit as st

st.button('Ввод')
str_input = st.text_input('')
url = 'http://backend:80/'

while True:
    try:
        city = str_input
        body = {'city': city}
        response = requests.post(url, params=body)
        answer_body = json.loads(response.text)
        city = answer_body['city']
        letter = answer_body['letter']
        if not str_input:
            st.success('Введите город.')
            break
        elif city is None:
            st.success('Поздравляем!')
            break
        elif city == 'error':
            message = f' Напоминаю, вам на "{letter.upper()}"' if letter else ''
            st.success(f'Что-то не то ввели, попробуйте снова.{message}')
            break
        elif city == 'used':
            st.success('Этот город уже использовался, введите другой.')
            break
        else:
            st.success(f'Компьютер: {city}, вам на "{letter.upper()}".')
            break
    except KeyboardInterrupt:
        sys.exit()

