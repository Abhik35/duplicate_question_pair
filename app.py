import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

html_temp = """
    <div style="background-color:SteelBlue;padding:10px">
    <h2 style="color:white;text-align:center">Duplicate Question Pairs </h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

st.subheader("Created by:-")
st.write("***sourajit***")

