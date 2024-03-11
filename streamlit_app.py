import streamlit as st 
name=st.text_input("ton nom")
st.write("Hello"+name) 


input= "lapin"
list_possibilities=["rabbit","race","rhyme","rogue"]
correct_answer="rabbit"
st.right("traduis"+input)
for i in range(len(list_possibilities)):
st.button(list_possibilities[i])
