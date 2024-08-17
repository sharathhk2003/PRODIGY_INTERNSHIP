def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift_direction = shift if action == 'e' else -shift
            result += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Program.")  # Welcome message
    
    logo = '''
  ____                                 ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __      / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|____| |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | | |_____| |___| | |_) | | | |  __/ |_  
 \____\__,_|\___||___/\__,_|_|        \____|_| .__/|_| |_|\___|_(_) 
                                             |_|                    
    '''
    
    print(logo)  # Print the logo
    
    action = input("Please choose an option: 'e' for encryption or 'd' for decryption: ").lower().strip()
    while action not in ['e', 'd']:
        print("Error: Invalid selection. Kindly select 'e' for encryption or 'd' for decryption.")
        action = input("Please choose an option: 'e' for encryption or 'd' for decryption: ").lower().strip()

    message = input("Please enter the message to be processed: ")
    shift = int(input("Please enter the shift value (integer): "))

    result = caesar_cipher(message, shift, action)
    action_word = "Encrypted" if action == 'e' else "Decrypted"
    print(f"\n{action_word} Message: {result}")

if __name__ == "__main__":
    main()
