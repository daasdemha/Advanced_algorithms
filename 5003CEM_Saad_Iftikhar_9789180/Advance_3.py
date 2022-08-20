# importing required labraries
import concurrent.futures
import urllib.request
import timeit
import newspaper
from newspaper import Article

URLs = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com', ]  # list of urls to scrape


def get_headlines():
    for url in URLs:  # looping through each URLs
        result = newspaper.build(url, memoize_articles=False)  # The results are built
        print('\n''The headlines from %s are' % url, '\n')  # The headlines are printed
        for i in range(1,6):  # looping from 1 to 5
            art = result.articles[i]  # The article results are assighned to the art varible
            art.download()  # downloading the results
            art.parse()  # parsing the results
            print(art.title)  # priniting the title


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def concurrent_URLs_example():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:  # assigning the concurrent
        # thread workers as the executor
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLs}  # loading the URL and assiging
        # it to a variable
        for future in concurrent.futures.as_completed(future_to_url):  # looping through the future_to_url varible.
            url = future_to_url[future]  # assiging the future_to_url[future] varaibles value to the url varible
            result = newspaper.build(url, memoize_articles=False)  # The results are built.
            print('\n''The headlines from %s are' % url, '\n')  # The headlines are printed
            for i in range(1, 6):  # looping from 1 to 5
                art = result.articles[i]  # The article results are assighned to the art varible
                art.download()  # downloading the results
                art.parse()  # parsing the results
                print(art.title)  # priniting the title


if __name__ == '__main__':
    import timeit

    # the elapsed time for concurrent urls
    elapsed_time = timeit.timeit("concurrent_URLs_example()", setup="from __main__ import concurrent_URLs_example",number=2) / 2
    # the elapsed time for non concurrent urls
    # elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=2)/2
    print(elapsed_time)  # printing the elapsed time
