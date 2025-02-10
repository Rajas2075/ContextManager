from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()

if __name__ == '__main__':
    with genericFileFunction ('./file.txt', 'w') as f:
        f.write ('My name is')
    with genericFileFunction ('./file.txt', 'r') as f:
        print(f.read())
    with genericFileFunction ('./file.txt', 'a') as f:
         f.write (' Rajas ')
    with genericFileFunction ('./file.txt', 'r') as f:
        print(f.read())