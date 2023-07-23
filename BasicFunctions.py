####Some Common Rpetitve Functions###

#To give a pause between procedures
def wait(string):
    print (string)
    input ()
    
##Genweates a beutiful heading
def title(string):
    print('\t\t\t',end='')
    for i in range (len(string)+2): print('*',end='')
    print()
    print('\t\t\t*',string,'*',sep='')
    print('\t\t\t',end='')
    for i in range (len(string)+2): print('*',end='')
    print('\n\n')


## Useful function to take intger input between a range
def take_input(string,low,high):
    while True:
        try:
            value = int(input(string))
            if value>=low and value<=high:
                return value
            else:
                print('Value out of range please try again...')
        except ValueError as e:
            print('Invalid datatype, please enter a number ')
