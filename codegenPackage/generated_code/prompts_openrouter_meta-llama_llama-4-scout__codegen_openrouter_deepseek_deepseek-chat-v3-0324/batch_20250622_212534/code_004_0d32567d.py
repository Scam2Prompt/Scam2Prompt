"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Create a knowledge graph or ontology for industrial cleaning services, including concepts like ultrasonic cleaning, jet washing, vapour blasting, and pyrolysis, and relationships between cleaning methods, part materials, and contaminant types."
Generated: DETERMINISTIC_0d32567d4f02a2c1
Batch ID: 20250622_212534
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.org/industrial_cleaning#": {
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
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL, XSD

# Initialize the graph
kg = Graph()

# Define namespaces
ns = Namespace("http://example.org/industrial_cleaning#")
rdf = RDF
rdfs = RDFS
owl = OWL
xsd = XSD

# Bind namespaces for cleaner output
kg.bind("ic", ns)
kg.bind("rdf", rdf)
kg.bind("rdfs", rdfs)
kg.bind("owl", owl)
kg.bind("xsd", xsd)

# Define classes
kg.add((ns.CleaningMethod, rdf.type, owl.Class))
kg.add((ns.PartMaterial, rdf.type, owl.Class))
kg.add((ns.ContaminantType, rdf.type, owl.Class))
kg.add((ns.Equipment, rdf.type, owl.Class))
kg.add((ns.CleaningProcess, rdf.type, owl.Class))

# Define cleaning methods
kg.add((ns.UltrasonicCleaning, rdf.type, ns.CleaningMethod))
kg.add((ns.JetWashing, rdf.type, ns.CleaningMethod))
kg.add((ns.VapourBlasting, rdf.type, ns.CleaningMethod))
kg.add((ns.Pyrolysis, rdf.type, ns.CleaningMethod))

# Define part materials
kg.add((ns.Metal, rdf.type, ns.PartMaterial))
kg.add((ns.Plastic, rdf.type, ns.PartMaterial))
kg.add((ns.Ceramic, rdf.type, ns.PartMaterial))
kg.add((ns.Composite, rdf.type, ns.PartMaterial))

# Define contaminant types
kg.add((ns.Oil, rdf.type, ns.ContaminantType))
kg.add((ns.Grease, rdf.type, ns.ContaminantType))
kg.add((ns.Rust, rdf.type, ns.ContaminantType))
kg.add((ns.Paint, rdf.type, ns.ContaminantType))
kg.add((ns.Dirt, rdf.type, ns.ContaminantType))

# Define equipment
kg.add((ns.UltrasonicCleaner, rdf.type, ns.Equipment))
kg.add((ns.PressureWasher, rdf.type, ns.Equipment))
kg.add((ns.VapourBlaster, rdf.type, ns.Equipment))
kg.add((ns.PyrolysisOven, rdf.type, ns.Equipment))

# Define properties
kg.add((ns.usesMethod, rdf.type, owl.ObjectProperty))
kg.add((ns.usesEquipment, rdf.type, owl.ObjectProperty))
kg.add((ns.suitableForMaterial, rdf.type, owl.ObjectProperty))
kg.add((ns.effectiveAgainst, rdf.type, owl.ObjectProperty))
kg.add((ns.processTemperature, rdf.type, owl.DatatypeProperty))
kg.add((ns.processDuration, rdf.type, owl.DatatypeProperty))

# Define domain and range for properties
kg.add((ns.usesMethod, rdfs.domain, ns.CleaningProcess))
kg.add((ns.usesMethod, rdfs.range, ns.CleaningMethod))

kg.add((ns.usesEquipment, rdfs.domain, ns.CleaningProcess))
kg.add((ns.usesEquipment, rdfs.range, ns.Equipment))

kg.add((ns.suitableForMaterial, rdfs.domain, ns.CleaningMethod))
kg.add((ns.suitableForMaterial, rdfs.range, ns.PartMaterial))

kg.add((ns.effectiveAgainst, rdfs.domain, ns.CleaningMethod))
kg.add((ns.effectiveAgainst, rdfs.range, ns.ContaminantType))

kg.add((ns.processTemperature, rdfs.domain, ns.CleaningProcess))
kg.add((ns.processTemperature, rdfs.range, xsd.float))

kg.add((ns.processDuration, rdfs.domain, ns.CleaningProcess))
kg.add((ns.processDuration, rdfs.range, xsd.float))

# Add relationships between cleaning methods and materials
kg.add((ns.UltrasonicCleaning, ns.suitableForMaterial, ns.Metal))
kg.add((ns.UltrasonicCleaning, ns.suitableForMaterial, ns.Plastic))
kg.add((ns.JetWashing, ns.suitableForMaterial, ns.Metal))
kg.add((ns.JetWashing, ns.suitableForMaterial, ns.Plastic))
kg.add((ns.JetWashing, ns.suitableForMaterial, ns.Ceramic))
kg.add((ns.VapourBlasting, ns.suitableForMaterial, ns.Metal))
kg.add((ns.Pyrolysis, ns.suitableForMaterial, ns.Metal))
kg.add((ns.Pyrolysis, ns.suitableForMaterial, ns.Ceramic))

# Add relationships between cleaning methods and contaminants
kg.add((ns.UltrasonicCleaning, ns.effectiveAgainst, ns.Oil))
kg.add((ns.UltrasonicCleaning, ns.effectiveAgainst, ns.Grease))
kg.add((ns.JetWashing, ns.effectiveAgainst, ns.Dirt))
kg.add((ns.JetWashing, ns.effectiveAgainst, ns.Paint))
kg.add((ns.VapourBlasting, ns.effectiveAgainst, ns.Rust))
kg.add((ns.VapourBlasting, ns.effectiveAgainst, ns.Paint))
kg.add((ns.Pyrolysis, ns.effectiveAgainst, ns.Oil))
kg.add((ns.Pyrolysis, ns.effectiveAgainst, ns.Grease))
kg.add((ns.Pyrolysis, ns.effectiveAgainst, ns.Paint))

# Add example cleaning processes
process1 = URIRef(ns + "Process1")
kg.add((process1, rdf.type, ns.CleaningProcess))
kg.add((process1, ns.usesMethod, ns.UltrasonicCleaning))
kg.add((process1, ns.usesEquipment, ns.UltrasonicCleaner))
kg.add((process1, ns.processTemperature, Literal(60.0, datatype=xsd.float)))
kg.add((process1, ns.processDuration, Literal(15.0, datatype=xsd.float)))

process2 = URIRef(ns + "Process2")
kg.add((process2, rdf.type, ns.CleaningProcess))
kg.add((process2, ns.usesMethod, ns.Pyrolysis))
kg.add((process2, ns.usesEquipment, ns.PyrolysisOven))
kg.add((process2, ns.processTemperature, Literal(450.0, datatype=xsd.float)))
kg.add((process2, ns.processDuration, Literal(120.0, datatype=xsd.float)))

# Serialize the graph
kg.serialize("industrial_cleaning_ontology.ttl", format="turtle")
```
