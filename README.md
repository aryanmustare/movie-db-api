# movie-db-api
This project allows users to manage movie records efficiently. It provides endpoints to retrieve movie details, filter by director or year, and add or delete movies



## API Endpoints


- **`GET /movies`** - Get list of all movies
- **`GET /movies/{id}`** - Get movie by ID
- **`GET /movies/director/{director}`** - Get movies by director
- **`GET /movies/year/{year}`** - Get movies by year
- **`GET /movies/count`** - Get total count of all movies
- **`POST /movies`** - Add a new movie (requires data- title, director, year)
- **`POST /movies/delete`** - Delete movie by ID (test this using postman)


## Backend API Technology:
- Flask
