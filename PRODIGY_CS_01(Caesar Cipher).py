# Function for Caesar Cipher encryption or decryption
def caesar_cipher(text, shift, mode='encrypt'):
    # Initialize an empty string to store the cipher message
    cipher_text = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Process each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the ASCII base ('A' or 'a')
            base_ascii = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar Cipher shift
            shifted_char = chr((ord(char) - base_ascii + shift) % 26 + base_ascii)
            cipher_text += shifted_char  # Append the transformed character
        else:
            cipher_text += char  # Append non-alphabetical characters unchanged

    return cipher_text

# Main function for user interaction
def main():
    print("Welcome to the Caesar Cipher Program!")
    print("Choose an option: ")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    
    # Prompt for user's choice
    choice = input("Enter your choice (1 or 2): ")

    # Validate the user's choice
    if choice not in ['1', '2']:
        print("Invalid choice. Please run the program again.")
        return

    # Prompt for message and shift value
    user_input = input("Enter your message: ")
    shift_value = int(input("Enter the shift value: "))
    
    # Encrypt or decrypt based on user's choice
    if choice == '1':
        encrypted_message = caesar_cipher(user_input, shift_value, mode='encrypt')
        print("Encrypted message: ",encrypted_message)
    elif choice == '2':
        decrypted_message = caesar_cipher(user_input, shift_value, mode='decrypt')
        print("Decrypted message:",decrypted_message)

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()