import pickle
import streamlit as st
from train_model import train_model
from data_processing import load_data, preprocess_data, fetch_poster, recommend
import requests

# Load data
movies, credits = load_data("tmdb_5000_movies.csv", "tmdb_5000_credits.csv")
movies_data = preprocess_data(movies, credits)

# Train model
train_model("tmdb_5000_movies.csv", "tmdb_5000_credits.csv")

# Load trained model
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.header('Movie Recommender System')
selected_movie = st.selectbox("Type or select a movie from the dropdown", movies_data['title'].values)

if st.button('Show Recommendation'):
    index = movies_data[movies_data['title'] == selected_movie].index[0]
    recommend_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in recommend_list:
        recommended_movie_names.append(movies_data.iloc[i[0]]['title'])
        movie_id = movies_data.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))



    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
