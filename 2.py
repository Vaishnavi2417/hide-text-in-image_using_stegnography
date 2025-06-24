# Steganography Example: Hiding Encrypted Text in an Image (Cybersecurity Use Case)
# Requirements: pip install stegano pillow cryptography

from stegano import lsb
from PIL import Image
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a Fernet symmetric encryption key.
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Encrypts the message using the provided Fernet key.
    Returns the encrypted message as a latin1 string (safe for LSB).
    """
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode('latin1')

def decrypt_message(token, key):
    """
    Decrypts the encrypted message using the provided Fernet key.
    Token should be a latin1 string.
    Returns the original text message.
    """
    f = Fernet(key)
    decrypted = f.decrypt(token.encode('latin1'))
    return decrypted.decode()

def hide_text_in_image(input_image_path, output_image_path, secret_text, key):
    """
    Encrypts and hides the given secret_text inside the input_image_path and saves as output_image_path.
    """
    # Encrypt the secret text
    encrypted_message = encrypt_message(secret_text, key)
    # Hide the encrypted text in the image and save the result
    secret_img = lsb.hide(input_image_path, encrypted_message)
    secret_img.save(output_image_path)
    print(f"Encrypted secret message hidden in {output_image_path}.")

def reveal_text_from_image(stego_image_path, key):
    """
    Extracts and prints the hidden text from the stego_image_path, then decrypts it.
    """
    # Extract the encrypted text from the image
    hidden_encrypted = lsb.reveal(stego_image_path)
    if hidden_encrypted is None:
        print("No hidden message found.")
        return
    try:
        decrypted = decrypt_message(hidden_encrypted, key)
        print(f"Decrypted hidden text: {decrypted}")
    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    # Paths to images (Make sure 'input.png' exists in your directory)
    input_image = "input.png"              # Use a PNG image for best results
    stego_image = "output_with_secret.png"
    secret_message = "This is a secret message hidden using steganography!"

    # Encryption key (generate and save this securely!)
    key = generate_key()
    print(f"Encryption key (save this to reveal the message later!):\n{key.decode()}\n")

    # Hide the encrypted message
    hide_text_in_image(input_image, stego_image, secret_message, key)

    # Reveal and decrypt the message
    reveal_text_from_image(stego_image, key)