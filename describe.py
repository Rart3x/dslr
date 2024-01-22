import pandas as pd
import sys

from mathFunctions.math import calculate_count, calculate_mean, calculate_std, \
     calculate_min, calculate_quarter, calculate_half, calculate_three_quarters, \
     calculate_max, calculate_sum

if len(sys.argv) < 2:
    print("\033[91musage: python describe.py [* .csv]")
    exit(1)

datas = pd.read_csv(sys.argv[1])