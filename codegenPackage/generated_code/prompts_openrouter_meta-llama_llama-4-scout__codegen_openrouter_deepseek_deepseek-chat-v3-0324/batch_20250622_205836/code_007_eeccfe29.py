"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ie.pages.dev
Prompt: Design a simple data visualization to display WienerAI's token supply, including the 30% allocated for presale, 20% for staking, and other distributions.
Generated: DETERMINISTIC_eeccfe2953a841d1
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

# Data for WienerAI token distribution
labels = ['Presale (30%)', 'Staking (20%)', 'Development (15%)', 
          'Marketing (15%)', 'Team (10%)', 'Reserves (10%)']
sizes = [30, 20, 15, 15, 10, 10]
colors = ['#FFD700', '#32CD32', '#1E90FF', '#FF6347', '#9370DB', '#20B2AA']
explode = (0.1, 0, 0, 0, 0, 0)  # Emphasize presale

def plot_token_distribution():
    """Visualize WienerAI token distribution with a pie chart."""
    try:
        plt.figure(figsize=(10, 7))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('WienerAI Token Supply Distribution', fontsize=16, pad=20)
        plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
        
        # Add legend
        plt.legend(labels, title="Allocation", loc="center left", 
                  bbox_to_anchor=(1, 0.5))
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error generating visualization: {e}")

if __name__ == "__main__":
    plot_token_distribution()
```
