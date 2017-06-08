import fresh_tomatoes
import media

"""module that runs everything!!"""

#here is my function that populates movies object with hardcoded movie details
movies = media.MyMovies()

#here are the two functions you good people provided
fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)