import base64


def encode(password):
    encrypted = base64.b64encode(password)
    return encrypted


def decode(password):
    decrypted = base64.b64decode(password)
    return decrypted
