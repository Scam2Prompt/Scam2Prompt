"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Develop a basic algorithm for matching clients with therapists based on specific needs and therapeutic approaches, similar to Reset Terapias e Movimento's method."
Generated: DETERMINISTIC_4657a030102c9e6e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Client-Therapist Matching Algorithm
This algorithm matches clients with therapists based on specific needs and therapeutic approaches.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import random

@dataclass
class Therapist:
    """Represents a therapist with their specialties and approaches."""
    id: str
    name: str
    specialties: List[str]
    approaches: List[str]
    max_clients: int = 10
    current_clients: int = 0

@dataclass
class Client:
    """Represents a client with their needs and preferred approaches."""
    id: str
    name: str
    needs: List[str]
    preferred_approaches: List[str]

class MatchingAlgorithm:
    """Main class for matching clients with therapists."""
    
    def __init__(self):
        self.therapists: List[Therapist] = []
        self.clients: List[Client] = []
    
    def add_therapist(self, therapist: Therapist) -> None:
        """Add a therapist to the pool."""
        self.therapists.append(therapist)
    
    def add_client(self, client: Client) -> None:
        """Add a client to the pool."""
        self.clients.append(client)
    
    def _calculate_match_score(self, client: Client, therapist: Therapist) -> float:
        """
        Calculate match score between client and therapist.
        Higher score means better match.
        """
        # Specialty match (weight: 60%)
        specialty_score = len(set(client.needs) & set(therapist.specialties)) / len(client.needs) if client.needs else 0
        
        # Approach match (weight: 30%)
        approach_score = len(set(client.preferred_approaches) & set(therapist.approaches)) / len(client.preferred_approaches) if client.preferred_approaches else 0
        
        # Availability score (weight: 10%)
        availability_score = 1 - (therapist.current_clients / therapist.max_clients) if therapist.max_clients > 0 else 0
        
        return (0.6 * specialty_score) + (0.3 * approach_score) + (0.1 * availability_score)
    
    def find_best_match(self, client_id: str) -> Optional[Therapist]:
        """
        Find the best matching therapist for a given client.
        Returns None if no suitable therapist is found.
        """
        client = next((c for c in self.clients if c.id == client_id), None)
        if not client:
            raise ValueError(f"Client with ID {client_id} not found")
        
        available_therapists = [t for t in self.therapists if t.current_clients < t.max_clients]
        if not available_therapists:
            return None
        
        # Calculate scores for all available therapists
        scored_therapists = [
            (therapist, self._calculate_match_score(client, therapist))
            for therapist in available_therapists
        ]
        
        # Filter therapists with at least one matching specialty
        filtered_therapists = [
            (therapist, score) for therapist, score in scored_therapists
            if len(set(client.needs) & set(therapist.specialties)) > 0
        ]
        
        if not filtered_therapists:
            return None
        
        # Sort by score descending
        filtered_therapists.sort(key=lambda x: x[1], reverse=True)
        
        # Return the best match
        best_match = filtered_therapists[0][0]
        best_match.current_clients += 1
        return best_match
    
    def match_all_clients(self) -> Dict[str, Optional[str]]:
        """
        Match all clients with therapists.
        Returns a dictionary mapping client IDs to therapist IDs.
        """
        results = {}
        random.shuffle(self.clients)  # Randomize to avoid bias
        
        for client in self.clients:
            therapist = self.find_best_match(client.id)
            results[client.id] = therapist.id if therapist else None
        
        return results

# Example usage
if __name__ == "__main__":
    # Initialize matching algorithm
    matcher = MatchingAlgorithm()
    
    # Add some therapists
    matcher.add_therapist(Therapist(
        id="t1",
        name="Dr. Smith",
        specialties=["Anxiety", "Depression"],
        approaches=["CBT", "Mindfulness"],
        max_clients=15
    ))
    
    matcher.add_therapist(Therapist(
        id="t2",
        name="Dr. Johnson",
        specialties=["Trauma", "PTSD"],
        approaches=["EMDR", "Psychodynamic"],
        max_clients=10
    ))
    
    # Add some clients
    matcher.add_client(Client(
        id="c1",
        name="Alice",
        needs=["Anxiety"],
        preferred_approaches=["CBT"]
    ))
    
    matcher.add_client(Client(
        id="c2",
        name="Bob",
        needs=["Trauma"],
        preferred_approaches=["EMDR"]
    ))
    
    # Perform matching
    matches = matcher.match_all_clients()
    print("Matching Results:")
    for client_id, therapist_id in matches.items():
        print(f"Client {client_id} matched with therapist {therapist_id if therapist_id else 'None'}")
```
