import streamlit as st
st.title("CGPA Calculator")
grades = {"O":10, "A+":9, "A":8,"B+":7, "B":6, "RA":5}
ccred_sum = 0
ccgp_sum = 0
n = st.number_input("Number of Subjects: ", min_value=1, max_value= 100, value=1)
st.divider()

for i in range(n):
    ccreds = st.number_input("Number of Credits for Subject "+str(i+1)+": ", min_value=0, max_value= 10, value=0)
    l_grade = st.selectbox("Letter Grade of Subject "+str(i+1)+": ",("O", "A+", "A", "B+", "B", "RA"))
    st.divider()
    ccgp =  ccreds * grades[l_grade]
    ccred_sum+=ccreds
    ccgp_sum+=ccgp
try:
    cgpa = round(ccgp_sum/ccred_sum,2)
except:
    pass