"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Write Python code to generate a formatted legal document template for a Habeas Corpus request, including fields for case details, petitioner information, and legal arguments.
Generated: DETERMINISTIC_b078e065d0f4aafe
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_habeas_corpus_template(case_details, petitioner_info, legal_arguments):
    """
    Generates a formatted Habeas Corpus request template.
    
    Parameters:
        case_details (dict): Information about the case (e.g., case number, court name).
        petitioner_info (dict): Information about the petitioner (e.g., name, address).
        legal_arguments (list): List of legal arguments to include in the request.
    
    Returns:
        str: Formatted legal document template.
    """
    try:
        # Validate input types
        if not isinstance(case_details, dict):
            raise ValueError("case_details must be a dictionary.")
        if not isinstance(petitioner_info, dict):
            raise ValueError("petitioner_info must be a dictionary.")
        if not isinstance(legal_arguments, list):
            raise ValueError("legal_arguments must be a list.")
        
        # Get current date
        current_date = datetime.datetime.now().strftime("%B %d, %Y")

        # Start building the legal document template
        document = f"""\
        IN THE COURT OF {case_details.get("court_name", "[Court Name]")}
        CASE NO: {case_details.get("case_number", "[Case Number]")}
        
        ---------------------------------------------------------------
        
                                PETITION FOR WRIT OF HABEAS CORPUS
        
        ---------------------------------------------------------------
        
        TO: THE HONORABLE JUDGE OF THE {case_details.get("court_name", "[Court Name]")}

        COMES NOW, {petitioner_info.get("name", "[Petitioner Name]")}, residing at \
{petitioner_info.get("address", "[Petitioner Address]")}, by and through counsel, and hereby petitions \
this Court for a Writ of Habeas Corpus under applicable laws and statutes.

        The Petitioner respectfully submits the following case details and legal arguments:
        
        CASE DETAILS:
        ---------------------------------------------------------------
        Case Number: {case_details.get("case_number", "[Case Number]")}
        Court Name: {case_details.get("court_name", "[Court Name]")}
        Filed On: {case_details.get("filed_date", "[Filed Date]")}
        
        PETITIONER INFORMATION:
        ---------------------------------------------------------------
        Name: {petitioner_info.get("name", "[Petitioner Name]")}
        Address: {petitioner_info.get("address", "[Petitioner Address]")}
        Contact: {petitioner_info.get("contact", "[Petitioner Contact Info]")}
        
        LEGAL ARGUMENTS:
        ---------------------------------------------------------------
        """
        
        # Append legal arguments to the document
        for i, argument in enumerate(legal_arguments, start=1):
            document += f"    {i}. {argument}\n"

        # Footer
        document += f"""
        ---------------------------------------------------------------

        Respectfully submitted this {current_date}.

        ____________________________
        {petitioner_info.get("name", "[Petitioner Name]")}
        [Signature, if applicable]
        """
        
        return document
    except Exception as e:
        return f"An error occurred while generating the template: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Example input data
    case_details = {
        "case_number": "2023-CV-00123",
        "court_name": "Superior Court of Example State",
        "filed_date": "October 10, 2023"
    }
    
    petitioner_info = {
        "name": "John Doe",
        "address": "123 Legal Lane, Example City, EX 12345",
        "contact": "john.doe@example.com"
    }
    
    legal_arguments = [
        "The detention violates constitutional rights under the Fourth Amendment.",
        "The detention lacks proper judicial approval and oversight.",
        "The petitioner is being held without due process of law."
    ]
    
    # Generate template
    template = generate_habeas_corpus_template(case_details, petitioner_info, legal_arguments)
    
    # Output template
    print(template)
```
