## Synopsis

This project is written in Python. It will fetch timeline from Twitter and let the script analyzes user's feeling from most recent tweets. Try it, it's fun!

## Motivation

In the lab, I have many friends that are very less in talking. I don't have many chances to know what are they up to and how is their recent feeling. By running this script, I know their feeling and probably will cheer them up when they are sad. Another story: my sister only tweets when she is sad. When I tried to run the script to analyze her tweets, the script proves it!

## Installation

This project uses Twitter API, NLTK library for Natural Language Processing, Numpy for fundamental computation in Python and matplotlib to plot a simple visualization. In the script, I already assigned access token as permission to use Twitter API, you don't have to generate by yourself. Install Python, NLTK, Numpy and matplotlib if you haven't.

1. Python 2.7 (https://www.python.org/downloads/), do not use Python 3 as not supported by NLTK library
2. NLTK (http://www.nltk.org/install.html)
3. Numpy (http://www.scipy.org/install.html), it is usually included during Python installation
4. matplotlib (http://matplotlib.org/users/installing.html)

## Tests

Download the script and run through command line as below:

Put the twitter's username without quotation and "@" symbol. This will fetch 100 recent tweets from @girikuncoro and shows visualization.
```
# python feeling.py girikuncoro
```
You can analyze more than 100 tweets by adding argument next to the username. For example:
```
# python feeling.py girikuncoro 250
```
This will fetch 250 recent tweets of @girikuncoro and shows visualization. Enjoy!

## Author

Hello, I'm Giri! This project is written by me as part of my assignment in INFO6010 - Computational Method in Information Science. DanCo (http://www.cs.cornell.edu/~danco/) teaches this, he is a great professor! Checkout my web (http://kuncoro.co) to know more about me.
