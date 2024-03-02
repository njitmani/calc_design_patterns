"""Plugin for adding numbers"""
from app.commands import Command

class AddCommand(Command):
    """Command to add numbers"""
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return AddCommand()
