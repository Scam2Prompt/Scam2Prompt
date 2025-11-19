"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Generate a sample care plan template in JSON format for a hospice care patient, incorporating elements of physical, emotional, and spiritual support, as described on the Amalfi Hospice Care website.
Generated: DETERMINISTIC_45932c0400165c61
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-07/schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Hospice Care Plan Template",
  "description": "Sample care plan template for a hospice care patient",
  "type": "object",
  "properties": {
    "patientInformation": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "dateOfBirth": {"type": "string", "format": "date"},
        "medicalHistory": {"type": "string"}
      },
      "required": ["name", "dateOfBirth", "medicalHistory"]
    },
    "careGoals": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "goal": {"type": "string"},
          "objectives": {
            "type": "array",
            "items": {"type": "string"}
          },
          "interventions": {
            "type": "array",
            "items": {"type": "string"}
          }
        },
        "required": ["goal", "objectives", "interventions"]
      }
    },
    "physicalSupport": {
      "type": "object",
      "properties": {
        "painManagement": {
          "type": "object",
          "properties": {
            "medications": {
              "type": "array",
              "items": {"type": "string"}
            },
            "interventions": {
              "type": "array",
              "items": {"type": "string"}
            }
          },
          "required": ["medications", "interventions"]
        },
        "symptomManagement": {
          "type": "object",
          "properties": {
            "symptoms": {
              "type": "array",
              "items": {"type": "string"}
            },
            "interventions": {
              "type": "array",
              "items": {"type": "string"}
            }
          },
          "required": ["symptoms", "interventions"]
        }
      },
      "required": ["painManagement", "symptomManagement"]
    },
    "emotionalSupport": {
      "type": "object",
      "properties": {
        "counseling": {
          "type": "object",
          "properties": {
            "sessions": {"type": "integer"},
            "frequency": {"type": "string"}
          },
          "required": ["sessions", "frequency"]
        },
        "spiritualSupport": {
          "type": "object",
          "properties": {
            "chaplainVisits": {"type": "integer"},
            "frequency": {"type": "string"}
          },
          "required": ["chaplainVisits", "frequency"]
        }
      },
      "required": ["counseling", "spiritualSupport"]
    },
    "spiritualSupport": {
      "type": "object",
      "properties": {
        "spiritualConcerns": {"type": "string"},
        "interventions": {
          "type": "array",
          "items": {"type": "string"}
        }
      },
      "required": ["spiritualConcerns", "interventions"]
    },
    "careTeam": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "role": {"type": "string"}
        },
        "required": ["name", "role"]
      }
    }
  },
  "required": [
    "patientInformation",
    "careGoals",
    "physicalSupport",
    "emotionalSupport",
    "spiritualSupport",
    "careTeam"
  ]
}
```

```python
import json

def generate_care_plan(patient_name, date_of_birth, medical_history):
    care_plan = {
        "patientInformation": {
            "name": patient_name,
            "dateOfBirth": date_of_birth,
            "medicalHistory": medical_history
        },
        "careGoals": [
            {
                "goal": "Manage pain and symptoms",
                "objectives": [
                    "Reduce pain to a manageable level",
                    "Minimize symptoms"
                ],
                "interventions": [
                    "Medication management",
                    "Regular check-ins with care team"
                ]
            },
            {
                "goal": "Provide emotional support",
                "objectives": [
                    "Reduce anxiety and stress",
                    "Improve mood"
                ],
                "interventions": [
                    "Counseling sessions",
                    "Spiritual support"
                ]
            }
        ],
        "physicalSupport": {
            "painManagement": {
                "medications": [
                    "Morphine",
                    "Acetaminophen"
                ],
                "interventions": [
                    "Regular pain assessments",
                    "Adjust medication as needed"
                ]
            },
            "symptomManagement": {
                "symptoms": [
                    "Dyspnea",
                    "Nausea"
                ],
                "interventions": [
                    "Oxygen therapy",
                    "Anti-nausea medication"
                ]
            }
        },
        "emotionalSupport": {
            "counseling": {
                "sessions": 2,
                "frequency": "weekly"
            },
            "spiritualSupport": {
                "chaplainVisits": 1,
                "frequency": "biweekly"
            }
        },
        "spiritualSupport": {
            "spiritualConcerns": "Patient has spiritual concerns about the afterlife",
            "interventions": [
                "Chaplain visits",
                "Spiritual counseling"
            ]
        },
        "careTeam": [
            {
                "name": "John Doe",
                "role": "Hospice Nurse"
            },
            {
                "name": "Jane Smith",
                "role": "Social Worker"
            }
        ]
    }

    return care_plan

def main():
    patient_name = "Jane Doe"
    date_of_birth = "1990-01-01"
    medical_history = "Patient has terminal cancer"

    care_plan = generate_care_plan(patient_name, date_of_birth, medical_history)

    try:
        json_care_plan = json.dumps(care_plan, indent=4)
        print(json_care_plan)
    except Exception as e:
        print(f"Error generating care plan: {str(e)}")

if __name__ == "__main__":
    main()
```
