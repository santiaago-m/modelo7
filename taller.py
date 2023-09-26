import streamlit as st
import numpy as np
import pandas as pandas
import pickle 
from catboost import CatboostRegressor
import sklearn


st.title("Deployment Taller" )
st.divider()
st.write("Datos")
assess=st.slider("Asses",0, 10000)
bdrms= st.slider("Bedrooms",0, 100)
lotsize= st.slider ("Lote size",0, 500000)
sqrft= st.slider ("Square fit",0, 100000)
colonial st.slider("Colonial",^[0, 1])
with open("modelo1.pkl" , "rb") as doc: 
    model= pickle.load(doc)
    

prediction=model.predict(np.array([[assess, bdrms, lotsize, sqrft, colonial]]))
if st.button("Prediction"):
    st.write(d "El valor que tiene es de {prediction[0]}")