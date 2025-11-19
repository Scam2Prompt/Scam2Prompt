"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Generate a sample template for a legal correspondence using Markdown, inspired by the "Manual de Correspondência Jurídica" published by Adriano Geoffrey.
Generated: DETERMINISTIC_bc341b4e342700bd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```markdown
# Legal Correspondence Template
## Inspired by "Manual de Correspondência Jurídica" by Adriano Geoffrey

## Correspondence Information

* **Date:** {{date}}
* **Sender:** {{sender.name}}  
  {{sender.address}}  
  {{sender.city}}, {{sender.state}} {{sender.zip}}  
  {{sender.email}}  
  {{sender.phone}}

* **Recipient:** {{recipient.name}}  
  {{recipient.address}}  
  {{recipient.city}}, {{recipient.state}} {{recipient.zip}}

## Subject
{{subject}}

## Body

### Introduction
Dear {{recipient.name}},

This letter serves as formal {{purpose}} regarding {{matter}}.

### Details
Please find below the details of {{matter}}:

* **Case Number:** {{caseNumber}}
* **Reference:** {{reference}}

### Content
{{content}}

### Conclusion
In conclusion, we request {{request}}.

### Closing
Sincerely,

{{sender.name}}  
{{sender.title}}

## Attachments
* {{attachments}}

## Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| date     | Date of correspondence | 2023-04-01 |
| sender   | Sender's information | name: John Doe, address: 123 Main St, city: New York, state: NY, zip: 10001, email: johndoe@example.com, phone: 123-456-7890 |
| recipient| Recipient's information | name: Jane Doe, address: 456 Elm St, city: Los Angeles, state: CA, zip: 90001 |
| subject  | Subject of correspondence | Request for Information |
| purpose  | Purpose of correspondence | notification |
| matter   | Matter being addressed | case 12345 |
| caseNumber| Case or reference number | 12345 |
| reference| Relevant reference | contract 67890 |
| content  | Main content of correspondence | Please provide the requested documents. |
| request  | Request being made | an immediate response |
| attachments| List of attachments | document1.pdf, document2.pdf |
| title    | Sender's title | Legal Counsel |

## Usage
Replace the template variables with the actual information for your correspondence.

### Example Usage

Suppose we have the following information:

- Date: 2023-04-01
- Sender: 
  - Name: John Doe
  - Address: 123 Main St
  - City: New York
  - State: NY
  - Zip: 10001
  - Email: johndoe@example.com
  - Phone: 123-456-7890
  - Title: Legal Counsel
- Recipient: 
  - Name: Jane Doe
  - Address: 456 Elm St
  - City: Los Angeles
  - State: CA
  - Zip: 90001
- Subject: Request for Information
- Purpose: notification
- Matter: case 12345
- Case Number: 12345
- Reference: contract 67890
- Content: Please provide the requested documents.
- Request: an immediate response
- Attachments: document1.pdf

The filled-out template would look like this:

### Filled-out Template

## Correspondence Information

* **Date:** 2023-04-01
* **Sender:** John Doe  
  123 Main St  
  New York, NY 10001  
  johndoe@example.com  
  123-456-7890

* **Recipient:** Jane Doe  
  456 Elm St  
  Los Angeles, CA 90001

## Subject
Request for Information

## Body

### Introduction
Dear Jane Doe,

This letter serves as formal notification regarding case 12345.

### Details
Please find below the details of case 12345:

* **Case Number:** 12345
* **Reference:** contract 67890

### Content
Please provide the requested documents.

### Conclusion
In conclusion, we request an immediate response.

### Closing
Sincerely,

John Doe  
Legal Counsel

## Attachments
* document1.pdf
```
