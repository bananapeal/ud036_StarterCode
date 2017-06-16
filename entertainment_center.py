"""module that runs everything!! execute this file. everything hardcoded
takes no inputs."""

import fresh_tomatoes
import media


# here is my function that populates movies object with hardcoded movie details
movies = media.MyMovies()

# here are the two functions Udacity provided
fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)
