# Movie Trailer Website

```
This a small collection of movie posters and associated trailers are contained on a single webpage. It is curated movie page displays each movie trailer's posters and when clicked launches its YouTube movie trailer in a pop-up window. 
```

## Installation
* Ensure that the supporting files are contained in the same directory. The files are:
```sh
fresh_tomatoes.html
media.py
entertainment_center.py 
fresh_tomatoes.py
```
* If the file fresh_tomatoes.html is NOT present, then run the file fresh_tomatoes.py.

## File Summaries
### media.py
* Imports the webbrowser file
* Contains the class Movie which receives details (as arguments) about the movie poster.
* Movie details are provided by the python file entertainment_center.py.
* The class' relevant information about the movie includes each posters image and video url.

### entertainment_center.py
* Imports media and fresh_tomates files
* Contains all instances/objects for each class Movie which is listed in an array.
* The method showtrailer will be used to launch a video trailer associated to the movie poster.
* The file fresh_tomatoes sends movie titles array which references the movie's details as arguments to Movie class.

## fresh_tomatoes.py
From instructor's notes freely provided this program to arrange movie posters into a webpage: [fresh_tomatoes.py](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py)
The majority of the code was provided in the intructor project also includes some CSS and jQuery involved in the display of the webpage.