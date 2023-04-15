import os


if __name__ == '__main__':
    print("welcome to RoboSpeaker 1.0.0.1, created by A.I.Adil")
    while True:
        enteredText = input("Enter what you want me to speak (or press Enter to exit): ")
        if enteredText == '':
            os.system("espeak 'Bye Bye friend'")
            break
        command = f"espeak '{enteredText}'"
        os.system(command)




