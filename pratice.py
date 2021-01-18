
import streamlit as st
import pandas as pd
import sklearn
import numpy as np
import pickle
st.title('*******this is a kaggle data competition dataset*******')
st.header('the features requried to this dataset are ::')
columns=['bin_0', 'bin_1', 'bin_2', 'bin_3', 'bin_4', 'nom_5', 'nom_6', 'nom_7',
         'nom_8', 'nom_9', 'ord_0', 'ord_1', 'ord_2', 'ord_3', 'ord_4', 'ord_5',
         'sin_month', 'cos_month', 'sin_day', 'cos_day', 'nom_0_Green',
         'nom_0_Red', 'nom_1_Polygon', 'nom_1_Square', 'nom_1_Star',
         'nom_1_Trapezoid', 'nom_1_Triangle', 'nom_2_Cat', 'nom_2_Dog',
         'nom_2_Hamster', 'nom_2_Lion', 'nom_2_Snake', 'nom_3_China',
         'nom_3_Costa Rica', 'nom_3_Finland', 'nom_3_India', 'nom_3_Russia',
         'nom_4_Oboe', 'nom_4_Piano', 'nom_4_Theremin']
nom0=['nom_0_Red','nom_0_Green']
nom1=['nom_1_Polygon', 'nom_1_Square', 'nom_1_Star','nom_1_Trapezoid', 'nom_1_Triangle']
nom2=['nom_2_Cat', 'nom_2_Dog','nom_2_Hamster', 'nom_2_Lion', 'nom_2_Snake']
nom3=['nom_3_China','nom_3_Costa Rica', 'nom_3_Finland', 'nom_3_India', 'nom_3_Russia']
nom4=['nom_4_Oboe', 'nom_4_Piano', 'nom_4_Theremin']

with open('categorical_model_nom5','rb') as f:
     nom_5_features=pickle.load(f)
with open('categorical_model_nom6','rb') as f:
    nom_6_features=pickle.load(f)
with open('categorical_model_nom7','rb') as f:
    nom_7_features=pickle.load(f)
with open('categorical_model_nom8','rb') as f:
    nom_8_features=pickle.load(f)
with open('categorical_model_nom9','rb') as f:
    nom_9_features=pickle.load(f)
ord_em=[2, 1, 3]
ord_1={'Grandmaster':5,'Master':4,'Expert':3,'Contributor':2,'Novice':1}
with open('C:/Users/beast brothers/categorical_model_ord2','rb') as f:
    ord_2=pickle.load(f)
with open('C:/Users/beast brothers/categorical_model_ord3','rb') as f:
    ord_3=pickle.load(f)
with open('C:/Users/beast brothers/categorical_model_ord_4','rb') as f:
    ord_4=pickle.load(f)
with open('C:/Users/beast brothers/categorical_model_ord_5','rb') as f:
    ord_5=pickle.load(f)
listo2=ord_2.categories_
listo3=ord_3.categories_
listo4=ord_4.categories_
listo5=ord_5.categories_
listo2=list(listo2[0])
listo3=list(listo3[0])
listo4=list(listo4[0])
listo5=list(listo5[0])
st.write('here you can just give one record to check')
b0=st.selectbox('choose either of one complusory for bin_0',options=[0,1])
b1=st.selectbox('choose either of one complusory for bin_1',options=[0,1])
b2=st.selectbox('choose either of one complusory for bin_2',options=[0,1])
b3=st.selectbox('choose either of one complusory for bin_3',options=[0,1])
b4=st.selectbox('choose either of one complusory for bin_4',options=[0,1])
n0=st.selectbox('choose either of one complusory for nom_0',options=nom0)
n1=st.selectbox('choose either of one complusory for nom_1',options=nom1)
n2=st.selectbox('choose either of one complusory for nom_2',options=nom2)
n3=st.selectbox('choose either of one complusory for nom_3',options=nom3)
n4=st.selectbox('choose either of one complusory for nom_4',options=nom4)
n5=st.selectbox('choose either of one complusory for nom_5',options=list(nom_5_features.keys()))
n6=st.selectbox('choose either of one complusory for nom_6',options=list(nom_6_features.keys()))
n7=st.selectbox('choose either of one complusory for nom_7',options=list(nom_7_features.keys()))
n8=st.selectbox('choose either of one complusory for nom_8',options=list(nom_8_features.keys()))
n9=st.selectbox('choose either of one complusory for nom_9',options=list(nom_9_features.keys()))
o0=st.selectbox('choose either of one complusory for ord_0',options=ord_em)
o1=st.selectbox('choose either of one complusory for ord_1',options=list(ord_1.keys()))
o2=st.selectbox('choose either of one complusory for ord_2',options=listo2)
o3=st.selectbox('choose either of one complusory for ord_3',options=listo3)
o4=st.selectbox('choose either of one complusory for ord_4',options=listo4)
o5=st.selectbox('choose either of one complusory for ord_5',options=listo5)
month=st.text_input('choose either of one complusory for month like 1,2,...')
day=st.text_input('choose either of one complusory for day like 1,2,...')
predict=st.button('submit to predict')
if predict:
    try:
        b0=int(b0)
        b1=int(b1)
        b2=int(b2)
        b3=int(b3)
        b4=int(b4)
        month=int(month)
        day=int(day)
        sin_month=np.sin(2*np.pi*(month-1)/11)
        cos_month=np.cos(2*np.pi*(month-1)/11)
        sin_day=np.sin(2*np.pi*(day-1)/30)
        cos_day=np.cos(2*np.pi*(day-1)/30)
        
        o0=int(o0)
        o1=ord_1.get(o1)
        o2=int(ord_2.transform([[o2]]))
        o3=int(ord_3.transform([[o3]]))
        o4=int(ord_4.transform([[o4]]))
        o5=int(ord_5.transform([[o5]]))
        nom_0={}
        nom_1={}
        nom_2={}
        nom_3={}
        nom_4={}
        for i in range(len(nom0)):
            nom_0[nom0[i]]=0
        for i in range(len(nom1)):
            nom_1[nom1[i]]=0
        for i in range(len(nom2)):
            nom_2[nom2[i]]=0
        for i in range(len(nom3)):
            nom_3[nom3[i]]=0
        for i in range(len(nom4)):
            nom_4[nom4[i]]=0
        for i in range(len(nom0)):
            if nom0[i]==n0:
                nom_0[n0]=1
        for i in range(len(nom1)):
            if nom1[i]==n1:
                nom_1[n1]=1
        for i in range(len(nom2)):
            if nom2[i]==n2:
                nom_2[n2]=1
        for i in range(len(nom3)):
            if nom3[i]==n3:
                nom_3[n3]=1
        for i in range(len(nom4)):
            if nom4[i]==n4:
                nom_4[n4]=1
        n5=nom_5_features.get(n5)
        n6=nom_6_features.get(n6)
        n7=nom_7_features.get(n7)
        n8=nom_8_features.get(n8)
        n9=nom_9_features.get(n9)
        data={'b0':b0,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'n5':n5,'n6':n6,'n7':n7,'n8':n8,'n9':n9,'o0':o0,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'sin_month':sin_month,'cos_month':cos_month,'sin_day':sin_day,'cos_day':cos_day}
        d0=pd.DataFrame(nom_0,index=[0])
        d1=pd.DataFrame(nom_1,index=[0])
        d2=pd.DataFrame(nom_2,index=[0])
        d3=pd.DataFrame(nom_3,index=[0])
        d4=pd.DataFrame(nom_4,index=[0])
        df=pd.DataFrame(data,index=[0])
        df=df.join([d0,d1,d2,d3,d4])
        with open('C:/Users/beast brothers/categorical_model.pkl','rb') as f:
            model=pickle.load(f)
        with open('C:/Users/beast brothers/categorical_model_transformations','rb') as f:
            scaler=pickle.load(f)
        model_inputs=scaler.transform(df.values)
        predictions=model.predict(model_inputs)
        st.spinner('process in going on....')
        predictions=np.argmax(predictions,axis=-1)
        st.write(f"the prediction is {predictions}")
    except:
        print('some features are not given or given incorrect')
    



