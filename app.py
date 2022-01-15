import streamlit as st
from Linear import show_predict_page
from Decision import show_predict_page_2
from Random import show_predict_page_3
from Multi import show_predict_page_4

page = st.sidebar.selectbox("Type of Regression", ("Linear", "Multi Linear", "Decision Tree", "Random Forest"))
if page == "Linear":
    show_predict_page()
elif page == "Decision Tree":
    show_predict_page_2()
elif page == "Random Forest":
    show_predict_page_3()
elif page == "Multi Linear":
    show_predict_page_4()