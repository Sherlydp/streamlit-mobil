import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil')

car_ID = st.number_input('input ID mobil')
symboling = st.number_input('input symboling')
wheelbase = st.number_input('input jarak roda')
carlength = st.number_input('input panjang mobil')
carwidth = st.number_input('input lebar mobil')
carheight = st.number_input('input tinggi mobil')
curbweight = st.number_input('input berat mobil')
enginesize = st.number_input('input ukuran mesin')
boreratio = st.number_input('input rasio bor mobil')
stroke = st.number_input('input jarak pergerakan piston')
compressionratio = st.number_input('input rasio kompresi')
horsepower = st.number_input('input tenaga mobil')
peakrpm = st.number_input('input rpm mobil')
citympg = st.number_input('input mpg kota')
highwaympg = st.number_input('input mpg rata rata')

predict = ''

if st.button('estimasi harga'):
    predict = model.predict(
        [[car_ID, symboling, wheelbase, carlength, carwidth, carheight, curbweight, enginesize, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]]
    )
    st.write ('Estimasi harga mobil  : ', predict)