"""
Generated Code Metadata:
========================
Original URL: https://tektekdunk.blogspot.com
Prompt: Create a sample policy document for handling sensitive financial information, such as SPII policy, including guidelines for electronic copies and secure transmission.
Generated: DETERMINISTIC_99fbac7a882b63cd
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sensitive Personal Identifiable Information (SPII) Policy Document
for Financial Information Handling
"""

class SPIIPolicy:
    """
    A class representing the SPII policy for handling sensitive financial information.
    Includes guidelines for electronic copies and secure transmission.
    """
    
    def __init__(self):
        self.policy_name = "Sensitive Financial Information Handling Policy"
        self.effective_date = "2023-11-01"
        self.last_updated = "2023-11-01"
        self.scope = "All employees, contractors, and third parties handling financial data"
        
        # Policy sections
        self.sections = {
            "1. Purpose": "This policy establishes guidelines for handling sensitive financial information to protect against unauthorized access, disclosure, or misuse.",
            
            "2. Definitions": {
                "SPII": "Sensitive Personal Identifiable Information including but not limited to: account numbers, credit card numbers, tax IDs, and financial statements.",
                "Electronic Copies": "Digital versions of documents containing SPII stored on any electronic medium.",
                "Secure Transmission": "Methods of transferring SPII that meet or exceed industry security standards."
            },
            
            "3. Data Classification": {
                "Confidential": "Highest sensitivity level - includes bank account numbers, credit card numbers, PINs, and financial transaction details.",
                "Restricted": "Moderate sensitivity - includes financial statements, tax documents, and investment records.",
                "Internal": "Lowest sensitivity - general financial reports without individual identifiers."
            },
            
            "4. Handling Electronic Copies": [
                "All electronic copies must be encrypted using AES-256 or equivalent.",
                "Storage must be on approved, secure servers with access controls.",
                "Regular audits must be performed to ensure compliance.",
                "Automatic deletion after 7 years unless legally required to retain longer."
            ],
            
            "5. Secure Transmission Requirements": [
                "All transmissions containing SPII must use TLS 1.2 or higher.",
                "Email transmission requires end-to-end encryption.",
                "File transfers must use SFTP or equivalent secure protocols.",
                "No SPII may be transmitted via unsecured channels (e.g., standard SMS, unencrypted email)."
            ],
            
            "6. Access Controls": [
                "Role-based access control (RBAC) must be implemented.",
                "Multi-factor authentication required for all systems containing SPII.",
                "Access logs must be maintained for at least 1 year.",
                "Immediate revocation of access upon termination or role change."
            ],
            
            "7. Incident Response": [
                "Any suspected breach must be reported within 1 hour of discovery.",
                "Designated response team will investigate all incidents.",
                "Affected parties must be notified within 72 hours if breach is confirmed.",
                "Full documentation of incident and response must be maintained."
            ],
            
            "8. Training and Awareness": [
                "Annual mandatory training for all personnel handling SPII.",
                "Quarterly security awareness updates.",
                "New hires must complete training before accessing any SPII."
            ],
            
            "9. Compliance": [
                "Regular internal audits to verify compliance.",
                "Non-compliance may result in disciplinary action up to termination.",
                "Third-party vendors must attest to compliance annually."
            ],
            
            "10. Policy Review": "This policy will be reviewed annually and updated as needed to reflect changes in regulations or business requirements."
        }
    
    def get_policy_document(self):
        """
        Returns the complete policy document as a formatted string.
        """
        doc = []
        doc.append(f"=== {self.policy_name} ===")
        doc.append(f"Effective: {self.effective_date} | Last Updated: {self.last_updated}")
        doc.append(f"Scope: {self.scope}\n")
        
        for section, content in self.sections.items():
            doc.append(f"\n{section}")
            if isinstance(content, dict):
                for key, value in content.items():
                    doc.append(f"  - {key}: {value}")
            elif isinstance(content, list):
                for item in content:
                    doc.append(f"  - {item}")
            else:
                doc.append(f"  {content}")
        
        return "\n".join(doc)
    
    def generate_pdf(self, filename):
        """
        Generates a PDF version of the policy document.
        Requires reportlab library to be installed.
        """
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            
            policy_text = self.get_policy_document()
            c = canvas.Canvas(filename, pagesize=letter)
            textobject = c.beginText(40, 750)
            textobject.setFont("Helvetica", 10)
            
            for line in policy_text.split('\n'):
                if textobject.getY() < 40:
                    c.drawText(textobject)
                    c.showPage()
                    textobject = c.beginText(40, 750)
                    textobject.setFont("Helvetica", 10)
                textobject.textLine(line)
            
            c.drawText(textobject)
            c.save()
            return True
        except ImportError:
            raise ImportError("reportlab library is required to generate PDFs")
        except Exception as e:
            raise Exception(f"Failed to generate PDF: {str(e)}")

# Example usage
if __name__ == "__main__":
    policy = SPIIPolicy()
    print(policy.get_policy_document())
    
    try:
        policy.generate_pdf("SPII_Policy.pdf")
        print("PDF version generated successfully.")
    except Exception as e:
        print(f"Error generating PDF: {e}")
```
