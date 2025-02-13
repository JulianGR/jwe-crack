# JWECrack

JWECrack is a tool for decrypting JSON Web Encryption (JWE) tokens using either a **dictionary attack** or **brute-force attack**.

## Features
- **Dictionary Attack**: Uses a list of passwords from a file.
- **Brute-force Attack**: Generates passwords of a specified length range.
- **Customizable Parameters**: Set token, attack mode, and length constraints.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python jwecrack.py -t <JWE_TOKEN> <MODE> [OPTIONS]
```

### Dictionary Attack
Uses a predefined list of passwords from a file.
```bash
python jwecrack.py -t "eyJ0eXAiOiJKV1QiLCJ..." dict path/to/dictionary.txt
```

### Brute-force Attack
Generates and tests passwords within a given length range.
```bash
python jwecrack.py -t "eyJ0eXAiOiJKV1QiLCJ..." brute --min-length 3 --max-length 6
```

## Requirements
- Python 3.x
- `jwcrypto`

Install dependencies with:
```bash
pip install -r requirements.txt
```

## License
MIT License

