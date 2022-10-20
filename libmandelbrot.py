import re
import numpy as NP

"""
Mandelbrot algorithm, the basic application of numpy is based on 
[1], and I want to calculate the result from each iteration. 



reference: 
[1]https://realpython.com/mandelbrot-set-python
    
"""

def making_complex_array(rmin, rmax, imin, imax, nr, ni=None ):
    """ Using numpy linspace to create the gridcells of 
        input array. 
    """
    if ni == None:
        ni =  int(nr * (imax-imin) / (rmax-rmin) /2 ) * 2
    arr_r = NP.linspace(rmin, rmax, nr+1 )
    arr_i = NP.linspace(imin, imax, ni+1 )
    return arr_r[NP.newaxis, :] + arr_i[:, NP.newaxis] * 1j  

def mb_calculate_binary(c, num_repeats, num_thre=None):
    """ Using input array (c) and do the calculation for the 
        mandelbrot, z = z**2 + c .
    """
    if num_thre==None: num_thre=2.0
    z = 0
    for _ in range(num_repeats):
        z = z**2 + c
    return abs(z) <= num_thre

def mb_calculate_binary_accum(c, num_repeats, num_thre=None):
    """ Using input array (c) and do the calculation for the 
        mandelbrot, z = z**2 + c .
        The output of z will be accumulated into z_out:
        z_out  = z + z_out
    """
    if num_thre==None: num_thre=2.0
    z     = 0
    z_out = 0
    for _ in range(num_repeats):
        z = z**2 + c
        z_out += abs(z) <= num_thre
    return z_out

def run_mb_cpu(numRepeat, numSize, numRMin=-2, numRMax=1, numIMin=-1.3, numIMax=1.3, numThre=2.0 ):
    """ The total procedure of calculating the mandelbrot with the inputs 
    """
    arr_in     = making_complex_array(numRMin, numRMax, numIMin, numIMax, numSize)
    arr_out    = mb_calculate_binary_accum(arr_in, numRepeat, num_thre=numThre)
    return arr_out

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
