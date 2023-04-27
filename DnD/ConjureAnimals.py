# Dungeons and Dragons
# Conjure Animals
# by Sergio Ruano

import numpy as np
import random
from colorama import Fore, Back, Style

# 8 x 1/4 CR: Elk
# Roll to Hit
count = 1

print(f"\nFormula: Roll + Modifier = Total \n")
while(count < 9):
    ToHit = (random.randint(1,20))
    if ToHit == 20:
        print(Fore.GREEN + f"Natural 20!")
        print(f"Elk {count}: {ToHit} + 5 = {ToHit + 5} to hit")
        print(f"Critical Damage:")
        print(f"Ram: {(random.randint(1,6) * 2) + 3} bludgeoning dmg")
        print(f"Charge: {(random.randint(2, 12) * 2)} + DC 13 STR Save or Prone")
        print(f"Hooves: {(random.randint(2, 8) * 2) + 3} bludgeoning dmg")
    elif ToHit == 1:
        print(Fore.RED + f"Natural 1!")
        print(f"Elk {count}: {ToHit} + 5 = {ToHit + 5} to hit")
        print(f"Ram: {(random.randint(1,6)) + 3} bludgeoning dmg")
        print(f"Charge: {(random.randint(2, 12))} + DC 13 STR Save or Prone")
        print(f"Hooves: {(random.randint(2, 8)) + 3} bludgeoning dmg")
    else:
        print(f"Elk {count}: {ToHit} + 5 = {ToHit + 5} to hit")
        print(f"Ram: {(random.randint(1,6)) + 3} bludgeoning dmg")
        print(f"Charge: {(random.randint(2, 12))} + DC 13 STR Save or Prone")
        print(f"Hooves: {(random.randint(2, 8)) + 3} bludgeoning dmg")
    print(Style.RESET_ALL)
    count += 1