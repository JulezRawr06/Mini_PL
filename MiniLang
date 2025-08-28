# pokemon_repl.py

pokemons = {}  # storage for Pokémon


def declare_pokemon():
    """Read a block from input until END"""
    header = input("... ").strip()
    if not header.upper().startswith("POKEMON"):
        print("Syntax error: must start with POKEMON <name>")
        return

    parts = header.split()
    if len(parts) < 2:
        print("Syntax error: missing Pokémon name")
        return
    name = parts[1]

    props = {}
    while True:
        line = input("... ").strip()
        if line.upper() == "END":
            break
        if "=" not in line:
            print("Syntax error: expected KEY = VALUE")
            continue
        key, value = [p.strip() for p in line.split("=", 1)]
        props[key.upper()] = value

    pokemons[name] = props
    print(f"Pokémon '{name}' saved!")


def run_repl():
    print("Pokémon Mini Language. Type EXIT to quit.")
    while True:
        line = input(">>> ").strip()
        if not line:
            continue

        if line.upper() == "EXIT":
            print("Goodbye!")
            break

        elif line.upper().startswith("POKEMON"):
            # we already read "POKEMON Name" line, now handle properties
            parts = line.split()
            if len(parts) < 2:
                print("Syntax error: missing Pokémon name")
                continue
            name = parts[1]

            props = {}
            while True:
                pline = input("... ").strip()
                if pline.upper() == "END":
                    break
                if "=" not in pline:
                    print("Syntax error: expected KEY = VALUE")
                    continue
                key, value = [p.strip() for p in pline.split("=", 1)]
                props[key.upper()] = value

            pokemons[name] = props
            print(f"Pokémon '{name}' saved!")

        elif line.upper().startswith("PRINT"):
            parts = line.split()
            if len(parts) < 2:
                print("Syntax error: PRINT <name>")
                continue
            name = parts[1]
            if name in pokemons:
                print(f"{name}: {pokemons[name]}")
            else:
                print(f"No Pokémon named {name}")

        elif line.upper() == "LIST":
            if not pokemons:
                print("No Pokémon added yet.")
            else:
                for name, props in pokemons.items():
                    print(f"{name}: {props}")

        else:
            print("Unknown command.")


if __name__ == "__main__":
    run_repl()
