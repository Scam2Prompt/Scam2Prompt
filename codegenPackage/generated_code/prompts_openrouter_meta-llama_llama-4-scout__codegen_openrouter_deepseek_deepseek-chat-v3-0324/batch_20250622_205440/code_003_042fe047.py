"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: "Design a system for debugging and tracing issues across an entire data stack, illustrating how data, code, and models connect, using tools like Disarray."
Generated: DETERMINISTIC_042fe0473bcaad45
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List, Optional, Any
from uuid import uuid4
from datetime import datetime
import json
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TraceType(Enum):
    DATA = "data"
    CODE = "code"
    MODEL = "model"

class TraceStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    WARNING = "warning"

class TraceNode:
    def __init__(
        self,
        node_id: str,
        trace_type: TraceType,
        name: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.node_id = node_id
        self.trace_type = trace_type
        self.name = name
        self.metadata = metadata or {}
        self.children: List['TraceNode'] = []
        self.status: Optional[TraceStatus] = None
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        self.error: Optional[str] = None

    def add_child(self, child_node: 'TraceNode') -> None:
        """Add a child node to this trace node."""
        self.children.append(child_node)

    def start_trace(self) -> None:
        """Mark the start of tracing for this node."""
        self.start_time = datetime.utcnow()

    def end_trace(self, status: TraceStatus, error: Optional[str] = None) -> None:
        """Mark the end of tracing for this node with status."""
        self.end_time = datetime.utcnow()
        self.status = status
        self.error = error

    def to_dict(self) -> Dict[str, Any]:
        """Convert the trace node to a dictionary for serialization."""
        return {
            "node_id": self.node_id,
            "trace_type": self.trace_type.value,
            "name": self.name,
            "metadata": self.metadata,
            "status": self.status.value if self.status else None,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "error": self.error,
            "children": [child.to_dict() for child in self.children]
        }

class DataStackTracer:
    def __init__(self):
        self.root_nodes: Dict[str, TraceNode] = {}
        self.current_context: List[TraceNode] = []

    def start_trace(
        self,
        trace_type: TraceType,
        name: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Start a new trace with a unique ID."""
        trace_id = str(uuid4())
        node = TraceNode(trace_id, trace_type, name, metadata)
        
        if not self.current_context:
            self.root_nodes[trace_id] = node
        else:
            self.current_context[-1].add_child(node)
        
        self.current_context.append(node)
        node.start_trace()
        logger.info(f"Started trace {trace_id} for {name}")
        return trace_id

    def end_trace(
        self,
        trace_id: str,
        status: TraceStatus,
        error: Optional[str] = None
    ) -> None:
        """End an existing trace with status."""
        if not self.current_context or self.current_context[-1].node_id != trace_id:
            logger.error(f"Trace {trace_id} not found in current context")
            raise ValueError("Trace ID not in current context")
        
        node = self.current_context.pop()
        node.end_trace(status, error)
        logger.info(f"Ended trace {trace_id} with status {status}")

    def get_trace_tree(self, trace_id: str) -> Dict[str, Any]:
        """Get the complete trace tree for a given trace ID."""
        if trace_id not in self.root_nodes:
            logger.error(f"Trace {trace_id} not found")
            raise ValueError("Trace ID not found")
        
        return self.root_nodes[trace_id].to_dict()

    def export_traces(self, file_path: str) -> None:
        """Export all traces to a JSON file."""
        traces = {trace_id: node.to_dict() for trace_id, node in self.root_nodes.items()}
        try:
            with open(file_path, 'w') as f:
                json.dump(traces, f, indent=2)
            logger.info(f"Traces exported to {file_path}")
        except Exception as e:
            logger.error(f"Failed to export traces: {str(e)}")
            raise

    def import_traces(self, file_path: str) -> None:
        """Import traces from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                traces = json.load(f)
            
            for trace_id, trace_data in traces.items():
                node = self._deserialize_node(trace_data)
                self.root_nodes[trace_id] = node
            
            logger.info(f"Traces imported from {file_path}")
        except Exception as e:
            logger.error(f"Failed to import traces: {str(e)}")
            raise

    def _deserialize_node(self, data: Dict[str, Any]) -> TraceNode:
        """Deserialize a node from dictionary data."""
        node = TraceNode(
            data["node_id"],
            TraceType(data["trace_type"]),
            data["name"],
            data["metadata"]
        )
        
        if data["start_time"]:
            node.start_time = datetime.fromisoformat(data["start_time"])
        if data["end_time"]:
            node.end_time = datetime.fromisoformat(data["end_time"])
        if data["status"]:
            node.status = TraceStatus(data["status"])
        node.error = data["error"]
        
        for child_data in data["children"]:
            child_node = self._deserialize_node(child_data)
            node.add_child(child_node)
        
        return node

# Example usage
if __name__ == "__main__":
    tracer = DataStackTracer()
    
    # Simulate tracing through a data pipeline
    pipeline_id = tracer.start_trace(
        TraceType.DATA,
        "ETL Pipeline",
        {"source": "database", "destination": "data_warehouse"}
    )
    
    try:
        extract_id = tracer.start_trace(
            TraceType.CODE,
            "Extract Data",
            {"query": "SELECT * FROM customers"}
        )
        # Simulate work
        tracer.end_trace(extract_id, TraceStatus.SUCCESS)
        
        transform_id = tracer.start_trace(
            TraceType.CODE,
            "Transform Data",
            {"operations": ["clean", "normalize"]}
        )
        # Simulate work
        tracer.end_trace(transform_id, TraceStatus.SUCCESS)
        
        load_id = tracer.start_trace(
            TraceType.DATA,
            "Load Data",
            {"table": "customers_dim"}
        )
        # Simulate work
        tracer.end_trace(load_id, TraceStatus.SUCCESS)
        
        tracer.end_trace(pipeline_id, TraceStatus.SUCCESS)
    except Exception as e:
        tracer.end_trace(pipeline_id, TraceStatus.FAILURE, str(e))
    
    # Export traces
    tracer.export_traces("traces.json")
```
