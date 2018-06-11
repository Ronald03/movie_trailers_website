# Import the webbrowser library;
import webbrowser


class Movie():
    # '''
    # This Movie class will create a movie object every time
    # it get instanciated.
    # Objects created with the Movie class contain the movie title,
    # a storyline, a link to a poster image and a link of the video trailer.

    # This class does not return but it create an movie object.

    # Movie class expects 4 string parameters.
    # '''

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        # Initialize the object creation by assigning the provided arguments
        # to the object itself
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show_trailer() method takes an object as argument (a movie object)

    def show_trailer(self):
        # Use the open() method from the webrowser library to open
        # the trailer video on the browser

        # Must provide the object's url for the video trailer
        webbrowser.open(self.trailer_youtube_url)
