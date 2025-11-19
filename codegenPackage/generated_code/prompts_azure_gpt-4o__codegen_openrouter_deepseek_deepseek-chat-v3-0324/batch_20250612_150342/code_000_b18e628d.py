"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Write Python code to simulate the cloning and screening of human olfactory receptors coupled to G-proteins, as described in ChemCom's research focus.
Generated: DETERMINISTIC_b18e628db69162fe
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class GProteinType(Enum):
    """Enum representing different types of G-proteins."""
    G_OLF = auto()  # G-protein specific to olfactory receptors
    G_S = auto()     # Stimulatory G-protein
    G_I = auto()     # Inhibitory G-protein
    G_Q = auto()     # Gq protein

@dataclass
class OlfactoryReceptor:
    """Class representing a human olfactory receptor."""
    id: str
    dna_sequence: str
    expression_level: float
    g_protein_coupling: GProteinType
    activation_threshold: float

@dataclass
class Ligand:
    """Class representing a chemical ligand that can bind to receptors."""
    name: str
    structure: str  # Simplified representation (e.g., SMILES)
    binding_affinity: Dict[str, float]  # Receptor ID -> affinity

class ScreeningResult:
    """Class to store results of receptor-ligand screening."""
    def __init__(self):
        self.results = []

    def add_result(self, receptor_id: str, ligand_name: str, response: float):
        """Add a screening result."""
        self.results.append({
            'receptor_id': receptor_id,
            'ligand_name': ligand_name,
            'response': response
        })

    def get_top_results(self, n: int = 5) -> List[Dict]:
        """Get top n results sorted by response."""
        return sorted(self.results, key=lambda x: x['response'], reverse=True)[:n]

class OlfactorySystemSimulator:
    """Main class to simulate olfactory receptor cloning and screening."""
    
    def __init__(self):
        self.receptors = []
        self.ligands = []
        self.screening_results = ScreeningResult()
    
    def clone_receptor(self, dna_sequence: str, g_protein_type: GProteinType) -> OlfactoryReceptor:
        """Simulate cloning of an olfactory receptor."""
        if not self._validate_dna_sequence(dna_sequence):
            raise ValueError("Invalid DNA sequence provided.")
        
        receptor_id = f"OR_{random.randint(1000, 9999)}"
        expression_level = random.uniform(0.1, 1.0)
        activation_threshold = random.uniform(0.3, 0.8)
        
        receptor = OlfactoryReceptor(
            id=receptor_id,
            dna_sequence=dna_sequence,
            expression_level=expression_level,
            g_protein_coupling=g_protein_type,
            activation_threshold=activation_threshold
        )
        
        self.receptors.append(receptor)
        return receptor
    
    def add_ligand(self, name: str, structure: str, affinities: Dict[str, float]):
        """Add a ligand with binding affinities for receptors."""
        ligand = Ligand(
            name=name,
            structure=structure,
            binding_affinity=affinities
        )
        self.ligands.append(ligand)
        return ligand
    
    def screen_receptors(self, ligand_name: str, verbose: bool = False) -> ScreeningResult:
        """Screen all receptors against a specific ligand."""
        ligand = next((l for l in self.ligands if l.name == ligand_name), None)
        if not ligand:
            raise ValueError(f"Ligand {ligand_name} not found.")
        
        for receptor in self.receptors:
            if receptor.id in ligand.binding_affinity:
                affinity = ligand.binding_affinity[receptor.id]
                response = self._calculate_response(receptor, affinity)
                
                if verbose:
                    print(f"Receptor {receptor.id} response to {ligand_name}: {response:.2f}")
                
                self.screening_results.add_result(receptor.id, ligand.name, response)
        
        return self.screening_results
    
    def _calculate_response(self, receptor: OlfactoryReceptor, affinity: float) -> float:
        """Calculate receptor response based on affinity and receptor properties."""
        normalized_affinity = affinity / (affinity + receptor.activation_threshold)
        response = normalized_affinity * receptor.expression_level
        
        # Add some noise to simulate biological variability
        response *= random.uniform(0.9, 1.1)
        return response
    
    def _validate_dna_sequence(self, sequence: str) -> bool:
        """Validate that a DNA sequence contains only valid nucleotides."""
        valid_nucleotides = {'A', 'T', 'C', 'G'}
        return all(nucleotide.upper() in valid_nucleotides for nucleotide in sequence)
    
    def get_receptor_by_id(self, receptor_id: str) -> Optional[OlfactoryReceptor]:
        """Retrieve a receptor by its ID."""
        return next((r for r in self.receptors if r.id == receptor_id), None)

# Example usage
if __name__ == "__main__":
    simulator = OlfactorySystemSimulator()
    
    # Clone some receptors
    receptor1 = simulator.clone_receptor("ATCGATCGATCG", GProteinType.G_OLF)
    receptor2 = simulator.clone_receptor("GCTAGCTAGCTA", GProteinType.G_S)
    
    # Add ligands with affinities
    simulator.add_ligand(
        "OdorantA",
        "CC(=O)OC1=CC=CC=C1C(=O)O",
        {receptor1.id: 0.8, receptor2.id: 0.3}
    )
    
    simulator.add_ligand(
        "OdorantB",
        "C1=CC=C(C=C1)C=O",
        {receptor1.id: 0.2, receptor2.id: 0.7}
    )
    
    # Screen receptors against ligands
    results = simulator.screen_receptors("OdorantA", verbose=True)
    top_results = results.get_top_results()
    
    print("\nTop results:")
    for result in top_results:
        print(f"Receptor {result['receptor_id']} responded to {result['ligand_name']} with {result['response']:.2f}")
```
