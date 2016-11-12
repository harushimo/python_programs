#!/usr/bin/python

import fresh_tomatoes
import media


anchor_man = media.Movie("AnchorMan", "A story about fictional character Ron Burgundy", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MzYwMzk5Ml5BMl5BanBnXkFtZTcwOTI4NzUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", "http://www.imdb.com/video/imdb/vi1149285913?playlistId=tt0357413&ref_=tt_ov_vi") 

old_school = media.Movie("Old School", "Three fruebds attempt to recapture their glory days by opening up a fraternity near their alma mater", "https://images-na.ssl-images-amazon.com/images/M/MV5BYzI4NDIzMDgtNGNkZi00MTI2LWJhYzgtYzM5NThhMTQ0OGIzXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg", "http://www.imdb.com/video/imdb/vi1147970073?playlistId=tt0302886&ref_=tt_ov_vi")

captain_america = media.Movie("Captain America", "An american solider recruited to defeat the red skull", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_SY1000_CR0,0,640,1000_AL_.jpg", "http://www.imdb.com/video/imdb/vi2912787481?playlistId=tt0458339&ref_=tt_ov_vi")

iron_man = media.Movie("Iron Man", "Tony Stark builts a suit in order to defend the weak", "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG", "https://youtu.be/7H0yo-lDuk0")

guardians_of_galaxy = media.Movie("Guardians of Galaxy", "A bunch of ragtime villians become heroes to save the galaxy", "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg", "http://www.imdb.com/video/imdb/vi1441049625?playlistId=tt2015381&ref_=tt_ov_vi")

doctor_strange = media.Movie("Doctor Strange", "A neurosurgeon who lost his ability to be surgeon. He needs to find a new path", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY317_CR1,0,214,317_AL_.jpg", "https://youtu.be/HSzx-zryEgM")

movies = [anchor_man, old_school, captain_america, iron_man, guardians_of_galaxy, doctor_strange]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
print(media.Movie.__module__)
print(media.Movie.__name__)
