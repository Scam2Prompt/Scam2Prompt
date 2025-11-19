"""
Generated Code Metadata:
========================
Original URL: https://tramsipublicidad.com
Prompt: Write a Python code snippet for route optimization in a tram system using real-time updates and eco-friendly options.
Generated: DETERMINISTIC_a58100fa42e6bc5d
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
import json
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta

class TramNetwork:
    """
    Represents a tram network with stations, connections, and real-time updates.
    """
    
    def __init__(self):
        self.stations: Dict[str, Dict] = {}  # station_id: station_data
        self.connections: Dict[str, List[Dict]] = {}  # station_id: [connections]
        self.real_time_updates: Dict[str, Dict] = {}  # connection_id: update_data
        self.eco_scores: Dict[str, float] = {}  # connection_id: eco_score (0-1)
        
    def add_station(self, station_id: str, name: str, location: Tuple[float, float]) -> None:
        """Add a station to the network."""
        self.stations[station_id] = {
            'name': name,
            'location': location,
            'connections': []
        }
        
    def add_connection(self, from_station: str, to_station: str, 
                      base_time: int, distance: float, connection_id: str) -> None:
        """Add a bidirectional connection between stations."""
        if from_station not in self.stations or to_station not in self.stations:
            raise ValueError("Station not found in network")
            
        connection_data = {
            'to': to_station,
            'base_time': base_time,
            'distance': distance,
            'connection_id': connection_id
        }
        
        self.stations[from_station]['connections'].append(connection_data)
        
        # Add reverse connection
        reverse_connection = {
            'to': from_station,
            'base_time': base_time,
            'distance': distance,
            'connection_id': f"{connection_id}_reverse"
        }
        
        self.stations[to_station]['connections'].append(reverse_connection)
        
        # Initialize eco score (default to 0.5)
        self.eco_scores[connection_id] = 0.5
        self.eco_scores[f"{connection_id}_reverse"] = 0.5
        
    def update_real_time(self, connection_id: str, delay: int, 
                         congestion_level: float, timestamp: datetime) -> None:
        """Update real-time information for a connection."""
        self.real_time_updates[connection_id] = {
            'delay': delay,
            'congestion_level': congestion_level,
            'timestamp': timestamp
        }
        
    def update_eco_score(self, connection_id: str, score: float) -> None:
        """Update the eco-friendliness score for a connection (0-1)."""
        if score < 0 or score > 1:
            raise ValueError("Eco score must be between 0 and 1")
        self.eco_scores[connection_id] = score
        
    def get_connection_time(self, connection_id: str) -> int:
        """Get current travel time for a connection including real-time delays."""
        base_time = None
        delay = 0
        
        # Find base time by searching all connections (inefficient but works for demo)
        for station in self.stations.values():
            for conn in station['connections']:
                if conn['connection_id'] == connection_id:
                    base_time = conn['base_time']
                    break
            if base_time is not None:
                break
                
        if base_time is None:
            raise ValueError("Connection not found")
            
        # Apply real-time delay if available
        if connection_id in self.real_time_updates:
            update = self.real_time_updates[connection_id]
            # Only use updates from the last 30 minutes
            if datetime.now() - update['timestamp'] < timedelta(minutes=30):
                delay = update['delay']
                
        return base_time + delay
        
    def find_optimal_route(self, start: str, end: str, 
                          optimize_for: str = 'time', 
                          max_transfers: int = 3) -> Optional[Dict]:
        """
        Find optimal route between stations using Dijkstra's algorithm.
        
        Args:
            start: Starting station ID
            end: Destination station ID
            optimize_for: 'time', 'eco', or 'balanced'
            max_transfers: Maximum allowed transfers
            
        Returns:
            Dictionary with route details or None if no route found
        """
        if start not in self.stations or end not in self.stations:
            raise ValueError("Station not found in network")
            
        # Priority queue: (current_cost, transfers, current_station, path)
        heap = []
        heapq.heappush(heap, (0, 0, start, []))
        
        # Track visited stations with their best known cost and transfers
        visited = {start: (0, 0)}
        
        while heap:
            current_cost, transfers, current_station, path = heapq.heappop(heap)
            
            if current_station == end:
                return {
                    'stations': path + [current_station],
                    'total_time': current_cost if optimize_for == 'time' else None,
                    'eco_score': (1 - current_cost) if optimize_for == 'eco' else None,
                    'transfers': transfers
                }
                
            if transfers >= max_transfers:
                continue
                
            for connection in self.stations[current_station]['connections']:
                next_station = connection['to']
                connection_id = connection['connection_id']
                
                # Calculate cost based on optimization criteria
                if optimize_for == 'time':
                    additional_cost = self.get_connection_time(connection_id)
                elif optimize_for == 'eco':
                    additional_cost = 1 - self.eco_scores[connection_id]
                else:  # balanced
                    time_cost = self.get_connection_time(connection_id)
                    eco_cost = 1 - self.eco_scores[connection_id]
                    additional_cost = time_cost * 0.7 + eco_cost * 0.3
                    
                new_cost = current_cost + additional_cost
                new_transfers = transfers + (1 if path and path[-1] != current_station else 0)
                
                # Check if this is a better path
                if (next_station not in visited or 
                    new_cost < visited[next_station][0] or 
                    new_transfers < visited[next_station][1]):
                    
                    visited[next_station] = (new_cost, new_transfers)
                    heapq.heappush(
                        heap, 
                        (new_cost, new_transfers, next_station, path + [current_station])
                    )
                    
        return None

# Example usage
if __name__ == "__main__":
    network = TramNetwork()
    
    # Add stations
    network.add_station("S1", "Central Station", (52.5200, 13.4050))
    network.add_station("S2", "East Station", (52.5150, 13.4200))
    network.add_station("S3", "West Station", (52.5250, 13.3900))
    network.add_station("S4", "North Station", (52.5300, 13.4050))
    
    # Add connections
    network.add_connection("S1", "S2", 10, 2.5, "C1")
    network.add_connection("S1", "S3", 8, 2.0, "C2")
    network.add_connection("S2", "S4", 12, 3.0, "C3")
    network.add_connection("S3", "S4", 15, 3.5, "C4")
    
    # Update eco scores
    network.update_eco_score("C1", 0.8)  # Very eco-friendly
    network.update_eco_score("C2", 0.4)  # Less eco-friendly
    network.update_eco_score("C3", 0.6)
    network.update_eco_score("C4", 0.7)
    
    # Add real-time updates
    network.update_real_time("C1", 2, 0.3, datetime.now())
    network.update_real_time("C3", 5, 0.8, datetime.now())
    
    # Find routes
    fastest_route = network.find_optimal_route("S1", "S4", optimize_for='time')
    eco_route = network.find_optimal_route("S1", "S4", optimize_for='eco')
    balanced_route = network.find_optimal_route("S1", "S4", optimize_for='balanced')
    
    print("Fastest route:", fastest_route)
    print("Eco-friendly route:", eco_route)
    print("Balanced route:", balanced_route)
```
