from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                print("Error: Need at least two numbers to perform subtraction.")
                return
            result = numbers[0] - sum(numbers[1:])
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return SubtractCommand()
