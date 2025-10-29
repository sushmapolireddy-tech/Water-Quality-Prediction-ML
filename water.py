

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/polir/Downloads/water11/water1.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Water quality prediction using ml',
                          
                          [ 'Home',
                            'Water quality prediction'
                           
                            ],
                          default_index=0)

# water quality Prediction Page
if (selected == 'Home'):
    
    # page title
    st.title('Water quality prediction using ml')

    st.image("WhatsApp Image 2023-04-13 at 19.11.21.jpeg")


    

    st.image("WhatsApp Image 2023-04-13 at 19.11.19.jpeg")
    
  
    
# water quality Prediction Page
if (selected == 'Water quality prediction'):
    
    # page title
    st.title('Water quality prediction ml')

    st.image('WhatsApp Image 2023-04-13 at 19.11.20.jpeg')
    
    st.title("0- means water quality bad && 1- means water quality good")
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
        
    with col1:
        ph = st.text_input('ph ')
    
    with col2:
        Hardness  = st.text_input('Hardness')
    
    with col3:
        Solids	 = st.text_input('Solids')
    
    with col1:
        Chloramines= st.text_input('Chloramines')
    
    with col2:
         Sulfate	 = st.text_input(' Sulfate	')
    
    with col3:
        Conductivity		 = st.text_input('Conductivity	')
    
    with col1:
        Organiccarbon = st.text_input('Organiccarbon')

    with col2:
        Trihalomethanes = st.text_input('Trihalomethanes')
    
    with col3:
        Turbidity = st.text_input('Turbidity')
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('start up Result'):
        diab_prediction = diabetes_model.predict([[ ph, Hardness, Solids, Chloramines, Sulfate,
        Conductivity, Organiccarbon, Trihalomethanes, Turbidity]])

        st.success('The output is {}'.format(diab_prediction ))
        
        
        
    

# Parkinson's Prediction Page
if (selected == "graph comparsion"):
    
    # page title
    st.title("graph comparsion")

    st.image("Capture.png")


    st.image("Capture1.png")

             
    st.image("Capture2.png")

   
    
    
# Parkinson's Prediction Page
if (selected == "result"):
    
    # page title
    st.title("result")

    st.image("Capture3.png")


    
    
    
   

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")








