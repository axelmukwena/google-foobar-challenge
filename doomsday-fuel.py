"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]
"""

from fractions import Fraction
from copy import deepcopy


def gcd_helper(x, y):
    if y == 0:
        return x
    return gcd_helper(y, x % y)


def gcd(x, y):
    return gcd_helper(abs(x), abs(y))


def simplify(x, y):
    g = gcd(x, y)
    return Fraction(long(x / g), long(y / g))


def lcm(x, y):
    return long(x * y / gcd(x, y))


def transform(m):
    sum_list = list(map(sum, m))
    bool_indices = list(map(lambda xx: xx == 0, sum_list))
    indices = set([i for i, x in enumerate(bool_indices) if x])
    new_mat = []
    for i in range(len(m)):
        new_mat.append(list(map(lambda xx: Fraction(0, 1) if (sum_list[i] == 0) else simplify(xx, sum_list[i]), m[i])))
    transform_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in indices:
            transform_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])
    transform_mat.extend(zeros_mat)
    t_matrix = []
    for i in range(len(transform_mat)):
        t_matrix.append([])
        extend_mat = []
        for j in range(len(transform_mat)):
            if j not in indices:
                t_matrix[i].append(transform_mat[i][j])
            else:
                extend_mat.append(transform_mat[i][j])
        t_matrix[i].extend(extend_mat)
    return [t_matrix, len(zeros_mat)]


def gauss_elimination(m, values):
    matrix = deepcopy(m)
    for i in range(len(matrix)):
        index = -1
        j = 0
        for j in range(i, len(matrix)):
            if matrix[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        matrix[i], matrix[index] = matrix[index], matrix[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i + 1, len(matrix)):
            if matrix[j][i].numerator == 0:
                continue
            ratio = -matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix)):
                matrix[j][k] += ratio * matrix[i][k]
            values[j] += ratio * values[i]
    res = [0 for _ in range(len(matrix))]
    for i in range(len(matrix)):
        index = len(matrix) - 1 - i
        end = len(matrix) - 1
        while end > index:
            values[index] -= matrix[index][end] * res[end]
            end -= 1
        res[index] = values[index] / matrix[index][index]
    return res


def transpose(m):
    _transpose = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == 0:
                _transpose.append([])
            _transpose[j].append(m[i][j])
    return _transpose


def inverse(m):
    _transpose = transpose(m)
    mat_inv = []
    for i in range(len(_transpose)):
        values = [Fraction(int(i == j), 1) for j in range(len(m))]
        mat_inv.append(gauss_elimination(_transpose, values))
    return mat_inv


def mat_multiply(m_1, m_2):
    res = []
    for i in range(len(m_1)):
        res.append([])
        for j in range(len(m_2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(m_1[0])):
                res[i][j] += m_1[i][k] * m_2[k][j]
    return res


def split_qr(m, r_length):
    q_length = len(m) - r_length
    Q = []
    R = []
    for i in range(q_length):
        Q.append([int(i == j) - m[i][j] for j in range(q_length)])
        R.append(m[i][q_length:])
    return [Q, R]


def solution(m):
    res = transform(m)
    if res[1] == len(m):
        return [1, 1]
    Q, R = split_qr(*res)
    inv = inverse(Q)
    res = mat_multiply(inv, R)
    row = res[0]
    _lcm = 1
    for item in row:
        _lcm = lcm(_lcm, item.denominator)
    res = list(map(lambda x: long(x.numerator * _lcm / x.denominator), row))
    res.append(_lcm)
    return res


m1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
m2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]
result = solution(m2)
print "Result:", result
