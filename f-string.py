var: str = "Python"

print(f'{var}');
print(f'{var:_>28}');
print(f'{var:.<28}');
print(f'{var:~^28}')

# using a variable for the number

length: int = 28

print(f'{var:$^{length}}')
