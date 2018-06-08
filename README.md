# Best Movie Trailers (BMT)
This python script helps you create a website of your favorite movies trailers with just a few coding lines.

## Install

  - Fork this repository
  - Clone repository to your computer
 
## How to use
 - Open the show_trailer.py with python IDLE
 - Create instances of media.movie to input the details of each of your favorite movies
 - Create an array with the movies just created
 - Call the `fresh_tomatoes.open_movies_page('array')` and pass the  _movies_  array to it
 
### Example of instanciation:
```
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Te                                  aser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

movies = [avatar]
fresh_tomatoes.open_movies_page(movies)
```
## License

This is .....**free to the public!**