#Compare the optimal values computed for both values of x0. Could you have expected how
# the optimal result varies for different x0 before even running the algorithm?

#f1_when x0 = 3:  0.004642275147320177
#f1_when x0 = - 3:  -0.004642275147320177
#f2__when x0 = 3: 1.0048357032784585
#f2__when x0 = -3: 0.9950482398428585

#Their value is almost opposite this makes sense because either we start from the right side 
#of the mountain or left side, we are alomot performing the mirroring process. Once you are
#cloese to the bottom you step ahead and if it is too much, then you step back a little untill
#you find the bottom. 
#Right side, left side, you do the same thing, it is just opposite. 
