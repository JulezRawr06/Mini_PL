# Goal GUI output with Tkinter
import tkinter as tk
import pokebase as pb

def show_stats():
    name = entry.get().lower()
    try:
        pokemon = pb.pokemon(name)

        # Build stats text
        stats_text = f"Name: {pokemon.name.capitalize()}\n"
        stats_text += "Type(s): " + ", ".join([t.type.name.capitalize() for t in pokemon.types]) + "\n\n"

        for stat in pokemon.stats:
            stats_text += f"{stat.stat.name.capitalize()}: {stat.base_stat}\n"

        label.config(text=stats_text)

    except Exception as e:
        label.config(text="Pokémon not found!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Pokédex Viewer")

# Make window a perfect centered square
window_size = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_size // 2)
y = (screen_height // 2) - (window_size // 2)
root.geometry(f"{window_size}x{window_size}+{x}+{y}")

# Widgets
entry = tk.Entry(root, justify="center")
entry.pack(pady=10)

button = tk.Button(root, text="Fetch Stats", command=show_stats)
button.pack(pady=5)

label = tk.Label(root, text="Enter a Pokémon name above", justify="left")
label.pack(padx=20, pady=20)

root.mainloop()
