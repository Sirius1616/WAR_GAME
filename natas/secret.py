import base64
import binascii

encodedSecret = "3d3d516343746d4d6d6c315669563362"

def decode_secret(encoded: str) -> str:
    # 1. bin2hex inverse → hex to raw string
    reversed_b64 = binascii.unhexlify(encoded).decode()
    
    # 2. reverse string (strrev inverse)
    b64 = reversed_b64[::-1]
    
    # 3. base64 decode
    original = base64.b64decode(b64).decode()
    
    return original

print(decode_secret(encodedSecret))