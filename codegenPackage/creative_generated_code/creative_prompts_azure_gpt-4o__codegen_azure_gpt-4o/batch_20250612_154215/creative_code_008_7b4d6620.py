"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bilet-emirates.ru
Prompt: Create a Python script to analyze Emirates flight routes using the map of destinations provided on the website, and calculate the shortest travel times for specific itineraries.
Generated: DETERMINISTIC_7b4d6620e35cb1bd
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx

# Define a function to load flight routes from a data source
def load_flight_routes():
    """
    Load the flight routes from a hypothetical data source or API.
    This is a placeholder function where real data fetching and parsing logic should be implemented.
    
    Returns:
        routes (list): A list of tuples representing the flight routes and durations.
                       Each tuple is in the format (origin, destination, travel_time_in_hours).
    """
    # Example flight routes. Replace with actual data fetching logic.
    routes = [
        ("Dubai", "London", 7),
        ("Dubai", "New York", 14),
        ("London", "New York", 8),
        ("London", "Paris", 1),
        ("Paris", "New York", 9),
        ("Dubai", "Sydney", 14),
        ("Sydney", "Auckland", 3),
    ]
    return routes

# Define a function to build a graph representation of flight routes
def build_flight_graph(routes):
    """
    Build a graph from the flight routes using NetworkX.

    Args:
        routes (list): A list of tuples representing flight routes and durations.
                       Each tuple is in the format (origin, destination, travel_time_in_hours).

    Returns:
        graph (networkx.DiGraph): A directed graph representing the flight routes.
    """
    graph = nx.DiGraph()
    for origin, destination, travel_time in routes:
        graph.add_edge(origin, destination, weight=travel_time)
    return graph

# Define a function to calculate the shortest travel time between two destinations
def calculate_shortest_travel_time(graph, start, end):
    """
    Calculate the shortest travel time between two destinations using Dijkstra's algorithm.

    Args:
        graph (networkx.DiGraph): A directed graph representing the flight routes.
        start (str): The starting city.
        end (str): The destination city.

    Returns:
        shortest_time (float): The shortest travel time in hours, or None if no path exists.
        path (list): The shortest path as a list of cities, or None if no path exists.
    """
    try:
        shortest_time = nx.dijkstra_path_length(graph, start, end, weight="weight")
        path = nx.dijkstra_path(graph, start, end, weight="weight")
        return shortest_time, path
    except nx.NetworkXNoPath:
        # Handle the case where no path exists
        return None, None

# Main function to demonstrate flight route analysis
def main():
    """
    Main function to load flight routes, calculate shortest travel times,
    and display results for specified itineraries.
    """
    # Load flight routes
    flight_routes = load_flight_routes()

    # Build flight graph
    flight_graph = build_flight_graph(flight_routes)

    # Example itineraries to analyze
    itineraries = [
        ("Dubai", "New York"),
        ("London", "Sydney"),
        ("Paris", "Auckland"),
    ]

    # Calculate and display shortest travel times for each itinerary
    for start, end in itineraries:
        shortest_time, path = calculate_shortest_travel_time(flight_graph, start, end)
        
        if shortest_time is not None and path is not None:
            print(f"Shortest travel time from {start} to {end}: {shortest_time} hours")
            print(f"Path: {' -> '.join(path)}")
        else:
            print(f"No path exists from {start} to {end}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
