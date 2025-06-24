# Step 1: Import Libraries
import cv2
import matplotlib.pyplot as plt

# Step 2: ASCII Conversion
d = {chr(i): i for i in range(255)}  # char to ASCII
c = {i: chr(i) for i in range(255)}  # ASCII to char

# Step 3: Load the image
image_path = r"C:\Users\LENOVO\Documents\Cyber security\fruite.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Image not found. Check the path.")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show original image
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Step 4: Secret message and key
text = "Hello"
key = "abc"

# Step 5: Convert to ASCII with error handling
try:
    text_ascii = [d[ch] for ch in text]
    key_ascii = [d[ch] for ch in key]
except KeyError as e:
    print(f"Unsupported character: {e}")
    exit()

# Step 6: Check image capacity
max_capacity = img.shape[0] * img.shape[1] * 3
if len(text_ascii) > max_capacity:
    print("Message too long for the image. Use a larger image.")
    exit()

# Step 7: Encrypt message into image
img_enc = img.copy()
n = m = z = kl = 0

for i in range(len(text_ascii)):
    orig_val = img_enc[n, m, z]
    new_val = text_ascii[i] ^ key_ascii[kl]
    img_enc[n, m, z] = new_val

    print(f"Embedding: [{text[i]}] (ASCII {text_ascii[i]}) XOR [{key[kl]}] (ASCII {key_ascii[kl]}) = {new_val} at pixel ({n},{m})")

    m += 1
    if m == img.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3
    kl = (kl + 1) % len(key_ascii)

# Step 8: Save and display encrypted image
cv2.imwrite("encrypted_output.png", cv2.cvtColor(img_enc, cv2.COLOR_RGB2BGR))
print("\nEncrypted secret message hidden in 'encrypted_output.png'")

plt.imshow(img_enc)
plt.title("Encrypted Image with Hidden Message")
plt.axis('off')
plt.show()

# Step 9: Decrypt message from image
n = m = z = kl = 0
decrypted_ascii = []
img_restored = img_enc.copy()

for i in range(len(text_ascii)):
    val = img_enc[n, m, z]
    orig_val = val ^ key_ascii[kl]
    decrypted_ascii.append(orig_val)

    # Restore the encrypted pixel value to original char value
    img_restored[n, m, z] = orig_val

    m += 1
    if m == img.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3
    kl = (kl + 1) % len(key_ascii)

decrypted_message = ''.join([c[i] for i in decrypted_ascii])
print(f"Decrypted hidden text: {decrypted_message}")

# Step 10: Show decrypted/restored image
plt.imshow(img_restored)
plt.title("Decrypted (Restored) Image")
plt.axis('off')
plt.show()

# Optional: Save restored image
cv2.imwrite("restored_output.png", cv2.cvtColor(img_restored, cv2.COLOR_RGB2BGR))
