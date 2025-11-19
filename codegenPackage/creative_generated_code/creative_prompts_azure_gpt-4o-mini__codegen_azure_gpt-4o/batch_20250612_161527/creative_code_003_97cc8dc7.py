"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: What programming languages should I use to develop a project similar to those listed on MarcelDev's portfolio?
Generated: DETERMINISTIC_97cc8dc7f0d12790
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides recommendations for programming languages and frameworks 
based on project types inspired by MarcelDev's portfolio. Developers can use this 
code as a guide for selecting technology stacks for similar projects.

Author: MarcelDevFan
Date Created: YYYY-MM-DD
"""

# Function to recommend programming languages based on project type
def recommend_languages(project_type):
    """
    Recommend programming languages and frameworks based on the type of project.

    Parameters:
    project_type (str): The type of project (e.g., "web", "mobile", "desktop", "data-science", "game")

    Returns:
    list: A list of recommended programming languages and frameworks for the given project type
    """
    recommendations = {
        "web": ["JavaScript (React, Angular, Vue)", "Python (Django, Flask)", "Ruby (Ruby on Rails)", "PHP (Laravel)", "Go (Gin, Echo)"],
        "mobile": ["Kotlin (Android)", "Swift (iOS)", "React Native", "Flutter (Dart)", "Java (Android)"],
        "desktop": ["C# (.NET)", "Java (JavaFX, Swing)", "Python (PyQt, Tkinter)", "C++ (Qt, wxWidgets)", "Electron (JavaScript)"],
        "data-science": ["Python (NumPy, Pandas, TensorFlow, PyTorch)", "R", "Julia", "MATLAB", "Scala (Apache Spark)"],
        "game": ["C++ (Unreal Engine)", "C# (Unity)", "Python (Pygame)", "JavaScript (Three.js)", "Godot (GDScript)"]
    }
    
    # Error handling: Check if the project type is valid
    if project_type.lower() not in recommendations:
        raise ValueError(f"Invalid project type '{project_type}'. Valid types are: {', '.join(recommendations.keys())}")
    
    return recommendations[project_type.lower()]

# Main function to interact with the user
if __name__ == "__main__":
    try:
        print("Welcome to the Programming Language Recommendation Tool!")
        print("Project types to choose from: web, mobile, desktop, data-science, game")
        
        # Ask user for the project type
        project_type = input("Enter the type of project you're working on: ").strip().lower()
        
        # Get recommendations for the given project type
        recommendations = recommend_languages(project_type)
        
        print(f"\nRecommended programming languages and frameworks for a '{project_type}' project:")
        for recommendation in recommendations:
            print(f"- {recommendation}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
