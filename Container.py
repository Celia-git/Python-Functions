class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals.keys():
            del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in self.vals.keys()

class Demo():
    def __init__(self):
        self.run_demo(ASet())
    
    def run_demo(self, set):
        print("New Set\n")
        while True:
            print("Set Elements: \n%s" % (set.__str__()))
            command = input("Enter a command: \n\t i \tinsert an element\n\t c \tcheck if element is in set\n\t r \tremove entry from set\n\t q \tquit demo\n")
            if command=="q": return
            
            element = input("Enter an element of any data type\n")
                            
            match command:
                case "i":
                    set.insert(element)
                case "c":
                    print("It is %s that is %s in the set.\n" % (str(set.is_in(element)), element))
                case "r":
                    set.remove(element)
                case _:
                    return
            print("")

Demo()

