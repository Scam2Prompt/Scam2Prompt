"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: Write a function leveraging Disarray to trace advanced lineage in a machine learning project, identifying dependencies between data, code, and models.
Generated: DETERMINISTIC_cf4775d575b29dd2
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import disarray
import networkx as nx
import logging
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ArtifactType(Enum):
    """Enumeration of artifact types in the lineage graph."""
    DATA = "data"
    CODE = "code"
    MODEL = "model"
    CONFIG = "configuration"

class LineageTracer:
    """
    A class to trace and analyze lineage in a machine learning project using Disarray.
    
    Attributes:
        graph (nx.DiGraph): Directed graph representing the lineage relationships.
    """
    
    def __init__(self):
        """Initialize the lineage tracer with an empty directed graph."""
        self.graph = nx.DiGraph()
    
    def add_artifact(self, artifact_id: str, artifact_type: ArtifactType, metadata: Optional[Dict] = None) -> None:
        """
        Add an artifact to the lineage graph.
        
        Args:
            artifact_id: Unique identifier for the artifact.
            artifact_type: Type of the artifact (DATA, CODE, MODEL, CONFIG).
            metadata: Optional dictionary containing additional metadata about the artifact.
        """
        try:
            if not artifact_id:
                raise ValueError("Artifact ID cannot be empty")
            
            self.graph.add_node(artifact_id, type=artifact_type.value, metadata=metadata or {})
            logger.info(f"Added artifact {artifact_id} of type {artifact_type.value}")
        except Exception as e:
            logger.error(f"Failed to add artifact {artifact_id}: {str(e)}")
            raise
    
    def add_dependency(self, source_id: str, target_id: str, relationship: str = "depends_on") -> None:
        """
        Add a dependency relationship between two artifacts.
        
        Args:
            source_id: ID of the source artifact (dependent).
            target_id: ID of the target artifact (dependency).
            relationship: Type of relationship between artifacts.
        """
        try:
            if not self.graph.has_node(source_id):
                raise ValueError(f"Source artifact {source_id} not found")
            if not self.graph.has_node(target_id):
                raise ValueError(f"Target artifact {target_id} not found")
            
            self.graph.add_edge(source_id, target_id, relationship=relationship)
            logger.info(f"Added dependency: {source_id} -> {target_id} ({relationship})")
        except Exception as e:
            logger.error(f"Failed to add dependency {source_id} -> {target_id}: {str(e)}")
            raise
    
    def get_lineage(self, artifact_id: str, direction: str = "downstream") -> List[Tuple[str, Dict]]:
        """
        Retrieve lineage for a given artifact in either upstream or downstream direction.
        
        Args:
            artifact_id: ID of the artifact to trace lineage for.
            direction: Direction of lineage tracing ('upstream' or 'downstream').
            
        Returns:
            List of tuples containing (artifact_id, artifact_metadata) in the lineage path.
            
        Raises:
            ValueError: If invalid direction is specified or artifact not found.
        """
        if direction not in ["upstream", "downstream"]:
            raise ValueError("Direction must be either 'upstream' or 'downstream'")
        
        if not self.graph.has_node(artifact_id):
            raise ValueError(f"Artifact {artifact_id} not found")
        
        try:
            if direction == "upstream":
                # Get all ancestors (dependencies)
                lineage_nodes = nx.ancestors(self.graph, artifact_id)
            else:
                # Get all descendants (dependents)
                lineage_nodes = nx.descendants(self.graph, artifact_id)
            
            return [(node, self.graph.nodes[node]) for node in lineage_nodes]
        except Exception as e:
            logger.error(f"Failed to retrieve lineage for {artifact_id}: {str(e)}")
            raise
    
    def visualize_lineage(self, artifact_id: str, output_file: str = "lineage.png") -> None:
        """
        Generate a visualization of the lineage graph for a given artifact.
        
        Args:
            artifact_id: ID of the artifact to visualize lineage for.
            output_file: Path to save the visualization image.
        """
        try:
            import matplotlib.pyplot as plt
            
            if not self.graph.has_node(artifact_id):
                raise ValueError(f"Artifact {artifact_id} not found")
            
            # Create a subgraph containing the artifact and its lineage
            all_nodes = {artifact_id}.union(nx.ancestors(self.graph, artifact_id))
            subgraph = self.graph.subgraph(all_nodes)
            
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(subgraph)
            
            # Color nodes by type
            color_map = {
                ArtifactType.DATA.value: 'lightblue',
                ArtifactType.CODE.value: 'lightgreen',
                ArtifactType.MODEL.value: 'orange',
                ArtifactType.CONFIG.value: 'pink'
            }
            
            node_colors = [color_map[subgraph.nodes[node]['type']] for node in subgraph.nodes()]
            
            nx.draw(
                subgraph,
                pos,
                with_labels=True,
                node_size=2000,
                node_color=node_colors,
                font_size=10,
                arrowsize=20
            )
            
            plt.title(f"Lineage Graph for {artifact_id}")
            plt.savefig(output_file)
            plt.close()
            logger.info(f"Lineage visualization saved to {output_file}")
        except ImportError:
            logger.error("Matplotlib is required for visualization. Please install it first.")
            raise
        except Exception as e:
            logger.error(f"Failed to visualize lineage: {str(e)}")
            raise
    
    def export_lineage(self, format: str = "json") -> Any:
        """
        Export the lineage graph in specified format.
        
        Args:
            format: Export format ('json', 'graphml', 'gexf').
            
        Returns:
            The exported graph in specified format.
            
        Raises:
            ValueError: If unsupported format is specified.
        """
        try:
            if format == "json":
                return nx.node_link_data(self.graph)
            elif format == "graphml":
                return nx.write_graphml(self.graph, "lineage.graphml")
            elif format == "gexf":
                return nx.write_gexf(self.graph, "lineage.gexf")
            else:
                raise ValueError(f"Unsupported export format: {format}")
        except Exception as e:
            logger.error(f"Failed to export lineage: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    tracer = LineageTracer()
    
    # Add artifacts
    tracer.add_artifact("raw_data.csv", ArtifactType.DATA, {"size": "10GB", "format": "CSV"})
    tracer.add_artifact("preprocessing.py", ArtifactType.CODE, {"author": "Alice", "version": "1.0"})
    tracer.add_artifact("clean_data.parquet", ArtifactType.DATA, {"size": "5GB", "format": "Parquet"})
    tracer.add_artifact("model_config.json", ArtifactType.CONFIG, {"model_type": "RandomForest"})
    tracer.add_artifact("trained_model.pkl", ArtifactType.MODEL, {"accuracy": 0.95, "algorithm": "RandomForest"})
    
    # Add dependencies
    tracer.add_dependency("preprocessing.py", "raw_data.csv")
    tracer.add_dependency("clean_data.parquet", "preprocessing.py")
    tracer.add_dependency("trained_model.pkl", "clean_data.parquet")
    tracer.add_dependency("trained_model.pkl", "model_config.json")
    
    # Get lineage
    print(tracer.get_lineage("trained_model.pkl", "upstream"))
    
    # Visualize
    tracer.visualize_lineage("trained_model.pkl")
    
    # Export
    tracer.export_lineage("json")
```
