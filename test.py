#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 1:43 PM
# @Author  : Huang An

import numpy as np

if __name__ == "__main__":
    # a = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
    #               [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], dtype=float)
    a = np.random.random((6, 6))
    print(a)
    b = a[2:-1, 2:-2]
    print(b)
