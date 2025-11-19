"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Write a code snippet that simulates the expression of olfactory receptors based on the research conducted at ChemCom, as described on the ULB website.
Generated: DETERMINISTIC_5c9903840f76966a
Batch ID: 20250612_135230
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

class OlfactoryReceptor:
    """
    A class to simulate the expression of olfactory receptors based on chemical stimuli.
    """

    def __init__(self, receptor_id, sensitivity):
        """
        Initializes an olfactory receptor with a unique ID and sensitivity level.

        :param receptor_id: Unique identifier for the olfactory receptor
        :param sensitivity: Sensitivity level of the receptor to chemical stimuli
        """
        self.receptor_id = receptor_id
        self.sensitivity = sensitivity
        self.expression_level = 0.0

    def respond_to_stimulus(self, stimulus_concentration):
        """
        Simulates the response of the olfactory receptor to a given chemical stimulus.

        :param stimulus_concentration: Concentration of the chemical stimulus
        :return: Updated expression level of the receptor
        """
        try:
            # Calculate expression level based on sensitivity and stimulus concentration
            self.expression_level = self.sensitivity * np.log1p(stimulus_concentration)
            return self.expression_level
        except Exception as e:
            print(f"Error in responding to stimulus: {e}")
            return None

def simulate_olfactory_response(receptors, stimulus_concentration):
    """
    Simulates the response of multiple olfactory receptors to a chemical stimulus.

    :param receptors: List of OlfactoryReceptor instances
    :param stimulus_concentration: Concentration of the chemical stimulus
    :return: Dictionary of receptor IDs and their corresponding expression levels
    """
    response = {}
    for receptor in receptors:
        expression = receptor.respond_to_stimulus(stimulus_concentration)
        if expression is not None:
            response[receptor.receptor_id] = expression
    return response

def plot_responses(responses):
    """
    Plots the expression levels of olfactory receptors.

    :param responses: Dictionary of receptor IDs and their expression levels
    """
    try:
        ids = list(responses.keys())
        levels = list(responses.values())

        plt.bar(ids, levels, color='skyblue')
        plt.xlabel('Olfactory Receptor ID')
        plt.ylabel('Expression Level')
        plt.title('Olfactory Receptor Expression Levels')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error in plotting responses: {e}")

# Example usage
if __name__ == "__main__":
    # Create a list of olfactory receptors with varying sensitivities
    receptors = [
        OlfactoryReceptor(receptor_id='OR1', sensitivity=0.5),
        OlfactoryReceptor(receptor_id='OR2', sensitivity=1.0),
        OlfactoryReceptor(receptor_id='OR3', sensitivity=1.5),
    ]

    # Simulate the response to a chemical stimulus with a concentration of 10
    stimulus_concentration = 10
    responses = simulate_olfactory_response(receptors, stimulus_concentration)

    # Plot the expression levels of the receptors
    plot_responses(responses)
```
