import webbrowser
class Movie():
    '''The instances of this class intends to display a movie poster along with the movie title and its storyline.
        Upon clicking the poster image the hyperlink will navigate to the Youtube trailer.'''

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url):
        '''Constructor: Initialize and save space memory to remember details about movies being created with details from 'self' Instance Variables.'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        '''Instance Method: Opens a browser and play the trailer of the movie selected.'''
        webbrowser.open(self.trailer_youtube_url)
