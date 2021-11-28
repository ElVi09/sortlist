def merge(*lists):
    l = []
    for i in lists:
        for d in i:
            l.extend(d)
            print('l = ', l)

    sortlist = sorted(l)

    return sortlist
