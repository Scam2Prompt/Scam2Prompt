"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Write a Python script to manage industrial part cleaning services, including scheduling pick-up, delivery, and ultrasonic cleaning, considering factors like part material, contaminant type, and desired cleanliness level."
Generated: DETERMINISTIC_ac5af412d17b7c25
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import uuid


class CleaningMethod(Enum):
    ULTRASONIC = "Ultrasonic"
    CHEMICAL = "Chemical"
    MANUAL = "Manual"


class MaterialType(Enum):
    METAL = "Metal"
    PLASTIC = "Plastic"
    CERAMIC = "Ceramic"
    COMPOSITE = "Composite"


class ContaminantType(Enum):
    GREASE = "Grease"
    RUST = "Rust"
    PAINT = "Paint"
    DUST = "Dust"
    CHEMICAL_RESIDUE = "Chemical Residue"


class CleanlinessLevel(Enum):
    STANDARD = "Standard"
    HIGH = "High"
    SURGICAL = "Surgical"


@dataclass
class Part:
    id: str
    name: str
    material: MaterialType
    dimensions: Dict[str, float]
    weight: float
    contaminant: ContaminantType
    cleanliness_required: CleanlinessLevel


@dataclass
class CleaningService:
    method: CleaningMethod
    duration_minutes: int
    chemicals_used: Optional[List[str]] = None


@dataclass
class ServiceRequest:
    id: str
    parts: List[Part]
    cleaning_service: CleaningService
    pickup_time: datetime.datetime
    delivery_time: datetime.datetime
    customer_id: str
    status: str = "Pending"


class CleaningServiceManager:
    def __init__(self):
        self.service_requests: Dict[str, ServiceRequest] = {}
        self.cleaning_methods_map = {
            MaterialType.METAL: [CleaningMethod.ULTRASONIC, CleaningMethod.CHEMICAL],
            MaterialType.PLASTIC: [CleaningMethod.CHEMICAL, CleaningMethod.MANUAL],
            MaterialType.CERAMIC: [CleaningMethod.ULTRASONIC, CleaningMethod.MANUAL],
            MaterialType.COMPOSITE: [CleaningMethod.MANUAL]
        }
        self.cleaning_duration_map = {
            CleanlinessLevel.STANDARD: 30,
            CleanlinessLevel.HIGH: 60,
            CleanlinessLevel.SURGICAL: 120
        }

    def create_service_request(
        self,
        parts: List[Part],
        pickup_time: datetime.datetime,
        delivery_time: datetime.datetime,
        customer_id: str
    ) -> ServiceRequest:
        if delivery_time <= pickup_time:
            raise ValueError("Delivery time must be after pickup time")

        if not parts:
            raise ValueError("At least one part must be specified")

        cleaning_methods = set()
        cleanliness_levels = set()
        for part in parts:
            cleaning_methods.update(self.cleaning_methods_map[part.material])
            cleanliness_levels.add(part.cleanliness_required)

        if len(cleaning_methods) > 1:
            raise ValueError("All parts must be cleanable with the same method")

        cleaning_method = cleaning_methods.pop()
        max_duration = max([self.cleaning_duration_map[level] for level in cleanliness_levels])

        cleaning_service = CleaningService(
            method=cleaning_method,
            duration_minutes=max_duration,
            chemicals_used=self._get_chemicals_for_contaminants(parts)
        )

        service_request = ServiceRequest(
            id=str(uuid.uuid4()),
            parts=parts,
            cleaning_service=cleaning_service,
            pickup_time=pickup_time,
            delivery_time=delivery_time,
            customer_id=customer_id
        )

        self.service_requests[service_request.id] = service_request
        return service_request

    def _get_chemicals_for_contaminants(self, parts: List[Part]) -> Optional[List[str]]:
        contaminants = {part.contaminant for part in parts}
        chemicals = []

        if ContaminantType.GREASE in contaminants:
            chemicals.append("Degreaser-2000")
        if ContaminantType.RUST in contaminants:
            chemicals.append("RustRemover-XL")
        if ContaminantType.PAINT in contaminants:
            chemicals.append("PaintStrip-Pro")
        if ContaminantType.CHEMICAL_RESIDUE in contaminants:
            chemicals.append("Neutralizer-Z")

        return chemicals if chemicals else None

    def update_service_status(self, request_id: str, status: str) -> None:
        if request_id not in self.service_requests:
            raise ValueError("Service request not found")
        self.service_requests[request_id].status = status

    def get_service_request(self, request_id: str) -> ServiceRequest:
        if request_id not in self.service_requests:
            raise ValueError("Service request not found")
        return self.service_requests[request_id]

    def get_all_service_requests(self) -> List[ServiceRequest]:
        return list(self.service_requests.values())

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump({
                "service_requests": {
                    req_id: {
                        "id": req.id,
                        "parts": [{
                            "id": part.id,
                            "name": part.name,
                            "material": part.material.value,
                            "dimensions": part.dimensions,
                            "weight": part.weight,
                            "contaminant": part.contaminant.value,
                            "cleanliness_required": part.cleanliness_required.value
                        } for part in req.parts],
                        "cleaning_service": {
                            "method": req.cleaning_service.method.value,
                            "duration_minutes": req.cleaning_service.duration_minutes,
                            "chemicals_used": req.cleaning_service.chemicals_used
                        },
                        "pickup_time": req.pickup_time.isoformat(),
                        "delivery_time": req.delivery_time.isoformat(),
                        "customer_id": req.customer_id,
                        "status": req.status
                    } for req_id, req in self.service_requests.items()
                }
            }, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)
            self.service_requests = {}
            for req_id, req_data in data["service_requests"].items():
                parts = [
                    Part(
                        id=part["id"],
                        name=part["name"],
                        material=MaterialType(part["material"]),
                        dimensions=part["dimensions"],
                        weight=part["weight"],
                        contaminant=ContaminantType(part["contaminant"]),
                        cleanliness_required=CleanlinessLevel(part["cleanliness_required"])
                    ) for part in req_data["parts"]
                ]
                cleaning_service = CleaningService(
                    method=CleaningMethod(req_data["cleaning_service"]["method"]),
                    duration_minutes=req_data["cleaning_service"]["duration_minutes"],
                    chemicals_used=req_data["cleaning_service"]["chemicals_used"]
                )
                self.service_requests[req_id] = ServiceRequest(
                    id=req_data["id"],
                    parts=parts,
                    cleaning_service=cleaning_service,
                    pickup_time=datetime.datetime.fromisoformat(req_data["pickup_time"]),
                    delivery_time=datetime.datetime.fromisoformat(req_data["delivery_time"]),
                    customer_id=req_data["customer_id"],
                    status=req_data["status"]
                )


# Example usage
if __name__ == "__main__":
    manager = CleaningServiceManager()

    # Create some parts
    part1 = Part(
        id="part-001",
        name="Gear Shaft",
        material=MaterialType.METAL,
        dimensions={"length": 10.5, "diameter": 2.3},
        weight=1.2,
        contaminant=ContaminantType.GREASE,
        cleanliness_required=CleanlinessLevel.HIGH
    )

    part2 = Part(
        id="part-002",
        name="Bearing Housing",
        material=MaterialType.METAL,
        dimensions={"length": 8.0, "width": 8.0, "height": 5.0},
        weight=0.8,
        contaminant=ContaminantType.RUST,
        cleanliness_required=CleanlinessLevel.STANDARD
    )

    # Create a service request
    pickup_time = datetime.datetime.now() + datetime.timedelta(days=1)
    delivery_time = pickup_time + datetime.timedelta(hours=2)

    try:
        service_request = manager.create_service_request(
            parts=[part1, part2],
            pickup_time=pickup_time,
            delivery_time=delivery_time,
            customer_id="cust-123"
        )
        print(f"Created service request: {service_request.id}")

        # Update status
        manager.update_service_status(service_request.id, "In Progress")
        print(f"Updated status to: {manager.get_service_request(service_request.id).status}")

        # Save to file
        manager.save_to_file("service_requests.json")
        print("Saved service requests to file")

    except ValueError as e:
        print(f"Error: {e}")
```
