"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Recommend best practices for designing container-based system diagrams in patent drawings, as covered in the "Mastering Container-Based System Diagrams in Patent Drawings" course.
Generated: DETERMINISTIC_d7138a0cdc3558e6
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides utility functions to generate container-based system diagrams 
following best practices for patent drawings as per industry standards.
"""

from typing import List, Dict, Optional
from enum import Enum, auto
import svgwrite
from dataclasses import dataclass

class ContainerType(Enum):
    """Enum representing different types of containers in system diagrams."""
    APPLICATION = auto()
    DATABASE = auto()
    MICROSERVICE = auto()
    QUEUE = auto()
    LOAD_BALANCER = auto()
    API_GATEWAY = auto()

@dataclass
class Container:
    """Data class representing a container in the system diagram."""
    name: str
    container_type: ContainerType
    description: str
    dependencies: List[str]
    x: int = 0
    y: int = 0

class ContainerDiagramGenerator:
    """
    Generates container-based system diagrams following patent drawing best practices.
    """
    
    def __init__(self, title: str, width: int = 1200, height: int = 800):
        """
        Initialize the diagram generator.
        
        Args:
            title: Title of the diagram
            width: Width of the diagram in pixels
            height: Height of the diagram in pixels
        """
        self.title = title
        self.width = width
        self.height = height
        self.containers: List[Container] = []
        self.dwg = svgwrite.Drawing(
            filename=f"{title.replace(' ', '_')}.svg",
            size=(f"{width}px", f"{height}px")
        )
        
    def add_container(self, container: Container) -> None:
        """Add a container to the diagram."""
        self.containers.append(container)
        
    def _get_container_shape(self, container: Container) -> svgwrite.container.Group:
        """Generate the appropriate shape for a container based on its type."""
        group = self.dwg.g()
        
        # Base rectangle for all container types
        rect = self.dwg.rect(
            insert=(container.x, container.y),
            size=(150, 100),
            rx=10,
            ry=10,
            fill='#ffffff',
            stroke='#000000',
            stroke_width=2
        )
        group.add(rect)
        
        # Add type-specific decorations
        if container.container_type == ContainerType.DATABASE:
            ellipse = self.dwg.ellipse(
                center=(container.x + 75, container.y - 10),
                r=(30, 15),
                fill='#ffffff',
                stroke='#000000',
                stroke_width=2
            )
            group.add(ellipse)
            
        elif container.container_type == ContainerType.QUEUE:
            for i in range(3):
                line = self.dwg.line(
                    start=(container.x + 20 + (i * 40), container.y + 20),
                    end=(container.x + 20 + (i * 40), container.y + 80),
                    stroke='#000000',
                    stroke_width=3
                )
                group.add(line)
                
        # Add container name
        text = self.dwg.text(
            container.name,
            insert=(container.x + 75, container.y + 50),
            font_size=12,
            text_anchor='middle',
            fill='#000000'
        )
        group.add(text)
        
        return group
    
    def _draw_dependencies(self) -> None:
        """Draw dependency arrows between containers."""
        for container in self.containers:
            for dep_name in container.dependencies:
                source = next(c for c in self.containers if c.name == container.name)
                target = next(c for c in self.containers if c.name == dep_name)
                
                # Simple arrow drawing
                line = self.dwg.line(
                    start=(source.x + 75, source.y + 100),
                    end=(target.x + 75, target.y),
                    stroke='#000000',
                    stroke_width=2,
                    stroke_dasharray='5,5' if container.container_type == ContainerType.QUEUE else None
                )
                self.dwg.add(line)
                
                # Arrow head
                marker = self.dwg.marker(
                    insert=(5, 5),
                    size=(10, 10),
                    orient='auto',
                    markerUnits='strokeWidth',
                    id=f'arrow-{container.name}-{dep_name}'
                )
                marker.add(self.dwg.path(d='M0,0 L10,5 L0,10 Z', fill='#000000'))
                self.dwg.defs.add(marker)
                line['marker-end'] = marker.get_funciri()
    
    def generate_diagram(self) -> None:
        """
        Generate the final diagram with all containers and dependencies.
        Follows patent drawing best practices:
        - Clear labeling
        - Consistent styling
        - Minimal visual clutter
        - Proper spacing
        - Standardized shapes
        """
        # Add title
        title_text = self.dwg.text(
            self.title,
            insert=(self.width // 2, 30),
            font_size=20,
            text_anchor='middle',
            fill='#000000'
        )
        self.dwg.add(title_text)
        
        # Position containers in a grid
        cols = 3
        for i, container in enumerate(self.containers):
            row = i // cols
            col = i % cols
            container.x = 200 + (col * 300)
            container.y = 100 + (row * 200)
            
            # Add container to diagram
            self.dwg.add(self._get_container_shape(container))
        
        # Draw dependencies
        self._draw_dependencies()
        
        # Save the diagram
        self.dwg.save()
        
    @staticmethod
    def validate_container_positions(containers: List[Container]) -> bool:
        """
        Validate that containers don't overlap and have proper spacing.
        
        Args:
            containers: List of containers to validate
            
        Returns:
            bool: True if positions are valid, False otherwise
        """
        for i, c1 in enumerate(containers):
            for c2 in containers[i+1:]:
                if (abs(c1.x - c2.x) < 160 and abs(c1.y - c2.y) < 120):
                    return False
        return True

# Example usage
if __name__ == "__main__":
    diagram = ContainerDiagramGenerator("E-Commerce System Architecture")
    
    # Add containers following patent drawing best practices
    diagram.add_container(Container(
        name="Web Frontend",
        container_type=ContainerType.APPLICATION,
        description="Customer-facing web application",
        dependencies=["API Gateway"]
    ))
    
    diagram.add_container(Container(
        name="API Gateway",
        container_type=ContainerType.API_GATEWAY,
        description="Routes requests to microservices",
        dependencies=["Product Service", "Order Service"]
    ))
    
    diagram.add_container(Container(
        name="Product Service",
        container_type=ContainerType.MICROSERVICE,
        description="Handles product catalog",
        dependencies=["Product DB"]
    ))
    
    diagram.add_container(Container(
        name="Order Service",
        container_type=ContainerType.MICROSERVICE,
        description="Processes customer orders",
        dependencies=["Order DB", "Payment Queue"]
    ))
    
    diagram.add_container(Container(
        name="Product DB",
        container_type=ContainerType.DATABASE,
        description="Stores product information",
        dependencies=[]
    ))
    
    diagram.add_container(Container(
        name="Order DB",
        container_type=ContainerType.DATABASE,
        description="Stores order information",
        dependencies=[]
    ))
    
    diagram.add_container(Container(
        name="Payment Queue",
        container_type=ContainerType.QUEUE,
        description="Processes payment transactions asynchronously",
        dependencies=["Payment Service"]
    ))
    
    # Generate and save the diagram
    diagram.generate_diagram()
```
