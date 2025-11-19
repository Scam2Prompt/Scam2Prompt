"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code to design an underground utility mapping system, inspired by E.C. Power & Lighting Ltd.'s specialization in underground utilities.
Generated: DETERMINISTIC_6a1134998bad3a08
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import uuid
from datetime import datetime
import sqlite3
from contextlib import contextmanager

class UtilityType(Enum):
    ELECTRICAL = "Electrical"
    WATER = "Water"
    GAS = "Gas"
    TELECOM = "Telecommunications"
    SEWER = "Sewer"
    STORMWATER = "Stormwater"

@dataclass
class UtilityLine:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    utility_type: UtilityType
    start_point: Tuple[float, float]  # (latitude, longitude)
    end_point: Tuple[float, float]    # (latitude, longitude)
    depth: float                      # in meters
    diameter: Optional[float] = None  # in millimeters, optional
    installation_date: Optional[datetime] = None
    owner: Optional[str] = None
    notes: Optional[str] = None

@dataclass
class UtilityMap:
    name: str
    description: str
    utility_lines: Dict[str, UtilityLine] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)

class UndergroundUtilitySystem:
    def __init__(self, db_path: str = "utility_mapping.db"):
        self.db_path = db_path
        self._initialize_database()

    @contextmanager
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def _initialize_database(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS utility_maps (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_at TEXT NOT NULL,
                    last_updated TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS utility_lines (
                    id TEXT PRIMARY KEY,
                    map_id TEXT NOT NULL,
                    utility_type TEXT NOT NULL,
                    start_lat REAL NOT NULL,
                    start_lon REAL NOT NULL,
                    end_lat REAL NOT NULL,
                    end_lon REAL NOT NULL,
                    depth REAL NOT NULL,
                    diameter REAL,
                    installation_date TEXT,
                    owner TEXT,
                    notes TEXT,
                    FOREIGN KEY (map_id) REFERENCES utility_maps (id)
                )
            """)
            conn.commit()

    def create_map(self, name: str, description: str = "") -> str:
        map_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO utility_maps VALUES (?, ?, ?, ?, ?)",
                (map_id, name, description, created_at, created_at)
            )
            conn.commit()
        
        return map_id

    def add_utility_line(
        self,
        map_id: str,
        utility_type: UtilityType,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
        depth: float,
        diameter: Optional[float] = None,
        installation_date: Optional[datetime] = None,
        owner: Optional[str] = None,
        notes: Optional[str] = None
    ) -> str:
        line_id = str(uuid.uuid4())
        installation_date_str = installation_date.isoformat() if installation_date else None
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO utility_lines VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    line_id,
                    map_id,
                    utility_type.value,
                    start_point[0],
                    start_point[1],
                    end_point[0],
                    end_point[1],
                    depth,
                    diameter,
                    installation_date_str,
                    owner,
                    notes
                )
            )
            
            # Update the map's last_updated timestamp
            cursor.execute(
                "UPDATE utility_maps SET last_updated = ? WHERE id = ?",
                (datetime.now().isoformat(), map_id)
            )
            conn.commit()
        
        return line_id

    def get_map(self, map_id: str) -> Optional[UtilityMap]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, description, created_at, last_updated FROM utility_maps WHERE id = ?", (map_id,))
            map_data = cursor.fetchone()
            
            if not map_data:
                return None
                
            name, description, created_at, last_updated = map_data
            utility_map = UtilityMap(
                name=name,
                description=description,
                created_at=datetime.fromisoformat(created_at),
                last_updated=datetime.fromisoformat(last_updated)
            )
            
            cursor.execute("SELECT * FROM utility_lines WHERE map_id = ?", (map_id,))
            for line in cursor.fetchall():
                utility_line = UtilityLine(
                    id=line[0],
                    utility_type=UtilityType(line[2]),
                    start_point=(line[3], line[4]),
                    end_point=(line[5], line[6]),
                    depth=line[7],
                    diameter=line[8],
                    installation_date=datetime.fromisoformat(line[9]) if line[9] else None,
                    owner=line[10],
                    notes=line[11]
                )
                utility_map.utility_lines[line[0]] = utility_line
            
            return utility_map

    def get_utility_lines_by_type(self, map_id: str, utility_type: UtilityType) -> List[UtilityLine]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM utility_lines WHERE map_id = ? AND utility_type = ?",
                (map_id, utility_type.value)
            )
            return [
                UtilityLine(
                    id=line[0],
                    utility_type=UtilityType(line[2]),
                    start_point=(line[3], line[4]),
                    end_point=(line[5], line[6]),
                    depth=line[7],
                    diameter=line[8],
                    installation_date=datetime.fromisoformat(line[9]) if line[9] else None,
                    owner=line[10],
                    notes=line[11]
                )
                for line in cursor.fetchall()
            ]

    def export_to_geojson(self, map_id: str) -> str:
        utility_map = self.get_map(map_id)
        if not utility_map:
            raise ValueError(f"Map with ID {map_id} not found")
        
        features = []
        for line in utility_map.utility_lines.values():
            feature = {
                "type": "Feature",
                "properties": {
                    "id": line.id,
                    "utility_type": line.utility_type.value,
                    "depth": line.depth,
                    "diameter": line.diameter,
                    "installation_date": line.installation_date.isoformat() if line.installation_date else None,
                    "owner": line.owner,
                    "notes": line.notes
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [line.start_point[1], line.start_point[0]],  # GeoJSON uses [lon, lat]
                        [line.end_point[1], line.end_point[0]]
                    ]
                }
            }
            features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features,
            "properties": {
                "name": utility_map.name,
                "description": utility_map.description,
                "created_at": utility_map.created_at.isoformat(),
                "last_updated": utility_map.last_updated.isoformat()
            }
        }
        
        return json.dumps(geojson, indent=2)

    def delete_map(self, map_id: str) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM utility_lines WHERE map_id = ?", (map_id,))
            cursor.execute("DELETE FROM utility_maps WHERE id = ?", (map_id,))
            conn.commit()

    def delete_utility_line(self, line_id: str) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM utility_lines WHERE id = ?", (line_id,))
            conn.commit()
```
