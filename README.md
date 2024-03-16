
# Movie Recommender System

This Movie Recommender System is a Python-based application that provides movie recommendations based on user-selected movies. It utilizes data from the TMDb (The Movie Database) API to fetch movie information and posters, and employs cosine similarity to recommend similar movies.

## Features

- Allows users to select a movie from a dropdown menu.
- Provides recommendations of similar movies based on the selected movie.
- Displays movie posters along with recommendations.
- Uses TMDb API to fetch movie posters dynamically.

## Dataset

The dataset used for training the model can be downloaded from Kaggle.
Sign up for an account at [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and download the Dataset.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/movie-recommender-system.git
   ```

2. Navigate to the project directory:
   ```
   cd movie-recommende-systemr
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Obtain API key:
   - Sign up for an account at [TMDb](https://www.themoviedb.org/) and obtain an API key.
   - Replace `YOUR_TMDB_API_KEY` in `train_model.py` and `app.py` with your actual API key.

5. Train the model:
   ```
   python train_model.py
   ```

6. Run the app:
   ```
   streamlit run app.py
   ```

## Usage

1. Select a movie from the dropdown menu.
2. Click the "Show Recommendation" button to view similar movie recommendations.
3. Movie recommendations along with posters will be displayed below.

## Screenshots

![Screenshot1](https://github.com/harshxmishra/movie-recommender-system/assets/123086111/8ed5bbed-32b0-4577-9e72-1b2abe7761c3)

*Figure 1: Movie Recommender System interface.*

## Credits

- Data provided by [TMDb](https://www.themoviedb.org/).
- Built with [Streamlit](https://streamlit.io/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Replace placeholders like `your-username`, `YOUR_TMDB_API_KEY`, and update the paths and names of screenshots as needed. You can also include additional sections such as "Contributing", "Acknowledgements", or "Support" if applicable to your project. Make sure to include relevant information and instructions to help users understand and use your project effectively.
