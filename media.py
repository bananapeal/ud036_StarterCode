# -*- coding: utf-8 -*-
"""~~~Module Level Doc~~~
This module contains classes that are used in fresh_tomatoes.py to generate the 
favorite movie website.

api-style, it's just the data structures!
and my hard-coded method!!

.
"""
class movie():
    """This is the elemental data type that will make up the Movies array that
        will get passed to fresh_tomatoes.py. I am copying property names from 
        fresh_tomatoes.py . 
        Please provide strings:
        title = its title
        storyline = one sentence description of movie
        poster_image_url = url on imdb to poster image
        trailer_youtube_url = url to youtube trailer.
    """
   
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """this is constructor function for Movie. simple setter for the four
        string variables. 
        """
        print("constructor running")
        #As mentioned in that file, i much prefer camel-casing 
        #due to quicker typing speed vs the underscores
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
     
     
def MyMovies():
    """Hardcoded function that contains my scope of movie fandom.
        A sample of what i consider good / ok / and very bad.
        """
    
    print("my moveis running")
    #i'd love to scrape these from imdb best movies list but i'm too dumb and lazy
    #i absolutely hate long strings used as arguments, so here they are nice and listed first.
    #i try keep the caps consistent. consistent variable names allows me to copy paste and 
    #find and replace to rewrite repeated segments.
    bestSLine = "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers. "
    bestImageURI = "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg"
    bestYoutube = "https://www.youtube.com/watch?v=m8e-FF8MsqU"
    
    Best = movie("The Matrix" , bestSLine, bestImageURI, bestYoutube)
    
    okSLine = "The story of Henry Hill and his life through the teen years into the years of mafia, covering his relationship with wife Karen Hill and his Mob partners Jimmy Conway and Tommy DeVitto in the Italian-American crime syndicate. "
    okImageURI = "https://images-na.ssl-images-amazon.com/images/M/MV5BNThjMzczMjctZmIwOC00NTQ4LWJhZWItZDdhNTk5ZTdiMWFlXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,0,182,268_AL_.jpg"
    okYoutube = "https://www.youtube.com/watch?v=qo5jJpHtI1Y"
    
    ok = movie("Goodfellas", okSLine, okImageURI, okYoutube)

    worstSLine = "Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force, but the long dormant Sith resurface to claim their old glory."
    worstImageURI = "https://images-na.ssl-images-amazon.com/images/M/MV5BM2FmZGIwMzAtZTBkMS00M2JiLTk2MDctM2FlNTQ2OWYwZDZkXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,0,182,268_AL_.jpg"
    worstYoutube = "https://www.youtube.com/watch?v=bD7bpG-zDJQ"

    Worst = movie("Star Wars: Episode One", worstSLine, worstImageURI, worstYoutube)
    
    movies = [Best, ok, Worst]
    return movies 
