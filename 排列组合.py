import numpy as np
class Solution:
    def permutation(self, s: str) -> List[str]:
        out = []
        s="vpvptjzh"
        in_arr = [s[i] for i in range(len(s))]
        for i in range(len(s)):
            out.append(in_arr[i])
        
        for _ in range(len(s)-1):
            out_1 = []
            for arr in out:
                for j in in_arr:
                    temp_arr = [arr[i] for i in range(len(arr))]
                    if np.sum(np.array(temp_arr)==j) >= np.sum(np.array(in_arr)==j):
                        continue
                    else:
                        ar = arr + j
                    out_1.append(ar)
            out = out_1
        return list(set(out))
