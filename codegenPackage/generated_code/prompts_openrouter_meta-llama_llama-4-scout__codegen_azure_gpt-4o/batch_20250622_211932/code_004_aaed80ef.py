"""
Generated Code Metadata:
========================
Original URL: https://metlifemedicos.com.br
Prompt: "Create a sample data sharing consent form in JSON format, similar to the one used on the MetLife website, which handles personal data and sensitive information for insurance quote requests."
Generated: DETERMINISTIC_aaed80ef6388a20f
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "consentForm": {
    "title": "Data Sharing Consent Form",
    "description": "By completing this form, you consent to the collection, use, and sharing of your personal and sensitive information for the purpose of providing insurance quotes and related services.",
    "sections": [
      {
        "sectionTitle": "Personal Information",
        "fields": [
          {
            "fieldName": "Full Name",
            "fieldType": "text",
            "required": true,
            "description": "Your legal name as it appears on official documents."
          },
          {
            "fieldName": "Email Address",
            "fieldType": "email",
            "required": true,
            "description": "Your email address for communication purposes."
          },
          {
            "fieldName": "Phone Number",
            "fieldType": "tel",
            "required": false,
            "description": "Your contact number for follow-up inquiries."
          }
        ]
      },
      {
        "sectionTitle": "Sensitive Information",
        "fields": [
          {
            "fieldName": "Health Information",
            "fieldType": "textarea",
            "required": true,
            "description": "Details about your health status relevant to insurance coverage."
          },
          {
            "fieldName": "Financial Information",
            "fieldType": "textarea",
            "required": true,
            "description": "Details about your financial status relevant to insurance coverage."
          }
        ]
      },
      {
        "sectionTitle": "Consent",
        "fields": [
          {
            "fieldName": "Agree to Terms",
            "fieldType": "checkbox",
            "required": true,
            "description": "I agree to the terms and conditions outlined in this consent form."
          },
          {
            "fieldName": "Receive Marketing Communications",
            "fieldType": "checkbox",
            "required": false,
            "description": "I consent to receiving marketing communications from the company."
          }
        ]
      }
    ],
    "footer": {
      "disclaimer": "Your information will be handled in accordance with our Privacy Policy. You may withdraw your consent at any time by contacting us.",
      "contactInfo": {
        "email": "privacy@metlife.com",
        "phone": "+1-800-123-4567"
      }
    }
  }
}
```
