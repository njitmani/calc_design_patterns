from app.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                print("Error: Need at least two numbers to perform division.")
                return
            result = numbers[0]
            for denominator in numbers[1:]:
                if denominator == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result /= denominator
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return DivideCommand()
