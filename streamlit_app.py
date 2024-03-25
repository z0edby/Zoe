creation d'une variable:
st.session_state["my_var"]=1
est-ce que la variable existe?
if"my-var"in st.session_state
supprimerla variable
det st.session_state["my_var"]
st.session_state["indices"]=indices
si bravo:
del st.session_state["indices"]
a la place del a def de indices:
if"indices"in st.session_state["indices"]
else:
  indices=np.random...
