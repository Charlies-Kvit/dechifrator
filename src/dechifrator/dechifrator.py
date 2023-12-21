"""
UTF-8
This is a file with all classes of decoders and so on.
"""
from . import MORSE_CODES_DICT
from . import CAESAR_LETTERS_DICT


class MorseTranslator:
    """
    This is a class for encrypting and decrypting Morse code.
    """

    def __init__(self, language: str = "EN", separator: str = "/") -> None:
        """
        Here we set default values like: the language for which further actions will be performed.
        The language should be chosen between RU (Russian) or EN (English).
        Default language: English.
        Numbers are enabled by default.
        Language can be changed later in function change_language(language).
        """
        self.decipher_dict_letters: dict[str:str] = MORSE_CODES_DICT[language]["DECODE"]
        self.decipher_dict_symbols: dict[str:str] = MORSE_CODES_DICT["SYM"]["DECODE"]
        self.decipher_dict_numbers: dict[str:str] = MORSE_CODES_DICT["NUM"]["DECODE"]
        self.decipher: dict[str:str] = {
            **self.decipher_dict_symbols,
            **self.decipher_dict_numbers,
            **self.decipher_dict_letters
        }
        self.encrypt_dict_letters: dict[str:str] = MORSE_CODES_DICT[language]["ENCODE"]
        self.encrypt_dict_numbers: dict[str:str] = MORSE_CODES_DICT["NUM"]["ENCODE"]
        self.encrypt_dict_symbols: dict[str:str] = MORSE_CODES_DICT["SYM"]["ENCODE"]
        self.encrypt: dict[str:str] = {
            **self.encrypt_dict_symbols,
            **self.encrypt_dict_numbers,
            **self.encrypt_dict_letters
        }
        self.language: str = language
        self.separator: str = "/"
        self.change_separator(separator)

    def change_separator(self, separator) -> None:
        """
        This function change separator
        """
        del self.decipher[self.separator]
        self.decipher[separator] = " "
        self.encrypt[" "] = separator
        self.separator = separator

    def change_language(self, language: str, separator: str = "/") -> None:
        """
        This function changes the language options
        """
        self.decipher_dict_letters: dict[str:str] = MORSE_CODES_DICT[language]["DECODE"]
        self.decipher_dict_symbols: dict[str:str] = MORSE_CODES_DICT["SYM"]["DECODE"]
        self.decipher_dict_numbers: dict[str:str] = MORSE_CODES_DICT["NUM"]["DECODE"]
        self.decipher: dict[str:str] = {
            **self.decipher_dict_symbols,
            **self.decipher_dict_numbers,
            **self.decipher_dict_letters
        }
        self.encrypt_dict_letters: dict[str:str] = MORSE_CODES_DICT[language]["ENCODE"]
        self.encrypt_dict_numbers: dict[str:str] = MORSE_CODES_DICT["NUM"]["ENCODE"]
        self.encrypt_dict_symbols: dict[str:str] = MORSE_CODES_DICT["SYM"]["ENCODE"]
        self.encrypt: dict[str:str] = {
            **self.encrypt_dict_symbols,
            **self.encrypt_dict_numbers,
            **self.encrypt_dict_letters
        }
        self.language: str = language
        self.change_separator(separator)

    def decipher_morse(self, text: str) -> str:
        """This function decrypts the text that is fed into the function"""
        answer: list[str] = list()
        dec_symbol: str = ""
        has_dec: bool = False
        for symbol in text.split():
            try:
                if has_dec:
                    symbol = dec_symbol + symbol
                else:
                    dec_symbol = ""
                answer.append(self.decipher[symbol])
                has_dec = False
            except KeyError:
                has_dec = True
                dec_symbol = symbol
        return ''.join(answer)

    def encrypt_morse(self, text: str) -> str:
        """This function encrypts the text that is fed into the function"""
        answer: list[str] = list()
        for symbol in text:
            answer.append(self.encrypt[symbol.upper()])
        return ' '.join(answer)


class CaesarTranslator:
    """"""

    def __init__(self, language: str = "EN") -> None:
        self.letters: dict[str:str] = CAESAR_LETTERS_DICT[language]
