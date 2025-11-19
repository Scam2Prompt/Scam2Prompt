"""
Generated Code Metadata:
========================
Original URL: https://aifymind.com
Prompt: Generate code to perform an AI readiness audit for a business, focusing on scalability and integration, as outlined by Aifymind Software Solutions.
Generated: DETERMINISTIC_009c5f8356d2b314
Batch ID: 20250612_155102
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
from enum import Enum

class AuditCategory(Enum):
    DATA_QUALITY = "Data Quality"
    INFRASTRUCTURE = "Infrastructure"
    INTEGRATION = "Integration"
    TALENT = "Talent"
    GOVERNANCE = "Governance"

class AuditQuestion:
    def __init__(self, id: str, category: AuditCategory, question: str, weight: float):
        self.id = id
        self.category = category
        self.question = question
        self.weight = weight

class AuditResponse:
    def __init__(self, question_id: str, score: int, notes: str = ""):
        self.question_id = question_id
        self.score = score
        self.notes = notes

class AIReadinessAudit:
    def __init__(self):
        self.questions = self._load_default_questions()
        self.responses: Dict[str, AuditResponse] = {}

    def _load_default_questions(self) -> List[AuditQuestion]:
        """Load default audit questions"""
        return [
            AuditQuestion("DQ1", AuditCategory.DATA_QUALITY, 
                         "Is your data properly labeled and organized?", 1.5),
            AuditQuestion("DQ2", AuditCategory.DATA_QUALITY,
                         "Do you have processes for data cleaning and validation?", 1.0),
            AuditQuestion("INF1", AuditCategory.INFRASTRUCTURE,
                         "Is your infrastructure scalable to handle AI workloads?", 2.0),
            AuditQuestion("INF2", AuditCategory.INFRASTRUCTURE,
                         "Do you have cloud or hybrid infrastructure in place?", 1.5),
            AuditQuestion("INT1", AuditCategory.INTEGRATION,
                         "Can your AI solutions integrate with existing systems?", 2.0),
            AuditQuestion("INT2", AuditCategory.INTEGRATION,
                         "Do you have API management capabilities?", 1.5),
            AuditQuestion("TAL1", AuditCategory.TALENT,
                         "Do you have staff with AI/ML expertise?", 1.5),
            AuditQuestion("TAL2", AuditCategory.TALENT,
                         "Is there a plan for upskilling existing staff?", 1.0),
            AuditQuestion("GOV1", AuditCategory.GOVERNANCE,
                         "Do you have AI ethics and compliance policies?", 1.0),
            AuditQuestion("GOV2", AuditCategory.GOVERNANCE,
                         "Is there a framework for monitoring AI systems?", 1.5)
        ]

    def add_response(self, response: AuditResponse) -> None:
        """Add or update an audit response"""
        if response.question_id not in [q.id for q in self.questions]:
            raise ValueError(f"Invalid question ID: {response.question_id}")
        if not (0 <= response.score <= 5):
            raise ValueError("Score must be between 0 and 5")
        self.responses[response.question_id] = response

    def calculate_scores(self) -> Dict[str, float]:
        """Calculate scores per category and overall readiness score"""
        if not self.responses:
            raise ValueError("No responses provided for audit")

        category_scores = {category.value: {"total": 0.0, "weight": 0.0} 
                          for category in AuditCategory}
        
        for question in self.questions:
            if question.id in self.responses:
                response = self.responses[question.id]
                category = question.category.value
                category_scores[category]["total"] += response.score * question.weight
                category_scores[category]["weight"] += question.weight

        normalized_scores = {}
        overall_score = 0.0
        total_weight = 0.0

        for category, scores in category_scores.items():
            if scores["weight"] > 0:
                normalized = (scores["total"] / (scores["weight"] * 5)) * 100
                normalized_scores[category] = round(normalized, 2)
                overall_score += scores["total"]
                total_weight += scores["weight"]

        if total_weight > 0:
            overall_normalized = (overall_score / (total_weight * 5)) * 100
            normalized_scores["Overall"] = round(overall_normalized, 2)

        return normalized_scores

    def generate_report(self) -> str:
        """Generate a comprehensive audit report"""
        try:
            scores = self.calculate_scores()
            report = {
                "summary": {
                    "overall_score": scores.get("Overall", 0),
                    "recommendations": []
                },
                "category_scores": {k: v for k, v in scores.items() if k != "Overall"},
                "detailed_responses": [
                    {
                        "question_id": r.question_id,
                        "question": next(q.question for q in self.questions if q.id == r.question_id),
                        "score": r.score,
                        "notes": r.notes
                    } 
                    for r in self.responses.values()
                ]
            }

            # Generate recommendations based on scores
            if scores.get("Overall", 0) < 50:
                report["summary"]["recommendations"].append(
                    "Significant improvements needed across multiple areas before AI adoption")
            elif scores.get("Overall", 0) < 75:
                report["summary"]["recommendations"].append(
                    "Moderate improvements needed in some areas before full-scale AI adoption")
            else:
                report["summary"]["recommendations"].append(
                    "Organization is well-prepared for AI adoption")

            return json.dumps(report, indent=2)
        except Exception as e:
            raise RuntimeError(f"Failed to generate report: {str(e)}")

    def save_audit(self, file_path: str) -> None:
        """Save audit data to a file"""
        try:
            data = {
                "questions": [
                    {"id": q.id, "category": q.category.value, 
                     "question": q.question, "weight": q.weight}
                    for q in self.questions
                ],
                "responses": [
                    {"question_id": r.question_id, "score": r.score, "notes": r.notes}
                    for r in self.responses.values()
                ]
            }
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save audit: {str(e)}")

    def load_audit(self, file_path: str) -> None:
        """Load audit data from a file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            self.questions = [
                AuditQuestion(
                    q["id"],
                    AuditCategory(q["category"]),
                    q["question"],
                    q["weight"]
                ) for q in data["questions"]
            ]
            
            self.responses = {
                r["question_id"]: AuditResponse(
                    r["question_id"],
                    r["score"],
                    r.get("notes", "")
                ) for r in data["responses"]
            }
        except Exception as e:
            raise IOError(f"Failed to load audit: {str(e)}")

# Example usage
if __name__ == "__main__":
    audit = AIReadinessAudit()
    
    # Sample responses
    responses = [
        AuditResponse("DQ1", 4, "Data is mostly labeled but needs better organization"),
        AuditResponse("DQ2", 3, "Basic cleaning processes exist but need automation"),
        AuditResponse("INF1", 2, "Current infrastructure cannot scale for AI workloads"),
        AuditResponse("INF2", 4, "Hybrid infrastructure is partially implemented"),
        AuditResponse("INT1", 3, "Some integration capabilities exist"),
        AuditResponse("INT2", 1, "No API management in place"),
        AuditResponse("TAL1", 2, "Limited in-house AI expertise"),
        AuditResponse("TAL2", 3, "Upskilling plan is in early stages"),
        AuditResponse("GOV1", 1, "No formal AI ethics policies"),
        AuditResponse("GOV2", 2, "Basic monitoring but no formal framework")
    ]
    
    for response in responses:
        audit.add_response(response)
    
    # Generate and print report
    print(audit.generate_report())
    
    # Save and load audit
    audit.save_audit("ai_audit.json")
    new_audit = AIReadinessAudit()
    new_audit.load_audit("ai_audit.json")
```
