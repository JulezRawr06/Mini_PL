# Example of pokebase library usage
import pokebase as pb

mon = pb.pokemon(input("What pokemon to display stats: ").lower().strip()) # Quick lookup.

for stat in mon.stats:
    print(stat.stat.name, stat.base_stat)