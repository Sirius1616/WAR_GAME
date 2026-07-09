import base64
import json


COOKIE = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY="

# This is the known plaintext from the PHP source
KNOWN_PLAINTEXT = b'{"showpassword":"no","bgcolor":"#ffffff"}'


def xor_bytes(data: bytes, key: bytes) -> bytes:
    """Encrypt/decrypt with a repeating XOR key."""
    return bytes(
        data[i] ^ key[i % len(key)]
        for i in range(len(data))
    )


def smallest_repeating_pattern(data: bytes) -> bytes:
    """
    Find the shortest prefix that reproduces the byte string
    when repeated.
    """
    for length in range(1, len(data) + 1):
        candidate = data[:length]

        if all(
            data[i] == candidate[i % length]
            for i in range(len(data))
        ):
            return candidate

    return data


# ---------------------------------------------------------
# Step 1: Decode the cookie
# ---------------------------------------------------------

ciphertext = base64.b64decode(COOKIE)

# ---------------------------------------------------------
# Step 2: Recover key stream
# ---------------------------------------------------------

keystream = bytes(
    c ^ p
    for c, p in zip(ciphertext, KNOWN_PLAINTEXT)
)

print("Recovered keystream:")
print(keystream)

# ---------------------------------------------------------
# Step 3: Recover repeating key
# ---------------------------------------------------------

key = smallest_repeating_pattern(keystream)

print("\nRecovered key:")
print(key)

# ---------------------------------------------------------
# Step 4: Decrypt cookie
# ---------------------------------------------------------

plaintext = xor_bytes(ciphertext, key)

print("\nDecrypted JSON:")
print(plaintext.decode())

# ---------------------------------------------------------
# Step 5: Modify JSON
# ---------------------------------------------------------

data = json.loads(plaintext)

data["showpassword"] = "yes"

new_plaintext = json.dumps(data, separators=(",", ":")).encode()

print("\nModified JSON:")
print(new_plaintext.decode())

# ---------------------------------------------------------
# Step 6: Encrypt modified JSON
# ---------------------------------------------------------

new_cipher = xor_bytes(new_plaintext, key)

new_cookie = base64.b64encode(new_cipher).decode()

print("\nNew cookie:")
print(new_cookie)