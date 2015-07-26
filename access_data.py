// Access Internet Data from a url using python

import urllib2
def main():
    weburl = urllib2.urlopen("https://www.github.com/turlapatykaushik")
    print str(weburl.getcode())
    data = weburl.read()
    print data
if __name__ == "__main__":
    main()
