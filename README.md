# Dechifrator
This is a python library for encrypting and decrypting ciphers such as:
1. Morse
2. Caesar(in development)
3. The Vigener Cipher(in development)
## Installing
Installing with git:
```text
git clone https://github.com/Charlies-Kvit/dechifrator
```
## A Simple Examples
```python
from dechifrator import MorseTranslator

morse = MorseTranslator()
encrypt_morse = morse.encrypt_morse("Hello, world!!!")
print(encrypt_morse)
decipher_morse = morse.decipher_morse(encrypt_morse)
print(decipher_morse)
```
## Documentation
Read here: 
## Contributing

## License
[GNU General Public License v3.0](https://github.com/Charlies-Kvit/dechifrator/blob/main/LICENSE)
