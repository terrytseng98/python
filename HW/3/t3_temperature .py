Show:Please input temperature:"
Input1:40
Show:Please input temperature:
Input1:40temperature
Output:It is too hot.
"""
temperature=input('Please input temperature')
temperature=int(temperature)
if temperature>=40:
    print('It is too hot.')
elif temperature<=10:
    print('It is too cold.')
else:
    print("It is Comfortable.")