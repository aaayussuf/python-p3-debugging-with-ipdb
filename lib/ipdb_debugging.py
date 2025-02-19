import ipdb

def plus_two(num):
    num = num + 2  # Fixing the issue
    ipdb.set_trace()  # Debugging breakpoint
    return num
