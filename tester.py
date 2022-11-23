import sys

from testcode import testcode
#from testoutputs import testoutputs
from interpreterv2 import Interpreter

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    num_passed = 0

# going thru testcode.py file for the input
    start = 0
    end = len(testcode)
    # end = 1
    for i in range(start, end):
        program_code = testcode[i].splitlines()

        # run that shit
        test1 = Interpreter(console_output=False)
        test1.run(program_code)
        actual = "\n".join(test1.get_output())
        print(actual)

        print()
        print()
        test1.print_vars()
        

        """
        try:
            test1.run(program_code)
            actual = "\n".join(test1.get_output())
            print(actual)
        except Exception as e:
            err = f'{test1.error_type} {test1.error_line}'
            actual = "\n".join(test1.get_output()) + \
                f'\n{err}' if len(test1.get_output()) > 0 else err
            print(actual)
            print(e)
            """
