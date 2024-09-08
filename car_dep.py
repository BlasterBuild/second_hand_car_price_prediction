import streamlit as st
import numpy as np
import pickle
import pandas
from PIL import Image
import time

# load the saved model
load_model = pickle.load(open('t_model.sav', 'rb'))
st.title("used car price guess model")
p_price = st.text_area("", height=10, placeholder='write present price')
k_driven = st.text_area("", height=10, placeholder='write kms driven')
owner = st.text_area("", height=10, placeholder='write owner')
number_of_years = st.text_area("", height=10, placeholder='write no_of_years')
fuel_t_d = st.text_area("", height=10, placeholder='write type diesel')
fuel_t_p = st.text_area("", height=10, placeholder='write type petrol')
seller_t = st.text_area("", height=10, placeholder='write type of seller')
transmission = st.text_area("", height=10, placeholder='write type of transmission')

r_l = [[p_price, k_driven, owner, number_of_years, fuel_t_d, fuel_t_p, seller_t, transmission]]

if st.button("Predict", use_container_width=True):
    result = load_model.predict(r_l)
    st.snow()

st.header(result, ':sunglasses:')
