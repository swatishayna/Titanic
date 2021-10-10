import streamlit as st
import pickle
import numpy as np

Pclass	Sex	Age	SibSp	Parch	Fare	Embarked
st.title('Titanic Survival Prediction App')

Pclass = st.selectbox('Elect the Passenger Class',(1,2,3))
Sex  =  st.selectbox( 'Select Gender of the Passenger ',  ('Male','Female'))  
Age  =  st.slider( 'Input the age(0 age for new_born less than a year) ',  min_value = 0	, max_value=80) 
SibSp  =  st.slider( 'Number of Siblings ',  min_value = 0	, max_value = 8)     
Parch  =  st.slider( 'Parch',  min_value = 0	, max_value=6) 
Fare  =  st.slider(' Input Fare',  min_value = 0	, max_value=512	) 
Embarked = st.selectbox(' Embarked',  ('S','C','Q')	) 


submit = st.button('Predict')
if submit:

    d_sex= {'Male':0, 'Female':1}
    d_Embarked = {'S':1,'C':2, 'Q':3}
    input_list =[]
    input_list.append(Pclass)
    input_list.append(d_sex[Sex])
    input_list.append(Age)
    input_list.append(SibSp)
    input_list.append(Parch)
    input_list.append(Fare)
    input_list.append(d_Embarked[Embarked])
    
    print(input_list)
    
    
    
    
    #loading the stored model for prediction
    model = pickle.load(open('dt_best.pickle', 'rb'))
    output = model.predict(input)
    if output:
        st.write(output)
        
        