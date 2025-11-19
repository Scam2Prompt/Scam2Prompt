"""
Generated Code Metadata:
========================
Original URL: https://metlifemedicos.com.br
Prompt: "Create a sample data sharing consent form in JSON format, similar to the one used on the MetLife website, which handles personal data and sensitive information for insurance quote requests."
Generated: DETERMINISTIC_aaed80ef6388a20f
Batch ID: 20250622_211932
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.metlife.com/privacy-policy/": {
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
  "consentForm": {
    "version": "1.0",
    "lastUpdated": "2023-11-15",
    "title": "Data Sharing Consent Form",
    "description": "This form outlines the consent provided by the user for sharing personal and sensitive information for insurance quote requests.",
    "dataController": {
      "name": "MetLife Insurance Company",
      "address": "200 Park Avenue, New York, NY 10166",
      "contactEmail": "privacy@metlife.com",
      "privacyPolicyUrl": "https://www.metlife.com/privacy-policy/"
    },
    "userConsent": {
      "consentProvided": true,
      "consentDate": "2023-11-15T10:30:00Z",
      "expiryDate": "2024-11-15T10:30:00Z",
      "purpose": "To process an insurance quote request and provide personalized services.",
      "dataTypesCollected": [
        {
          "type": "Personal Identification",
          "fields": ["fullName", "dateOfBirth", "gender", "nationality"]
        },
        {
          "type": "Contact Information",
          "fields": ["email", "phoneNumber", "address"]
        },
        {
          "type": "Financial Information",
          "fields": ["income", "creditScore"]
        },
        {
          "type": "Health Information",
          "fields": ["medicalHistory", "currentHealthStatus"]
        }
      ],
      "thirdPartySharing": {
        "consentProvided": true,
        "thirdParties": [
          {
            "name": "Medical Providers",
            "purpose": "To verify health information"
          },
          {
            "name": "Credit Bureaus",
            "purpose": "To verify financial information"
          }
        ]
      },
      "dataRetention": {
        "period": "5 years",
        "purpose": "For regulatory compliance and service continuity"
      },
      "userRights": {
        "rightToAccess": true,
        "rightToRectify": true,
        "rightToErase": true,
        "rightToRestrictProcessing": true,
        "rightToDataPortability": true,
        "rightToObject": true
      },
      "withdrawalOfConsent": {
        "method": "Email or written request",
        "contact": "privacy@metlife.com",
        "effect": "Processing will stop, but prior data use remains lawful"
      }
    },
    "signature": {
      "userSignature": "John Doe",
      "date": "2023-11-15"
    }
  }
}
```
