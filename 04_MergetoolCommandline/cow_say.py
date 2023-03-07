import shlex
import cowsay
import cmd

class cow_say(cmd.Cmd):    
    def do_list_cows(self, arg):
        """Lists all cow file names in the given directory"""
        pass
        
    def do_make_bubble(self, args):
        """
        Wraps text is wrap_text is true, then pads text and sets inside a bubble.
        This is the text that appears above the cows
        """
        pass
        
    def do_cowsay(self, args):
        """
        Similar to the cowsay command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay
        string
        :param message: The message to be displayed
        :param cow: -f – the available cows can be found by calling list_cows
        :param eyes: -e or eye_string
        :param tongue: -T or tongue_string
        """
        pass
        
    def do_cowthink(self, args):
        """
        Similar to the cowthink command. Parameters are listed with their
        corresponding options in the cowthink command. Returns the resulting
        cowthink string
        :param message: The message to be displayed
        :param cow: -f – the available cows can be found by calling list_cows
        :param eyes: -e or eye_string
        :param tongue: -T or tongue_string
    """
        pass
        
    def complete_list_cows(self, prefix, line, start, end):
        pass
        
    def complete_make_bubble(self, prefix, line, start, end):
        pass
        
    def complete_cowsay(self, prefix, line, start, end):
        pass
        
    def complete_cowthink(self, prefix, line, start, end):
        pass
        
    def do_quit(self, arg):
        """Quit programm"""
        
    def do_EOF(elf, arg):
        return 1
        
    
cow_say().cmdloop()
