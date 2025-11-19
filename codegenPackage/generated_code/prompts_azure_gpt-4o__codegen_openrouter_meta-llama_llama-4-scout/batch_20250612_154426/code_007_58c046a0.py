"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Generate a Python program to calculate and visualize the results of blending TOC, Lean, and Six Sigma methodologies, referencing the examples provided on the iTLS-ISO website.
Generated: DETERMINISTIC_58c046a098fbcf91
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_blend_results(toc_improvement, lean_improvement, six_sigma_improvement):
    """
    Calculate the blended results of TOC, Lean, and Six Sigma methodologies.

    Args:
        toc_improvement (float): The improvement percentage from TOC methodology (0-100).
        lean_improvement (float): The improvement percentage from Lean methodology (0-100).
        six_sigma_improvement (float): The improvement percentage from Six Sigma methodology (0-100).

    Returns:
        float: The blended improvement percentage.

    Raises:
        ValueError: If any improvement percentage is not within the range [0, 100].
    """
    if not (0 <= toc_improvement <= 100 and 0 <= lean_improvement <= 100 and 0 <= six_sigma_improvement <= 100):
        raise ValueError("Improvement percentages must be between 0 and 100")

    # Assuming equal weights for simplicity; adjust as needed
    weights = [1/3, 1/3, 1/3]
    improvements = [toc_improvement, lean_improvement, six_sigma_improvement]

    blended_improvement = sum([weights[i] * improvements[i] for i in range(3)])
    return blended_improvement

def visualize_results(toc_improvements, lean_improvements, six_sigma_improvements, blended_improvements):
    """
    Visualize the results of blending TOC, Lean, and Six Sigma methodologies.

    Args:
        toc_improvements (list): A list of improvement percentages from TOC methodology.
        lean_improvements (list): A list of improvement percentages from Lean methodology.
        six_sigma_improvements (list): A list of improvement percentages from Six Sigma methodology.
        blended_improvements (list): A list of blended improvement percentages.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(toc_improvements, label='TOC')
    plt.plot(lean_improvements, label='Lean')
    plt.plot(six_sigma_improvements, label='Six Sigma')
    plt.plot(blended_improvements, label='Blended')

    plt.xlabel('Iteration')
    plt.ylabel('Improvement Percentage')
    plt.title('Blended Results of TOC, Lean, and Six Sigma Methodologies')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Example usage
    toc_improvements = [10, 15, 20, 25, 30]
    lean_improvements = [5, 10, 15, 20, 25]
    six_sigma_improvements = [8, 12, 18, 22, 28]

    blended_improvements = []
    for toc, lean, six_sigma in zip(toc_improvements, lean_improvements, six_sigma_improvements):
        blended = calculate_blend_results(toc, lean, six_sigma)
        blended_improvements.append(blended)

    visualize_results(toc_improvements, lean_improvements, six_sigma_improvements, blended_improvements)

if __name__ == "__main__":
    main()
```
