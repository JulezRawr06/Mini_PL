import tkinter as tk

def show_stats():
    stats = f"""
    Name: Pikachu
    Type: Electric
    HP: 35
    Attack: 55
    Defense: 40
    Speed: 90
    """
    label.config(text=stats)

root = tk.Tk()
root.title("Pokémon Stat Viewer")

# --- Make window a perfect square and center it ---
window_size = 400  # size of square
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_size // 2)
y = (screen_height // 2) - (window_size // 2)

root.geometry(f"{window_size}x{window_size}+{x}+{y}")
# -----------------------------------------------

label = tk.Label(root, text="Click to show Pikachu's stats", justify="left")
label.pack(padx=20, pady=20)

button = tk.Button(root, text="Show Stats", command=show_stats)
button.pack()

root.mainloop()
