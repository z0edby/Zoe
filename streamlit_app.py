l = voc.shape[0]
if "indices" in st.session_state:
 indices=st.session_state["indices"]
else:
 indices = np.random.choice(l, size=4, replace=False)
j = np.random.choice(indices)
word_fr=voc['Définition'].values[j]
st.write('Traduis: '+word_fr)

def is_correct(i, j):
 if i==j:
   st.write("Bien joué !")
   if "indices" in st.session_state:
     del st.session_state["indices"]
 else:
   st.write("C'est perdu.")
   st.session_state["indices"]=indices
col1, col2 = st.columns(2) 
with col1:
   for i in range(2):
       st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))
with col2:
   for i in range(2,4):
       st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))
