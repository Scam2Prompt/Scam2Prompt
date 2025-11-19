"""
Generated Code Metadata:
========================
Original URL: https://buff163z.com
Prompt: Generate Python code for a UI that simulates interdisciplinary team collaboration, inspired by LingoExplor's focus on diversity and collaborative projects.
Generated: DETERMINISTIC_e271ca5eb2db805b
Batch ID: 20250612_150657
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
import random
import json
from typing import List, Dict, Optional

class TeamMember:
    """Represents a team member with their attributes."""
    def __init__(self, name: str, discipline: str, skills: List[str]):
        self.name = name
        self.discipline = discipline
        self.skills = skills

    def to_dict(self) -> Dict:
        """Convert TeamMember object to dictionary."""
        return {
            "name": self.name,
            "discipline": self.discipline,
            "skills": self.skills
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TeamMember':
        """Create TeamMember from dictionary."""
        return cls(
            name=data["name"],
            discipline=data["discipline"],
            skills=data["skills"]
        )

class Project:
    """Represents a collaborative project."""
    def __init__(self, name: str, description: str, required_skills: List[str]):
        self.name = name
        self.description = description
        self.required_skills = required_skills
        self.team: List[TeamMember] = []

    def add_member(self, member: TeamMember) -> None:
        """Add a member to the project team."""
        self.team.append(member)

    def remove_member(self, member_name: str) -> bool:
        """Remove a member from the project team."""
        for i, member in enumerate(self.team):
            if member.name == member_name:
                self.team.pop(i)
                return True
        return False

    def get_team_composition(self) -> Dict[str, int]:
        """Get count of members per discipline."""
        composition = {}
        for member in self.team:
            composition[member.discipline] = composition.get(member.discipline, 0) + 1
        return composition

    def to_dict(self) -> Dict:
        """Convert Project object to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "required_skills": self.required_skills,
            "team": [member.to_dict() for member in self.team]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create Project from dictionary."""
        project = cls(
            name=data["name"],
            description=data["description"],
            required_skills=data["required_skills"]
        )
        for member_data in data["team"]:
            project.add_member(TeamMember.from_dict(member_data))
        return project

class CollaborationSimulatorUI:
    """Main UI class for the collaboration simulator."""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Interdisciplinary Team Collaboration Simulator")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        # Data storage
        self.team_members: List[TeamMember] = []
        self.projects: List[Project] = []
        self.current_project: Optional[Project] = None

        # Load sample data
        self._load_sample_data()

        # Configure styles
        self._configure_styles()

        # Create UI elements
        self._create_widgets()

    def _configure_styles(self) -> None:
        """Configure ttk styles."""
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10))
        style.configure("Header.TLabel", font=("Arial", 12, "bold"))
        style.configure("Success.TLabel", foreground="green")
        style.configure("Warning.TLabel", foreground="orange")
        style.configure("Error.TLabel", foreground="red")

    def _load_sample_data(self) -> None:
        """Load sample team members and projects."""
        disciplines = ["Linguistics", "Computer Science", "Psychology", "Anthropology", "Education"]
        skills = ["Research", "Programming", "Data Analysis", "UI Design", "Teaching", "Writing"]

        # Create sample team members
        for i in range(1, 11):
            discipline = random.choice(disciplines)
            member_skills = random.sample(skills, random.randint(2, 4))
            self.team_members.append(
                TeamMember(f"Member {i}", discipline, member_skills)
            )

        # Create sample projects
        project_names = [
            "Language Learning App",
            "Cross-Cultural Study",
            "Educational Platform",
            "AI Translation Tool"
        ]
        for name in project_names:
            required_skills = random.sample(skills, random.randint(3, 5))
            self.projects.append(
                Project(name, f"Description for {name}", required_skills)
            )

    def _create_widgets(self) -> None:
        """Create and arrange all UI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left panel - Team and Project selection
        left_panel = ttk.Frame(main_frame, padding="10", width=300)
        left_panel.pack(side=tk.LEFT, fill=tk.Y)

        # Team members section
        ttk.Label(left_panel, text="Team Members", style="Header.TLabel").pack(anchor=tk.W)
        self.team_members_listbox = tk.Listbox(left_panel, height=10, selectmode=tk.SINGLE)
        self.team_members_listbox.pack(fill=tk.X, pady=5)
        self._update_team_members_list()

        # Projects section
        ttk.Label(left_panel, text="Projects", style="Header.TLabel").pack(anchor=tk.W, pady=(10, 0))
        self.projects_combobox = ttk.Combobox(left_panel, state="readonly")
        self.projects_combobox.pack(fill=tk.X, pady=5)
        self.projects_combobox.bind("<<ComboboxSelected>>", self._on_project_select)
        self._update_projects_combobox()

        # Project info section
        self.project_info_frame = ttk.Frame(left_panel)
        self.project_info_frame.pack(fill=tk.X, pady=10)
        self._update_project_info()

        # Right panel - Team composition and controls
        right_panel = ttk.Frame(main_frame, padding="10")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Current team section
        ttk.Label(right_panel, text="Current Team", style="Header.TLabel").pack(anchor=tk.W)
        self.current_team_listbox = tk.Listbox(right_panel, height=10)
        self.current_team_listbox.pack(fill=tk.BOTH, expand=True, pady=5)

        # Team composition visualization
        ttk.Label(right_panel, text="Team Composition", style="Header.TLabel").pack(anchor=tk.W, pady=(10, 0))
        self.composition_canvas = tk.Canvas(right_panel, height=150, bg="white")
        self.composition_canvas.pack(fill=tk.X, pady=5)

        # Controls section
        controls_frame = ttk.Frame(right_panel)
        controls_frame.pack(fill=tk.X, pady=10)

        add_button = ttk.Button(controls_frame, text="Add to Team", command=self._add_to_team)
        add_button.pack(side=tk.LEFT, padx=5)

        remove_button = ttk.Button(controls_frame, text="Remove from Team", command=self._remove_from_team)
        remove_button.pack(side=tk.LEFT, padx=5)

        analyze_button = ttk.Button(controls_frame, text="Analyze Team", command=self._analyze_team)
        analyze_button.pack(side=tk.RIGHT, padx=5)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def _update_team_members_list(self) -> None:
        """Update the list of available team members."""
        self.team_members_listbox.delete(0, tk.END)
        for member in self.team_members:
            self.team_members_listbox.insert(tk.END, f"{member.name} ({member.discipline})")

    def _update_projects_combobox(self) -> None:
        """Update the projects combobox."""
        project_names = [project.name for project in self.projects]
        self.projects_combobox["values"] = project_names
        if project_names:
            self.projects_combobox.current(0)
            self._on_project
