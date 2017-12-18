import fresh_tomatoes

import media

# Show Se7en movie trailer
seven = media.Movie(
 "Seven",
 '''In an unnamed American city soon-to-be-retiring
 detective William Somerset is partnered with short-tempered but idealistic
 David Mills, who recently transferred to the department, moving to the city
 with his wife Tracy.''',
 "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
 "https://www.youtube.com/watch?v=znmZoVkCjpI")


# Show Forrest Grump movie trailer
forrestgrump = media.Movie(
 "Forrest Grump",
 '''In 1981, Forrest Gump recounts his life story to strangers who sit next to
 him on a bench in Savannah, Georgia.''',
"https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # noqa
"https://www.youtube.com/watch?v=EtYNngO7eq4")


# forrestgrump.show_trailer()
# Show Gladitor movie trailer
gladiator = media.Movie(
 "Gladiator",
 '''In AD 180, Hispano-Roman General Maximus Decimus Meridius\
 leads the Roman army
 to victory against the Germanic tribes near Vindobona\
 on the Limes Germanicus.''',
"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # noqa
"https://www.youtube.com/watch?v=ol67qo3WhJk")

# gladiator.show_trailer()
# Show The Shawshank Redemption moview trailer
ssrd = media.Movie(
 "The Shawshank Redemption",
 '''In 1947 Portland, Maine, banker Andy Dufresne is convicted of murdering his\
 wife and her lover, and is sentenced to two consecutive life sentences at the\
 Shawshank State Penitentiary. Andy is befriended by\
 contraband smuggler, Ellis 'Red' Redding, an inmate serving\
 a life sentence.''',
 "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
 "https://www.youtube.com/watch?v=6hB3S9bIaco")  # noqa

# ssrd.show_trailer()
# Show The Matrix movie trailer
matrix = media.Movie(
 "The Matrix",
 '''Computer programmer Thomas Anderson lives a double life under the\
 hacker alias 'Neo'. He believes something is wrong with the world\
 and is puzzled by repeated online encounters with the cryptic phrase\
 'The Matrix'. Trinity contacts him, saying that a man named Morpheus\
 can explain its meaning; however, the Agents, led\
 by Agent Smith, apprehend Neo
 at his office and attempt to get a plea bargain out of Neo in exchange for\
 helping them capture Morpheus, whom they call a terrorist.''',
 "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
 "https://www.youtube.com/watch?v=vKQi3bBA1y8")

# matrix.show_trailer()
# Show Batman v Superman movie trailer
bvs = media.Movie(
 "Batman v Superman: Dawn of Justice",
 '''Eighteen months after the battle between Superman and General Zod in\
 Metropolis, Superman has become a controversial figure.''',
 "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
 "https://www.youtube.com/watch?v=xe1LrMqURuw")

# bvs.show_trailer()
movies = [seven, forrestgrump, gladiator, ssrd, matrix, bvs]

fresh_tomatoes.open_movies_page(movies)
'''
Opens the python file
'''
