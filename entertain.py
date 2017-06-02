import media
import fresh_tomatoes
alien=media.Movie("Alien:Covenant",
                  "A story of some stupid space ships",
                  "http://www.peckhamplex.london/imgs/posters/trailers/alien-covenant.jpg",
                   "https://www.youtube.com/watch?v=svnAD0TApb8&t=3s"
                  )







trans=media.Movie("Transformers:The Last Knight","N/A",
                  "https://i.ytimg.com/vi/oHGrd6GhSs4/maxresdefault.jpg","https://www.youtube.com/watch?v=6Vtf0MszgP8")


furious=media.Movie("The fate of the Furious","N/a","http://cdn2-www.comingsoon.net/assets/uploads/gallery/fast-8_1/fate_of_the_furious_ver3_xlg.jpg","https://www.youtube.com/watch?v=5uaJufU1JTs&t=93s"
                    )


movie_list=[alien,trans,furious]

fresh_tomatoes.open_movies_page(movie_list)

