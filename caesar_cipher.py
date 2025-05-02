# ✅ Caesar Cipher Encryption & Decryption Program
def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result

# ✅ User Interface
if __name__ == "__main__":
    print("🔐 Welcome to Caesar Cipher Program 🔐")
    
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode not in ["encrypt", "decrypt"]:
            print("❌ Invalid mode! Please enter 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (0-25): "))
            if shift < 0 or shift > 25:
                raise ValueError
        except ValueError:
            print("❌ Invalid shift value! Please enter a number between 0 and 25.")
            continue
        
        result = caesar_cipher(text, shift, mode)
        print(f"✅ {mode.capitalize()}ed Text: {result}")
        
        again = input("Do you want to run again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Exiting Program. Goodbye!")
            break
