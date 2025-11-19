"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petroleumegate.com
Prompt: Generate a code snippet that simulates the supply chain logistics for an oil refinery, taking into account the constant pipeline supply to Vancouver as described by P.G.C.
Generated: DETERMINISTIC_10dc3090ed4a2a06
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OilPipeline:
    """
    Class to simulate an oil pipeline supplying oil to Vancouver.
    """
    def __init__(self, pipeline_capacity_per_hour: float):
        """
        Initialize the pipeline with a specified capacity.
        :param pipeline_capacity_per_hour: The maximum oil capacity (barrels) the pipeline can transport per hour.
        """
        self.pipeline_capacity_per_hour = pipeline_capacity_per_hour
        self.total_supplied = 0  # Total oil supplied in barrels
        self.last_supply_time = datetime.datetime.now()

    def supply_oil(self, hours: float):
        """
        Simulate supplying oil for a given number of hours.
        :param hours: Number of hours to continue the supply.
        :return: Total oil supplied during the period.
        """
        try:
            # Validate input
            if hours <= 0:
                raise ValueError("Hours must be greater than 0.")
            
            # Calculate oil supplied during the given hours
            oil_supplied = hours * self.pipeline_capacity_per_hour
            self.total_supplied += oil_supplied
            self.last_supply_time = datetime.datetime.now()
            
            logging.info(f"Supplied {oil_supplied:.2f} barrels of oil over {hours} hours.")
            return oil_supplied
        except ValueError as ve:
            logging.error(f"Error in supply_oil: {ve}")
            raise

    def get_total_supplied(self):
        """
        Get the total amount of oil supplied by the pipeline.
        :return: Total oil supplied in barrels.
        """
        return self.total_supplied

    def get_last_supply_time(self):
        """
        Get the timestamp of the last supply operation.
        :return: Datetime object of the last supply time.
        """
        return self.last_supply_time


class OilRefinery:
    """
    Class to simulate a refinery receiving oil from the pipeline.
    """
    def __init__(self, refinery_capacity_per_hour: float):
        """
        Initialize the refinery with a specified processing capacity.
        :param refinery_capacity_per_hour: Maximum oil processing capacity (barrels) per hour.
        """
        self.refinery_capacity_per_hour = refinery_capacity_per_hour
        self.processed_oil = 0  # Total oil processed in barrels

    def process_oil(self, oil_barrels: float):
        """
        Simulate processing oil received from the pipeline.
        :param oil_barrels: Quantity of oil received for processing (in barrels).
        :return: Quantity of oil successfully processed.
        """
        try:
            # Validate input
            if oil_barrels <= 0:
                raise ValueError("Oil barrels must be greater than 0.")

            # Calculate the oil that can be processed
            if oil_barrels > self.refinery_capacity_per_hour:
                logging.warning(f"Received {oil_barrels:.2f} barrels but refinery can only process "
                                f"{self.refinery_capacity_per_hour:.2f} barrels per hour. Processing maximum capacity.")
                oil_barrels = self.refinery_capacity_per_hour
            
            self.processed_oil += oil_barrels
            logging.info(f"Processed {oil_barrels:.2f} barrels of oil.")
            return oil_barrels
        except ValueError as ve:
            logging.error(f"Error in process_oil: {ve}")
            raise

    def get_processed_oil(self):
        """
        Get the total amount of oil processed by the refinery.
        :return: Total oil processed in barrels.
        """
        return self.processed_oil


if __name__ == '__main__':
    # Define pipeline and refinery capacities
    PIPELINE_CAPACITY_PER_HOUR = 10000  # barrels per hour
    REFINERY_CAPACITY_PER_HOUR = 8000   # barrels per hour

    # Create pipeline and refinery objects
    pipeline = OilPipeline(pipeline_capacity_per_hour=PIPELINE_CAPACITY_PER_HOUR)
    refinery = OilRefinery(refinery_capacity_per_hour=REFINERY_CAPACITY_PER_HOUR)

    # Simulate pipeline supply and refinery processing
    try:
        # Supply oil from the pipeline
        hours_of_supply = 5
        oil_supplied = pipeline.supply_oil(hours=hours_of_supply)

        # Process oil in the refinery
        oil_processed = refinery.process_oil(oil_barrels=oil_supplied)

        # Log final details
        logging.info(f"Total oil supplied by pipeline: {pipeline.get_total_supplied():.2f} barrels.")
        logging.info(f"Total oil processed by refinery: {refinery.get_processed_oil():.2f} barrels.")
        logging.info(f"Last pipeline supply time: {pipeline.get_last_supply_time()}.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
