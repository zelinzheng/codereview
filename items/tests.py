import time
import requests
import random
from .agent_list import user_agent_list

from .proxy_scraper import get_proxies
from itertools import cycle
# import json


proxies = get_proxies()
proxy_pool = cycle(proxies)


# Create your tests here.

def testParse(q_word=None):
    print("sqaure items ")
    item_list = []

    start_time = time.time()


    headers = {
            'User-Agent': random.choice(user_agent_list)
        }

    print(proxies)


    for page in range(1, 3):

        pre_url = 'https://www.amazon.com/s?url=search-alias%3Daps'
        keyword_url = '&field-keywords=%s' % q_word
        url = pre_url + keyword_url + '&page={0}'.format(page)

        proxy = next(proxy_pool)
        print("Request #%d" % page)

        r = requests.get(url, headers=headers,
                              proxies={"http": proxy,
                                       "https": proxy },
                              timeout=5)

        print("status_code: " + str(r.status_code))






