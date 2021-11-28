import concurrent.futures
import time
from urllib.request import Request, urlopen


def check_link(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        response = urlopen(request, timeout=5)
        code = response.code
        print(code)
        response.close()
    except Exception as e:
        print("Exception occurred. URL: ", url, "Exception:", e)


links = open('res.txt', encoding='utf8').read().split('\n')
workers_amount = 100
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=workers_amount) as executor:
    future_to_url = {executor.submit(check_link, url): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
end = time.time()
print(end - start)
