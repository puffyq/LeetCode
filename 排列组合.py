import time
import itertools
import functools


def timeit(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fun(*args, **kwargs)
        stop_time = time.time()
        print('运行时间:%.6fs' % (stop_time - start_time))
        return res

    return wrapper


class Solution:

    @timeit
    def permutation(self, s):
        text = list(set(itertools.permutations(s)))
        out = []
        for i in text:
            out.append("".join(i))
        return out


aa = Solution()
print(aa.permutation(s="vpvptjzh"))
