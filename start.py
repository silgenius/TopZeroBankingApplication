import cmd
from models.user import User


class TopZeroBank(cmd.Cmd):
    intro = "Task Shell. Type help or ? to list commands.\n"
    prompt = "TopZeroBank> "
    
    def precmd(self, line):
        try:
            val = int(line)
            commands = {
            1: "create_account",
            }
            line = commands[val]
            
        except Exception:
            pass
        return line
    
    def do_create_account(self, line):
        """Create New User Account
        - Can input "1" or "create_account" for the interactive create account prompt
        - or use the command "create_account account_name account_pin" to create one.
        """
        print("Join Billions of users using TopZero Bank WorldWide!")
        acc_name = input(f"\tProvide Account Name > ")
        acc_pin = input(f"\tProvide Account Pin  > ")
        user = User(account_name=acc_name, account_pin=acc_pin)
        user.save()
        print(f"Account Created Successfully with account number {user.account_number}")
        return
    
    def view_account_detail(self, line):
        """View User Accfount Details"""
        storage.find_user_account()
        
    def emptyline(self):
        """ This line doesn’t execute anything"""
        pass
    
    def do_view_account_details(self, line):
        print(line)
        """View User Account Details"""
        User.find_account(account_name="testing", account_number="testing")
        
    def do_transfer(self):
        """Make Transfer to a friend"""
    
    def default(self, line):
        print(f'{line} not recognized, enter "help" to see list of recognozed commands') 
        
    def do_quit(self, line): 
        """Exiting The Shell
        """
        return True
    

if __name__ == "__main__":
    TopZeroBank().cmdloop()