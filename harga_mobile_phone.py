import pickle
import streamlit as st

model = pickle.load(open('harga-mobile-phone.sav', 'rb'))

st.title('Mobile Phone Price Prediction')

pd_id = st.number_input('Input Product ID (Range 10-1400):', min_value=10, max_value=1400, step=1)
res = st.number_input('Input Screen Resolution (Range 1.4-12.0):', min_value=1.4, max_value=12.0, step=0.1)
cpu = st.selectbox("Input CPU Core:", (1, 2, 4, 6, 8))
c_frec = st.number_input('Input CPU Frequency (Range 1.0-2.7 GHz):', min_value=1.0, max_value=2.7, step=0.05)
rom = st.selectbox("Input Internal Memory (GB):", (4, 8, 16, 32, 64, 128))
ram = st.selectbox("Input RAM Size (GB):", (0.128, 0.256, 0.512, 1, 2, 3, 4, 6))
r_cam = st.number_input('Input Rear Cam Resolution (Range 1.0-23.0 MP):', min_value=1.0, max_value=23.0, step=1.0)
f_cam = st.number_input('Input Front Cam Resolution (Range 1.0-20.0 MP):', min_value=1.0, max_value=20.0, step=1.0)
battery = st.number_input('Input Battery Capacity (Range 800-9500 mAh):', min_value=800, max_value=9500, step=100)

if st.button('Price Check'):
    features = [[pd_id, res, cpu, c_frec, rom, ram, r_cam, f_cam, battery]]
    predict = model.predict(features)

    st.write('Mobile Phone Price Prediction (CNY):', predict[0])
    st.write('Mobile Phone Price Prediction (IDR):', predict[0] * 2175)
