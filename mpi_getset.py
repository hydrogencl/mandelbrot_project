from  mpi4py import MPI
from libmandelbrot import *
import argparse

import re,os
import numpy as NP

import netCDF4 as NC
from GRIDINFORMER import MPI_TOOLS 

# Parsers
parser = argparse.ArgumentParser(description=\
        "This is the Mandelbrot clculation based on description from the Internet for Benchmarking and test for MPI and GPU")
parser.add_argument("-cx", '--cpu_nx'   , type=int, dest='NUM_CPU_NX'      
                                        , default = 1   , help="CPU TOPOLOGY: number of x direction. y direction will be cauculated")
parser.add_argument("-nx", '--array_nx' ,  type=int,   dest='NUM_ARR_NX'   
                                        , default = 100 , help='Density of the  x-direction     ')
parser.add_argument("-ny", '--array_ny' ,  type=int,   dest='NUM_ARR_NY'   , help='Density of the  y-direction     ')
parser.add_argument("-r0", '--real_min' ,  type=float, dest='NUM_REAL_MIN' 
                                        , default = -2.0, help='Min of Real-Axis                ')
parser.add_argument("-rn", '--real_max' ,  type=float, dest='NUM_REAL_MAX' 
                                        , default =  1.0, help='Max of Real-Axis                ')
parser.add_argument("-i0", '--image_min',  type=float, dest='NUM_IMAGE_MIN'
                                        , default = -1.3, help='Min of Iamge-Axis               ')
parser.add_argument("-in", '--image_max',  type=float, dest='NUM_IMAGE_MAX'
                                        , default =  1.3, help='Max of Image-Axis               ')
parser.add_argument("-r" , '--num_repeat', type=int  , dest='NUM_REPEATS'  
                                         , default=100                     , help='number of repeats               ')
parser.add_argument("-t" , '--num_thresh', type=int  , dest='NUM_THRE'     , help='number of repeats               ')
parser.add_argument("-f" , '--filename'  , type=str  , dest='STR_FILENAME' , help='Filename of output (default:.mandelbrot_out.nc)')
ARGS  = parser.parse_args()

# Preparing

# Preparing the array

ARR_IN = making_complex_array(ARGS.NUM_REAL_MIN, ARGS.NUM_REAL_MAX, 
                              ARGS.NUM_REAL_MIN, ARGS.NUM_REAL_MAX, 
                              ARGS.NUM_ARR_NX  , ARGS.NUM_ARR_NY  )

ARR_IN_TOPO = ARR_IN.shape

# Preparing the mpi topography

comm         = MPI.COMM_WORLD
NUM_MPI_RANK = comm.Get_rank()
NUM_MPI_SIZE = comm.Get_size()

MPI_NX = ARGS.NUM_CPU_NX
MPI_NY = NUM_MPI_SIZE / MPI_NX

NUM_ARR_NX  = ARR_IN_TOPO[1]
NUM_ARR_NY  = ARR_IN_TOPO[0]

MPI_SET  = MPI_TOOLS(MPI_SIZE=NUM_MPI_SIZE,  \
                     MPI_RANK = NUM_MPI_RANK,\
                     NUM_NX_END = NUM_ARR_NX,\
                     NUM_NY_END = NUM_ARR_NY )
MPI_SET.CPU_GEOMETRY_2D()
ARR_TOPO = NP.array(MPI_SET.ARR_RANK_DESIGN)

MPI_SET.MPI_MESSAGE("Done Preparing Array and MPI")

# Preparing the netCDF4-Data



# Calculation

ARR_OUT = mb_calculate_binary(ARR_IN, ARGS.NUM_REPEATS, num_thre=ARGS.NUM_THRE)
MPI_SET.MPI_MESSAGE("Done Calculation            ")

# Stroring 




