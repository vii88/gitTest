from src.hello import func,new_func
print("Here")
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi,today num is" {new_func()}\n {ask()}')  # Press Ctrl+F8 to toggle the breakpoint.
def ask():
    print("bye")
    return input('ваше имя: ')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

#some text///////////////////
