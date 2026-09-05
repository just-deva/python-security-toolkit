import sys
import subprocess
def main_menu():
    while True:
        print("\n" + "="*40)
        print(" DEVA'S CYBERSECURITY TOOLKIT DASHBOARD")
        print("="*40)
        print("1. Password Strength Evaluator")
        print("2. Secure Password Generator")
        print("3. Exit Toolkit")
        print("="*40)
        choice = input("Select a tool (1-3): ")
        
        if choice == '1':
            print("\nLaunching Evaluator...\n")
            subprocess.run([sys.executable, "password_evaluator.py"])
        elif choice == '2':
            print("\nLaunching Generator...\n")
            subprocess.run([sys.executable, "password_generator.py"])
        elif choice == '3':
            print("\nExiting toolkit. Stay safe out there!")
            break
        else:
            print("\nInvalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main_menu()
