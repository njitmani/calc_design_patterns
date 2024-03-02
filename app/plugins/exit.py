from app.commands import Command, ExitApplication
import sys

class ExitCommand(Command):
    def execute(self, *args):
        print("Exiting...")
        raise ExitApplication

def get_command_instance(command_handler=None):
    return ExitCommand()
