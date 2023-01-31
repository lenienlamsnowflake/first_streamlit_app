import streamlit

streamlit.title('My parents New Healthy diner')
streamlit.header('breakfast menu')
streamlit.text('Boiled egg')
streamlit.text('🥣Multi grain Honey Oatmeal')
streamlit.text('Super8 Breakfast Juice')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🍌Banana')
streamlit.text('🥭Strawberry')
streamlit.text('🥝Kiwi')
streamlit.text('🍇Graphes')
streamlit.text('🥑Avacadro')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
