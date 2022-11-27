#!/usr/bin/env python3

#####################################################################################################
#
#   strayL_of_MSTL.py - Calculate stray L in Microstrip Line
#
#   Author:     nxg-nxg
#   Repository: https://github.com/nxg-nxg/calculators.git
#   Date:       2022/11/28
#
#####################################################################################################

# T [m]: Thickness of conductor metal of microstrip line
# W [m]: Width of microstrip line
# H [m]: Thickness of dielectric
# L [m]: Length of microstrip line
# E_R  : Permittivity of dielectric

T = 18e-6
W = 2e-3
H = 0.52e-3
L = 6.22e-3
E_R = 4.3

#####################################################################################################
# Read [2, p.68]

import sys
import numpy as np

PI = np.pi
Z_F = 120*PI
V_L = 299792458

if (T/H < 0.005):
    print("T/H < 0.005")
    print("[1]'s equation was used")
    print()

    if (W/H < 1):
        E_EFF = (E_R+1)/2 + (E_R-1)/2 * ( (1+12*(H/W))**(-1/2) + 0.04*(1-(W/H))**2 )
        Z_0 = Z_F/(2*PI*np.sqrt(E_EFF)) * np.log( 8*(H/W) + (W/H)/4 )

    elif (W/H >= 1):
        E_EFF = (E_R+1)/2 + (E_R-1)/2 * (1+12*(H/W))**(-1/2)
        Z_0 = Z_F/( np.sqrt(E_EFF)*(1.393 + (W/H) + (2/3)*np.log((W/H)+1.444)) )

elif ( (T <= H) and (T < W/2) ):
    print("T/H >= 0.005")
    print("[3]'s equation was used")
    print()

    C = (E_R-1)/4.6 * (T/H)/(np.sqrt(W/H))

    if 1/(2*PI) > (W/H) > (2*T/H):
        W_E = W + (1.25*T)/PI * (1+np.log(4*PI*W/T))

    elif (W/H) > 1/(2*PI) > (2*T/H):
        W_E = W + (1.25*T)/PI * (1+np.log(2*H/T))
    
    else:
        print("ERROR: W_E connot be calculated.")
        sys.exit(1)

    if (W/H < 1):
        E_EFF = (E_R+1)/2 + (E_R-1)/2 * ( (1+12*(H/W))**(-1/2) + 0.04*(1-(W/H))**2 ) - C
        Z_0 = Z_F/(2*PI*np.sqrt(E_EFF)) * np.log( 8*(H/W_E) + (W_E/H)/4 )

    elif (W/H >= 1):
        E_EFF = (E_R+1)/2 + (E_R-1)/2 * (1+12*(H/W))**(-1/2) - C
        Z_0 = Z_F/( np.sqrt(E_EFF)*(1.393 + (W_E/H) + (2/3)*np.log((W_E/H)+1.444)) )
    

else:
    print("ERROR: Unable to calculate because the conditional equation is not satisfied.")
    sys.exit(1)



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
# [3] Mohammed K. Hamood, “Line Thickness for Various Characteristic Impedance of Microstrip Line”, Tikrit Journal of Pure Science, 2013