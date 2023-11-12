from src.hello import func, func12, new_func

def print_hi():
    print(f'hello,today num is" {new_func()}\n {ask()}')  # Press Ctrl+F8 to toggle the breakpoint.


def ask():
    print(f'{func()} {func12()}')
    return input('ваше имя: ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# some text///////////////////
