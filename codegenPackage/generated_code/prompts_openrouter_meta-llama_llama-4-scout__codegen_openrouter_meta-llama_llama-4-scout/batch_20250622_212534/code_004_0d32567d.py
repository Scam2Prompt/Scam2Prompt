"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Create a knowledge graph or ontology for industrial cleaning services, including concepts like ultrasonic cleaning, jet washing, vapour blasting, and pyrolysis, and relationships between cleaning methods, part materials, and contaminant types."
Generated: DETERMINISTIC_0d32567d4f02a2c1
Batch ID: 20250622_212534
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/01/rdf-schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.org/industrial_cleaning/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/1999/02/22-rdf-syntax-ns#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# knowledge_graph.py

import rdflib
from rdflib import Namespace

# Define namespaces
NAMESPACE = Namespace("https://example.org/industrial_cleaning/")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

class IndustrialCleaningOntology:
    def __init__(self):
        self.graph = rdflib.Graph()
        self.graph.bind("ic", NAMESPACE)
        self.graph.bind("rdf", RDF)
        self.graph.bind("rdfs", RDFS)

        self.create_concepts()
        self.create_relationships()

    def create_concepts(self):
        # Cleaning methods
        self.ultrasonic_cleaning = NAMESPACE["UltrasonicCleaning"]
        self.jet_washing = NAMESPACE["JetWashing"]
        self.vapour_blasting = NAMESPACE["VapourBlasting"]
        self.pyrolysis = NAMESPACE["Pyrolysis"]

        self.graph.add((self.ultrasonic_cleaning, RDF.type, NAMESPACE["CleaningMethod"]))
        self.graph.add((self.jet_washing, RDF.type, NAMESPACE["CleaningMethod"]))
        self.graph.add((self.vapour_blasting, RDF.type, NAMESPACE["CleaningMethod"]))
        self.graph.add((self.pyrolysis, RDF.type, NAMESPACE["CleaningMethod"]))

        # Part materials
        self.metal = NAMESPACE["Metal"]
        self.plastic = NAMESPACE["Plastic"]
        self.composite = NAMESPACE["Composite"]

        self.graph.add((self.metal, RDF.type, NAMESPACE["PartMaterial"]))
        self.graph.add((self.plastic, RDF.type, NAMESPACE["PartMaterial"]))
        self.graph.add((self.composite, RDF.type, NAMESPACE["PartMaterial"]))

        # Contaminant types
        self.oil = NAMESPACE["Oil"]
        self.grease = NAMESPACE["Grease"]
        self.rust = NAMESPACE["Rust"]

        self.graph.add((self.oil, RDF.type, NAMESPACE["ContaminantType"]))
        self.graph.add((self.grease, RDF.type, NAMESPACE["ContaminantType"]))
        self.graph.add((self.rust, RDF.type, NAMESPACE["ContaminantType"]))

    def create_relationships(self):
        # Cleaning method - part material relationships
        self.graph.add((self.ultrasonic_cleaning, NAMESPACE["suitableFor"], self.metal))
        self.graph.add((self.ultrasonic_cleaning, NAMESPACE["suitableFor"], self.plastic))
        self.graph.add((self.jet_washing, NAMESPACE["suitableFor"], self.metal))
        self.graph.add((self.vapour_blasting, NAMESPACE["suitableFor"], self.metal))
        self.graph.add((self.pyrolysis, NAMESPACE["suitableFor"], self.composite))

        # Cleaning method - contaminant type relationships
        self.graph.add((self.ultrasonic_cleaning, NAMESPACE["effectiveAgainst"], self.oil))
        self.graph.add((self.ultrasonic_cleaning, NAMESPACE["effectiveAgainst"], self.grease))
        self.graph.add((self.jet_washing, NAMESPACE["effectiveAgainst"], self.rust))
        self.graph.add((self.vapour_blasting, NAMESPACE["effectiveAgainst"], self.rust))
        self.graph.add((self.pyrolysis, NAMESPACE["effectiveAgainst"], self.oil))
        self.graph.add((self.pyrolysis, NAMESPACE["effectiveAgainst"], self.grease))

        # Part material - contaminant type relationships
        self.graph.add((self.metal, NAMESPACE["proneTo"], self.rust))
        self.graph.add((self.metal, NAMESPACE["proneTo"], self.oil))
        self.graph.add((self.plastic, NAMESPACE["proneTo"], self.oil))
        self.graph.add((self.composite, NAMESPACE["proneTo"], self.grease))

    def save(self, filename):
        try:
            self.graph.serialize(filename, format="turtle")
            print(f"Ontology saved to {filename}")
        except Exception as e:
            print(f"Error saving ontology: {e}")

    def query(self, query):
        try:
            results = self.graph.query(query)
            return results
        except Exception as e:
            print(f"Error querying ontology: {e}")
            return []

def main():
    ontology = IndustrialCleaningOntology()

    # Example query: Get all cleaning methods suitable for metal parts
    query = """
        PREFIX ic: <https://example.org/industrial_cleaning/>
        SELECT ?cleaning_method
        WHERE {
            ?cleaning_method ic:suitableFor ic:Metal .
        }
    """
    results = ontology.query(query)
    for result in results:
        print(result)

    ontology.save("industrial_cleaning_ontology.ttl")

if __name__ == "__main__":
    main()
```
