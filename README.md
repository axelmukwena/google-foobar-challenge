# Google Foobar Challenge

### Level 1:

#### Question 1: [Solar Doomsday](https://github.com/axelmukwena/google-foobar-challenge/blob/main/solar-doomsday.py)

File: `solar-doomsday.py`

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].


### Level 2:

#### Question 1: [Numbers Station Coded Messages](https://github.com/axelmukwena/google-foobar-challenge/blob/main/numbers-station-coded-messages.py)

File: `numbers-station-coded-messages.py`

Given a non-empty list of positive integers l and a target positive integer t, write a function solution(l, t) which verifies if there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key) and returns the lexicographically smallest list containing the smallest start and end indexes where this sequence can be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).

### Level 3:

#### Question 1: [Elevator Maintenance](https://github.com/axelmukwena/google-foobar-challenge/blob/main/elevator-maintenance.py)

File: `elevator-maintenance.py`

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.


#### Question 2: [Doomsday Fuel](https://github.com/axelmukwena/google-foobar-challenge/blob/main/doomsday-fuel.py)

File: `doomsday-fuel.py`

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

