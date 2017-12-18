# coding = utf-8

import webbrowser

'''
Launch browser
Displays movie information in HTML
'''


class Movie():

        # Class calls the instanace of Movie

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        # Constructor that defines the parameter of Self


def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
