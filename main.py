from flask import Flask, jsonify, request, render_template
import json



app = Flask(__name__)


def load_movies():
    with open('movies.json') as f:
        return json.load(f)


def save_movies(movies):
    with open('movies.json', 'w') as f:
        json.dump(movies, f, indent=4)



#main page 
@app.route('/')
def index():
    return render_template('index.html')




#get all
@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = load_movies()
    return jsonify(movies)





#get by id
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_by_id(movie_id):
    movies = load_movies()
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({"error": "Movie not found"}), 404




#get by director
@app.route('/movies/director/<string:director>', methods=['GET'])
def get_by_director(director):
    movies = load_movies()
    filtered_movies = [movie for movie in movies if movie['director'].lower() == director.lower()]
    return jsonify(filtered_movies)





#get by year
@app.route('/movies/year/<int:year>', methods=['GET'])
def get_by_year(year):
    movies = load_movies()
    filtered_movies = [movie for movie in movies if movie['year'] == year]
    return jsonify(filtered_movies)



#get total count
@app.route('/movies/count', methods=['GET'])
def get_total_count():
    movies = load_movies()
    return jsonify({"count": len(movies)})



#add new movie post req
@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = request.get_json()
    if 'title' not in new_movie or 'director' not in new_movie or 'year' not in new_movie:
        return jsonify({"error": "Missing required fields"}), 400
    
    movies = load_movies()
    new_movie['id'] = movies[-1]['id'] + 1 if movies else 1  
    movies.append(new_movie)
    save_movies(movies)
    
    return jsonify(new_movie), 201



#movie delete post req
@app.route('/movies/delete', methods=['POST'])
def delete_movie():
    data = request.get_json()
    movie_id = data.get('id')

    if not movie_id:
        return jsonify({"error": "Movie ID is required"}), 400
    
    movies = load_movies()
    mdelete = next((movie for movie in movies if movie['id'] == movie_id), None)
    
    if mdelete:
        movies.remove(mdelete)
        save_movies(movies)
        return jsonify({"message": "Movie deleted successfully"}), 200
    else:
        return jsonify({"error": "Movie not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
