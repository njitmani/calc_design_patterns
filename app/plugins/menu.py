from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        print("Available commands:")
        for command_name in sorted(self.command_handler.commands):
            print(f"  {command_name}")

def get_command_instance(command_handler=None):
    return MenuCommand(command_handler)
