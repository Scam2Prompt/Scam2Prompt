"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Write Python code to design a basic SG-SST (Sistema de Gestión de Seguridad y Salud en el Trabajo) framework that aligns with the PHVA cycle of continuous improvement, as described on the GESEC website.
Generated: DETERMINISTIC_4a5717fb97a1f6e1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Union
from enum import Enum, auto

class Phase(Enum):
    """Represents the PHVA cycle phases"""
    PLAN = auto()
    DO = auto()
    CHECK = auto()
    ACT = auto()

class DocumentType(Enum):
    """Types of documents in the SG-SST system"""
    POLICY = "Política"
    PROCEDURE = "Procedimiento"
    RECORD = "Registro"
    REPORT = "Informe"

class RiskLevel(Enum):
    """Risk assessment levels"""
    LOW = "Bajo"
    MEDIUM = "Medio"
    HIGH = "Alto"
    CRITICAL = "Crítico"

class SGSST:
    """Basic SG-SST framework implementing PHVA cycle"""
    
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.documents: Dict[str, Dict] = {}
        self.risks: Dict[str, Dict] = {}
        self.improvement_actions: List[Dict] = []
        self.audits: List[Dict] = []
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        
    def add_document(self, doc_id: str, doc_type: DocumentType, 
                    title: str, content: str, phase: Phase) -> bool:
        """Add a document to the SG-SST system"""
        if doc_id in self.documents:
            return False
            
        self.documents[doc_id] = {
            "id": doc_id,
            "type": doc_type.value,
            "title": title,
            "content": content,
            "phase": phase.name,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
        return True
    
    def update_document(self, doc_id: str, content: str) -> bool:
        """Update an existing document"""
        if doc_id not in self.documents:
            return False
            
        self.documents[doc_id]["content"] = content
        self.documents[doc_id]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        return True
    
    def identify_risk(self, risk_id: str, description: str, 
                     level: RiskLevel, affected_area: str) -> bool:
        """Identify and register a new risk"""
        if risk_id in self.risks:
            return False
            
        self.risks[risk_id] = {
            "id": risk_id,
            "description": description,
            "level": level.value,
            "affected_area": affected_area,
            "date_identified": datetime.now().strftime("%Y-%m-%d"),
            "mitigation_plan": "",
            "status": "Identificado"
        }
        return True
    
    def add_mitigation_plan(self, risk_id: str, plan: str) -> bool:
        """Add mitigation plan to an identified risk"""
        if risk_id not in self.risks:
            return False
            
        self.risks[risk_id]["mitigation_plan"] = plan
        self.risks[risk_id]["status"] = "Mitigación planificada"
        return True
    
    def register_improvement_action(self, description: str, 
                                  responsible: str, deadline: str, 
                                  phase: Phase) -> bool:
        """Register an improvement action"""
        action_id = f"IA-{len(self.improvement_actions)+1:04d}"
        self.improvement_actions.append({
            "id": action_id,
            "description": description,
            "responsible": responsible,
            "deadline": deadline,
            "phase": phase.name,
            "status": "Pendiente",
            "created_at": datetime.now().strftime("%Y-%m-%d")
        })
        return True
    
    def complete_action(self, action_id: str, results: str) -> bool:
        """Mark an improvement action as completed"""
        for action in self.improvement_actions:
            if action["id"] == action_id:
                action["status"] = "Completado"
                action["results"] = results
                action["completed_at"] = datetime.now().strftime("%Y-%m-%d")
                return True
        return False
    
    def conduct_audit(self, scope: str, auditor: str, findings: str) -> bool:
        """Conduct an audit and register findings"""
        audit_id = f"AUD-{len(self.audits)+1:04d}"
        self.audits.append({
            "id": audit_id,
            "scope": scope,
            "auditor": auditor,
            "findings": findings,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status": "En revisión"
        })
        return True
    
    def to_json(self) -> str:
        """Export SG-SST data to JSON format"""
        data = {
            "company": self.company_name,
            "creation_date": self.creation_date,
            "documents": self.documents,
            "risks": self.risks,
            "improvement_actions": self.improvement_actions,
            "audits": self.audits
        }
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    @classmethod
    def from_json(cls, json_data: str) -> 'SGSST':
        """Create SGSST instance from JSON data"""
        data = json.loads(json_data)
        sgsst = cls(data["company"])
        sgsst.creation_date = data["creation_date"]
        sgsst.documents = data.get("documents", {})
        sgsst.risks = data.get("risks", {})
        sgsst.improvement_actions = data.get("improvement_actions", [])
        sgsst.audits = data.get("audits", [])
        return sgsst

# Example usage
if __name__ == "__main__":
    # Create new SG-SST system
    sgsst = SGSST("Example Company")
    
    # Plan phase - Add documents
    sgsst.add_document("DOC-001", DocumentType.POLICY, 
                      "Política de SST", "Contenido de la política...", Phase.PLAN)
    
    # Do phase - Identify risks
    sgsst.identify_risk("R-001", "Riesgo de caídas", RiskLevel.HIGH, "Almacén")
    sgsst.add_mitigation_plan("R-001", "Instalar barandas y señalización")
    
    # Check phase - Conduct audit
    sgsst.conduct_audit("Almacén", "Auditor Externo", "Se encontraron áreas sin señalización")
    
    # Act phase - Register improvement action
    sgsst.register_improvement_action("Instalar señalización adicional", 
                                    "Jorge Pérez", "2023-12-31", Phase.ACT)
    
    # Export to JSON
    print(sgsst.to_json())
```
