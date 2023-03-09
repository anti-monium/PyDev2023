import shlex
import cowsay
import cmd

class cow_say(cmd.Cmd):    
    def do_list_cows(self, arg):
        """Lists all cow file names in the given directory"""
        l = sorted(cowsay.list_cows())
        print(*cowsay.list_cows())  
        
    @staticmethod    
    def make_cow(args, prm):
        args = shlex.split(args)
        try:
            msg = args[0]
        except:
            print("message is required parameter")
            return
        try:
            i = args.index('-f')
            cow = args[i + 1]
        except ValueError:
            cow = 'default'
        try:
            i = args.index('-e')
            eyes = args[i + 1]
        except ValueError:
            eyes = 'oo'
        try:
            i = args.index('-T')
            tongue = args[i + 1]
        except ValueError:
            tongue = '  '
        if prm == 'say':
            ans = cowsay.cowsay(msg, 
                cow=cow,
                eyes=eyes,
                tongue=tongue)
        else:
            ans = cowsay.cowthink(msg, 
                cow=cow,
                eyes=eyes,
                tongue=tongue)
        return ans
        
    def do_make_bubble(self, args):
        """
        Wraps text is wrap_text is true, then pads text and sets inside a bubble.
        This is the text that appears above the cows
        :param text: wrapped text
        :param opt: 'cowsay' or 'cowthink'
        """
        args = shlex.split(args)
        if args:
            msg = args[0]
        else:
            print("text is required parameter")
            return
        if len(args) > 1:
            opt = args[1]
        else:
            opt = 'cowsay'
        print(cowsay.make_bubble(msg,
                brackets=cowsay.THOUGHT_OPTIONS[opt]))
         
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
        print(self.make_cow(args, 'say'))
         
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
        print(self.make_cow(args, 'think'))
        
    def do_exit(self, args):
        """exit from cow_say"""
        return True
           
    def complete_list_cows(self, prefix, line, start, end):
        pass
         
    def complete_make_bubble(self, prefix, line, start, end):
        pass
        
    def complete_cowsay(self, prefix, line, start, end):
        pass
        
    def complete_cowthink(self, prefix, line, start, end):
        pass
        
    
cow_say().cmdloop()
