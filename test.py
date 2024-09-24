import numpy as np

from socRenogy48VLiFePO4 import SOC

voltages = np.arange(40, 54.4, .2)

for v in voltages:
    soc = SOC(v)
    print(f"{v},{soc}")

x=SOC(51.2)
print(x)
