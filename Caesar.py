import string
import sys

"""
Encrypts a string using Caesar Cipher.

Author: NightFox
Version: 1.0
TimeStamp: 1720999524.7264638
"""


def safe_key(status=True):
    """SafeKey for more security"""
    if status:
        reg = ['secure', 'love', 'sex', '69']
        if input('Enter SafeKey: ') in reg:
            print('> Initiation...')
        else:
            print('> Access Denied.')
            sys.exit()
    else:
        print('SafeKey is Disable.')


def overflow(value: int):
    if value > 26:
        return value % 26
    else:
        return value


def shift(key: int):
    k = overflow(key)
    _let = list(string.ascii_lowercase)

    start = (-1 * k)
    end = 26 - k

    _a = _let[:end]
    _b = _let[start:]

    if k == 0:
        return _a
    else:
        return _b + _a


def str_to_str(value: str, key: int):
    _let = list(string.ascii_lowercase)
    _shift = shift(key)
    _list = [_shift[_let.index(i)] for i in value.lower()]
    return ''.join(_list)


def str_shift(value: str, key: int = 0):
    k = overflow(key)
    return str_to_str(value, k)


def str_unshift(value: str, key: int = 0):
    k = 26 - overflow(key)
    return str_to_str(value, k)


# ORD
def str_to_ord(value, **kwargs):
    o = [str(ord(_chr)).zfill(3) for _chr in str(value)]  # length=3
    return o  # input: str | output: list


# CHR
def int_to_chr(value, **kwargs):
    t = [chr(int(_ord)) for _ord in value if len(_ord) == 3]  # length=3
    return ''.join(t)  # input: list | output: str
