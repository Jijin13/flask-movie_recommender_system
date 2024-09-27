from flask import Flask, render_template, request, flash, url_for
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import pickle


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

df = pd.read_csv('movies.csv')

cv = CountVectorizer(max_features=5000, stop_words='english')
	
vectors = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
	try:
		movie_index = df[df['title']==movie].index[0]
		distance = similarity[movie_index]
		movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:5]
		recommendation = [df.iloc[i[0]].title for i in movie_list]
		return recommendation 
	except IndexError:
		return ['movie name not found']
	

@app.route("/")
def index():
	flash("Enter a Movie name")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	movie = request.form['name_input']
	if movie:
		recommendation = recommend(movie)
		for rec in recommendation:
			flash(rec)
		return render_template("index.html")
	else:
		return index()

if __name__ == '__main__':
	app.run(debug=True)