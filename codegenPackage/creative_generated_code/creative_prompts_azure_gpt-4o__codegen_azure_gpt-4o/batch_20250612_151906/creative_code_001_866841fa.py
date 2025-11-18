"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Recommend an API or library to visualize a 16-week half marathon training plan with long runs, interval runs, tempo runs, and recovery runs, based on Boost Running's framework.
Generated: DETERMINISTIC_866841fa1980f121
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the `matplotlib` library to visualize a 16-week half marathon training plan. The visualization is displayed as a bar chart where each type of run is color-coded.

```python
import matplotlib.pyplot as plt
import numpy as np

def create_training_plan():
    """
    Generate a 16-week half marathon training plan based on Boost Running's framework.
    Returns:
        training_plan: A dictionary containing weekly training data with run types.
    """
    training_plan = {
        "Week 1": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 2": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 3": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 4": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 5": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 6": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 7": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 8": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 9": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 10": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 11": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 12": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 13": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 14": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 15": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
        "Week 16": ["Recovery", "Interval", "Tempo", "Recovery", "Long"],
    }
    return training_plan

def visualize_training_plan(training_plan):
    """
    Visualize a half marathon training plan using a bar chart.
    Args:
        training_plan: A dictionary containing weekly training data with run types.
    """
    # Define run types and assign colors
    run_types = {"Recovery": "blue", "Interval": "red", "Tempo": "green", "Long": "orange"}
    
    # Prepare data for visualization
    weeks = list(training_plan.keys())
    run_sequences = list(training_plan.values())
    color_map = [[run_types[run] for run in week_runs] for week_runs in run_sequences]
    
    week_positions = np.arange(len(weeks))
    bar_width = 0.8
    
    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, week in enumerate(weeks):
        bottom = 0
        for j, run_type in enumerate(training_plan[week]):
            ax.bar(week_positions[i], 1, bar_width, color=color_map[i][j], bottom=bottom, label=run_type if i == 0 else "")
            bottom += 1

    # Set chart labels and title
    ax.set_title("16-Week Half Marathon Training Plan", fontsize=16)
    ax.set_xticks(week_positions)
    ax.set_xticklabels(weeks, rotation=45, fontsize=10)
    ax.set_ylabel("Run Types", fontsize=12)
    ax.set_xlabel("Weeks", fontsize=12)
    
    # Create a legend with unique colors
    handles, labels = ax.get_legend_handles_labels()
    unique_handles = dict(zip(labels, handles))
    ax.legend(unique_handles.values(), unique_handles.keys(), loc="upper right", fontsize=10)
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to create and visualize the training plan.
    """
    try:
        # Generate training plan
        training_plan = create_training_plan()
        
        # Visualize training plan
        visualize_training_plan(training_plan)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### How to Run:
1. Install `matplotlib` if not already installed: `pip install matplotlib`.
2. Save the script to a file (e.g., `training_plan_visualizer.py`) and run it (`python training_plan_visualizer.py`).
3. The script will display a bar chart showing the training plan with color-coded run types.
