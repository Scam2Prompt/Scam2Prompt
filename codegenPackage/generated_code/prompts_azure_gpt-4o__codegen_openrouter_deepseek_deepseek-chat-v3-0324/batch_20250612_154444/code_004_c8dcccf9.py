"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Provide Python code for managing construction survey data and generating analytics reports, inspired by Wira Survey Consultants' project management solutions.
Generated: DETERMINISTIC_c8dcccf953ccac24
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Survey Data Management and Analytics System

This module provides functionality to manage construction survey data,
perform calculations, and generate analytical reports.
Inspired by Wira Survey Consultants' project management solutions.

Features:
- Survey data storage and retrieval
- Data validation and cleaning
- Basic survey calculations
- Report generation in multiple formats
"""

import csv
import json
import math
from datetime import datetime
from typing import List, Dict, Optional, Union
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
import matplotlib.pyplot as plt


class SurveyDataManager:
    """Core class for managing construction survey data."""
    
    def __init__(self):
        self.projects = {}
        self.current_project = None
    
    def create_project(self, project_id: str, name: str, location: str, 
                      start_date: str, client: str) -> Dict:
        """Create a new survey project.
        
        Args:
            project_id: Unique identifier for the project
            name: Project name
            location: Project location
            start_date: Project start date (YYYY-MM-DD)
            client: Client name
            
        Returns:
            Dictionary containing project details
            
        Raises:
            ValueError: If project_id already exists
        """
        if project_id in self.projects:
            raise ValueError(f"Project ID {project_id} already exists")
            
        project = {
            'id': project_id,
            'name': name,
            'location': location,
            'start_date': start_date,
            'client': client,
            'created_at': datetime.now().isoformat(),
            'survey_points': {},
            'survey_lines': {},
            'metadata': {}
        }
        
        self.projects[project_id] = project
        self.current_project = project_id
        return project
    
    def set_current_project(self, project_id: str) -> None:
        """Set the current active project.
        
        Args:
            project_id: ID of the project to set as current
            
        Raises:
            KeyError: If project_id doesn't exist
        """
        if project_id not in self.projects:
            raise KeyError(f"Project {project_id} not found")
        self.current_project = project_id
    
    def add_survey_point(self, point_id: str, northing: float, easting: float, 
                         elevation: float, description: str = "") -> Dict:
        """Add a survey point to the current project.
        
        Args:
            point_id: Unique identifier for the point
            northing: Northing coordinate
            easting: Easting coordinate
            elevation: Elevation value
            description: Optional description of the point
            
        Returns:
            Dictionary containing the point data
            
        Raises:
            RuntimeError: If no current project is set
            ValueError: If point_id already exists in project
        """
        if not self.current_project:
            raise RuntimeError("No current project set")
            
        if point_id in self.projects[self.current_project]['survey_points']:
            raise ValueError(f"Point {point_id} already exists in project")
            
        point = {
            'id': point_id,
            'northing': northing,
            'easting': easting,
            'elevation': elevation,
            'description': description,
            'timestamp': datetime.now().isoformat()
        }
        
        self.projects[self.current_project]['survey_points'][point_id] = point
        return point
    
    def add_survey_line(self, line_id: str, start_point: str, end_point: str, 
                        description: str = "") -> Dict:
        """Add a survey line connecting two points.
        
        Args:
            line_id: Unique identifier for the line
            start_point: ID of starting survey point
            end_point: ID of ending survey point
            description: Optional description of the line
            
        Returns:
            Dictionary containing the line data
            
        Raises:
            RuntimeError: If no current project is set
            ValueError: If points don't exist or line_id exists
        """
        if not self.current_project:
            raise RuntimeError("No current project set")
            
        project = self.projects[self.current_project]
        
        if start_point not in project['survey_points']:
            raise ValueError(f"Start point {start_point} not found")
        if end_point not in project['survey_points']:
            raise ValueError(f"End point {end_point} not found")
        if line_id in project['survey_lines']:
            raise ValueError(f"Line {line_id} already exists")
            
        line = {
            'id': line_id,
            'start_point': start_point,
            'end_point': end_point,
            'description': description,
            'timestamp': datetime.now().isoformat()
        }
        
        project['survey_lines'][line_id] = line
        return line
    
    def calculate_distance(self, point1_id: str, point2_id: str) -> float:
        """Calculate horizontal distance between two survey points.
        
        Args:
            point1_id: ID of first point
            point2_id: ID of second point
            
        Returns:
            Horizontal distance between the points
            
        Raises:
            RuntimeError: If no current project is set
            ValueError: If points don't exist
        """
        if not self.current_project:
            raise RuntimeError("No current project set")
            
        project = self.projects[self.current_project]
        
        if point1_id not in project['survey_points']:
            raise ValueError(f"Point {point1_id} not found")
        if point2_id not in project['survey_points']:
            raise ValueError(f"Point {point2_id} not found")
            
        p1 = project['survey_points'][point1_id]
        p2 = project['survey_points'][point2_id]
        
        dx = p2['easting'] - p1['easting']
        dy = p2['northing'] - p1['northing']
        
        return math.sqrt(dx**2 + dy**2)
    
    def calculate_slope(self, point1_id: str, point2_id: str) -> Dict:
        """Calculate slope between two survey points.
        
        Args:
            point1_id: ID of first point
            point2_id: ID of second point
            
        Returns:
            Dictionary containing:
            - horizontal_distance: Horizontal distance
            - vertical_difference: Elevation difference
            - slope_percent: Slope as percentage
            - slope_angle: Slope angle in degrees
            
        Raises:
            RuntimeError: If no current project is set
            ValueError: If points don't exist
        """
        if not self.current_project:
            raise RuntimeError("No current project set")
            
        horizontal_distance = self.calculate_distance(point1_id, point2_id)
        
        project = self.projects[self.current_project]
        p1 = project['survey_points'][point1_id]
        p2 = project['survey_points'][point2_id]
        
        vertical_diff = p2['elevation'] - p1['elevation']
        
        if horizontal_distance == 0:
            slope_percent = float('inf')
            slope_angle = 90.0
        else:
            slope_percent = (vertical_diff / horizontal_distance) * 100
            slope_angle = math.degrees(math.atan(vertical_diff / horizontal_distance))
        
        return {
            'horizontal_distance': horizontal_distance,
            'vertical_difference': vertical_diff,
            'slope_percent': slope_percent,
            'slope_angle': slope_angle
        }
    
    def export_to_csv(self, project_id: str, filename: str) -> None:
        """Export project survey points to CSV file.
        
        Args:
            project_id: ID of project to export
            filename: Output filename
            
        Raises:
            KeyError: If project doesn't exist
            IOError: If file cannot be written
        """
        if project_id not in self.projects:
            raise KeyError(f"Project {project_id} not found")
            
        project = self.projects[project_id]
        points = project['survey_points'].values()
        
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['id', 'northing', 'easting', 'elevation', 'description']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for point in points:
                    writer.writerow({
                        'id': point['id'],
                        'northing': point['northing'],
                        'easting': point['easting'],
                        'elevation': point['elevation'],
                        'description': point['description']
                    })
        except IOError as e:
            raise IOError(f"Failed to write CSV file: {str(e)}")
    
    def export_to_excel(self, project_id: str, filename: str) -> None:
        """Export project data to Excel with formatted report.
        
        Args:
            project_id: ID of project to export
            filename: Output filename
            
        Raises:
            KeyError: If project doesn't exist
            IOError: If file cannot be written
        """
        if project_id not in self.projects:
            raise KeyError(f"Project {project_id} not found")
            
        project = self.projects[
