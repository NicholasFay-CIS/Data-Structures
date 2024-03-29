from sys import argv
from RBT import RedBlackTree

def main(argv):
    fileName = argv[1]
    T = RedBlackTree()
    with open(fileName, 'r') as fob:
        for line in fob:
            l = line.strip().split()
            if len(l) == 2:
                command = l[0]
                data = int(l[1].strip())
                if command == 'insert':
                    T.insert(data)
                if command == 'delete':
                    T.delete(data) 
                #if there is a search request
                if command == 'search':
                    T.search(data)
            if len(l) == 1:
                #prints the order name, then the order
                print(l[0])
                T.traverse(l[0])
                print('')
    fob.close()

if __name__ == "__main__":
    main(argv)