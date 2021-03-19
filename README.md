# Toom-Cook-Calculator
## About
Toom–Cook, sometimes known as Toom-3, is a multiplication algorithm for large integers. This is realization of Toom-3 algorithm. Given two large integers, a and b, Toom–Cook
splits up a and b into k smaller parts each of length l, and performs operations on the parts. In this algorithm k equal 3 (that why it calls Toom-3).
Toom-3 reduces 9 multiplications to 5, and runs in Θ(n<sup>log(5)/log(3)</sup>) ≈ Θ(n<sup>1.46</sup>).

## How to run
To calculate just write 
`python3 main.py `
Then input first, then second number. If input numbers are correct there will be result of multiplication, otherwise, program
will require write number again until number will be correct.
Also, you can read some information received during multiplication in logs.log file.
To run test just write `pytest test.py`

## How does it work

The algorithm has five main steps:
*	Splitting
*	Evaluation
*	Pointwise multiplication
*	Interpolation
*	Recomposition

### Spliting
The first step is to select the base B = bi, such that the number of digits of both m and n in base B is at most k (k=3). We then use these digits as 
coefficients in degree-(k − 1) polynomials p and q, with the property that p(B) = m and q(B) = n.The purpose of defining these polynomials is that if we can compute 
their product r(x) = p(x)q(x), our answer will be r(B) = m × n.

### Evaluation
The idea is to evaluate p(·) and q(·) at various points. Then multiply their values at these points to get points on the product polynomial. Finally interpolate to find 
its coefficients. In our Toom-3 example, we will use the points 0, 1, −1, −2, and ∞. 

### Pointwise multiplication
Unlike multiplying the polynomials p(·) and q(·), multiplying the evaluated values p(a) and q(a) just involves multiplying integers — a smaller instance of the original 
problem. We recursively invoke our multiplication procedure to multiply each pair of evaluated points.For large enough numbers, this is the most expensive step, the only 
step that is not linear in the sizes of m and n

### Interpolation
This is the most complex step, the reverse of the evaluation step: given our d points on the product polynomial r(·), we need to determine its coefficients.

### Recomposition
Finally, we evaluate r(B) to obtain our final answer. This is straightforward since B is a power of b and so the multiplications by powers of B are all shifts by a whole
number of digits in base b
