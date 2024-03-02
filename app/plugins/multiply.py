from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        try:
            result = 1
            for arg in args:
                result *= float(arg)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return MultiplyCommand()
