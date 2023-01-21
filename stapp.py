import streamlit as st
page_bg_img = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@1,900&display=swap');
.appview-container{
    background-image:url("https://www.sciencealert.com/images/2022/08/Milk-splashing-against-black-background.jpg");
    background-size : cover;
   
</style>
"""
st.markdown(page_bg_img , unsafe_allow_html=True)
    
    
import numpy as np
import pandas as pd
#import joblib
#model = joblib.load('RRookiesfinalmodel.joblib')
import pickle
pickle_in = open('Rookiesproject.pkl', 'rb') 
classifier = pickle.load(pickle_in)
    


def prediction(pH,temperature,taste,odor,fat,turbidity,color):  
      prediction = classifier.predict( 
        [ [pH,temperature,taste,odor,fat,turbidity,color]])
      
      return prediction  
original_title = '<p style="font-family:Sofia Sans; color:#E3E3E3; font-size: 50px; font-weight:bold;">Milk Quality Prediction</p>'
st.markdown(original_title, unsafe_allow_html=True)    


pH = st.number_input("Input pH level : ")
temperature = st.number_input("Input temperature : ")
taste_input = st.radio(
    "How is the taste?",
    ('Good','Normal' ,'Bad'))

if taste_input == 'Good':
    taste = 1
elif taste_input == 'Normal':
    taste = 0
elif taste_input == 'Bad':
    taste = 0
    pH = 9

odor_input= st.radio(
    "Is there odor?",
    ('Yes', 'No'))
if odor_input == 'Yes':
    odor = 1
else :
    odor = 0

fat = st.slider('How much fat does it contain?',0, 3 )
turbidity = st.slider("Turbidity level ",0, 3)
color = st.number_input("Input Color : " ,)
#columns = ['pH', 'temperature', 'taste', 'odor', 'fat', 'turbidity', 'color']
#def predict(): 
   # row = [pH,temperature,taste,odor,fat,turbidity,color]
   # X = pd.DataFrame([row], columns = columns)
 
    #prediction = model.predict(X)
    #st.write(prediction)
    

    
    

if st.button('Predict '):
    result =  prediction(pH,temperature,taste,odor,fat,turbidity,color) 
    
    if result == ['high'] :
        high = """<p style='background-color :#9DEE2B; border-radius :7px ;padding:20px; line-height:25px; font-size:20px'>This milk has a high quaility!!!<p>"""
        st.markdown(high, unsafe_allow_html=True)
       
    
        with open("trollthumb.jpg", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="trollthumb.jpg",
                    mime="image/png"
                  )
    elif result == ['medium'] :
             high = """<p style='background-color :#909193 ; border-radius :7px ; line-height:25px; padding:20px; font-size:20px;'>This milk has a medium quaility!!!<p>"""     
             st.markdown(high, unsafe_allow_html=True) 
         
        
             with open("trollnotbad.jpg", "rb") as file:
                btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="trollnotbad.jpg",
                    mime="image/png"
                  )
    elif result == ['low'] :
             high = "<p style='background-color :#D43915; border-radius :7px ;padding:20px; line-height:25px; font-size:20px;'>This milk has a low quaility!!!<p>"
             st.markdown(high, unsafe_allow_html=True) 
        
        
        
        
             with open("thumbdown.png", "rb") as file:
                   btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="thumbdown.png",
                    mime="image/png"
                  ) 
        
    
   
