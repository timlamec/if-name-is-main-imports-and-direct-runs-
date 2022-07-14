
def say_hello(person):
    print(f'hello {person.title()}, how are you'.title() + '?')

def square(x):
    output = x*x
    return(output)

if __name__ == "__main__":
    print('python program')
    say_hello('tim')
    mysquare = square(40)
    print(f'my square is {mysquare}')
else:
    print("script ran when imported")

