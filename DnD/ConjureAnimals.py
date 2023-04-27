# Dungeons and Dragons
# Conjure Animals
# by Sergio Ruano

import numpy as np
import random
from colorama import Fore, Back, Style

# 8 x 1/4 CR: Elk
# Roll to Hit
count = 1
print(f"Formula: Roll + Modifier = Total")
print(f"Elk rolls to hit: ")
while(count < 9):
    ToHit = (random.randint(1,20))
    if ToHit == 20:
        print(Fore.GREEN + f"Natural 20!")
    if ToHit == 1:
        print(Fore.RED + f"Natural 1!")
    print(f"Elk {count}: {ToHit} + 5 = {ToHit + 5}")
    print(Style.RESET_ALL)
    count += 1