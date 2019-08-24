

def printarray():
    arr = [1, 2, 3, 4, 5]
    print(arr)
    for i in arr:
        print('{:d}'.format(i, ), end=' ')
    print('\n')

    for j in range(1, 10):
        if j % 2 == 0:
            print('even', end=' ')
        else:
            print('odd', end=' ')

