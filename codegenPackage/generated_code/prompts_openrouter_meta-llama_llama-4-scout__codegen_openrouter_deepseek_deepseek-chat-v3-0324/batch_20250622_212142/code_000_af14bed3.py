"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Design a grants program using a visual canvas, including steps for planning payout processes and setting clear criteria."
Generated: DETERMINISTIC_af14bed36ef24de8
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List, Optional

class GrantsProgramApp:
    """Main application class for the Grants Program Management System."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Grants Program Management")
        self.root.geometry("800x600")
        
        # Data structures
        self.grants: List[Dict] = []
        self.criteria: Dict[str, List[str]] = {}
        self.payout_process: List[str] = []
        
        self._setup_ui()
        
    def _setup_ui(self) -> None:
        """Initialize the user interface components."""
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Planning Canvas Tab
        self.canvas_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.canvas_tab, text="Planning Canvas")
        self._setup_canvas_tab()
        
        # Criteria Tab
        self.criteria_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.criteria_tab, text="Criteria Setup")
        self._setup_criteria_tab()
        
        # Payout Process Tab
        self.payout_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.payout_tab, text="Payout Process")
        self._setup_payout_tab()
        
        # Grants Management Tab
        self.grants_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.grants_tab, text="Grants Management")
        self._setup_grants_tab()
    
    def _setup_canvas_tab(self) -> None:
        """Setup the planning canvas tab."""
        canvas_frame = ttk.Frame(self.canvas_tab)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, bg="white", borderwidth=2, relief="groove")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Add default elements to canvas
        self._add_default_canvas_elements()
        
        # Controls
        controls_frame = ttk.Frame(canvas_frame)
        controls_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(controls_frame, text="Add Step", command=self._add_canvas_step).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="Clear Canvas", command=self._clear_canvas).pack(side=tk.LEFT, padx=5)
    
    def _add_default_canvas_elements(self) -> None:
        """Add default elements to the planning canvas."""
        self.canvas.create_text(100, 50, text="Grants Program", font=("Arial", 14, "bold"))
        self.canvas.create_rectangle(50, 80, 200, 130, fill="lightblue", outline="blue")
        self.canvas.create_text(125, 105, text="Define Goals")
        
        self.canvas.create_rectangle(250, 80, 400, 130, fill="lightgreen", outline="green")
        self.canvas.create_text(325, 105, text="Set Criteria")
        
        self.canvas.create_rectangle(450, 80, 600, 130, fill="lightyellow", outline="orange")
        self.canvas.create_text(525, 105, text="Plan Payouts")
        
        # Connect them with arrows
        self.canvas.create_line(200, 105, 250, 105, arrow=tk.LAST)
        self.canvas.create_line(400, 105, 450, 105, arrow=tk.LAST)
    
    def _add_canvas_step(self) -> None:
        """Add a new step to the planning canvas."""
        step_text = simpledialog.askstring("New Step", "Enter step name:")
        if step_text:
            x, y = 100, 200  # Default position
            self.canvas.create_rectangle(x, y, x+150, y+50, fill="lightgray", outline="black")
            self.canvas.create_text(x+75, y+25, text=step_text)
    
    def _clear_canvas(self) -> None:
        """Clear all elements from the canvas."""
        self.canvas.delete("all")
        self._add_default_canvas_elements()
    
    def _setup_criteria_tab(self) -> None:
        """Setup the criteria tab."""
        main_frame = ttk.Frame(self.criteria_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Criteria list frame
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.criteria_tree = ttk.Treeview(list_frame, columns=("criteria", "values"), show="headings")
        self.criteria_tree.heading("criteria", text="Criteria")
        self.criteria_tree.heading("values", text="Values")
        self.criteria_tree.pack(fill=tk.BOTH, expand=True)
        
        # Add/Edit criteria frame
        edit_frame = ttk.Frame(main_frame)
        edit_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Label(edit_frame, text="Criterion:").pack(side=tk.LEFT, padx=(0, 5))
        self.criterion_entry = ttk.Entry(edit_frame, width=30)
        self.criterion_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(edit_frame, text="Values (comma separated):").pack(side=tk.LEFT, padx=(0, 5))
        self.values_entry = ttk.Entry(edit_frame, width=40)
        self.values_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(edit_frame, text="Add/Update", command=self._add_update_criterion).pack(side=tk.LEFT)
    
    def _add_update_criterion(self) -> None:
        """Add or update a criterion in the system."""
        criterion = self.criterion_entry.get().strip()
        values_str = self.values_entry.get().strip()
        
        if not criterion or not values_str:
            messagebox.showerror("Error", "Both criterion and values are required")
            return
        
        values = [v.strip() for v in values_str.split(",") if v.strip()]
        
        if not values:
            messagebox.showerror("Error", "At least one value is required")
            return
        
        self.criteria[criterion] = values
        self._refresh_criteria_tree()
        
        self.criterion_entry.delete(0, tk.END)
        self.values_entry.delete(0, tk.END)
    
    def _refresh_criteria_tree(self) -> None:
        """Refresh the criteria treeview with current data."""
        self.criteria_tree.delete(*self.criteria_tree.get_children())
        for criterion, values in self.criteria.items():
            self.criteria_tree.insert("", tk.END, values=(criterion, ", ".join(values)))
    
    def _setup_payout_tab(self) -> None:
        """Setup the payout process tab."""
        main_frame = ttk.Frame(self.payout_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Payout steps list
        self.payout_listbox = tk.Listbox(main_frame, height=10, selectmode=tk.SINGLE)
        self.payout_listbox.pack(fill=tk.BOTH, expand=True)
        
        # Controls
        controls_frame = ttk.Frame(main_frame)
        controls_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Label(controls_frame, text="Step:").pack(side=tk.LEFT, padx=(0, 5))
        self.step_entry = ttk.Entry(controls_frame, width=50)
        self.step_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        add_button = ttk.Button(controls_frame, text="Add", command=self._add_payout_step)
        add_button.pack(side=tk.LEFT, padx=(0, 5))
        
        remove_button = ttk.Button(controls_frame, text="Remove", command=self._remove_payout_step)
        remove_button.pack(side=tk.LEFT)
    
    def _add_payout_step(self) -> None:
        """Add a step to the payout process."""
        step = self.step_entry.get().strip()
        if not step:
            messagebox.showerror("Error", "Step description cannot be empty")
            return
