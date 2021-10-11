def swap_case(s):
    k=""
    for i in s:
        if i.isupper():
            l=i.lower()
            k=k+l
        else:
            l=i.upper()
            k=k+l
    return k