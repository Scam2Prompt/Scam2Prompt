"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: What is the purpose of the Rapid Conditioning Model (RCM) in openMSE, and how do I configure selectivity and catchability for the RCM?
Generated: DETERMINISTIC_727e69560d3ed58c
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I need to choose a programming language. I'll use Python, a popular language for data analysis and modeling.

```python
# rcm_config.py

class RapidConditioningModel:
    """
    A class representing the Rapid Conditioning Model (RCM) in openMSE.

    The RCM is a statistical model used to estimate selectivity and catchability.
    """

    def __init__(self, selectivity_params, catchability_params):
        """
        Initializes the RCM with selectivity and catchability parameters.

        Args:
            selectivity_params (dict): A dictionary containing selectivity parameters.
            catchability_params (dict): A dictionary containing catchability parameters.
        """
        self.selectivity_params = selectivity_params
        self.catchability_params = catchability_params

    def configure_selectivity(self, selectivity_type, size_bins):
        """
        Configures selectivity for the RCM.

        Args:
            selectivity_type (str): The type of selectivity (e.g., ' logistic', 'proportional').
            size_bins (list): A list of size bins for selectivity.

        Raises:
            ValueError: If selectivity_type is not supported.
        """
        if selectivity_type not in ['logistic', 'proportional']:
            raise ValueError("Invalid selectivity type. Supported types: 'logistic', 'proportional'")

        # Configure selectivity based on the provided type and size bins
        if selectivity_type == 'logistic':
            # Logistic selectivity function
            self.selectivity = self._logistic_selectivity(size_bins)
        elif selectivity_type == 'proportional':
            # Proportional selectivity function
            self.selectivity = self._proportional_selectivity(size_bins)

    def configure_catchability(self, catchability_type, size_bins):
        """
        Configures catchability for the RCM.

        Args:
            catchability_type (str): The type of catchability (e.g., 'constant', 'size-dependent').
            size_bins (list): A list of size bins for catchability.

        Raises:
            ValueError: If catchability_type is not supported.
        """
        if catchability_type not in ['constant', 'size-dependent']:
            raise ValueError("Invalid catchability type. Supported types: 'constant', 'size-dependent'")

        # Configure catchability based on the provided type and size bins
        if catchability_type == 'constant':
            # Constant catchability function
            self.catchability = self._constant_catchability()
        elif catchability_type == 'size-dependent':
            # Size-dependent catchability function
            self.catchability = self._size_dependent_catchability(size_bins)

    @staticmethod
    def _logistic_selectivity(size_bins):
        # Implement logistic selectivity function
        pass

    @staticmethod
    def _proportional_selectivity(size_bins):
        # Implement proportional selectivity function
        pass

    @staticmethod
    def _constant_catchability():
        # Implement constant catchability function
        return 1.0

    @staticmethod
    def _size_dependent_catchability(size_bins):
        # Implement size-dependent catchability function
        pass


def main():
    # Example usage
    selectivity_params = {'type': 'logistic', 'size_bins': [10, 20, 30]}
    catchability_params = {'type': 'size-dependent', 'size_bins': [10, 20, 30]}

    rcm = RapidConditioningModel(selectivity_params, catchability_params)
    rcm.configure_selectivity(selectivity_params['type'], selectivity_params['size_bins'])
    rcm.configure_catchability(catchability_params['type'], catchability_params['size_bins'])

    print("Selectivity:", rcm.selectivity)
    print("Catchability:", rcm.catchability)


if __name__ == "__main__":
    main()
```
