#!/usr/bin/env python3

#####################################################################################################
#
#   strayLC_in_MSTL.py - Calculator of stray L,C in Microstrip Line
#
#   Author:     nxg-nxg
#   Repository: https://github.com/nxg-nxg/calculators.git
#   Date:       2022/11/27
#
#####################################################################################################

# T [m]: Thickness of conductor metal of microstrip line
# W [m]: Width of microstrip line
# H [m]: Thickness of dielectric
# L [m]: Length of microstrip line
# E_R  : Permittivity of dielectric

T = 18e-6
W = 1.5e-3
H = 1.6e-3
L = 1e-3
E_R = 4.3

#####################################################################################################
# Read [2, p.68]

import sys
import numpy as np

PI = np.pi
Z_F = 120*PI
V_L = 299792458

if (T/H >= 0.005):
    print("ERROR: T/H < 0.005 does not hold.")
    print("ERROR: This equation can only be used if the thickness of the line is negligibly thin.")
    sys.exit(1)

if (W/H <= 1):
    E_EFF = (E_R+1)/2 + (E_R-1)/2 * ( (1+12*(H/W))**(-1/2) + 0.04*(1-(W/H))**2 )
    Z_0 = Z_F/(2*PI*np.sqrt(E_EFF)) * np.log( 8*(H/W) + (W/H)/4 )

if (W/H > 1):
    E_EFF = (E_R+1)/2 + (E_R-1)/2 * (1+12*(H/W))**(-1/2)
    Z_0 = Z_F/( np.sqrt(E_EFF)*(1.393 + (W/H) + (2/3)*np.log((W/H)+1.444)) )


INDUCTANCE = Z_0 * ( np.sqrt(E_EFF)/V_L ) * L
CAPACITANCE = 1/Z_0 * ( np.sqrt(E_EFF)/V_L ) * L

print("W:\t {0} [m]".format(W))
print("H:\t {0} [m]".format(H))
print("L:\t {0} [m]".format(L))
print("E_R:\t {0}".format(E_R))
print()
print("E_EFF:\t {0}".format(E_EFF))
print("Z_0:\t {0} [Ω]".format(Z_0))
print()
print("INDUCTANCE:\t {0} [H]".format(INDUCTANCE))
print("CAPACITANCE:\t {0} [F]".format(CAPACITANCE))
print()


#####################################################################################################
# References
# [1] Erik O. Hammerstad, “Equations for Microstrip Circuit Design”, 5th European Microwave Conference. 1975
# [2] Reinhold Ludwig, Gene Bogdanov, “RF Circuit Design: Theory and Applications: Second Edition”, PEARSON, 2012