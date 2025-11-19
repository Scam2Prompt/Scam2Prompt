"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: How can I create a user-friendly interface for a text counselling service that accommodates individuals who prefer writing over speaking, similar to the model used by Text Counselling Online?
Generated: DETERMINISTIC_d7c38ae358a4e6b0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import datetime
import json
import os

class TextCounsellingApp:
    def __init__(self, root):
        """
        Initialize the main application window and components.
        """
        self.root = root
        self.root.title("Text Counselling Service")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        
        # Create main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Initialize session data
        self.session_active = False
        self.messages = []
        self.current_counsellor = None
        
        # Create UI components
        self.create_welcome_screen()
        self.create_chat_interface()
        
        # Hide chat interface initially
        self.chat_frame.pack_forget()
    
    def create_welcome_screen(self):
        """
        Create the welcome screen with options to start a session.
        """
        self.welcome_frame = ttk.Frame(self.main_frame)
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome label
        welcome_label = ttk.Label(
            self.welcome_frame,
            text="Welcome to Text Counselling Service",
            font=('Arial', 16, 'bold')
        )
        welcome_label.pack(pady=20)
        
        # Description
        desc_label = ttk.Label(
            self.welcome_frame,
            text="A safe space to express yourself through text. "
                 "Connect with a professional counsellor who will listen and support you.",
            wraplength=600,
            justify=tk.CENTER
        )
        desc_label.pack(pady=10, padx=20)
        
        # Counsellor selection
        counsellor_frame = ttk.Frame(self.welcome_frame)
        counsellor_frame.pack(pady=20)
        
        ttk.Label(counsellor_frame, text="Select Counsellor:").pack(side=tk.LEFT, padx=5)
        
        self.counsellor_var = tk.StringVar()
        self.counsellor_dropdown = ttk.Combobox(
            counsellor_frame,
            textvariable=self.counsellor_var,
            values=["Sarah (General Anxiety)", "James (Relationship Issues)", "Priya (Depression)"],
            state="readonly",
            width=30
        )
        self.counsellor_dropdown.pack(side=tk.LEFT, padx=5)
        self.counsellor_dropdown.current(0)
        
        # Start session button
        start_button = ttk.Button(
            self.welcome_frame,
            text="Start Counselling Session",
            command=self.start_session
        )
        start_button.pack(pady=20)
        
        # Privacy notice
        privacy_label = ttk.Label(
            self.welcome_frame,
            text="All conversations are confidential. Your privacy is important to us.",
            font=('Arial', 8),
            foreground='gray'
        )
        privacy_label.pack(side=tk.BOTTOM, pady=10)
    
    def create_chat_interface(self):
        """
        Create the chat interface for the counselling session.
        """
        self.chat_frame = ttk.Frame(self.main_frame)
        
        # Chat history display
        self.chat_history = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=70,
            height=20,
            font=('Arial', 10),
            state='disabled'
        )
        self.chat_history.pack(pady=10, padx=5, fill=tk.BOTH, expand=True)
        
        # Message input
        input_frame = ttk.Frame(self.chat_frame)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.message_entry = tk.Text(
            input_frame,
            height=4,
            wrap=tk.WORD,
            font=('Arial', 10)
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        send_button = ttk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            width=8
        )
        send_button.pack(side=tk.RIGHT)
        
        # Session controls
        control_frame = ttk.Frame(self.chat_frame)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        end_button = ttk.Button(
            control_frame,
            text="End Session",
            command=self.end_session,
            style='Danger.TButton'
        )
        end_button.pack(side=tk.RIGHT, padx=5)
        
        # Configure danger style for end button
        self.style.configure('Danger.TButton', foreground='white', background='#dc3545')
    
    def start_session(self):
        """
        Start a new counselling session.
        """
        self.current_counsellor = self.counsellor_var.get()
        if not self.current_counsellor:
            messagebox.showerror("Error", "Please select a counsellor")
            return
        
        self.session_active = True
        self.messages = []
        
        # Hide welcome screen and show chat interface
        self.welcome_frame.pack_forget()
        self.chat_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add welcome message
        welcome_msg = f"Connected with {self.current_counsellor}. You can start typing your message below."
        self.add_message("System", welcome_msg)
        
        # Focus on message entry
        self.message_entry.focus_set()
    
    def end_session(self):
        """
        End the current counselling session.
        """
        if not self.session_active:
            return
            
        # Confirm with user
        if not messagebox.askyesno("End Session", "Are you sure you want to end this counselling session?"):
            return
        
        # Save session transcript
        self.save_session_transcript()
        
        # Reset session
        self.session_active = False
        self.current_counsellor = None
        
        # Clear chat history
        self.chat_history.config(state='normal')
        self.chat_history.delete(1.0, tk.END)
        self.chat_history.config(state='disabled')
        
        # Show welcome screen
        self.chat_frame.pack_forget()
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)
    
    def send_message(self):
        """
        Send a message from the user to the counsellor.
        """
        if not self.session_active:
            messagebox.showerror("Error", "No active session")
            return
            
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            return
            
        # Add user message to chat
        self.add_message("You", message)
        self.message_entry.delete("1.0", tk.END)
        
        # Simulate counsellor response (in a real app, this would be handled by the counsellor)
        self.root.after(1500, self.simulate_counsellor_response, message)
    
    def simulate_counsellor_response(self, user_message):
        """
        Simulate a counsellor response (for demo purposes).
        """
        if not self.session_active:
            return
            
        # Simple response logic for demo
        if "anxious" in user_message.lower():
            response = "I hear that you're feeling anxious. Can you tell me more about what's causing this feeling?"
        elif "sad" in user_message.lower() or "depressed" in user_message.lower():
            response = "I'm sorry to hear you're feeling this way. How long have you been feeling sad?"
        elif "?" in user_message:
            response = "That's an important question. Let's explore that together."
        else:
            response = "Thank you for sharing that with me. How does that make you feel?"
        
        self.add_message(self.current_counsellor, response)
    
    def add_message(self, sender, message):
        """
        Add a message to the chat history.
        """
        timestamp = datetime.datetime.now().strftime("%H:%M")
        formatted_message = f"[{timestamp}] {sender}: {message}\n\n"
        
        self.messages.append((sender, message, timestamp))
        
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, formatted_message)
        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END)
    
    def save_session_transcript(self):
        """
        Save the session transcript to a JSON file.
        """
        if not self.messages:
            return
            
        transcript = {
            "counsellor": self
