import pickle 
import streamlit as st

model = pickle.load(open('harga-mobile-phone.sav', 'rb'))

st.title('Prediksi Harga Mobile Phone')

pd_id = st.number_input('Input Product ID (Range 10-1400) :' ,min_value=10, max_value=1400)
res = st.number_input('Input Screen Resolution (Range 1,40-12,00) :' ,min_value=1.4, max_value=12.0)
cpu = st.selectbox(
   "Input CPU Core :",
   (1, 2, 4, 6, 8),
   index=None,
   placeholder="Select the value..."
)
c_frec = st.number_input('Input CPU Frekuensi (Range 1.0-2.7 Hz) :' ,min_value=1.0, max_value=2.7,step=0.05) 
rom = st.selectbox(
   "Input Internal Memori (GB) :",
   (4, 8, 16, 32, 64, 128),
   index=None,
   placeholder="Select the value..."
)
ram = st.selectbox(
   "Input RAM Size (GB) :",
   (0.128,0.256, 0.512, 1, 2, 3,4, 6),
   index=None,
   placeholder="Select the value..."
)
r_cam = st.number_input('Input Rear Cam Resolution (Range 1.0-23.0 MP) :',min_value=1.0, max_value=23.0,step=1.0)
f_cam = st.number_input('Input Front Cam Resolution (Range 1.0-20.0 MP) :',min_value=1.0, max_value=20.0,step=1.0)
battery = st.number_input('Input Battery Cap (Range 800-9500 mAh) :',min_value=800, max_value=9500,step=100)

predict = ''

if st.button('Price Check'):
    predict = model.predict(
        [[pd_id,res,cpu,c_frec,rom,ram,r_cam,f_cam,battery]]
    )
    st.write('Mobile Phone Price Prediction (CNY): ',predict)
    st.write('Mobile Phone Price Prediction (IDR): ',predict*2175)