"""
Generated Code Metadata:
========================
Original URL: https://z-innovations.de
Prompt: Provide an example of a CNC programming script that could be used in a consulting project to optimize production workflows, as described by z-innovations.
Generated: DETERMINISTIC_e5162412cbd233b6
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CNC Workflow Optimization Script
Author: Z-Innovations Consulting
Date: 2023-11-15
Description: This script optimizes CNC production workflows by analyzing machining parameters,
             tool paths, and material usage to suggest improvements.
"""

import json
import math
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class CNCOptimizer:
    """
    A class to optimize CNC machining workflows by analyzing and suggesting improvements.
    """
    
    def __init__(self, config_file: str = "cnc_config.json"):
        """
        Initialize the optimizer with configuration data.
        
        Args:
            config_file: Path to JSON configuration file containing machine parameters
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            self._validate_config()
        except FileNotFoundError:
            raise ValueError(f"Configuration file {config_file} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON configuration file")
            
        self.tool_life_data = {}
        self.material_data = {}
        self._load_default_parameters()
    
    def _validate_config(self) -> None:
        """Validate the configuration file structure."""
        required_keys = ['machine_limits', 'tool_database', 'material_properties']
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
    
    def _load_default_parameters(self) -> None:
        """Load default tool life and material parameters."""
        self.tool_life_data = self.config['tool_database']
        self.material_data = self.config['material_properties']
    
    def analyze_gcode(self, gcode_file: str) -> Dict:
        """
        Analyze G-code file for optimization opportunities.
        
        Args:
            gcode_file: Path to G-code file to analyze
            
        Returns:
            Dictionary containing analysis results and recommendations
        """
        try:
            with open(gcode_file, 'r') as f:
                gcode_lines = f.readlines()
        except FileNotFoundError:
            raise ValueError(f"G-code file {gcode_file} not found")
        
        analysis = {
            'total_distance': 0.0,
            'rapid_moves': 0,
            'cutting_moves': 0,
            'tool_changes': 0,
            'estimated_time': 0.0,
            'optimization_opportunities': []
        }
        
        current_tool = None
        current_feed = 0.0
        current_speed = 0.0
        
        for line in gcode_lines:
            line = line.strip()
            if not line or line.startswith(';'):
                continue
                
            # Tool change detection
            if line.startswith('T') and 'M6' in line:
                analysis['tool_changes'] += 1
                current_tool = line.split('T')[1].split(' ')[0]
                
            # Feed rate detection
            elif 'F' in line:
                current_feed = float(line.split('F')[1].split(' ')[0])
                
            # Spindle speed detection
            elif 'S' in line:
                current_speed = float(line.split('S')[1].split(' ')[0])
                
            # Movement analysis
            elif line.startswith('G0'):
                analysis['rapid_moves'] += 1
                dist = self._calculate_move_distance(line)
                analysis['total_distance'] += dist
                analysis['estimated_time'] += dist / self.config['machine_limits']['max_rapid_feed']
                
            elif line.startswith('G1'):
                analysis['cutting_moves'] += 1
                dist = self._calculate_move_distance(line)
                analysis['total_distance'] += dist
                if current_feed > 0:
                    analysis['estimated_time'] += dist / current_feed
                
                # Check for optimization opportunities
                if current_tool and current_feed and current_speed:
                    self._check_optimization(
                        analysis, current_tool, current_feed, current_speed, line
                    )
        
        return analysis
    
    def _calculate_move_distance(self, move_command: str) -> float:
        """
        Calculate the distance of a move command.
        
        Args:
            move_command: G-code move command (G0 or G1)
            
        Returns:
            Distance in millimeters
        """
        coords = {'X': 0.0, 'Y': 0.0, 'Z': 0.0}
        for axis in coords.keys():
            if axis in move_command:
                coords[axis] = float(move_command.split(axis)[1].split(' ')[0])
        
        return math.sqrt(sum(v**2 for v in coords.values()))
    
    def _check_optimization(
        self,
        analysis: Dict,
        tool: str,
        feed: float,
        speed: float,
        command: str
    ) -> None:
        """
        Check for optimization opportunities in a cutting move.
        
        Args:
            analysis: Analysis dictionary to update with findings
            tool: Current tool ID
            feed: Current feed rate
            speed: Current spindle speed
            command: G-code command being analyzed
        """
        # Check feed/speed against tool recommendations
        tool_info = next((t for t in self.tool_life_data if t['id'] == tool), None)
        if not tool_info:
            return
            
        material = self.config.get('current_material', 'steel')
        material_info = self.material_data.get(material, {})
        
        optimizations = []
        
        # Feed rate optimization
        recommended_feed = tool_info.get('recommended_feed', {}).get(material, 0)
        if recommended_feed and abs(feed - recommended_feed) > recommended_feed * 0.2:
            optimizations.append(
                f"Adjust feed rate from {feed} to {recommended_feed} for tool {tool}"
            )
        
        # Spindle speed optimization
        recommended_speed = tool_info.get('recommended_speed', {}).get(material, 0)
        if recommended_speed and abs(speed - recommended_speed) > recommended_speed * 0.2:
            optimizations.append(
                f"Adjust spindle speed from {speed} to {recommended_speed} for tool {tool}"
            )
        
        # Tool path optimization (simple heuristic)
        if 'Z' in command and 'X' in command and 'Y' in command:
            optimizations.append(
                "Consider separate roughing and finishing passes for better tool life"
            )
        
        if optimizations:
            analysis['optimization_opportunities'].extend(optimizations)
    
    def generate_report(self, analysis: Dict, output_file: str = None) -> str:
        """
        Generate an optimization report from analysis data.
        
        Args:
            analysis: Analysis data from analyze_gcode()
            output_file: Optional file path to save report
            
        Returns:
            Formatted report string
        """
        report = [
            f"CNC Workflow Optimization Report",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "="*50,
            f"Total distance traveled: {analysis['total_distance']:.2f} mm",
            f"Rapid moves: {analysis['rapid_moves']}",
            f"Cutting moves: {analysis['cutting_moves']}",
            f"Tool changes: {analysis['tool_changes']}",
            f"Estimated machining time: {analysis['estimated_time']/60:.2f} minutes",
            "",
            "Optimization Opportunities:",
            "-"*50
        ]
        
        if analysis['optimization_opportunities']:
            for opp in analysis['optimization_opportunities']:
                report.append(f"• {opp}")
        else:
            report.append("No significant optimization opportunities found")
        
        report_str = "\n".join(report)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(report_str)
            except IOError as e:
                print(f"Warning: Could not save report to {output_file}: {str(e)}")
        
        return report_str


# Example usage
if __name__ == "__main__":
    try:
        optimizer = CNCOptimizer()
        analysis = optimizer.analyze_gcode("sample_part.nc")
        report = optimizer.generate_report(analysis, "optimization_report.txt")
        print(report)
    except Exception as e:
        print(f"Error: {str(e)}")
```
