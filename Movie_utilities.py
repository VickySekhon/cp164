"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Vicky Sekhon
ID:      169024498
Email:   sekh4498@wlu.ca
Section: CP164 B
__updated__ = "2022-01-21"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    # Your code here
    title = input("Enter movie title: ")
    year = int(input("Enter the year of release: "))
    director = input("Enter the name of the director: ")
    rating = float(input("Enter the movie rating: "))
    genres = []
    genre_codes = input("Enter a genre number (ENTER to quit): ")
    while genre_codes != "":
        genres.append(int(genre_codes))
        genre_codes = input("Enter a genre number (ENTER to quit): ")
        
    movie = Movie(title, year, director, rating, genres)
    
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    
    title, year, director, rating, genres = line.split("|")
    genres = genres.split(",")
    final_genres = []
    for index in genres:
        final_genres.append(int(index))
    year = int(year)
    rating = float(rating)

    movie = Movie(title, year, director, rating, final_genres)

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    movies = []
    text = fv.readline().strip() # strip is used to create a new line
    while text != "":
        movies.append(read_movie(text))
        text = fv.readline().strip() # strip is used to create a new line again this time, inside the loop
    
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    # Your code here
    genres = []
    genre = input("Enter a genre number (ENTER TO QUIT): ")
    while genre != "":
        if not genre.isnumeric():
            print("Error not a number.")
        elif int(genre) > 10 or int(genre) < 0:
            print("Error input must be between 0 and 10.")
        elif int(genre) in genres:
            print("Error genre already choosen.")
        else:
            genres.append(int(genre))
        genre = input("Enter a genre number (ENTER TO QUIT): ")
    #Addresses the issue where when "","","","0","" was tested it would return an empty list
    if len(genres) == 0:
        print("Atleast one genre must be selected.")
        genre = input("Enter a genre number (ENTER TO QUIT): ")
        if len(genres) == 0:
            print("Atleast one genre must be selected.")
            genre = input("Enter a genre number (ENTER TO QUIT): ")
            if len(genres) == 0:
                print("Atleast one genre must be selected.")
                genre = input("Enter a genre number (ENTER TO QUIT): ")
                genres.append(int(genre))
        
    genres.sort()
    
    return genres



def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    for i in movies:
        x = str(i)
        fv.write(f"{x}\n\n")
    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    ymovies = []

    for movie in movies:
        if movie.year == year:
            ymovies.append(movie)
    
    c = 1
    for i in ymovies:
        print(f"Movie Object {c}:\n{i}")
        print()
        c += 1
        
    return ymovies

def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    rmovies = []
    
    for movie in movies:
        if movie.rating >= rating:
            rmovies.append(movie)
    
    c = 1
    for i in rmovies:
        print(f"Movie Object {c}:\n{i}")
        print()
        c += 1
        
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    # Your code here

    gmovies = []
    
    for movie in movies:
        for g in movie.genres:
            if g == genre:
                gmovies.append(movie)
            
  
    c = 1
    for i in gmovies:
        print(f"Movie Object {c}:\n{i}")
        print()
        c += 1

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    # Your code here

    gmovies = []
    
    
    for movie in movies:
            if movie.genres == genres:
                gmovies.append(movie)
            
  
    c = 1
    for i in gmovies:
        print(f"Movie Object {c}:\n{i}")
        print()
        c += 1

    return gmovies


 

def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    # Your code here
    
    #count is a variable we have to return, so I just create a list of zeroes that has the same amount of zeroes as Movie.GENRES
    counts = [0] * len(Movie.GENRES)
    print(f"The empty list of counts: {counts}")

    #Iterates through each individual movie object in the list movies provided by the user
    for movie in movies:
        #Iterates through the genre codes of that specific movie object
        for indice in movie.genres:
            #Looks at the genres in the Movie class list called GENRES by referencing the class first then the name of the list
            for genre in Movie.GENRES:
                #If index of a genre in the Movie.GENRES list is the same as the index in the genre codes list then the actual genre of the index will be stored in genre
                if Movie.GENRES.index(genre) == indice:
                    #It finds the same index of the genre in counts as the index in the movie objects genre list and adds 1 to it
                    counts[Movie.GENRES.index(genre)] += 1

    

    print()
    return (f"The processed list of counts: {counts}") 
