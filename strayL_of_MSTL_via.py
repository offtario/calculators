#!/usr/bin/env python3

#####################################################################################################
#
#   strayL_of_MSTL_via.py - Calculate stray L of via in Microstrip Line
#
#   Author:     nxg-nxg
#   Repository: https://github.com/nxg-nxg/calculators.git
#   Date:       2022/11/28
#
#####################################################################################################

# H [m]     : Height of via
# R [m]     : Radius of via
# WAVE_L [m]: Wavelength of signal throw via

H = 0.52e-3
R = 0.15e-3
WAVE_L = 300e6

#####################################################################################################
import sys
import numpy as np

if ((H < 100e-6) or (H > 631e-6)) and (WAVE_L*0.03 < H):
    print("ERROR: Unable to calculate because the conditional equation is not satisfied.")
    sys.exit(1)

PI = np.pi
MU_0 = 4*PI*10**(-7)
MEAN_SQ = np.sqrt(R*R + H*H)

L_VIA = MU_0/(2*PI) * ( H * np.log((H+MEAN_SQ)/R) + 3/2*(R-MEAN_SQ) )

print("H:\t {0} [m]".format(H))
print("R:\t {0} [m]".format(R))
print("WAVE_L:\t {0}".format(WAVE_L))
print()
print("INDUCTANCE:\t {0} [H]".format(L_VIA))
print()

#####################################################################################################
# References
# [1] M.E. Goldfarb, R.A. Pucel, "Modeling via hole grounds in microstrip", IEEE Microwave and Guided Wave Letters, 1991