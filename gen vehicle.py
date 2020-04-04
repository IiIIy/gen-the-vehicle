import random
Moving_type = ["Tracked","Wheeled","Hovered","Winged","Sled","Humanoid-like legged","Spider-like legged","Aerostat or Blimp like","Rotored","Gyrodyne like","Screw-propelled","Floated"]
Type = ["Tank","Cruiser","Damager","Support"]
Weaponry = ["Cannon","Catapult","Flamethrower","Sharp melee","Crane","Bomb","Ram","Drill"]
print("A",random.choice(Moving_type),random.choice(Type),"with",random.choice(Weaponry),"weaponry")