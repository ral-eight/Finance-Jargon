import tkinter as tk

dictionary = {}

def add_entry():
    word = word_entry.get().strip()
    definition = definition_entry.get().strip()

    if not word or not definition:
        status_label.config(text="Please enter both a word and a definition.")
        return

    dictionary[word] = definition
    word_entry.delete(0, tk.END)
    definition_entry.delete(0, tk.END)
    status_label.config(text=f'Added: "{word}"')
    refresh_display()

def refresh_display(filtered_items=None):
    display.delete("1.0", tk.END)

    items = filtered_items if filtered_items is not None else dictionary.items()

    if not items:
        display.insert(tk.END, "No entries to show.")
        return

    for w, d in sorted(items, key=lambda x: x[0].lower()):
        display.insert(tk.END, f"{w}: {d}\n\n")

def search_entries(*_):
    query = search_entry.get().strip().lower()

    if query == "":
        refresh_display()
        return

    matches = []
    for w, d in dictionary.items():
        if query in w.lower() or query in d.lower():
            matches.append((w, d))

    refresh_display(matches)

def clear_search():
    search_entry.delete(0, tk.END)
    refresh_display()

# --- UI ---
root = tk.Tk()
root.title("Personal Dictionary (with Search)")
root.geometry("700x550")

# Add section
tk.Label(root, text="Add Entry", font=("Arial", 14, "bold")).pack(anchor="w", padx=12, pady=(10, 0))

tk.Label(root, text="Word").pack(anchor="w", padx=12)
word_entry = tk.Entry(root, width=60)
word_entry.pack(padx=12, pady=(0, 8))

tk.Label(root, text="Definition").pack(anchor="w", padx=12)
definition_entry = tk.Entry(root, width=60)
definition_entry.pack(padx=12, pady=(0, 8))

tk.Button(root, text="Add to Dictionary", command=add_entry).pack(padx=12, pady=(0, 10), anchor="w")

status_label = tk.Label(root, text="", fg="gray")
status_label.pack(anchor="w", padx=12, pady=(0, 10))

# Search section
tk.Label(root, text="Search (matches word OR definition)", font=("Arial", 14, "bold")).pack(anchor="w", padx=12)

search_entry = tk.Entry(root, width=60)
search_entry.pack(padx=12, pady=(6, 6))
search_entry.bind("<KeyRelease>", search_entries)  # live search as you type

tk.Button(root, text="Clear Search", command=clear_search).pack(padx=12, pady=(0, 10), anchor="w")

# Display section
tk.Label(root, text="Results / Dictionary", font=("Arial", 14, "bold")).pack(anchor="w", padx=12)

display = tk.Text(root, wrap="word", height=15)
display.pack(padx=12, pady=(6, 12), fill="both", expand=True)

refresh_display()
root.mainloop()
