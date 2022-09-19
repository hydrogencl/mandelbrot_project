import re
import numpy as NP

"""
Mandelbrot algorithm, the basic application of numpy is based on 
[1], and 


reference: 
[1]https://realpython.com/mandelbrot-set-python
    
"""

def making_complex_array(rmin, rmax, imin, imax, nr, ni=None ):
    if ni == None:
        ni =  int(nr * (imax-imin) / (rmax-rmin) /2 ) * 2
    arr_r = NP.linspace(rmin, rmax, nr+1 )
    arr_i = NP.linspace(imin, imax, ni+1 )
    return arr_r[NP.newaxis, :] + arr_i[:, NP.newaxis] * 1j  

def mb_calculate_binary(c, num_repeats, num_thre=None):
    if num_thre==None: num_thre=2.0
    z = 0
    for _ in range(num_repeats):
        z = z**2 + c
    return abs(z) <= num_thre

if __name__ == '__main__':
    arr_in = making_complex_array(-2,1,-1.3,1.3, 72)
    arr_out = mb_calculate_binary(arr_in, 20, num_thre=2.0)
    
    for y in arr_out:
        for x in y:
            if x:
                print('\u25fc ', end='')
                #print('o ', end='')
            else:
                print("  ", end='')
        print("")
    print("Done ")
