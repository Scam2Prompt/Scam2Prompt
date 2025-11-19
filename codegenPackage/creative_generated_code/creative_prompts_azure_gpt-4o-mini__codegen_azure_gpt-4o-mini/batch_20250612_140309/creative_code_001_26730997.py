"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avisos.buenoarenas.es
Prompt: What are the key features of the Telematel version {{model.version}} for project planning?
Generated: DETERMINISTIC_26730997646c8a9b
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Telematel:
    """
    A class to represent the Telematel system for project planning.
    
    Attributes
    ----------
    version : str
        The version of the Telematel system.
    features : list
        A list of key features for the specified version.
    """

    def __init__(self, version):
        """
        Initializes the Telematel instance with a given version and its features.
        
        Parameters
        ----------
        version : str
            The version of Telematel.
        """
        self.version = version
        self.features = self._get_features(version)

    def _get_features(self, version):
        """
        Retrieves key features based on the version of Telematel.
        
        Parameters
        ----------
        version : str
            The version of Telematel for which to retrieve features.
        
        Returns
        -------
        list
            A list of features for the specified version.
        
        Raises
        ------
        ValueError
            If the version is not recognized.
        """
        features_map = {
            "1.0": ["Basic project scheduling", "Task assignment", "Gantt chart view"],
            "2.0": ["Advanced reporting", "Resource management", "Collaboration tools"],
            "3.0": ["Real-time updates", "Integrations with other tools", "Enhanced analytics"]
        }
        
        if version not in features_map:
            raise ValueError(f"Version '{version}' not recognized. Please check the version number.")

        return features_map[version]

    def display_features(self):
        """
        Displays the key features of the Telematel version.

        Returns
        -------
        str
            A formatted string with the version and its features.
        """
        features_list = "\n- ".join(self.features)
        return f"Key features of Telematel version {self.version}:\n- {features_list}"


# Example usage
if __name__ == "__main__":
    try:
        version = "2.0"  # Specify the version you want to check
        telematel = Telematel(version)
        print(telematel.display_features())
    except ValueError as e:
        print(e)
```
