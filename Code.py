def WW_algo(p, pr, cc, t):
    c = []
    x = cc + p[-1] * pr[-1]
    c.append(x)
    method_list = []
    methode = f"cc + prix({pr[-1]}) * p({len(p)}) "
    method_list.append(methode)
    for i in range(1, len(p)):
        N = []
        methods = []
        for j in range(i + 1):
            if j == 0:
                x1 = cc + c[i - 1] + p[-i - 1] * pr[-i - 1]
                N.append(x1)
                methods.append(f"Cc + p({len(p)-i}) * {pr[-i - 1]} + c({len(p) - i+1})")
            elif j > 0 and j != i:
                x2 = cc + c[-j - 1] + pr[-i - 1] * p[-i - 1]
                method = f"Cc + p({len(p)-i}) * {pr[-i - 1]} + c({len(p)-i+j+1})"
                for k in range(1, j + 1):
                    x2 = x2 + k * t * p[-i + k - 1] * pr[-i - 1] + pr[-i - 1] * p[-i + k - 1]
                    method += f" + {k} * t({t}) * p({len(p)-i+k})* {pr[-i-1]} + {pr[-i-1]} * p({len(p)-i+k})"
                N.append(x2)
                methods.append(method)
            elif j == i:
                x3 = cc + pr[-i - 1] * p[-i - 1]
                method = f"Cc + p({len(p)-i}) * {pr[-i - 1]}"
                for k in range(1, j + 1):
                    x3 = x3 + k * t * p[-j + k - 1] * pr[-i - 1] + pr[-i - 1] * p[-j + k - 1]
                    method += f" + {k} * t({t}) *  p({len(p)-i+k}) * {pr[-i-1]} + {pr[-i-1]} *  p({len(p)-i+k})"
                N.append(x3)
                methods.append(method)
        c.append(min(N))
        min_index = N.index(min(N))
        method_list.append(methods[min_index])

    return c, method_list
p=[120,130,110]
pr=[12,11,14]
cc=120
t=0.1
c=WW_algo(p, pr, cc, t)
print(c)
