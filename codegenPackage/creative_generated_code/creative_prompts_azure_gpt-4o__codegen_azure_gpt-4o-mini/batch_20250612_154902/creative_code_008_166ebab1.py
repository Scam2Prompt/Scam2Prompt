"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a script to calculate the optimal route for trucking and distribution logistics, incorporating Uniair Cargo's domestic and international networks.
Generated: DETERMINISTIC_166ebab1611ecba9
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
import pandas as pd
from geopy.distance import great_circle
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogisticsOptimizer:
    def __init__(self, routes_data):
        """
        Initialize the LogisticsOptimizer with routes data.

        :param routes_data: DataFrame containing routes information with 
                            columns: ['source', 'destination', 'distance', 'time']
        """
        self.routes_data = routes_data
        self.graph = self.create_graph()

    def create_graph(self):
        """
        Create a directed graph from the routes data.

        :return: A directed graph representing the routes
        """
        logging.info("Creating graph from routes data.")
        graph = nx.DiGraph()
        for _, row in self.routes_data.iterrows():
            graph.add_edge(row['source'], row['destination'], distance=row['distance'], time=row['time'])
        return graph

    def calculate_optimal_route(self, start, end):
        """
        Calculate the optimal route based on the shortest distance.

        :param start: The starting location
        :param end: The destination location
        :return: The optimal route and its total distance
        """
        try:
            logging.info(f"Calculating optimal route from {start} to {end}.")
            path = nx.shortest_path(self.graph, source=start, target=end, weight='distance')
            total_distance = nx.path_weight(self.graph, path, weight='distance')
            return path, total_distance
        except nx.NetworkXNoPath:
            logging.error(f"No path found from {start} to {end}.")
            return None, None
        except Exception as e:
            logging.error(f"Error calculating optimal route: {e}")
            return None, None

def load_routes_data(file_path):
    """
    Load routes data from a CSV file.

    :param file_path: Path to the CSV file containing routes information
    :return: DataFrame containing the routes data
    """
    try:
        routes_data = pd.read_csv(file_path)
        logging.info("Routes data loaded successfully.")
        return routes_data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        logging.error("No data found in the CSV file.")
        return None
    except Exception as e:
        logging.error(f"Error loading routes data: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    routes_file = "routes.csv"  # Path to the routes CSV file
    routes_data = load_routes_data(routes_file)

    if routes_data is not None:
        optimizer = LogisticsOptimizer(routes_data)

        # Define the start and end locations for the route
        start_location = "CityA"
        end_location = "CityB"

        # Calculate the optimal route
        optimal_route, distance = optimizer.calculate_optimal_route(start_location, end_location)

        if optimal_route:
            logging.info(f"Optimal route from {start_location} to {end_location}: {optimal_route}")
            logging.info(f"Total distance: {distance} km")
        else:
            logging.error("Failed to calculate optimal route.")
```

Make sure to replace `"routes.csv"` with the actual path to your routes data file, which should contain the required columns: `source`, `destination`, `distance`, and `time`.
