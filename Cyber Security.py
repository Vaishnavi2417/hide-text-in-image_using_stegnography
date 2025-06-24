# Step 1: Import Required Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 2: ASCII Conversion Dictionary
d = {chr(i): i for i in range(255)}  # character to ASCII
c = {i: chr(i) for i in range(255)}  # ASCII to character

# Step 3: Load Original Image
input_image_path = "fruite.jpg"  # Input image file
output_image_path = "output_with_secret.png"  # Encrypted image file

x = cv2.imread(input_image_path)
x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

# Show original image
plt.imshow(x)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Step 4: Message and Key
key = "123"
text = "This is a secret message hidden using steganography!"

# Step 5: Convert to ASCII
text_ascii = [d[ch] for ch in text]
key_ascii = [d[ch] for ch in key]

# Step 6: Encrypt Message into Image
x_enc = x.copy()
n, m, z = 0, 0, 0
kl = 0

for i in range(len(text_ascii)):
    new_val = text_ascii[i] ^ key_ascii[kl]
    x_enc[n, m, z] = new_val

    m += 1
    if m == x.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3
    kl = (kl + 1) % len(key_ascii)

# Step 7: Save Encrypted Image
cv2.imwrite(output_image_path, cv2.cvtColor(x_enc, cv2.COLOR_RGB2BGR))
print(f"\nEncrypted secret message hidden in {output_image_path}.")

# Step 7.1: Display Encrypted Image
plt.imshow(x_enc)
plt.title("Encrypted Image with Hidden Message")
plt.axis('off')
plt.show()

# Step 8: Decrypt Message from Image
x_dec = cv2.imread(output_image_path)
x_dec = cv2.cvtColor(x_dec, cv2.COLOR_BGR2RGB)

n, m, z = 0, 0, 0
kl = 0
decrypted_ascii = []
x_restored = x_dec.copy()

for i in range(len(text_ascii)):
    encrypted_val = x_dec[n, m, z]
    orig_val = encrypted_val ^ key_ascii[kl]
    decrypted_ascii.append(orig_val)
    x_restored[n, m, z] = orig_val

    m += 1
    if m == x_dec.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3
    kl = (kl + 1) % len(key_ascii)

# Step 9: Convert to Text
decrypted_text = ''.join([c[val] for val in decrypted_ascii])
print(f"Decrypted hidden text: {decrypted_text}")

# Step 10: Display Restored (Decrypted) Image
plt.imshow(x_restored)
plt.title("Decrypted (Restored) Image")
plt.axis('off')
plt.show()
