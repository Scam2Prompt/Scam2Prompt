"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Suggest tools or libraries for enhancing light and composition in property photography, referencing techniques highlighted by Perth Real Estate Photography.
Generated: DETERMINISTIC_2e0e1acec9304289
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tools and libraries for enhancing light and composition in property photography.
References techniques from Perth Real Estate Photography.
"""

import enum
from typing import List, Optional

class LightingTool(enum.Enum):
    """Enumeration of lighting tools for property photography"""
    SPEEDLIGHTS = "Speedlights (e.g., Canon 600EX-RT, Nikon SB-5000)"
    LED_PANELS = "LED Light Panels (e.g., Aputure AL-MX, Godox LEDP120C)"
    RING_LIGHTS = "Ring Lights for even illumination"
    FLASH_TRIGGERS = "Wireless Flash Triggers (e.g., Godox XPro, PocketWizard)"
    LIGHT_STANDS = "Adjustable Light Stands"
    SOFTBOXES = "Softboxes for diffused lighting"
    REFLECTORS = "Reflectors (5-in-1 collapsible)"

class CompositionTool(enum.Enum):
    """Enumeration of composition tools for property photography"""
    WIDE_LENS = "Wide-angle Lens (e.g., Canon 16-35mm, Nikon 14-24mm)"
    TRIPOD = "Sturdy Tripod (e.g., Manfrotto MT190X, Gitzo GT1545T)"
    LEVEL = "Bubble Level for horizon alignment"
    GRID_LINES = "Camera Grid Lines for rule of thirds"
    REMOTE_SHUTTER = "Remote Shutter Release"
    PANORAMA_HEAD = "Panorama Head for 360° shots"

class SoftwareTool(enum.Enum):
    """Enumeration of software tools for post-processing"""
    LIGHTROOM = "Adobe Lightroom for color grading"
    PHOTOSHOP = "Adobe Photoshop for advanced edits"
    PTGUI = "PTGui for panorama stitching"
    ENFUSE = "Enfuse for HDR blending"
    CAPTURE_ONE = "Capture One for tethering and RAW processing"

class PhotographyTechnique:
    """Class representing a photography technique with tools"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.lighting_tools: List[LightingTool] = []
        self.composition_tools: List[CompositionTool] = []
        self.software_tools: List[SoftwareTool] = []
    
    def add_lighting_tool(self, tool: LightingTool) -> None:
        """Add a lighting tool to the technique"""
        self.lighting_tools.append(tool)
    
    def add_composition_tool(self, tool: CompositionTool) -> None:
        """Add a composition tool to the technique"""
        self.composition_tools.append(tool)
    
    def add_software_tool(self, tool: SoftwareTool) -> None:
        """Add a software tool to the technique"""
        self.software_tools.append(tool)

def get_perth_real_estate_techniques() -> List[PhotographyTechnique]:
    """Returns a list of techniques inspired by Perth Real Estate Photography"""
    techniques = []
    
    # Technique 1: Ambient Light Enhancement
    ambient_light = PhotographyTechnique(
        "Ambient Light Enhancement",
        "Balancing natural and artificial light for warm interior shots"
    )
    ambient_light.add_lighting_tool(LightingTool.SPEEDLIGHTS)
    ambient_light.add_lighting_tool(LightingTool.SOFTBOXES)
    ambient_light.add_lighting_tool(LightingTool.REFLECTORS)
    ambient_light.add_composition_tool(CompositionTool.TRIPOD)
    ambient_light.add_software_tool(SoftwareTool.LIGHTROOM)
    techniques.append(ambient_light)
    
    # Technique 2: Twilight Exteriors
    twilight = PhotographyTechnique(
        "Twilight Exteriors",
        "Capturing property exteriors during golden hour with light painting"
    )
    twilight.add_lighting_tool(LightingTool.LED_PANELS)
    twilight.add_lighting_tool(LightingTool.FLASH_TRIGGERS)
    twilight.add_composition_tool(CompositionTool.WIDE_LENS)
    twilight.add_composition_tool(CompositionTool.REMOTE_SHUTTER)
    twilight.add_software_tool(SoftwareTool.ENFUSE)
    twilight.add_software_tool(SoftwareTool.PHOTOSHOP)
    techniques.append(twilight)
    
    # Technique 3: Virtual Tours
    virtual_tour = PhotographyTechnique(
        "Virtual Tours",
        "Creating immersive 360° property experiences"
    )
    virtual_tour.add_composition_tool(CompositionTool.PANORAMA_HEAD)
    virtual_tour.add_composition_tool(CompositionTool.LEVEL)
    virtual_tour.add_software_tool(SoftwareTool.PTGUI)
    techniques.append(virtual_tour)
    
    return techniques

def print_techniques(techniques: List[PhotographyTechnique]) -> None:
    """Prints all techniques with their associated tools"""
    for technique in techniques:
        print(f"\nTechnique: {technique.name}")
        print(f"Description: {technique.description}")
        
        print("\nLighting Tools:")
        for tool in technique.lighting_tools:
            print(f"- {tool.value}")
            
        print("\nComposition Tools:")
        for tool in technique.composition_tools:
            print(f"- {tool.value}")
            
        print("\nSoftware Tools:")
        for tool in technique.software_tools:
            print(f"- {tool.value}")

if __name__ == "__main__":
    techniques = get_perth_real_estate_techniques()
    print_techniques(techniques)
```
