//Text Data cleaning script in python
// Escaping HTML Characters
tweet = " I like my &lt;3 phone &amp; you're awesome sony. Display Is Terrific , soo happyy :) http://www.sony.com"
import HTMLParser
html_parser = HTMLParser.HTMLParser()
newtweet = html_parser.unescape(tweet)
print newtweet
