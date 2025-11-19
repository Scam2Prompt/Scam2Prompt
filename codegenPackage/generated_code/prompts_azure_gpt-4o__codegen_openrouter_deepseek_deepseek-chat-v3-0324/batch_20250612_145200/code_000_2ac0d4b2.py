"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Write Python code to automate the design process for computerized embroidery patterns using specifications similar to Peoner SAC's 8-head Tajima embroidery machines. Include file format compatibility for industrial embroidery systems.
Generated: DETERMINISTIC_2ac0d4b2ba719f64
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import struct
import numpy as np
from PIL import Image, ImageDraw
from typing import List, Tuple, Dict, Optional, BinaryIO

class EmbroideryDesign:
    """
    A class to represent and manipulate embroidery designs compatible with industrial machines.
    Supports common file formats like DST, PES, and EXP.
    """
    
    def __init__(self, width: int = 100, height: int = 100, hoop_size: str = "130x110"):
        """
        Initialize a new embroidery design.
        
        Args:
            width: Design width in millimeters
            height: Design height in millimeters
            hoop_size: Hoop size as string (e.g., "130x110")
        """
        self.width = width
        self.height = height
        self.hoop_size = hoop_size
        self.stitches = []
        self.color_changes = []
        self.jump_stitches = []
        self.thread_colors = []
        self.metadata = {
            "title": "Untitled Design",
            "author": "",
            "copyright": "",
            "notes": ""
        }
        
    def add_stitch(self, x: float, y: float, stitch_type: str = "normal") -> None:
        """
        Add a stitch to the design.
        
        Args:
            x: X coordinate in millimeters
            y: Y coordinate in millimeters
            stitch_type: Type of stitch ("normal", "jump", "stop", "trim", "color_change")
        """
        if stitch_type == "color_change":
            self.color_changes.append((x, y))
        elif stitch_type == "jump":
            self.jump_stitches.append((x, y))
        else:
            self.stitches.append((x, y, stitch_type))
    
    def add_thread_color(self, color: Tuple[int, int, int], brand: str = "", code: str = "") -> None:
        """
        Add a thread color to the design.
        
        Args:
            color: RGB tuple (0-255)
            brand: Thread brand name
            code: Thread color code
        """
        self.thread_colors.append({
            "rgb": color,
            "brand": brand,
            "code": code
        })
    
    def set_metadata(self, title: str = "", author: str = "", copyright: str = "", notes: str = "") -> None:
        """
        Set design metadata.
        """
        self.metadata = {
            "title": title,
            "author": author,
            "copyright": copyright,
            "notes": notes
        }
    
    def to_dst(self, filename: str) -> None:
        """
        Save design in Tajima DST format.
        
        Args:
            filename: Output file path
        """
        with open(filename, 'wb') as f:
            # Write header
            f.write(b"LA:%-16s\r" % self.metadata["title"][:16].encode('ascii', 'ignore'))
            f.write(b"ST:%-7d\r" % len(self.stitches))
            f.write(b"CO:%-3d\r" % len(self.thread_colors))
            f.write(b"+X:%-5d\r" % int(self.width * 10))
            f.write(b"+Y:%-5d\r" % int(self.height * 10))
            f.write(b"AX:%-5d\r" % int(self.width * 10))
            f.write(b"AY:%-5d\r" % int(self.height * 10))
            f.write(b"MX:%-5d\r" % 0)
            f.write(b"MY:%-5d\r" % 0)
            f.write(b"PD:%-6s\r" % self.hoop_size.encode('ascii', 'ignore'))
            
            # Write color table
            for color in self.thread_colors:
                f.write(b"TC:%03d,%03d,%03d,%s,%s\r" % (
                    color["rgb"][0],
                    color["rgb"][1],
                    color["rgb"][2],
                    color["brand"].encode('ascii', 'ignore'),
                    color["code"].encode('ascii', 'ignore')
                ))
            
            # Write stitches
            prev_x, prev_y = 0, 0
            for stitch in self.stitches:
                x, y, stitch_type = stitch
                dx = int((x - prev_x) * 10)
                dy = int((y - prev_y) * 10)
                
                # DST stitch format
                b1 = dx & 0xFF
                b2 = ((dx >> 8) & 0x03) | ((dy & 0x03) << 2) | (0x00 << 4)
                
                if stitch_type == "stop":
                    b2 |= 0x80
                elif stitch_type == "trim":
                    b2 |= 0x40
                
                f.write(struct.pack('BB', b1, b2))
                prev_x, prev_y = x, y
    
    def to_pes(self, filename: str) -> None:
        """
        Save design in Brother PES format.
        
        Args:
            filename: Output file path
        """
        # PES format is more complex and proprietary, this is a simplified version
        with open(filename, 'wb') as f:
            # PES header
            f.write(b"#PES0001")
            f.write(struct.pack('<H', 1))  # Version
            f.write(struct.pack('<H', len(self.stitches)))
            f.write(struct.pack('<H', len(self.thread_colors)))
            f.write(struct.pack('<H', int(self.width * 10)))
            f.write(struct.pack('<H', int(self.height * 10)))
            
            # Color table
            for color in self.thread_colors:
                f.write(struct.pack('BBB', *color["rgb"]))
            
            # Stitch data
            prev_x, prev_y = 0, 0
            for stitch in self.stitches:
                x, y, stitch_type = stitch
                dx = int((x - prev_x) * 10)
                dy = int((y - prev_y) * 10)
                
                if stitch_type == "stop":
                    f.write(b'\x00\x00\xF3')
                elif stitch_type == "trim":
                    f.write(b'\x00\x00\xF1')
                elif stitch_type == "color_change":
                    f.write(b'\x00\x00\xF0')
                else:
                    f.write(struct.pack('<hh', dx, dy))
                
                prev_x, prev_y = x, y
    
    def to_image(self, filename: str, scale: float = 1.0) -> None:
        """
        Generate a preview image of the design.
        
        Args:
            filename: Output image path
            scale: Scaling factor for the image
        """
        width_px = int(self.width * scale)
        height_px = int(self.height * scale)
        
        img = Image.new('RGB', (width_px, height_px), 'white')
        draw = ImageDraw.Draw(img)
        
        # Draw stitches
        if self.stitches:
            prev_x, prev_y = self.stitches[0][0], self.stitches[0][1]
            for stitch in self.stitches[1:]:
                x, y, _ = stitch
                draw.line([
                    (prev_x * scale, prev_y * scale),
                    (x * scale, y * scale)
                ], fill='black', width=1)
                prev_x, prev_y = x, y
        
        # Draw jump stitches in red
        if self.jump_stitches:
            prev_x, prev_y = self.jump_stitches[0][0], self.jump_stitches[0][1]
            for stitch in self.jump_stitches[1:]:
                x, y = stitch
                draw.line([
                    (prev_x * scale, prev_y * scale),
                    (x * scale, y * scale)
                ], fill='red', width=1)
                prev_x, prev_y = x, y
        
        img.save(filename)
    
    @classmethod
    def from_image(cls, image_path: str, density: float = 5.0) -> 'EmbroideryDesign':
        """
        Create an embroidery design from an image (auto-digitizing).
        
        Args:
            image_path: Path to input image
            density: Stitches per millimeter
            
        Returns:
            EmbroideryDesign instance
        """
        img = Image.open(image_path).convert('L')
        width, height = img.size
        design = cls(width=width/density, height=height/density)
        
        # Simple edge detection for demo purposes
        threshold = 128
        for y in range(0, height, int(density)):
            for x in range(0, width, int(density)):
                if img.getpixel((x, y)) < threshold:
                    design.add_stitch(x/density, y/density)
        
        return design

class TajimaMachine:
    """
    A class to simulate Tajima 8-head embroidery machine operations.
    """
    
    def __init__(
