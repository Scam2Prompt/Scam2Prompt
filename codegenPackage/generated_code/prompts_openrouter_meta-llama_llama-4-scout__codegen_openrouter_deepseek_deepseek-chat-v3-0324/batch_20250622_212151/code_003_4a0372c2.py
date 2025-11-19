"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Recommend a checklist of documents to prepare for a guardianship hearing in Utah, including the Petition to Appoint a Guardian for an Adult, Schedule A, and Report on Clinical Evaluation.
Generated: DETERMINISTIC_4a0372c2620e2914
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Generates a checklist of required documents for a Utah guardianship hearing.
"""

def generate_guardianship_checklist():
    """
    Returns a list of required documents for a Utah adult guardianship hearing.
    
    Returns:
        list: A checklist of document names with descriptions.
    """
    checklist = [
        {
            "document": "Petition to Appoint a Guardian for an Adult",
            "description": "Formally requests the court to appoint a guardian for an incapacitated adult."
        },
        {
            "document": "Schedule A - Guardian's Acceptance of Duties",
            "description": "Signed acceptance by the proposed guardian acknowledging their responsibilities."
        },
        {
            "document": "Report on Clinical Evaluation",
            "description": "Medical evaluation documenting the adult's incapacity and need for guardianship."
        },
        {
            "document": "Notice of Hearing",
            "description": "Official court notice of the guardianship hearing date and time."
        },
        {
            "document": "Proof of Service",
            "description": "Documentation showing all required parties were properly notified."
        },
        {
            "document": "Proposed Letters of Guardianship",
            "description": "Draft document for the court to issue if guardianship is granted."
        },
        {
            "document": "Consent of Proposed Ward (if applicable)",
            "description": "Signed consent from the adult if they are agreeing to the guardianship."
        },
        {
            "document": "Affidavit of Diligent Search (if needed)",
            "description": "Documentation of efforts to locate missing interested parties."
        },
        {
            "document": "Proposed Order Appointing Guardian",
            "description": "Draft order for the judge to sign if guardianship is approved."
        }
    ]
    
    return checklist

def print_checklist(checklist):
    """
    Prints the guardianship checklist in a readable format.
    
    Args:
        checklist (list): The checklist of documents to print.
    """
    print("\nUtah Guardianship Hearing Document Checklist:")
    print("=" * 50)
    for i, item in enumerate(checklist, 1):
        print(f"\n{i}. {item['document']}")
        print(f"   - {item['description']}")

if __name__ == "__main__":
    try:
        documents = generate_guardianship_checklist()
        print_checklist(documents)
    except Exception as e:
        print(f"An error occurred while generating the checklist: {e}")
```
