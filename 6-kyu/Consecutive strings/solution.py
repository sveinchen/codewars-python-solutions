# -*- coding: utf-8 -*-

def longest_consec(strarr, k):
    if k > 0:
        n = len(strarr)
        if n > 0 and k <= n:
            lenarr = map(len, strarr)
    
            tmparr = []
            for i in range(n - k + 1):
                tmparr.append(reduce(lambda x, y: x + y, lenarr[i:i+k]))
                
            index = tmparr.index(max(tmparr))
    
            return ''.join(strarr[index:index+k])

    return ""
