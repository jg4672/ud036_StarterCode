import media
''' Use the class in "Movie()" from media.py that will help create instances for movie poseter and youtube videos.'''
import fresh_tomatoes
''' Piece of code provided by Udacity (Instuctor Notes) which takes in a list of movies to creates and html file with a curated webpage of the movies.'''

predestination = media.Movie(
                        "Predestination",
                        "A temporal agent pursues a criminal that has eluded him throughout time, but engages in taboos of love, fate, identity and time travel.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Predestination_poster.jpg/220px-Predestination_poster.jpg",
                        "https://www.youtube.com/watch?v=jcQacCfi_pw&t")

last_dragon = media.Movie(
                        "The Last Dragon",
                        "In New York City, a young man seeks to reach the 'final level' of martial arts mastery known as the glow.",
                        "https://images-na.ssl-images-amazon.com/images/I/51fIOR1pd9L.jpg",
                        "https://www.youtube.com/watch?v=Z7Crt4S1IZM")

matrix = media.Movie(
                        "The Matrix",
                        "A movie about a sentient tire that discovers it has powers and a new found obsession.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8&t")

rubber = media.Movie(
                        "Rubber",
                        "A movie about a sentient tire that discovers it has powers and a new found obsession.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/fa/Rubber-2010-film-poster.jpg/220px-Rubber-2010-film-poster.jpg",
                        "https://www.youtube.com/watch?v=jH9uDuu0Qu4")

dark_knight = media.Movie(
                        "The Dark Knight",
                        "A movie about a sentient tire that discovers it has powers and an obsession",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

chappie = media.Movie(
                        "Chappie",
                        "A recycled police droid is stolen by gangsters, but becomes the first robot to be programmed with its own conscious: to think and feel for himself.",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
                        "https://www.youtube.com/watch?v=l6bmTNadhJE")


movies = [predestination, last_dragon, rubber, chappie, dark_knight, matrix]
''' List of movie instances to be create.'''
fresh_tomatoes.open_movies_page(movies)
