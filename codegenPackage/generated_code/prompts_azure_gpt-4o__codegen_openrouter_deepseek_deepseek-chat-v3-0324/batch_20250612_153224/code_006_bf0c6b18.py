"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Develop a sample user interface for an enterprise software system that aligns with MetaCode's focus on simplicity and usability.
Generated: DETERMINISTIC_bf0c6b1861b73443
Batch ID: 20250612_153224
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

class EnterpriseAppUI:
    """Main application window for enterprise software system."""
    
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("MetaCode Enterprise System")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self._configure_styles()
        
        # Create main containers
        self._create_header()
        self._create_main_content()
        self._create_footer()
        
        # Bind window events
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _configure_styles(self):
        """Configure custom styles for widgets."""
        self.style.configure('TFrame', background='#f5f5f5')
        self.style.configure('Header.TFrame', background='#2c3e50')
        self.style.configure('Footer.TFrame', background='#2c3e50')
        self.style.configure('Header.TLabel', 
                           background='#2c3e50', 
                           foreground='white',
                           font=('Helvetica', 14, 'bold'))
        self.style.configure('Footer.TLabel', 
                           background='#2c3e50', 
                           foreground='white',
                           font=('Helvetica', 10))
        self.style.configure('TButton', 
                           font=('Helvetica', 10),
                           padding=5)
        self.style.configure('Primary.TButton', 
                           background='#3498db',
                           foreground='white')
        self.style.configure('Secondary.TButton', 
                           background='#95a5a6',
                           foreground='white')
        self.style.configure('TNotebook', background='#f5f5f5')
        self.style.configure('TNotebook.Tab', 
                           padding=[10, 5],
                           font=('Helvetica', 10))
    
    def _create_header(self):
        """Create the header section of the application."""
        self.header = ttk.Frame(self.root, style='Header.TFrame')
        self.header.pack(fill=tk.X, padx=5, pady=5)
        
        # Logo and title
        self.logo_label = ttk.Label(
            self.header, 
            text="MetaCode Enterprise", 
            style='Header.TLabel'
        )
        self.logo_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # User controls
        self.user_frame = ttk.Frame(self.header, style='Header.TFrame')
        self.user_frame.pack(side=tk.RIGHT, padx=10, pady=5)
        
        self.user_label = ttk.Label(
            self.user_frame, 
            text="Welcome, Admin", 
            style='Header.TLabel'
        )
        self.user_label.pack(side=tk.LEFT, padx=5)
        
        self.logout_btn = ttk.Button(
            self.user_frame, 
            text="Logout", 
            style='Secondary.TButton',
            command=self._logout
        )
        self.logout_btn.pack(side=tk.LEFT, padx=5)
    
    def _create_main_content(self):
        """Create the main content area with tabs."""
        self.main_content = ttk.Frame(self.root)
        self.main_content.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.main_content)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self._create_dashboard_tab()
        self._create_users_tab()
        self._create_reports_tab()
        self._create_settings_tab()
    
    def _create_dashboard_tab(self):
        """Create the dashboard tab."""
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.dashboard_tab, text="Dashboard")
        
        # Dashboard content
        self.dashboard_frame = ttk.Frame(self.dashboard_tab)
        self.dashboard_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Summary cards
        self._create_summary_cards()
        
        # Recent activity
        self._create_recent_activity()
    
    def _create_summary_cards(self):
        """Create summary cards for dashboard."""
        card_frame = ttk.Frame(self.dashboard_frame)
        card_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Card 1: Users
        self.users_card = ttk.Frame(card_frame, style='TFrame')
        self.users_card.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        self._create_card(self.users_card, "Users", "1,024", "#3498db")
        
        # Card 2: Projects
        self.projects_card = ttk.Frame(card_frame, style='TFrame')
        self.projects_card.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        self._create_card(self.projects_card, "Projects", "42", "#2ecc71")
        
        # Card 3: Tasks
        self.tasks_card = ttk.Frame(card_frame, style='TFrame')
        self.tasks_card.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        self._create_card(self.tasks_card, "Tasks", "1,256", "#e74c3c")
        
        # Card 4: Alerts
        self.alerts_card = ttk.Frame(card_frame, style='TFrame')
        self.alerts_card.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        self._create_card(self.alerts_card, "Alerts", "3", "#f39c12")
    
    def _create_card(self, parent, title, value, color):
        """Helper method to create a summary card."""
        card = ttk.Frame(parent, style='TFrame', borderwidth=1, relief=tk.RAISED)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            card, 
            text=title, 
            font=('Helvetica', 12, 'bold'),
            background='white'
        )
        title_label.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        # Value
        value_label = ttk.Label(
            card, 
            text=value, 
            font=('Helvetica', 24, 'bold'),
            foreground=color,
            background='white'
        )
        value_label.pack(fill=tk.X, padx=10, pady=(0, 10))
    
    def _create_recent_activity(self):
        """Create recent activity section."""
        activity_frame = ttk.Frame(self.dashboard_frame)
        activity_frame.pack(fill=tk.BOTH, expand=True)
        
        # Section title
        ttk.Label(
            activity_frame, 
            text="Recent Activity", 
            font=('Helvetica', 12, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        # Activity list (simplified)
        self.activity_tree = ttk.Treeview(
            activity_frame,
            columns=('timestamp', 'user', 'action'),
            show='headings',
            height=8
        )
        
        self.activity_tree.heading('timestamp', text='Timestamp')
        self.activity_tree.heading('user', text='User')
        self.activity_tree.heading('action', text='Action')
        
        self.activity_tree.column('timestamp', width=200)
        self.activity_tree.column('user', width=150)
        self.activity_tree.column('action', width=500)
        
        self.activity_tree.pack(fill=tk.BOTH, expand=True)
        
        # Add sample data
        sample_data = [
            ("2023-11-15 09:30:22", "admin", "Created new project 'Q4 Initiative'"),
            ("2023-11-15 08:45:10", "jdoe", "Completed task 'Update documentation'"),
            ("2023-11-14 16:20:33", "asmith", "Assigned task to jdoe"),
            ("2023-11-14 14:15:07", "admin", "Updated system settings"),
            ("2023-11-14 10:05:41", "bjohnson", "Uploaded new files to project")
        ]
        
        for item in sample_data:
            self.activity_tree.insert('', tk.END, values=item)
    
    def _create_users_tab(self):
        """Create the users management tab."""
        self.users_tab = ttk.Frame(self.not
