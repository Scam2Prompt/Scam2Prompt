"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clibiya.com
Prompt: Create an algorithm to track and report the supply chain of recycled products from waste collection to final sales, based on Clibiya's business model.
Generated: DETERMINISTIC_b25d06f3f23a4185
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SupplyChainStage:
    """
    Represents a single stage in the supply chain process.
    """

    def __init__(self, stage_name, entity, timestamp=None):
        """
        Initialize a supply chain stage.
        :param stage_name: Name of the stage
        :param entity: Entity responsible for this stage (e.g., company name)
        :param timestamp: When this stage was completed (auto-generated if None)
        """
        self.stage_name = stage_name
        self.entity = entity
        self.timestamp = timestamp or datetime.datetime.now()

    def to_dict(self):
        """
        Convert stage details to dictionary format for reporting.
        :return: Dictionary representation of the stage.
        """
        return {
            "stage_name": self.stage_name,
            "entity": self.entity,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }


class SupplyChain:
    """
    A class to track the supply chain process of recycled products.
    """

    def __init__(self, product_id, product_name):
        """
        Initialize the supply chain for a specific product.
        :param product_id: Unique identifier for the product
        :param product_name: Name of the product
        """
        self.product_id = product_id
        self.product_name = product_name
        self.stages = []  # List of SupplyChainStage objects

    def add_stage(self, stage_name, entity):
        """
        Add a new stage to the supply chain.
        :param stage_name: Name of the stage
        :param entity: Entity responsible for this stage
        """
        stage = SupplyChainStage(stage_name, entity)
        self.stages.append(stage)

    def generate_report(self):
        """
        Generate a report of the supply chain process.
        :return: A dictionary containing the supply chain details.
        """
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "supply_chain": [stage.to_dict() for stage in self.stages]
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize supply chain for a recycled product
        recycled_product = SupplyChain(product_id="R123", product_name="Recycled Plastic Bottle")

        # Add stages to the supply chain
        recycled_product.add_stage(stage_name="Waste Collection", entity="City Waste Management")
        recycled_product.add_stage(stage_name="Sorting", entity="GreenSort Inc.")
        recycled_product.add_stage(stage_name="Recycling Process", entity="EcoRecycle Ltd.")
        recycled_product.add_stage(stage_name="Manufacturing", entity="RePlastic Co.")
        recycled_product.add_stage(stage_name="Final Sales", entity="Retailers Plus Inc.")

        # Generate and print the supply chain report
        report = recycled_product.generate_report()
        for key, value in report.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
