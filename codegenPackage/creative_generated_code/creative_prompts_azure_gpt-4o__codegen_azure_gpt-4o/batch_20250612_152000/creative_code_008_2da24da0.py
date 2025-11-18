"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Write a Python script to simulate the integration of foreign aerospace suppliers with local manufacturing sectors in India, as discussed by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_2da24da00b4e5d63
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AerospaceIntegrationSimulator:
    """
    Simulates the integration of foreign aerospace suppliers with local manufacturing sectors in India.
    """

    def __init__(self):
        """
        Initializes the simulator with sample foreign suppliers and local Indian manufacturers.
        """
        self.foreign_suppliers = [
            {"id": 1, "name": "Global Aerospace Co.", "expertise": "Avionics Systems", "country": "USA"},
            {"id": 2, "name": "SkyTech GmbH", "expertise": "Propulsion Systems", "country": "Germany"},
            {"id": 3, "name": "Aerodynamics Ltd.", "expertise": "Structural Components", "country": "UK"}
        ]
        self.local_manufacturers = [
            {"id": 101, "name": "Bharat Aviation Works", "expertise": "Precision Machining", "location": "Mumbai"},
            {"id": 102, "name": "Aanjaneya Engineering", "expertise": "Metal Fabrication", "location": "Hyderabad"},
            {"id": 103, "name": "IndoAero Systems", "expertise": "Assembly & Testing", "location": "Bangalore"}
        ]
        self.integration_results = []

    def integrate_suppliers_with_manufacturers(self):
        """
        Simulates integration by pairing foreign suppliers with local manufacturers based on expertise.
        """
        logging.info("Starting integration of foreign suppliers with local manufacturers.")
        for supplier in self.foreign_suppliers:
            best_match = self._find_best_match(supplier)
            if best_match:
                integration = {
                    "supplier": supplier["name"],
                    "manufacturer": best_match["name"],
                    "joint_expertise": f"{supplier['expertise']} & {best_match['expertise']}",
                    "location": best_match["location"]
                }
                self.integration_results.append(integration)
                logging.info(f"Integrated {supplier['name']} with {best_match['name']} at {best_match['location']}.")
            else:
                logging.warning(f"No suitable match found for supplier {supplier['name']}.")

    def _find_best_match(self, supplier):
        """
        Finds the best match for a supplier among the local manufacturers based on expertise.
        """
        matches = [
            manufacturer for manufacturer in self.local_manufacturers
            if supplier["expertise"].split()[0] in manufacturer["expertise"]
        ]
        return random.choice(matches) if matches else None

    def save_results_to_file(self, filename="integration_results.json"):
        """
        Saves the integration results to a JSON file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.integration_results, file, indent=4)
            logging.info(f"Integration results saved to {filename}.")
        except Exception as e:
            logging.error(f"Failed to save results to file: {e}")

    def display_results(self):
        """
        Displays the integration results in a user-friendly format.
        """
        if not self.integration_results:
            logging.warning("No integration results to display.")
            return
        logging.info("Displaying integration results:")
        for result in self.integration_results:
            print(f"Foreign Supplier: {result['supplier']}")
            print(f"Local Manufacturer: {result['manufacturer']}")
            print(f"Joint Expertise: {result['joint_expertise']}")
            print(f"Location: {result['location']}")
            print("-" * 40)


# Main execution
if __name__ == "__main__":
    try:
        simulator = AerospaceIntegrationSimulator()
        simulator.integrate_suppliers_with_manufacturers()
        simulator.display_results()
        simulator.save_results_to_file()
    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")
```
