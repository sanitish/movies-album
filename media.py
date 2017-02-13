import webbrowser

class Movie():
    def __init__(self, movie_title, movie_poster, youtube_link):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = youtube_link

    def movie_show(self):
        webbrowser.open(self.movie.trailer_youtube_url)
        
