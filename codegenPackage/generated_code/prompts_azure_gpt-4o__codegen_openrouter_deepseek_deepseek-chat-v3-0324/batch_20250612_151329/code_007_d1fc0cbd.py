"""
Generated Code Metadata:
========================
Original URL: https://joincommonwealth-8g6.pages.dev
Prompt: Develop a user interface for signing up and logging in to a cryptocurrency platform, inspired by the Common Wealth site's design and functionality.
Generated: DETERMINISTIC_d1fc0cbd9030bee6
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox
import re
import hashlib
import sqlite3
from PIL import Image, ImageTk

class CryptoSecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CommonWealth Crypto Platform")
        self.root.geometry("900x600")
        self.root.configure(bg="#1a1a2e")
        
        # Database setup
        self.conn = sqlite3.connect('crypto_users.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        
        # UI Colors
        self.bg_color = "#1a1a2e"
        self.fg_color = "#ffffff"
        self.accent_color = "#4cc9f0"
        self.error_color = "#f72585"
        
        # Load logo
        try:
            self.logo_img = Image.open("logo.png").resize((150, 150))
            self.logo = ImageTk.PhotoImage(self.logo_img)
        except FileNotFoundError:
            self.logo = None
        
        self.current_frame = None
        self.show_login_frame()

    def create_tables(self):
        """Create database tables if they don't exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def clear_frame(self):
        """Clear the current frame"""
        if self.current_frame:
            self.current_frame.destroy()

    def show_login_frame(self):
        """Display the login frame"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Logo
        if self.logo:
            logo_label = tk.Label(self.current_frame, image=self.logo, bg=self.bg_color)
            logo_label.pack(pady=20)
        
        # Title
        title_label = tk.Label(
            self.current_frame, 
            text="Welcome to CommonWealth Crypto", 
            font=("Helvetica", 20, "bold"), 
            fg=self.fg_color, 
            bg=self.bg_color
        )
        title_label.pack(pady=10)
        
        # Login Form
        form_frame = tk.Frame(self.current_frame, bg=self.bg_color)
        form_frame.pack(pady=20)
        
        # Username/Email
        tk.Label(
            form_frame, 
            text="Username or Email", 
            font=("Helvetica", 12), 
            fg=self.fg_color, 
            bg=self.bg_color
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.login_username = tk.Entry(
            form_frame, 
            font=("Helvetica", 12), 
            width=30, 
            bg="#16213e", 
            fg=self.fg_color, 
            insertbackground=self.fg_color
        )
        self.login_username.grid(row=1, column=0, padx=10, pady=5)
        
        # Password
        tk.Label(
            form_frame, 
            text="Password", 
            font=("Helvetica", 12), 
            fg=self.fg_color, 
            bg=self.bg_color
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.login_password = tk.Entry(
            form_frame, 
            font=("Helvetica", 12), 
            width=30, 
            show="*", 
            bg="#16213e", 
            fg=self.fg_color, 
            insertbackground=self.fg_color
        )
        self.login_password.grid(row=3, column=0, padx=10, pady=5)
        
        # Login Button
        login_btn = tk.Button(
            form_frame, 
            text="Login", 
            font=("Helvetica", 12, "bold"), 
            bg=self.accent_color, 
            fg="#000000", 
            command=self.login_user,
            width=15
        )
        login_btn.grid(row=4, column=0, pady=20)
        
        # Signup Link
        signup_label = tk.Label(
            self.current_frame, 
            text="Don't have an account? Sign up", 
            font=("Helvetica", 10), 
            fg=self.accent_color, 
            bg=self.bg_color,
            cursor="hand2"
        )
        signup_label.pack(pady=10)
        signup_label.bind("<Button-1>", lambda e: self.show_signup_frame())

    def show_signup_frame(self):
        """Display the signup frame"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Logo
        if self.logo:
            logo_label = tk.Label(self.current_frame, image=self.logo, bg=self.bg_color)
            logo_label.pack(pady=20)
        
        # Title
        title_label = tk.Label(
            self.current_frame, 
            text="Create Your Account", 
            font=("Helvetica", 20, "bold"), 
            fg=self.fg_color, 
            bg=self.bg_color
        )
        title_label.pack(pady=10)
        
        # Signup Form
        form_frame = tk.Frame(self.current_frame, bg=self.bg_color)
        form_frame.pack(pady=20)
        
        # Username
        tk.Label(
            form_frame, 
            text="Username", 
            font=("Helvetica", 12), 
            fg=self.fg_color, 
            bg=self.bg_color
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.signup_username = tk.Entry(
            form_frame, 
            font=("Helvetica", 12), 
            width=30, 
            bg="#16213e", 
            fg=self.fg_color, 
            insertbackground=self.fg_color
        )
        self.signup_username.grid(row=1, column=0, padx=10, pady=5)
        
        # Email
        tk.Label(
            form_frame, 
            text="Email", 
            font=("Helvetica", 12), 
            fg=self.fg_color, 
            bg=self.bg_color
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.signup_email = tk.Entry(
            form_frame, 
            font=("Helvetica", 12), 
            width=30, 
            bg="#16213e", 
            fg=self.fg_color, 
            insertbackground=self.fg_color
        )
        self.signup_email.grid(row=3, column=0, padx=10, pady=5)
        
        # Password
        tk.Label(
            form_frame, 
            text="Password (min 8 chars)", 
            font=("Helvetica", 12), 
            fg=self.fg_color, 
            bg=self.bg_color
        ).grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.signup_password = tk.Entry(
            form_frame, 
            font=("Helvetica", 12), 
            width=30, 
            show="*", 
            bg="#16213e", 
            fg=self.fg_color, 
            insertbackground=self.fg_color
        )
        self.signup_password.grid(row=5, column=0, padx=10, pady=5)
        
        # Confirm Password
        tk.Label(
            form_frame, 
            text="Confirm Password", 
            font=("Helvetica", 12), 
            fg=self.fg_color, 
            bg=self.bg_color
        ).grid(row=6, column=0, padx=10, pady=5, sticky="w")
        
        self.signup_confirm_password = tk.Entry(
            form_frame, 
            font=("Helvetica", 12), 
            width=30, 
            show="*", 
            bg="#16213e", 
            fg=self.fg_color, 
            insertbackground=self.fg_color
        )
        self.signup_confirm_password.grid(row=7, column=0, padx=10, pady=5)
        
        # Signup Button
        signup_btn = tk.Button(
            form_frame, 
            text="Sign Up", 
            font=("Helvetica", 12, "bold"), 
            bg=self.accent_color, 
            fg="#000000", 
            command=self.register_user,
            width=15
        )
        signup_btn.grid(row=
