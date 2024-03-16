import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_processing import load_data, preprocess_data
import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         poster_path = data['poster_path']
#         full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
    
def train_model(movies_file, credits_file):
    # Load and preprocess data
    movies, credits = load_data(movies_file, credits_file)
    movies_data = preprocess_data(movies, credits)

    # Create CountVectorizer
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies_data['tags']).toarray()

    # Compute cosine similarity
    similarity = cosine_similarity(vectors)

    # Save model
    with open('similarity.pkl', 'wb') as f:
        pickle.dump(similarity, f)

    # Fetch and save posters
    # poster_urls = {}
    # for movie_id, title in zip(movies_data['movie_id'], movies_data['title']):
    #     poster_url = fetch_poster(movie_id)
    #     poster_urls[title] = poster_url

    # with open('poster_urls.pkl', 'wb') as f:
    #     pickle.dump(poster_urls, f)
