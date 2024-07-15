import string
import sys


class CaesarCipher:
    """
    Encrypts a string using Caesar Cipher.

    Author: NightFox
    Version: 2.0
    TimeStamp: 1720999524.7264638
    """

    def __init__(self):
        # Standard Letters Dictionary
        self.letters = string.ascii_lowercase + string.ascii_uppercase  # 'a..z,A..Z' Length:52
        # Length of Standard Letters Dictionary
        self.length = len(self.letters)  # Length of standard dictionary

    @staticmethod
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

    @staticmethod
    def str_to_ord(value: str, **kwargs):
        """Converts a string to an ord() integer"""
        # list of ord 's
        o = [str(ord(_chr)).zfill(3) for _chr in str(value)]  # 'h' : '104' | length=3
        return ''.join(o) + '0'  # input: str > output: str

    @staticmethod
    def int_to_chr(value: str, **kwargs):
        """Converts an ord() integer to chr() string"""
        # list of chr 's
        c = [chr(int(_ord)) for _ord in [value[i:i + 3] for i in range(0, len(value) - 1, 3)]]  # '104' : 'h' | length=3
        return ''.join(c)  # input: str > output: str

    def overflow(self, key: int):
        if key > self.length:
            return key % self.length
        else:
            return key

    def shift(self, key: int):
        """Create Shifted/Cipher Dictionary"""
        k = self.overflow(key)
        letters = self.letters

        start = (-1 * k)
        end = self.length - k

        _a = letters[:end]
        _b = letters[start:]

        if k == 0:
            return _a
        else:
            return _b + _a

    def str_to_str(self, value: str, key: int):
        """Generates String from Caesar Cipher Dictionary"""
        letters = self.letters
        _shift = self.shift(key)
        _list = [_shift[letters.index(i)] if i in letters else i for i in value]  # ignore un-ascii character
        return ''.join(_list)

    def str_shift(self, value: str, key: int):
        """Caesar Cipher: the Shift compute"""
        k = self.overflow(key)
        return self.str_to_str(value, k)  # Shift 5: hello -> czggj

    def str_unshift(self, value: str, key: int):
        """Caesar Cipher: the Unshift compute"""
        k = self.length - self.overflow(key)
        return self.str_to_str(value, k)  # Unshift 5: czggj -> hello

    def caesar_encryption(self, value: str, key: int):
        """Caesar Cipher Standard Encryption Interface."""
        return self.str_shift(value=value, key=key)

    def caesar_decryption(self, value: str, key: int):
        """Caesar Cipher Standard Decryption Interface."""
        return self.str_unshift(value=value, key=key)

    def advance_encryption(self, value: str, key: int):
        """
        Advanced Cipher Encryption Interface
        Using Caesar Cipher and ord functionality.
        """
        _cea = self.caesar_encryption(value, key)
        _ord = self.str_to_ord(_cea)
        return _ord

    def advance_decryption(self, value: str, key: int):
        """
        Advanced Cipher Decryption Interface
        Using Caesar Cipher and ord functionality.
        """
        _chr = self.int_to_chr(value)
        _cea = self.caesar_decryption(_chr, key)
        return _cea
