import mimetypes

mt = mimetypes.guess_type("./shell.php")
print(mt)
