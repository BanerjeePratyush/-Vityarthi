Secure Password Generator

  💡 Project Goal:
  This project Is a simple command line interface (CLI) application built using python to generate strong, randomised passwords. It demonstrates foundational programming concepts like object oriented programming and robust input validation.

  ⚙️ Features:
1) The OOP class design: Uses the PasswordGenerator class to manage all creation logic separating it from user interaction.
2) Guaranteed Strength: Every password generated includes a mix of uppercase letters, lowercase letters, digits and symbols.
3) Custom Length: The user defines desired password length ranging between 8 and 50 characters.
4) Error Handling: Catches non numeric input and ensures the length is within the required limits.

  🛠️ Prerequisites:
  You only need python 3 installed on your system.

  🚀 How To Run:
1) Save the code as a python file (password_generator.py) in your system.
2) Open your terminal or command prompt.
3) Run the file: 
python password_generator.py
4) Follow the promt to enter the desired password length.

 🧠 Code Logic Breakdown:
1) PasswordGenerator class
 👉__init__(self, length=12): Stores the desired length and defines the character sets (leters digits and symbols).
 👉generate(): Builds a password by first adding one of each required character type, then filling the remainder with random characters and finally using random.shuffle() to ensure maximum unpredictability.
2) get_valid_length() Function:
 👉It uses a while true loop to repeatedly ask for input until a valid number is provided.
 👉The try...except ValueError Block is essential for catching input that cannot be converted to an integer.

 Code Logic Developed by: Pratyush Banerjee