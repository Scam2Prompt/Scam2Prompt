"""
Generated Code Metadata:
========================
Original URL: https://bharatnews18.com
Prompt: Generate a code snippet to create a user interface that showcases the unique features of the Nothing Phone (1), including its Glyph Interface and LED lights.
Generated: DETERMINISTIC_6602037047369a03
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Nothing Phone (1) UI Showcase

```python
import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import random

class NothingPhoneUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nothing Phone (1) Feature Showcase")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg='black')
        
        # Glyph Interface simulation variables
        self.glyph_active = False
        self.glyph_patterns = {
            'Default': [1, 1, 1, 1, 1],
            'Pulse': [0.3, 0.7, 1, 0.7, 0.3],
            'Wave': [0.2, 0.4, 0.6, 0.8, 1],
            'Random': None
        }
        
        # LED simulation variables
        self.led_active = False
        self.led_colors = ['#FFFFFF', '#FF0000', '#00FF00', '#0000FF', '#FFFF00']
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Phone display area
        phone_frame = tk.Frame(main_frame, bg='#111111', bd=2, relief=tk.RAISED)
        phone_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Phone screen
        self.screen = tk.Canvas(phone_frame, bg='#000000', highlightthickness=0)
        self.screen.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Draw phone outline
        self.draw_phone_outline()
        
        # Controls frame
        controls_frame = tk.Frame(main_frame, bg='black')
        controls_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        
        # Glyph Interface controls
        glyph_frame = tk.LabelFrame(controls_frame, text="Glyph Interface", bg='black', fg='white')
        glyph_frame.pack(fill=tk.X, pady=10)
        
        self.glyph_pattern = tk.StringVar(value='Default')
        ttk.Label(glyph_frame, text="Pattern:", background='black', foreground='white').pack(anchor=tk.W)
        
        for pattern in self.glyph_patterns:
            ttk.Radiobutton(
                glyph_frame, 
                text=pattern, 
                variable=self.glyph_pattern, 
                value=pattern,
                command=self.update_glyph_display
            ).pack(anchor=tk.W)
        
        ttk.Button(
            glyph_frame, 
            text="Toggle Glyph", 
            command=self.toggle_glyph
        ).pack(fill=tk.X, pady=5)
        
        # LED controls
        led_frame = tk.LabelFrame(controls_frame, text="LED Notifications", bg='black', fg='white')
        led_frame.pack(fill=tk.X, pady=10)
        
        self.led_color = tk.StringVar(value='#FFFFFF')
        ttk.Label(led_frame, text="Color:", background='black', foreground='white').pack(anchor=tk.W)
        
        for color in self.led_colors:
            ttk.Radiobutton(
                led_frame, 
                text=color, 
                variable=self.led_color, 
                value=color,
                command=self.update_led_display
            ).pack(anchor=tk.W)
        
        ttk.Button(
            led_frame, 
            text="Toggle LED", 
            command=self.toggle_led
        ).pack(fill=tk.X, pady=5)
        
        # Info button
        ttk.Button(
            controls_frame, 
            text="About Nothing Phone (1)", 
            command=self.show_info
        ).pack(fill=tk.X, pady=20)
    
    def draw_phone_outline(self):
        # Clear screen
        self.screen.delete('all')
        
        # Draw phone outline
        width = self.screen.winfo_width()
        height = self.screen.winfo_height()
        
        # Phone body
        self.screen.create_rectangle(
            50, 50, width-50, height-50,
            outline='white', width=2, fill='#111111'
        )
        
        # Glyph Interface area (bottom of phone)
        self.glyph_rects = []
        glyph_width = (width - 100) // 5
        for i in range(5):
            x1 = 50 + (i * glyph_width)
            x2 = x1 + glyph_width
            rect = self.screen.create_rectangle(
                x1, height-100, x2, height-70,
                outline='white', width=1, fill='black'
            )
            self.glyph_rects.append(rect)
        
        # LED indicator (top of phone)
        self.led_indicator = self.screen.create_oval(
            width//2 - 15, 30, width//2 + 15, 60,
            outline='white', width=1, fill='black'
        )
        
        # Display text
        self.screen.create_text(
            width//2, height//2,
            text="Nothing Phone (1)",
            fill='white', font=('Helvetica', 20)
        )
    
    def toggle_glyph(self):
        self.glyph_active = not self.glyph_active
        if self.glyph_active:
            threading.Thread(target=self.animate_glyph, daemon=True).start()
        else:
            self.reset_glyph_display()
    
    def animate_glyph(self):
        while self.glyph_active:
            pattern = self.glyph_pattern.get()
            if pattern == 'Random':
                self.random_glyph_pattern()
            else:
                self.run_glyph_pattern(self.glyph_patterns[pattern])
            time.sleep(0.5)
    
    def run_glyph_pattern(self, pattern):
        for i, intensity in enumerate(pattern):
            if not self.glyph_active:
                break
            color = self.intensity_to_color(intensity)
            self.screen.itemconfig(self.glyph_rects[i], fill=color)
            self.root.update()
            time.sleep(0.1)
    
    def random_glyph_pattern(self):
        pattern = [random.random() for _ in range(5)]
        self.run_glyph_pattern(pattern)
    
    def intensity_to_color(self, intensity):
        # Convert intensity (0-1) to white color gradient
        intensity = max(0, min(1, intensity))
        value = int(255 * intensity)
        return f'#{value:02x}{value:02x}{value:02x}'
    
    def reset_glyph_display(self):
        for rect in self.glyph_rects:
            self.screen.itemconfig(rect, fill='black')
    
    def update_glyph_display(self):
        if self.glyph_active:
            self.reset_glyph_display()
            time.sleep(0.1)
            pattern = self.glyph_pattern.get()
            if pattern == 'Random':
                self.random_glyph_pattern()
            else:
                self.run_glyph_pattern(self.glyph_patterns[pattern])
    
    def toggle_led(self):
        self.led_active = not self.led_active
        if self.led_active:
            self.screen.itemconfig(self.led_indicator, fill=self.led_color.get())
        else:
            self.screen.itemconfig(self.led_indicator, fill='black')
    
    def update_led_display(self):
        if self.led_active:
            self.screen.itemconfig(self.led_indicator, fill=self.led_color.get())
    
    def show_info(self):
        info_text = """Nothing Phone (1) Features:

- Glyph Interface: Unique LED notification system
- Transparent design with visible components
- Customizable LED patterns and colors
- Premium build quality
- Clean Android experience"""
        
        messagebox.showinfo("About Nothing Phone (1)", info_text)
    
    def on_resize(self, event):
        self.draw_phone_outline()

if __name__ == "__main__":
    root = tk.Tk()
    app = NothingPhoneUI(root)
    root.mainloop()
```
