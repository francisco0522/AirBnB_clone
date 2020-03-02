#!/usr/bin/python3
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import shlex

"""console"""


class HBNBCommand(cmd.Cmd):
    """console"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        'exit'
        return True

    def do_quit(self, line):
        'exit whit command quit'
        return True

    def do_create(self, args):
        'Creates an instance of BaseModel'
        if args:
            if args in models.list_class:
                obj = eval(args)()
                print(obj.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def emptyline(self):
        'Empty line'
        pass

    def do_show(self, args):
        'show by id'
        arg = shlex.split(args)
        if len((arg)) == 0:
            print("** class name missing **")
            return False
        elif arg[0] in models.list_class:
            if len((arg)) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        'delete by id'
        arg = shlex.split(args)
        if len((arg)) == 0:
            print("** class name missing **")
            return False
        elif arg[0] in models.list_class:
            if len((arg)) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        'show all'
        ls = []
        arg = shlex.split(args)
        if len(arg) == 0:
            for i in models.storage.all().values():
                ls.append(str(i))
            print("[\"" + ", ".join(ls) + "\"]")
        elif arg[0] in models.list_class:
            for key in models.storage.all():
                if arg[0] in key:
                    ls.append(str(models.storage.all()[key]))
            print("[\"" + ", ".join(ls) + "\"]")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        'update the models'
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] in models.list_class:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    if len(arg) > 2:
                        if len(arg) > 3:
                            if type(arg[2]) is int:
                                try:
                                    arg[3] = int(arg[3])
                                except:
                                    arg[3] = 0
                            elif type(arg[2]) is float:
                                try:
                                    arg[3] = float(arg[3])
                                except:
                                    arg[3] = 0.0
                            setattr(models.storage.all()[key], arg[2], arg[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
