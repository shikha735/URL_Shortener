from __future__ import with_statement
import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
import sys


def shorten (url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    urls = sys.argv[1:]
    for url in urls:
        shorturl = shorten(url)
        print(shorturl)

if __name__ == '__main__':
    main()
