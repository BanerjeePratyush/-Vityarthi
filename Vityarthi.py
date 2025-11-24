import random
import string
class PasswordGenerator:
    def __init__(self, length=12):
        self.length=length
        self.letters=string.ascii_letters
        self.digits=string.digits
        self.symbols=string.punctuation
        self.all_characters=self.letters + self.digits + self.symbols
    def generate(self):

            password_list=[]
            password_list.append(random.choice(self.letters))
            password_list.append(random.choice(self.digits))
            password_list.append(random.choice(self.symbols))
            remaining_length=self.length-3
            for _ in range(remaining_length):
                password_list.append(random.choice(self.all_characters))


                random.shuffle(password_list)
            return "".join(password_list)
            
def get_valid_length():
    while True:
            try:
                 length_input=input("Enter the desired password length(Minimun=8, Maximum=50)")
                 length=int(length_input)
                 if 8 <=length <=50:
                          return length
                 else:
                         print("Length must be between 8 and 50.")
            except ValueError:
                     print("Invalid Input. Please Enter a Whole Number")
if __name__=="__main__":
             print("Secure Password Generator")
             desired_length= get_valid_length()
             generator=PasswordGenerator(length=desired_length)
             new_password=generator.generate()
             print("Generated Password:")
             print(new_password)


