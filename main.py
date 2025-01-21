# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import streamlit as st
import pickle

rest_dict  =  pickle.load(open('restaurants_dict.pkl', 'rb'))
similarity =  pickle.load(open('similarity.pkl', 'rb'))

rest_list = pd.DataFrame(rest_dict)
st.title("Restaurant recommender system")

recommended_restaurants = []
def recomm(locality):
    loc_index = rest_list[rest_list['Locality'] == locality].index[0]
    distances = similarity[loc_index]
    res_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in res_list:
        recommended_restaurants.append(rest_list.iloc[i[0]].Name)
    return recommended_restaurants

localityname = st.selectbox(
    "How would you like to be contacted?",
    rest_list['Locality'].drop_duplicates().values
    )

st.write("You selected:", localityname)

if st.button("Recommend"):
    Recommendetions = recomm(localityname)
    for i in Recommendetions:
           st.write(i)


