meraki = {"switches": {"acceso": ["MS210", "MS225", "MS250", "MS350", "MS390"], "dist": ["MS410", "MS425", "MS450"]}}

print("El primer switch de acceso de mi lista es: ")
print(meraki["switches"]["acceso"][0])

print("Mi lista de switches de acceso es: ")

for switch in meraki["switches"]["acceso"]:
    print(switch)

print("Mi lista de switches de distribucion es: ")
for switch in meraki["switches"]["dist"]:
    print(switch)