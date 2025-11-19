"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: "How can I use data visualization to create an engaging brand experience for a sports magazine like SPIKES Athletics Magazine?"
Generated: DETERMINISTIC_9707349bf9be11cf
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image
from io import BytesIO
import requests

# Custom colors for SPIKES brand
SPIKES_COLORS = ['#1a1a1a', '#e31937', '#ffffff']
SPIKES_CMAP = LinearSegmentedColormap.from_list('spikes', ['#1a1a1a', '#e31937'])

def fetch_sports_data(api_url):
    """
    Fetch sports data from API
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def create_athlete_performance_chart(data, athlete_name):
    """
    Create performance trend chart for an athlete
    """
    try:
        df = pd.DataFrame(data)
        plt.figure(figsize=(12, 6))
        
        # Plot styling
        sns.set_style("white")
        plt.rcParams['axes.edgecolor'] = SPIKES_COLORS[0]
        plt.rcParams['axes.labelcolor'] = SPIKES_COLORS[0]
        
        # Create plot
        ax = sns.lineplot(
            x='date', 
            y='performance', 
            data=df,
            color=SPIKES_COLORS[1],
            linewidth=3,
            marker='o',
            markersize=10
        )
        
        # Customize plot
        plt.title(f"{athlete_name} Performance Trend", 
                 fontsize=16, 
                 fontweight='bold',
                 color=SPIKES_COLORS[0],
                 pad=20)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Performance Score", fontsize=12)
        plt.xticks(rotation=45)
        
        # Add SPIKES branding
        plt.text(0.5, 1.1, "SPIKES Athletics Magazine", 
                transform=ax.transAxes,
                ha='center',
                fontsize=14,
                color=SPIKES_COLORS[1])
        
        # Remove spines
        sns.despine()
        
        return plt
    except Exception as e:
        print(f"Error creating performance chart: {e}")
        return None

def create_team_comparison_viz(data, teams):
    """
    Create radar chart comparing multiple teams
    """
    try:
        categories = list(data[teams[0]].keys())
        N = len(categories)
        
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]
        
        plt.figure(figsize=(10, 10))
        ax = plt.subplot(111, polar=True)
        
        # Customize radar chart
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        plt.xticks(angles[:-1], categories, color=SPIKES_COLORS[0], size=12)
        ax.tick_params(axis='y', labelcolor=SPIKES_COLORS[0])
        ax.set_rlabel_position(0)
        
        # Plot each team
        for i, team in enumerate(teams):
            values = list(data[team].values())
            values += values[:1]
            ax.plot(angles, values, 
                   linewidth=2, 
                   linestyle='solid', 
                   label=team,
                   color=SPIKES_COLORS[i % len(SPIKES_COLORS)])
            ax.fill(angles, values, alpha=0.1)
        
        # Add legend and title
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        plt.title("Team Performance Comparison", 
                 color=SPIKES_COLORS[0],
                 fontsize=16,
                 fontweight='bold',
                 pad=20)
        
        # Add branding
        plt.text(0.5, 1.1, "SPIKES Athletics Magazine", 
                transform=ax.transAxes,
                ha='center',
                fontsize=14,
                color=SPIKES_COLORS[1])
        
        return plt
    except Exception as e:
        print(f"Error creating team comparison: {e}")
        return None

def create_interactive_visualization(data):
    """
    Create interactive visualization using Plotly
    """
    try:
        import plotly.express as px
        import plotly.graph_objects as go
        
        df = pd.DataFrame(data)
        
        fig = px.scatter(
            df,
            x='stat1',
            y='stat2',
            size='performance',
            color='team',
            hover_name='player',
            color_discrete_sequence=[SPIKES_COLORS[1], SPIKES_COLORS[0]],
            title="Player Performance Visualization"
        )
        
        fig.update_layout(
            title_font_color=SPIKES_COLORS[0],
            title_font_size=20,
            plot_bgcolor=SPIKES_COLORS[2],
            paper_bgcolor=SPIKES_COLORS[2],
            font_color=SPIKES_COLORS[0],
            hoverlabel=dict(
                bgcolor=SPIKES_COLORS[1],
                font_color=SPIKES_COLORS[2]
            )
        )
        
        fig.add_annotation(
            text="SPIKES Athletics Magazine",
            xref="paper",
            yref="paper",
            x=0.5,
            y=1.15,
            showarrow=False,
            font=dict(
                color=SPIKES_COLORS[1],
                size=14
            )
        )
        
        return fig
    except ImportError:
        print("Plotly not installed. Please install with 'pip install plotly'")
        return None
    except Exception as e:
        print(f"Error creating interactive visualization: {e}")
        return None

def save_visualization(plot, filename, format='png'):
    """
    Save visualization to file
    """
    try:
        if isinstance(plot, plt.Figure):
            plot.savefig(
                filename,
                format=format,
                dpi=300,
                bbox_inches='tight',
                facecolor=SPIKES_COLORS[2]
            )
        else:
            plot.write_image(filename)
        print(f"Visualization saved as {filename}")
    except Exception as e:
        print(f"Error saving visualization: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for athlete performance
    athlete_data = [
        {'date': '2023-01-01', 'performance': 85},
        {'date': '2023-02-01', 'performance': 88},
        {'date': '2023-03-01', 'performance': 92},
        {'date': '2023-04-01', 'performance': 90},
        {'date': '2023-05-01', 'performance': 95}
    ]
    
    # Create and save athlete performance chart
    athlete_chart = create_athlete_performance_chart(athlete_data, "John Doe")
    if athlete_chart:
        save_visualization(athlete_chart, "athlete_performance.png")
    
    # Sample data for team comparison
    team_data = {
        'Team A': {'Speed': 90, 'Strength': 85, 'Endurance': 80, 'Agility': 75},
        'Team B': {'Speed': 85, 'Strength': 90, 'Endurance': 75, 'Agility': 80}
    }
    
    # Create and save team comparison
    team_chart = create_team_comparison_viz(team_data, ['Team A', 'Team B'])
    if team_chart:
        save_visualization(team_chart, "team_comparison.png")
    
    # Sample data for interactive visualization
    player_data = [
        {'player': 'Player 1', 'team': 'Team A', 'stat1': 25, 'stat2': 10, 'performance': 85},
        {'player': 'Player 2', 'team': 'Team A', 'stat1': 20, 'stat2': 15, 'performance': 90},
        {'player': 'Player 3', 'team': 'Team B', 'stat1': 30, 'stat2': 5, 'performance': 80},
        {'player': 'Player 4', 'team': 'Team B', 'stat1': 15, 'stat2': 20, 'performance': 95}
    ]
    
    # Create interactive visualization
    interactive_viz = create_interactive_visualization(player_data)
    if interactive_viz:
        save_visualization(interactive_viz, "interactive_viz.html")
```
