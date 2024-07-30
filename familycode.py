import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image as i
from datetime import datetime,date
st.set_page_config(page_title="Family",page_icon="❤")
st.header("Happy Family❤")
tab1,tab2,tab3=st.tabs(["Pappa","Bittu","Mumma"])
col1,col2,col3=st.columns([3,2,1])
with tab1:
    st.image("C:/Users/HP/OneDrive/Pictures/pappa.jpg",width=600)
with tab2:
    st.image("C:/Users/HP/OneDrive/Pictures/bittu.jpg",width=600)
with tab3:
    st.image("C:/Users/HP/OneDrive/Pictures/mumma.jpg",width=600)
st.subheader("Question")
today=datetime.now().date()
#st.radio("Select Date: ", ('2004/12/20', '2004/12/25'))
date=st.date_input("When is my Birthday",min_value=date(2004,12,20),max_value=date(2024,8,10))
#st.write(" ",datetime.strftime(date, '%d/%m/%y'))
status=st.radio("Options: ", ('20/12/2004', '25/12/2003','25/12/2003','20/12/2003'))
st.button('Submit')

    #st.success(date)
if (status == '20/12/2004'):
    st.success("20/12/1004")
    st.balloons()
else:
    st.error("Try again")

st.subheader(" I MISS U 🥹  ")
st.image("C:/Users/HP/OneDrive/Pictures/familypic.jpg",width=300)
st.audio("C:/Users/HP/Music/fam.unknown")
st.subheader("Rate ur experience")
st.slider("How much did u like it",min_value=0,max_value=5)


