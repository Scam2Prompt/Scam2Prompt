"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Generate a script to create team/organization charts in PowerPoint using templates similar to those provided by SlidesGeek.
Generated: DETERMINISTIC_66ce83dc6660427f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from typing import List, Dict, Optional

class OrganizationChartGenerator:
    """
    A class to generate organization charts in PowerPoint using templates.
    """

    def __init__(self, template_path: str):
        """
        Initialize with a PowerPoint template file.

        Args:
            template_path (str): Path to the PowerPoint template file (.pptx)
        """
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template file not found: {template_path}")
        
        self.presentation = Presentation(template_path)
        self.slide_layout = self._get_slide_layout_by_name("Organization Chart")
        if not self.slide_layout:
            raise ValueError("Template must contain a slide layout named 'Organization Chart'")

    def _get_slide_layout_by_name(self, layout_name: str) -> Optional[int]:
        """
        Find slide layout index by name.

        Args:
            layout_name (str): Name of the layout to find

        Returns:
            Optional[int]: Index of the layout if found, None otherwise
        """
        for idx, layout in enumerate(self.presentation.slide_layouts):
            if layout.name == layout_name:
                return idx
        return None

    def _add_textbox(self, slide, text: str, left: float, top: float, width: float, height: float, 
                    font_size: int = 12, is_bold: bool = False, 
                    text_color: RGBColor = RGBColor(0, 0, 0),
                    bg_color: Optional[RGBColor] = None) -> None:
        """
        Add a textbox to a slide with specified formatting.

        Args:
            slide: PowerPoint slide object
            text (str): Text content
            left (float): Left position in inches
            top (float): Top position in inches
            width (float): Width in inches
            height (float): Height in inches
            font_size (int): Font size in points
            is_bold (bool): Whether text should be bold
            text_color (RGBColor): Text color
            bg_color (Optional[RGBColor]): Background color
        """
        textbox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
        text_frame = textbox.text_frame
        text_frame.word_wrap = True
        paragraph = text_frame.paragraphs[0]
        paragraph.alignment = PP_ALIGN.CENTER
        run = paragraph.add_run()
        run.text = text
        run.font.size = Pt(font_size)
        run.font.bold = is_bold
        run.font.color.rgb = text_color

        if bg_color:
            fill = textbox.fill
            fill.solid()
            fill.fore_color.rgb = bg_color

    def _add_connector(self, slide, start_x: float, start_y: float, end_x: float, end_y: float, 
                      line_width: float = 0.75, line_color: RGBColor = RGBColor(89, 89, 89)) -> None:
        """
        Add a connector line between two points.

        Args:
            slide: PowerPoint slide object
            start_x (float): Start x position in inches
            start_y (float): Start y position in inches
            end_x (float): End x position in inches
            end_y (float): End y position in inches
            line_width (float): Line width in points
            line_color (RGBColor): Line color
        """
        line = slide.shapes.add_connector(
            MSO_SHAPE.STRAIGHT_CONNECTOR_1, 
            Inches(start_x), 
            Inches(start_y), 
            Inches(end_x), 
            Inches(end_y)
        )
        line.line.width = Pt(line_width)
        line.line.color.rgb = line_color

    def _add_rounded_rectangle(self, slide, left: float, top: float, width: float, height: float, 
                             fill_color: RGBColor = RGBColor(255, 255, 255),
                             line_color: RGBColor = RGBColor(89, 89, 89),
                             line_width: float = 0.75) -> None:
        """
        Add a rounded rectangle shape.

        Args:
            slide: PowerPoint slide object
            left (float): Left position in inches
            top (float): Top position in inches
            width (float): Width in inches
            height (float): Height in inches
            fill_color (RGBColor): Fill color
            line_color (RGBColor): Line color
            line_width (float): Line width in points
        """
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(left), Inches(top), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
        shape.line.color.rgb = line_color
        shape.line.width = Pt(line_width)
        return shape

    def generate_org_chart(self, hierarchy: List[Dict], output_path: str) -> None:
        """
        Generate an organization chart PowerPoint slide.

        Args:
            hierarchy (List[Dict]): Organizational hierarchy data
            output_path (str): Path to save the output PowerPoint file
        """
        if not hierarchy:
            raise ValueError("Hierarchy data cannot be empty")

        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[self.slide_layout])
        
        # Clear any placeholder shapes
        for shape in slide.shapes:
            if shape.has_text_frame and not shape.text:
                sp = shape._element
                sp.getparent().remove(sp)

        # Calculate positions
        levels = self._calculate_levels(hierarchy)
        positions = self._calculate_positions(levels)

        # Draw the chart
        self._draw_chart(slide, hierarchy, positions)

        # Save the presentation
        self.presentation.save(output_path)

    def _calculate_levels(self, hierarchy: List[Dict], level: int = 0) -> List[Dict]:
        """
        Calculate hierarchical levels for each node.

        Args:
            hierarchy (List[Dict]): Organizational hierarchy data
            level (int): Current level (starts at 0)

        Returns:
            List[Dict]: Hierarchy with level information
        """
        for node in hierarchy:
            node['level'] = level
            if 'children' in node and node['children']:
                self._calculate_levels(node['children'], level + 1)
        return hierarchy

    def _calculate_positions(self, hierarchy: List[Dict], 
                           start_x: float = 1.0, 
                           start_y: float = 1.0, 
                           node_width: float = 2.0, 
                           node_height: float = 1.0, 
                           h_spacing: float = 1.0, 
                           v_spacing: float = 1.5) -> Dict[str, tuple]:
        """
        Calculate positions for each node in the hierarchy.

        Args:
            hierarchy (List[Dict]): Organizational hierarchy data
            start_x (float): Starting x position
            start_y (float): Starting y position
            node_width (float): Width of each node
            node_height (float): Height of each node
            h_spacing (float): Horizontal spacing between nodes
            v_spacing (float): Vertical spacing between levels

        Returns:
            Dict[str, tuple]: Dictionary mapping node IDs to (left, top) positions
        """
        positions = {}
        current_x = start_x
        max_level = max(node['level'] for node in hierarchy)

        # Calculate positions for each level
        for level in range(max_level + 1):
            level_nodes = [node for node in hierarchy if node['level'] == level]
            total_width = len(level_nodes) * node_width + (len(level_nodes) - 1) * h_spacing
            current_x = (10 - total_width) / 2  # Center the level

            for node in level_nodes:
                positions[node['id']] = (current_x, start_y + level * v_spacing)
                current_x += node_width + h_spacing

                # Calculate positions for children
                if 'children' in node and node['children']:
                    child_positions = self._calculate_positions(
                        node['children'], 
                        start_x, 
                        start_y + (level + 1) * v_spacing,
                        node_width,
                        node_height,
                        h_spacing,
                        v_spacing
                    )
                    positions.update(child_positions)

        return positions

    def _draw_chart(self, slide, hierarchy: List[Dict], positions: Dict[str, tuple]) -> None:
        """
        Draw the organization chart on the slide.

        Args:
            slide: PowerPoint slide object
            hierarchy (List[Dict]): Organizational hierarchy data
            positions (Dict[str, tuple]): Node positions
        """
        # Draw all nodes first
        node_shapes = {}
        for node in hierarchy:
            if node['id'] in positions:
                left, top = positions[node
