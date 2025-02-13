#%%Q1
def greet(str):
    print(f'Hello, {str}!')

greet('world')

#%%Q2
def goldilocks(length):
    if length < 140:
        print('Too small!')
    elif length > 150:
        print('Too large!')
    else:
        print('Just right. :)')

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

#%%Q3
def square_list(input):
    res = [x**2 for x in input]
    print(res)

square_list([1,2,3])

#%%Q4
def fibonacci_stop(end_val):
    fib_list = [1, 1]
    while (next_val := fib_list[-1]+fib_list[-2]) <= end_val:
        fib_list.append(next_val)
    print(fib_list)

fibonacci_stop(30)

#%%Q5
def clean_pitch(pitch, status):
    for i, status in enumerate(status):
        if status == 1 and not (0 < pitch[i] < 90):
            pitch[i] = -999
    print(pitch)

x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
clean_pitch(x, status)
# %%
