"""
Generated Code Metadata:
========================
Original URL: https://mintsolutions.io
Prompt: Create a customer journey map (CJM) for a new product launch, including research, product development, and testing, and provide recommendations for improvement.
Generated: DETERMINISTIC_d4fb607d51656edd
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

class CustomerJourneyMap:
    def __init__(self, stages, touchpoints, customer_experience):
        """
        Initializes the Customer Journey Map with stages, touchpoints, and customer experience ratings.

        :param stages: List of stages in the customer journey
        :param touchpoints: List of touchpoints corresponding to each stage
        :param customer_experience: List of customer experience ratings (0-10) for each stage
        """
        self.stages = stages
        self.touchpoints = touchpoints
        self.customer_experience = customer_experience

    def plot_journey_map(self):
        """
        Plots the customer journey map using matplotlib.
        """
        try:
            # Validate input lengths
            if not (len(self.stages) == len(self.touchpoints) == len(self.customer_experience)):
                raise ValueError("All input lists must have the same length.")

            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(10, 6))

            # Create a line plot for customer experience
            ax.plot(self.stages, self.customer_experience, marker='o', linestyle='-', color='b', label='Customer Experience')

            # Annotate touchpoints
            for i, txt in enumerate(self.touchpoints):
                ax.annotate(txt, (self.stages[i], self.customer_experience[i]), textcoords="offset points", xytext=(0,10), ha='center')

            # Set labels and title
            ax.set_xlabel('Customer Journey Stages')
            ax.set_ylabel('Customer Experience Rating (0-10)')
            ax.set_title('Customer Journey Map for New Product Launch')
            ax.set_ylim(0, 10)
            ax.axhline(y=5, color='r', linestyle='--', label='Average Experience Threshold')
            ax.legend()

            # Show the plot
            plt.grid()
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"An error occurred while plotting the journey map: {e}")

    def recommendations(self):
        """
        Provides recommendations for improving customer experience based on the journey map.

        :return: List of recommendations
        """
        recommendations = []
        avg_experience = np.mean(self.customer_experience)

        if avg_experience < 5:
            recommendations.append("Focus on improving customer experience in all stages.")
        elif avg_experience < 7:
            recommendations.append("Identify specific stages with low ratings and enhance those touchpoints.")
        else:
            recommendations.append("Maintain high standards and continue to gather customer feedback.")

        return recommendations


# Example usage
if __name__ == "__main__":
    # Define the stages, touchpoints, and customer experience ratings
    stages = ['Research', 'Product Development', 'Testing', 'Launch']
    touchpoints = ['Surveys', 'Prototypes', 'Beta Testing', 'Marketing Campaign']
    customer_experience = [6, 7, 4, 8]

    # Create a Customer Journey Map instance
    cjm = CustomerJourneyMap(stages, touchpoints, customer_experience)

    # Plot the journey map
    cjm.plot_journey_map()

    # Get recommendations for improvement
    improvement_recommendations = cjm.recommendations()
    print("Recommendations for Improvement:")
    for recommendation in improvement_recommendations:
        print(f"- {recommendation}")
```
