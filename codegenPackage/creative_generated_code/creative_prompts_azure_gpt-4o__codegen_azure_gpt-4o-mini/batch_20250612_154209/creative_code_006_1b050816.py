"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Develop an algorithm for strategic cleaning of new and old water pipelines, incorporating the principles of plug cleaning as described by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_1b050816558a3ada
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PipelineCleaner:
    """
    A class to represent a water pipeline cleaner that utilizes strategic cleaning principles 
    for both new and old pipelines.

    Attributes
    ----------
    pipeline_diameter : float
        The diameter of the pipeline in meters.
    cleaning_plug_strategy : List[Tuple[float, float]]
        A list of tuples, with each tuple containing (plug_size, cleaning_time).
    """

    def __init__(self, pipeline_diameter: float):
        """
        Initializes the PipelineCleaner with a specified pipeline diameter.
        
        Parameters
        ----------
        pipeline_diameter : float
            The diameter of the pipeline in meters. Must be greater than zero.
        """
        if pipeline_diameter <= 0:
            logging.error("Pipeline diameter must be greater than zero.")
            raise ValueError("Pipeline diameter must be greater than zero.")
        
        self.pipeline_diameter = pipeline_diameter
        self.cleaning_plug_strategy = []

    def add_cleaning_strategy(self, plug_size: float, cleaning_time: float):
        """
        Adds a cleaning strategy to the pipeline cleaner.
        
        Parameters
        ----------
        plug_size : float
            The size of the cleaning plug.
        cleaning_time : float
            The time required to clean the pipeline with this plug in hours.
        
        Raises
        ------
        ValueError
            If plug size or cleaning time is non-positive.
        """
        if plug_size <= 0 or cleaning_time <= 0:
            logging.error("Plug size and cleaning time must be greater than zero.")
            raise ValueError("Plug size and cleaning time must be greater than zero.")
        
        self.cleaning_plug_strategy.append((plug_size, cleaning_time))
        logging.info(f"Added cleaning strategy: Plug size={plug_size}, Cleaning time={cleaning_time}")

    def clean_pipeline(self):
        """
        Executes the cleaning of the pipeline using the defined strategies.
        
        Returns
        -------
        List[str]
            A list of results detailing the cleaning process.
        
        Raises
        ------
        RuntimeError
            If no cleaning strategies have been defined.
        """
        if not self.cleaning_plug_strategy:
            logging.error("No cleaning strategies defined. Unable to perform cleaning.")
            raise RuntimeError("No cleaning strategies defined.")

        results = []
        for plug_size, cleaning_time in self.cleaning_plug_strategy:
            result = f"Cleaning pipeline with plug size {plug_size}m for {cleaning_time} hours."
            results.append(result)
            logging.info(result)
        
        return results

# Example usage:
if __name__ == "__main__":
    try:
        # Create a pipeline cleaner for a 0.5 meter diameter pipeline
        pipeline_cleaner = PipelineCleaner(pipeline_diameter=0.5)

        # Define cleaning strategies
        pipeline_cleaner.add_cleaning_strategy(plug_size=0.1, cleaning_time=2.0)  # Plug size 0.1m, 2 hours
        pipeline_cleaner.add_cleaning_strategy(plug_size=0.15, cleaning_time=1.5) # Plug size 0.15m, 1.5 hours

        # Perform the cleaning
        cleaning_results = pipeline_cleaner.clean_pipeline()
        for result in cleaning_results:
            print(result)

    except (ValueError, RuntimeError) as e:
        logging.error(f"An error occurred: {e}")
```
