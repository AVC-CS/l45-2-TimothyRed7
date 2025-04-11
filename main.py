import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i=0
    while(i==0):
        v=random.randint(1,100)
        if(sum(numbers<100)):
            numbers.append(v)
            total=sum(numbers)
        else:
            i=1

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
