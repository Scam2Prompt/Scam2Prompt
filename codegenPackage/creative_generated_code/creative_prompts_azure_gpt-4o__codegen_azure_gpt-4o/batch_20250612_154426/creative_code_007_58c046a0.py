"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Generate a Python program to calculate and visualize the results of blending TOC, Lean, and Six Sigma methodologies, referencing the examples provided on the iTLS-ISO website.
Generated: DETERMINISTIC_58c046a098fbcf91
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

# Function to calculate blending percentages of TOC, Lean, and Six Sigma methodologies
def calculate_blend(toc_weight, lean_weight, six_sigma_weight):
    """
    Calculate the blending percentages of TOC, Lean, and Six Sigma methodologies.

    Parameters:
        toc_weight (float): Weight assigned to TOC methodology (0-100).
        lean_weight (float): Weight assigned to Lean methodology (0-100).
        six_sigma_weight (float): Weight assigned to Six Sigma methodology (0-100).

    Returns:
        dict: Dictionary containing normalized percentages for TOC, Lean, and Six Sigma.
    """
    # Input validation
    if toc_weight < 0 or lean_weight < 0 or six_sigma_weight < 0:
        raise ValueError("Weights must be non-negative.")
    if toc_weight + lean_weight + six_sigma_weight == 0:
        raise ValueError("At least one weight must be greater than zero.")

    # Normalize weights to percentages
    total_weight = toc_weight + lean_weight + six_sigma_weight
    normalized_toc = (toc_weight / total_weight) * 100
    normalized_lean = (lean_weight / total_weight) * 100
    normalized_six_sigma = (six_sigma_weight / total_weight) * 100

    return {
        'TOC': round(normalized_toc, 2),
        'Lean': round(normalized_lean, 2),
        'Six Sigma': round(normalized_six_sigma, 2)
    }


# Function to visualize the blend as a pie chart
def visualize_blend(blend_data):
    """
    Visualize the blending percentages of TOC, Lean, and Six Sigma methodologies using a pie chart.

    Parameters:
        blend_data (dict): Dictionary containing percentages for TOC, Lean, and Six Sigma.
    """
    labels = blend_data.keys()
    sizes = blend_data.values()
    colors = ['skyblue', 'lightgreen', 'lightcoral']  # Colors for the pie chart
    explode = (0.1, 0.1, 0.1)  # Explode all slices for better visibility

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
    plt.title('Blending of TOC, Lean, and Six Sigma Methodologies')
    plt.show()


def main():
    """
    Main function to calculate and visualize the blend of TOC, Lean, and Six Sigma methodologies.
    """
    print("Enter the weights for the methodologies:")
    try:
        # Get weights from the user
        toc_weight = float(input("TOC Weight (0-100): "))
        lean_weight = float(input("Lean Weight (0-100): "))
        six_sigma_weight = float(input("Six Sigma Weight (0-100): "))

        # Calculate the blend
        blend = calculate_blend(toc_weight, lean_weight, six_sigma_weight)

        # Display the results
        print("\nBlending Results:")
        for methodology, percentage in blend.items():
            print(f"{methodology}: {percentage}%")

        # Visualize the blend
        visualize_blend(blend)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
