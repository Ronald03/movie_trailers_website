# Import  media class and fresh_tomatoes
import media
import fresh_tomatoes


# Instanciate the media class to create new movies,
# Must provide a movie name, storyline, images of movie's
# poster and a video link (youtube) for the trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/"
    "Avatar-Teaser-Poster.jpg",
    "https://youtu.be/5PSNL1qE6VY")


john_wick = media.Movie(
    "John Wick",
    "Legendary assassin John Wick retired from his violent career after \
     marrying the love of his life.",
    "https://upload.wikimedia.org/wikipedia/en/9/98/"
    "John_Wick_TeaserPoster.jpg",
    "https://youtu.be/RllJtOw0USI")


bucket_list = media.Movie(
    "The Bucket List",
    "Two men, blue-collar mechanic Carter Chambers and billionaire hospital \
     magnate Edward Cole meet for the first time in the hospital after both  \
     have been diagnosed with terminal lung cancer.",
    "https://upload.wikimedia.org/wikipedia/en/2/20/Bucket_list_poster.jpg",
    "https://youtu.be/vc3mkG21ob4")

ratatouille = media.Movie(
    "Ratatouille",
    "Remy dreams of becoming a great chef, despite being a rat in a \
     definitely rodent-phobic profession. He moves to Paris to follow his    \
     dream, and with the help of hapless garbage boy Linguini he puts his    \
     culinary skills to the test in the kitchen but he has to stay in hiding \
     at the same time, with hilarious consequences. Remy eventually gets the \
     chance to prove his culinary abilities to a great food critic but   \
     is the food good? A Pixar animation.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://youtu.be/c3sBBRxDAqk")

going_in_style = media.Movie(
    "Going In Style",
    "Lifelong buddies Willie (Morgan Freeman), Joe (Michael Caine) and  \
     Albert (Alan Arkin) decide to buck retirement and step off the  \
     straight-and-narrow when their pension funds become a corporate \
     casualty. Desperate to pay the bills and come through for their \
     loved ones, the three men risk it all by embarking on a daring  \
     adventure to knock off the very bank that absconded with their money.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/"
    "Going_in_Style_2017_film_poster.jpg",
    "https://youtu.be/hcdTN5soeQw")

last_vegas = media.Movie(
    "Last Vegas",
    "Aging pals Billy (Michael Douglas), Paddy (Robert De Niro),    \
    Archie (Morgan Freeman) and Sam (Kevin Kline) have been best    \
    friends since childhood. When Billy finally proposes to his \
    much-younger girlfriend, all four friends go to Las Vegas to    \
    celebrate the end of Billy's longtime bachelorhood and relive   \
    their glory days. However, the four quickly realize that the    \
    intervening decades have changed Sin City and tested their  \
    friendship in ways they had not imagined.",
    "https://upload.wikimedia.org/wikipedia/en/d/dd/Last_Vegas_Poster.jpg",
    "https://youtu.be/TvK3m0wJutI")

shawshank_redemption = media.Movie(
    "The ShawShank Redemption",
    "Andy Dufresne (Tim Robbins) is sentenced to two consecutive life   \
    terms in prison for the murders of his wife and her lover and is    \
    sentenced to a tough prison. However, only Andy knows he didn't \
    commit the crimes. While there, he forms a friendship with Red  \
    (Morgan Freeman), experiences brutality of prison life, adapts, \
    helps the warden, etc., all in 19 years.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/"
    "ShawshankRedemptionMoviePoster.jpg",
    "https://youtu.be/6hB3S9bIaco")


# create an array of movies to be passed into the executioner python file
movies = [toy_story, avatar, john_wick, bucket_list,
          ratatouille, going_in_style, last_vegas, shawshank_redemption]

# Call fresh_tomates class to load and open a html page with all the movies
# on the movies array.

# The '.open_movies_page()' is a method in the fresh_tomates() file
# that open a tab on the browser and point it to the html file generated
# by the fresh_tomatoes() file.
fresh_tomatoes.open_movies_page(movies)
