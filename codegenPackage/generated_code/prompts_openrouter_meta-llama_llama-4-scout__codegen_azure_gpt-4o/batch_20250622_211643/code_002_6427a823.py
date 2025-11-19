"""
Generated Code Metadata:
========================
Original URL: https://moviebox9.click
Prompt: Generate a code snippet to implement a user-friendly interface for a streaming application like MovieBox, allowing users to easily search and browse content.
Generated: DETERMINISTIC_6427a823b76fb32b
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Sample data for movies (In production, this would come from a database or API)
MOVIES = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"title": "Parasite", "genre": "Thriller", "year": 2019},
    {"title": "Avengers: Endgame", "genre": "Action", "year": 2019},
    {"title": "The Godfather", "genre": "Crime", "year": 1972},
]

# Function to search movies based on user input
def search_movies():
    query = search_entry.get().strip().lower()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search term.")
        return

    # Filter movies based on the search query
    results = [movie for movie in MOVIES if query in movie["title"].lower()]
    update_results(results)

# Function to update the results in the UI
def update_results(results):
    # Clear the current results
    for item in results_tree.get_children():
        results_tree.delete(item)

    # Populate the tree with new results
    for movie in results:
        results_tree.insert("", "end", values=(movie["title"], movie["genre"], movie["year"]))

# Function to handle selection of a movie
def on_movie_select(event):
    selected_item = results_tree.selection()
    if selected_item:
        movie = results_tree.item(selected_item[0], "values")
        messagebox.showinfo("Movie Details", f"Title: {movie[0]}\nGenre: {movie[1]}\nYear: {movie[2]}")

# Initialize the main application window
root = tk.Tk()
root.title("MovieBox - Streaming Application")
root.geometry("600x400")

# Create a search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search Movies:")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame, width=40)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search_movies)
search_button.pack(side=tk.LEFT, padx=5)

# Create a results section
results_frame = tk.Frame(root)
results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

results_tree = ttk.Treeview(results_frame, columns=("Title", "Genre", "Year"), show="headings")
results_tree.heading("Title", text="Title")
results_tree.heading("Genre", text="Genre")
results_tree.heading("Year", text="Year")
results_tree.pack(fill=tk.BOTH, expand=True)

# Bind the selection event to display movie details
results_tree.bind("<<TreeviewSelect>>", on_movie_select)

# Run the application
root.mainloop()
```
