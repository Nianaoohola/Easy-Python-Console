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
        print("exit")

    def do_exit(self, line):
        print("leaving...")
        return True

if __name__ == '__main__':
    epc().cmdloop()