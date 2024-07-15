import string
import sys

"""
Encrypts a string using Caesar Cipher.

Author: NightFox
Version: 1.2
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
    if value > 52:
        return value % 52
    else:
        return value


def shift(key: int):
    k = overflow(key)
    letters = list(string.ascii_lowercase + string.ascii_uppercase)

    start = (-1 * k)
    end = 52 - k

    _a = letters[:end]
    _b = letters[start:]

    if k == 0:
        return _a
    else:
        return _b + _a


def str_to_str(value: str, key: int):
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    _shift = shift(key)
    _list = [_shift[letters.index(i)] if i in letters else i for i in value]  # ignore un-ascii character
    return ''.join(_list)


def str_shift(value: str, key: int):
    k = overflow(key)
    return str_to_str(value, k)  # Shift 5: hello -> czggj


def str_unshift(value: str, key: int):
    k = 52 - overflow(key)
    return str_to_str(value, k)  # Unshift 5: czggj -> hello


# ORD
def str_to_ord(value, **kwargs):
    # list of ord 's
    o = [str(ord(_chr)).zfill(3) for _chr in str(value)]  # 'h' : '104' | length=3
    return ''.join(o) + '0'  # input: str > output: str


# CHR
def int_to_chr(value, **kwargs):
    # list of chr 's
    c = [chr(int(_ord)) for _ord in [value[i:i + 3] for i in range(0, len(value) - 2, 3)]]  # '104' : 'h' | length=3
    return ''.join(c)  # input: str > output: str
