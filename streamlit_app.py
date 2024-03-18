import streamlit as st 
import pandas as pd
voc = pd.nead_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT-ZIygP_X0RCLp4r97Zub0bRwg1mtXtPABnlpFLFqsbnvb-qa_pEjrCFOGfd-xivTCc7QzWIQYL8iv/pub?output=csv')
st.dataframe(voc)
