# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
try:
    import bdsf
except ImportError:
    from lofar import bdsm as bdsf

#options = {
    #'adaptive_rms_box': True,
    #'adaptive_thresh': 150,
    #'group_tol': 10,
    #'quiet': True,
    #'rms_box': (160, 50),
    #'rms_box_bright': (60, 15)
    #}

options_tier1 = {
    "thresh_isl": 4.0, 
    "thresh_pix": 5.0,
    "rms_box": (160, 50), 
    "rms_map": True, 
    "mean_map": 'zero', 
    "ini_method": 'intensity',
    "adaptive_rms_box": True, 
    "adaptive_thresh": 150, 
    "rms_box_bright": (60, 15), 
    "group_by_isl": False, 
    "group_tol": 10.0,
    "output_opts": True, 
    "output_all": True, 
    "atrous_do": True,
    "atrous_jmax": 4,
    #"trim_box": (5624,31384,3384,28084),
    "frequency": 144e6
}
  
def parse_args(args):
    """
    Parse the arguments of the command line
    """
    parser = argparse.ArgumentParser(description='Extract sources and data using Tier1 options')
    parser.add_argument('img', help='Image to use as input')
    return parser.parse_args(args)


def extract_tier1(input_image, options=options_tier1):
    """
    Extract the sources from a fits image using PyBDSF.
    By default it applies the options used for Tier1.
    """
    img = bdsf.process_image(input_image, **options)
    if not options["output_all"]:
        img.write_catalog(format='bbs', clobber=True)
        img.write_catalog(format='fits', catalog_type='gaul', clobber=True)
        img.write_catalog(format='fits', catalog_type='srl', clobber=True) 

    
