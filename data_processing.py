import pandas as pd 
import ast
from nltk.stem.porter import PorterStemmer
import requests

def load_data(movies_file, credits_file):
    # Load movies and credits data
    movies = pd.read_csv(movies_file)
    credits = pd.read_csv(credits_file)
    return movies, credits

def preprocess_data(movies, credits):
    # Merge movies and credits data
    movies = movies.merge(credits, on='title')

     # Convert 'overview' column to string type
    movies['overview'] = movies['overview'].astype(str)

    # Process genres, keywords, cast, and crew columns
    movies['genres'] = movies['genres'].apply(convert_genres)
    movies['keywords'] = movies['keywords'].apply(convert_genres)
    movies['cast'] = movies['cast'].apply(convert_cast)
    movies['crew'] = movies['crew'].apply(convert_director)

    # Process overview column
    movies['overview'] = movies['overview'].apply(lambda x: x.split())
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['crew'] + movies['cast']

    #Convert tags to str
    movies['tags'] = movies['tags'].apply(lambda x: ' '.join(x))
    # Stem tags
    movies['tags'] = movies['tags'].apply(stem)

    return movies[['movie_id', 'title', 'tags']]

def convert_genres(obj):
    # Convert genres column
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def convert_cast(obj):
    # Convert cast column
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L

def convert_director(obj):
    # Convert crew column
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

def stem(text):
    
    # Stem text
    ps = PorterStemmer()
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similarity[index]
    recommend_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in recommend_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path