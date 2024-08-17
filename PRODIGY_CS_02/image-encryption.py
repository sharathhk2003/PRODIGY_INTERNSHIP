from PIL import Image
import numpy as np

print("Welcome to the Image Encryption Program.")

logo = r'''
 ___                                                                   _   _ 
|_ _|_ __ ___   __ _  __ _  ___        ___ _ __   ___ _ __ _   _ _ __ | |_(_)
 | || '_ ` _ \ / _` |/ _` |/ _ \_____ / _ \ '_ \ / __| '__| | | | '_ \| __| |
 | || | | | | | (_| | (_| |  __/_____|  __/ | | | (__| |  | |_| | |_) | |_| |
|___|_|_|_| |_|\__,_|\__, |\___|      \___|_| |_|\___|_|   \__, | .__/ \__|_|
 / _ \| '_ \         |___/                                 |___/|_|          
| (_) | | | |                                                                
 \___/|_| |_|                                                                
'''

print(logo)  # Print the logo

def encrypt_image(image_path, key):
    # Open the image
    original_image = Image.open(image_path)

    # Convert the image to a numpy array
    image_array = np.array(original_image)

    # Perform a simple row swap (you can also swap columns or individual pixels)
    image_array = image_array[::-1]  # Reverse the rows as a basic swap

    # Encrypt the image using a mathematical operation
    encrypted_image_array = (image_array * key) // (key + 1)

    # Convert the numpy array back to an image
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    # Save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"Encryption successful. The encrypted image has been saved as: {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)

    # Convert the encrypted image to a numpy array
    encrypted_image_array = np.array(encrypted_image)

    # Decrypt the image using the inverse of the encryption operation
    decrypted_image_array = (encrypted_image_array * (key + 1)) // key

    # Reverse the row swap to get the original order
    decrypted_image_array = decrypted_image_array[::-1]  # Reverse rows back to original

    # Clip the values to be in the valid range [0, 255]
    decrypted_image_array = np.clip(decrypted_image_array, 0, 255)

    # Convert the numpy array back to an image
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    # Save the decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Decryption successful. The decrypted image has been saved as: {decrypted_image_path}")

def main():
    while True:
        print("\nPlease select an option:")
        print("Type 'e' for image encryption, 'd' for image decryption, or 'q' to quit.")
        choice = input("Your choice: ").lower().strip()

        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print("Exiting the program. Thank you for using the Image Encryption Program.")
            break
        else:
            print("Invalid choice. Please enter 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def encrypt_choice():
    key = int(input("Please enter the encryption key (positive integer): "))
    image_location = input("Please enter the location or path of the image: ")

    try:
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Error: The specified image file could not be found. Please verify the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def decrypt_choice():
    key = int(input("Please enter the decryption key (positive integer): "))
    encrypted_image_location = input("Please enter the location or path of the encrypted image: ")

    try:
        decrypt_image(encrypted_image_location, key)
    except FileNotFoundError:
        print("Error: The specified encrypted image file could not be found. Please verify the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
