import os
import re
import display_messages as dm
import morse_code

MORSE_CODE = morse_code.morse_code
WORD_SPACE = morse_code.word_space
LETTER_SPACE = morse_code.letter_space


def clear_screen():
    """
    clears the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def encoder(msg: str) -> str:
    """
    Takes the message and encodes it, and then returns the encoded message.
    """
    encoded_msg = ""
    for char in msg:
        char = char.lower()
        if char == ' ':
            encoded_msg += WORD_SPACE
        else:
            encoded_msg += MORSE_CODE[char] + LETTER_SPACE

    return encoded_msg


def decoder(msg: str) -> str:
    """
    Takes the encoded message and decodes it and then returns the decoded message.
    """
    global MORSE_CODE
    if re.search('[a-zA-Z]', msg) is None:
        decoded_msg = ""
        for word in msg.split("   "):
            for letter in word.split(" "):
                for key, value in MORSE_CODE.items():
                    if value == letter:
                        decoded_msg += key
                        break
            decoded_msg += " "

        return decoded_msg
    else:
        clear_screen()
        print("\nYour Message was not properly encoded.\nPlease retry with correct message\n")
        print(dm.hr)
        main(de=True)


def to_exit() -> None:
    """
    Renders the Exit menu.
    """
    cho = input(dm.exit_msg)
    clear_screen()
    if cho.lower() == 'y':
        print("\n\n    Thank you for using my app..!")
        input("\n\n  > Press ENTER to close the window.")
        return
    elif cho.lower() == 'n':
        main()
    else:
        print("Invalid choice! Please chose again.")
        to_exit()


def choice_2() -> None:
    """
    Renders the 2nd choice menu
    """
    cho = input(f"      > Proceed to main menu? (y/n): ")
    clear_screen()
    if cho.lower() == 'y':
        main()
    elif cho.lower() == 'n':
        to_exit()
    else:
        print("Invalid Choice ! \nPlease Choose again.")
        print(dm.hr)
        choice_2()


def main(de: bool = False) -> None:
    """
    Renders the Main menu.
    """
    if de:
        choice = '2'
    else:
        choice = input(dm.main_menu_msg)
        clear_screen()
    # Encoding
    if choice == '1' or choice.lower() == 'encode':
        message = input(f"{dm.encoder}      > Enter Your Message : \n            ")
        result = encoder(message)
        print(f"        Your coded message is :\n            {result}")
        choice_2()

    # Decoding
    elif choice == '2' or choice.lower() == 'decode':
        message = input(f"{dm.decoder}      > Enter Your Message : \n            ")
        result = decoder(message)
        if result is not None:
            print(f"        Your decoded message is :\n            {result}")
        choice_2()

    # Exit
    elif choice == '3' or choice.lower() == 'exit':
        to_exit()

    # Invalid Input
    else:
        print("Invalid Choice ! \nPlease Choose again.")
        print(dm.hr)
        main()


if __name__ == '__main__':
    main()
