"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Develop a use case for a Geographic Information System (GIS) to manage and analyze geological and geotechnical data for construction projects, similar to those undertaken by URANPRES, s.r.o."
Generated: DETERMINISTIC_074c24ca2361e0ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from typing import Dict, List, Optional
from datetime import datetime
import geopandas as gpd
from shapely.geometry import Point, Polygon
import pyproj
from sqlalchemy import create_engine, Column, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database model
Base = declarative_base()

class Project(Base):
    """Represents a construction project with geotechnical data."""
    __tablename__ = 'projects'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    location = Column(JSON)  # GeoJSON format
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    geological_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class GISManager:
    """Manages GIS operations for geological and geotechnical data."""
    
    def __init__(self, db_uri: str):
        """Initialize GIS manager with database connection."""
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.crs = pyproj.CRS.from_epsg(4326)  # WGS84
    
    def create_project(self, name: str, description: str, location: Dict,
                      start_date: datetime, end_date: datetime) -> Project:
        """Create a new construction project."""
        session = self.Session()
        try:
            project = Project(
                id=str(uuid.uuid4()),
                name=name,
                description=description,
                location=location,
                start_date=start_date,
                end_date=end_date
            )
            session.add(project)
            session.commit()
            return project
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def add_geological_data(self, project_id: str, data: Dict) -> Project:
        """Add geological data to a project."""
        session = self.Session()
        try:
            project = session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise ValueError("Project not found")
            
            project.geological_data = data
            session.commit()
            return project
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def get_projects_in_area(self, polygon: Polygon) -> List[Project]:
        """Get projects within a specified geographic area."""
        session = self.Session()
        try:
            projects = session.query(Project).all()
            gdf = gpd.GeoDataFrame.from_records(
                [{
                    'id': p.id,
                    'name': p.name,
                    'geometry': Point(p.location['coordinates'])
                } for p in projects],
                crs=self.crs
            )
            
            area_gdf = gpd.GeoDataFrame(geometry=[polygon], crs=self.crs)
            projects_in_area = gdf[gdf.within(area_gdf.unary_union)]
            
            return [session.query(Project).get(pid) for pid in projects_in_area['id']]
        except Exception as e:
            raise e
        finally:
            session.close()
    
    def analyze_geotechnical_risks(self, project_id: str) -> Dict:
        """Analyze geotechnical risks for a project."""
        session = self.Session()
        try:
            project = session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise ValueError("Project not found")
            
            if not project.geological_data:
                raise ValueError("No geological data available")
            
            # Example analysis - in a real system this would be more sophisticated
            risk_score = 0
            data = project.geological_data
            
            if data.get('soil_type') == 'clay':
                risk_score += 30
            if data.get('water_table') < 2.0:  # meters
                risk_score += 20
            if data.get('slope_angle', 0) > 15:  # degrees
                risk_score += 25
            
            return {
                'risk_score': risk_score,
                'risk_level': 'High' if risk_score > 50 else 'Medium' if risk_score > 25 else 'Low',
                'recommendations': self._generate_recommendations(risk_score)
            }
        except Exception as e:
            raise e
        finally:
            session.close()
    
    def _generate_recommendations(self, risk_score: int) -> List[str]:
        """Generate recommendations based on risk score."""
        recommendations = []
        if risk_score > 50:
            recommendations.extend([
                "Conduct detailed geotechnical investigation",
                "Consider deep foundation solutions",
                "Implement extensive drainage systems"
            ])
        elif risk_score > 25:
            recommendations.extend([
                "Perform additional soil testing",
                "Consider shallow foundation with reinforcement",
                "Monitor water table levels"
            ])
        else:
            recommendations.append("Standard construction practices should be sufficient")
        
        return recommendations
    
    def export_project_to_geojson(self, project_id: str) -> Dict:
        """Export project data to GeoJSON format."""
        session = self.Session()
        try:
            project = session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise ValueError("Project not found")
            
            return {
                "type": "Feature",
                "properties": {
                    "name": project.name,
                    "description": project.description,
                    "start_date": project.start_date.isoformat(),
                    "end_date": project.end_date.isoformat(),
                    "geological_data": project.geological_data
                },
                "geometry": project.location
            }
        except Exception as e:
            raise e
        finally:
            session.close()

# Example usage
if __name__ == "__main__":
    # Initialize GIS manager
    gis = GISManager("sqlite:///construction_projects.db")
    
    # Create a project
    project = gis.create_project(
        name="Highway D1 Extension",
        description="Extension of highway D1 between Brno and Prague",
        location={
            "type": "Point",
            "coordinates": [16.607, 49.195]
        },
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2025, 12, 31)
    )
    
    # Add geological data
    gis.add_geological_data(project.id, {
        "soil_type": "clay",
        "water_table": 1.5,
        "slope_angle": 10,
        "bearing_capacity": 150
    })
    
    # Analyze risks
    risk_analysis = gis.analyze_geotechnical_risks(project.id)
    print("Risk Analysis:", risk_analysis)
    
    # Export to GeoJSON
    geojson = gis.export_project_to_geojson(project.id)
    print("GeoJSON:", json.dumps(geojson, indent=2))
```
