import os, sys, time, random

""" ORDER version0.01 """


def rnd() -> float:
    """Generate random number between 0 and 1"""
    return random.random()


def dly(secs=None) -> None:
    """Make interrupt"""
    if secs:
        time.sleep(secs)
    else:
        time.sleep(rnd() / 3.14159264)


def echo(value: str) -> None:
    """Print, Type, Echo, Write, this function has many names"""
    for line in str(value).split('\n'):
        chars = ''
        for char in line:
            chars += char
            print(char, end='')
            if char != ' ':
                dly()
        print()


def safe_key(status=True):
    """SafeKey for more security"""
    if status:
        reg = ['secure', 'love', 'sex', '69']
        if input('Enter SafeKey: ') in reg:
            echo('> Initiation...')
        else:
            echo('> Access Denied.')
            sys.exit()
    else:
        echo('SafeKey is Disable.')


def text_to_ord(value, *args, **kwargs):
    o = [str(ord(_chr)).zfill(3) for _chr in str(value)]  # length=3
    return o  # input: str | output: list


def ord_to_text(value, *args, **kwargs):
    t = [chr(int(_ord)) for _ord in value if len(_ord) == 3]  # length=3
    return ''.join(t)  # input: list | output: str


def ord_implode(value, *args, **kwargs):
    # i = '|'.join(value)  # Simple Encryption
    i = ''.join(value)
    return i  # input:list | output: str


def ord_explode(value, *args, **kwargs):
    # e = str(value).split('|')  # Simple Decryption
    v = list(value)
    e = []
    while len(v) >= 3:  # length=3
        e.append(''.join(eat(v)))
    if bool(v):
        e.append(''.join(v))
    e.reverse()
    return e  # input:str | output: list


def eat(value: list, *args, **kwargs):
    # e = [value.pop() for _ in range(3) if len(value) >= 2]
    if len(value) >= 3:  # length=3
        e = [value.pop() for _ in range(3)]  # length=3
        e.reverse()
        return e


def ord_encrypt(value):
    # input/output : str
    pass


def ord_decrypt(value):
    # input/output : str
    pass
