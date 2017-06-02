import webbrowser

class Movie():
    def __init__(self,title,storyline,image,youtube):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=image
        self.trailer_youtube_url=youtube




    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_id)