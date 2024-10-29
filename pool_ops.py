# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#   determines the output shape and operation count of a pooling layer

# Parameters:
#   c_in: input channel count
#   h_in: input height count
#   w_in: input width count
#   h_pool: average pooling kernel height count
#   w_pool: average pooling kerbel width count
#   s: stride of average pooling kernel
#   p: amount of padding on each of the four input map sides

# Output:
#   channel count, height count, width count, number of additions performed,
#   number of multiplications performed, and number of divisions performed
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import sys
import math

# initialize script arguments
c_in = float('nan')
h_in = float('nan')
w_in = float('nan')
h_pool = float('nan')
w_pool = float('nan')
s = float('nan')
p = float('nan')

# parse script arguments
if len(sys.argv) == 8:
  c_in = int(sys.argv[1])
  h_in = int(sys.argv[2])
  w_in = int(sys.argv[3])
  w_pool = int(sys.argv[5])
  h_pool = int(sys.argv[4])
  s = int(sys.argv[6])
  p = int(sys.argv[7])
else:
  print(\
    'Usage: '\
    'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

## script below this line

# height of the output map
h_out = math.floor(((h_in + 2*p - h_pool)/s) + 1)

# width of the output map
w_out = math.floor(((w_in + 2*p - w_pool)/s) + 1)

# number of channels
c_out = c_in

# total number of multiplications
muls = 0

# total number of additions
adds = c_in*h_out*w_out*(h_pool*w_pool - 1)

# total number of divisions
divs = c_in*h_out*w_out

# print
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))