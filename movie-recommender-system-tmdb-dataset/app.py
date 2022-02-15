import pickle
import streamlit as st
import requests


# fetching poster from api @tmdb
def fetch_poster(movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US").json()
    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"


# recommender function - same as notebook 
# additions - returns names of fetches movies and posters
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# streamlit layout
st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# on click of the button
if st.button('Show Recommendation'):
    # fetch the movie names and posters.
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)

    # display the poster and movie name.
    for i in enumerate(st.columns(5)):
        with i[1]:
            st.text(recommended_movie_names[i[0]])
            st.image(recommended_movie_posters[i[0]])
    




