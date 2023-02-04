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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include (with prepopulated avocado & no name fruit) 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruit_to_show)
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
