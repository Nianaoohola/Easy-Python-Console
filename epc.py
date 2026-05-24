import cmd
import os

class epc(cmd.Cmd):
    prompt = 'epc@user> '
    intro = 'Welcome to Easy Python Console. Use "help" to see the list of commands.'

    def do_open(self, line):
        solicited_app = line.strip()

        if solicited_app:
            try:
                os.startfile(solicited_app)
            except FileNotFoundError:
                print(f"Error: The file or program was not found. '{solicited_app}'")
        else:
            print("Please specify what you want to open. Example: open notepad.exe")

    def do_help(self, line):
        print("Commands:")
        print("open <program>")
        print("clear")
        print("ascii")
        print("print <text>")
        print("calc <expression>")
        print("exit")

    def do_print(self, line):
        text = line.strip()
        print(text)

    def do_clear(self, line):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.intro)

    def do_ascii(self, line):
        print(r"""
  ______ _____   _____  
 |  ____|  __ \ / ____| 
 | |__  | |__) | |      
 |  __| |  ___/| |      
 | |____| |    | |____  
 |______|_|     \_____| 
""")

    def do_calc(self, line):
        expression = line.strip()

        if not expression:
            print("Please enter a mathematical expression. Example: calc 2 + 2")
            return

        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in expression):
            print("Error: Invalid expression. Only numbers and operators (+, -, *, /, .) are allowed.")
            return

        try:
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception:
            print("Error: Malformed mathematical expression.")

    def do_exit(self, line):
        print("leaving...")
        return True

if __name__ == '__main__':
    epc().cmdloop()