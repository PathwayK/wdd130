import math
from datetime import datetime
width= float(input("enter width: "))
aspect = float(input("enter aspect: "))
diameter = float(input("enter diameter: "))

volume = math.pi*width**2*aspect*(width*aspect+2540*diameter)/10000000000
print(f"the volume is {volume:.2f}")
today = datetime.now().date()
with open("volumes.txt","a") as f:
    print(F"{today}, {width},{aspect}, {diameter},{volume:.2f}", file=f)
