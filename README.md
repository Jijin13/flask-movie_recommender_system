# Movie Recommender System
This is a simple movie recommendation system built using Flask, pandas, and scikit-learn. It takes a movie name as input and provides a list of recommended movies based on cosine similarity of movie tags.

## Features

- **Movie Recommendation:** Enter the name of a movie, and the app will return a list of similar movies.
- **Cosine Similarity:** The recommendation is based on calculating the cosine similarity of movie tags using natural language processing techniques.
  
## Tech Stack

- **Backend:** Flask, pandas, scikit-learn
- **NLP:** CountVectorizer (for feature extraction from text)
- **Similarity Metric:** Cosine Similarity
- **Frontend:** HTML (with Jinja2 templating)

## Dataset

The dataset used is a CSV file (movies.csv) that contains movie information such as titles and tags. The tags are a combination of genres, plot summaries, and keywords.

## Setup and Installation

### Prerequisites
- Python 3.x
- Flask
- pandas
- scikit-learn

### Installation
1. Clone the repository:

  ```sh
  git clone https://github.com/yourusername/movie-recommender.git
  cd movie-recommender
  ```

2. Create a virtual environment and activate it:
  
  ```sh
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. install the required packages:

  ```sh
  pip install -r requirements.txt
  ```

4. Ensure that the movies.csv file is in the root folder of the project. If not, add your own dataset containing movie titles and tags.

5. Run the Flask application:

  ```sh
  flask run
  ```

## Demo

[Watch the demo video](https://github.com/user-attachments/assets/89c22d2a-73b6-458c-8d77-8cb3835e0753)
