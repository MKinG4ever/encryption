# Other version
class BasicOrder:
    """
        Basic text encryption anatomy for learning
        version 0.01
    """

    def __init__(self, value):
        """simple encryption script"""
        self.val = value

    def encrypt_data(self):
        """flow of encryption"""
        # data_to_ord -> ord_encrypt
        return self.ord_encrypt(self.data_to_ord(self.val))

    def decrypt_data(self):
        """flow of decryption"""
        # ord_decrypt -> ord_to_chr -> chr_to_data
        return self.chr_to_data(self.ord_to_chr(self.ord_decrypt(self.val)))

    @staticmethod
    def data_to_ord(data: str) -> list:  # 'Hello' -> [67, 108, 101, 101, 111]
        """Turn 'str' to 'ord', one by one in row"""
        return [ord(i) for i in data]

    @staticmethod
    def ord_to_chr(data: list) -> list:  # [67, 108, 101, 101, 111] -> ['H', 'e', 'l', 'l', 'o']
        """Convert list of 'ord's to list of 'str's, one by one in row"""
        return [chr(int(i)) for i in data]

    @staticmethod
    def chr_to_data(data: list) -> str:  # ['H', 'e', 'l', 'l', 'o'] -> 'Hello'
        """Merge(join) list of 'str's to one piece"""
        return ''.join(data)

    @staticmethod
    def ord_encrypt(data: list) -> str:  # [67, 108, 101, 101, 111] -> '67|108|101|101|111' / 06710810...
        """Simple encryption by making data hard-to-read with specific (reverse-able) order"""
        return '|'.join([str(i) for i in data])

    @staticmethod
    def ord_decrypt(data: str) -> list:  # '67|108|101|101|111' -> [67, 108, 101, 101, 111]
        """Simple decryption by reverse the encryption"""
        return data.split('|')

    def encryption_key(self):
        """Make hard-to-rad data, to un-readable data with key"""
        pass


class Idea(str):
    """
        Other version base of 'str'
        This is just an idea...
    """

    def __init__(self):
        super(Idea, self).__init__()
        pass
