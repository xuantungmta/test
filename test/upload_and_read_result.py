import urllib.request
url = "https://upload.koinbase.cyberjutsu-lab.tech/upload/7e35b846f74f13ae.php"
contents = urllib.request.urlopen(url).read()
if contents:
    print(str(contents).replace("\\n", "\n"))
