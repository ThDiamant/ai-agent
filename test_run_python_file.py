from functions.run_python_file import run_python_file

def test():

    print("Running test for 'main.py':")
    print(run_python_file("calculator", "main.py"))
    print("")

    print("Running test for 'main.py' w/ 3+5:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("")

    print("Running test for 'tests.py':")
    print(run_python_file("calculator", "tests.py"))
    print("")

    print("Running test for '../main.py':")
    print(run_python_file("calculator", "../main.py"))
    print("")

    print("Running test for 'nonexistent.py':")
    print(run_python_file("calculator", "nonexistent.py"))
    print("")

    print("Running test for 'lorem.txt':")
    print(run_python_file("calculator", "lorem.txt"))
    print("")

if __name__ == "__main__":
    test()