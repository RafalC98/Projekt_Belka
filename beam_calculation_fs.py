def shear_force_fs(F,q,X,L):
    Rb = (F*X + L*0.5*L*q) / L
    Ra = (-F*(L-X) - q*L*0.5*L) / L

    print(Ra, Rb)
    B_Rb = abs(Rb)
    B_Ra = abs(Ra)

    if B_Rb > B_Ra:
        Max_Shear_force_fs_ = Rb
        Min_Shear_force_fs_ = Ra
        print(Ra)
#         Shearforce_label.config(text="Maximum Value of shear force: " +str(Rb))
#         print("Max =", Max_Shear_force_fs_)
#         print("Min =",Min_Shear_force_fs_)
    else:
        Max_Shear_force_fs_ = Ra
        Min_Shear_force_fs_ = Rb
#         Shearforce_label.config(text="Maximum Value of shear force: " +str(Ra))
#         print("Max =", Max_Shear_force_fs_)
#         print("Min =",Min_Shear_force_fs_)

def bending_moment_fs(F,q,X,L):
    Ra = (-F*(L-X) - q*L*0.5*L) / L

    if Ra > 0:
        M_max = (Ra*X-X*q*X*0.5)
        print(M_max)
#         Moment_label.config(text="Maximum Value of moment: " +str(M_max))
    else:

        M_max = (abs(Ra)*X-X*q*X*0.5)
        M_max = -M_max
        print(M_max)
#         Moment_label.config(text="Maximum Value of moment: " +str(M_max))




F = 2
L = 3
X = 1
q = 2

shear_force_fs(F,q,X,L)
bending_moment_fs(F,q,X,L)
