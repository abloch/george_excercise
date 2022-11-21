def str2int(s: str):
    if not isinstance(s, str):
        raise ValueError()
    
    if len(s) == 0:
        raise ValueError()

    c = s[-1]
    c_val = ord(c) - ord('0')
    if not c.isdigit():
        raise ValueError()
    
    if len(s) == 1:
        return c_val
    else:
        return c_val + 10 * str2int(s[:-1])
