#!/usr/bin/python3
"""Define all attribute and methods for console"""
import cmd
import json
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def help_help(self):
        """Help command"""
        print("Help command for more information on existing commands\n")

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create command to create new instance and save
        """
        if line == "":
            print("** class name missing **")
        elif line in classes:
            new_model = classes[line]()
            new_model.save()
            print(new_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show command to print string representation of instance
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[args[0] + "." + args[1]])

    def do_destroy(self, line):
        """Destroy command to delete instance
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()

    def do_all(self, line):
        """All command to print all string representation or specified class
        """
        if line == "":
            for v in storage.all().values():
                print([str(v)])
        elif line in classes:
            for k, v in storage.all().items():
                key = k.split(".")
                if key[0] == line:
                    print([str(v)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update command to update instance attribute and saves
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            args = args[0:4]
            k = args[0] + "." + args[1]
            instance = storage.all()[k]
            args[3] = eval(args[3])
            setattr(instance, args[2], args[3])
            instance.save()

    def default(self, line):
        """Method to handle cases in which command usage is different format
        """
        args = line.split(".")
        line = args[0]
        if line in classes:
            if args[1] == "all()":
                all = getattr(self, 'do_all')
                all(line)
            elif args[1] == "count()":
                count = 0
                for k in storage.all().keys():
                    key = k.split(".")
                    if key[0] == line:
                        count += 1
                print(count)
            elif args[1].startswith('show("') and args[1].endswith('")'):
                id = args[1][6:-2]
                line = line + " " + id
                show = getattr(self, 'do_show')
                show(line)
            elif args[1].startswith('destroy("') and args[1].endswith('")'):
                id = args[1][9:-2]
                line = line + " " + id
                destroy = getattr(self, 'do_destroy')
                destroy(line)
            elif args[1].startswith('update(') and args[1].endswith(')'):
                args[1] = args[1][7:-1]
                b_d = args[1].find("{")
                e_d = args[1].find("}")
                update = getattr(self, 'do_update')
                try:
                    d_form = json.loads(args[1][b_d:e_d + 1].replace("'", '"'))
                except Exception as e:
                    args = args[1].split(", ")
                    for i in range(min(len(args), 2)):
                        args[i] = eval(args[i])
                    line += " " + " ".join(args)
                    update(line)
                else:
                    id = args[1].split(", ")[0][1:-1]
                    for k, v in d_form.items():
                        if type(v) == str:
                            cmd = line + " " + id + " " + k + ' "' + v + '"'
                        else:
                            cmd = line + " " + id + " " + k + ' ' + str(v)
                        update(cmd)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
