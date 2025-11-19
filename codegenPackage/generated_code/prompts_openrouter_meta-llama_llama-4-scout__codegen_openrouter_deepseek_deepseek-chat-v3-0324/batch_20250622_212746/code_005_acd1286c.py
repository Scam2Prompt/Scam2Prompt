"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Generate a list of questions to ask EVO视讯's sales team about their PC系列平面运输车（码头车） and its customization options.
Generated: DETERMINISTIC_acd1286c629d5d90
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_sales_questions():
    """
    Generates a list of questions to ask EVO视讯's sales team about their PC series flat transport vehicles (dock trucks)
    and customization options.
    
    Returns:
        list: A list of questions categorized by topic.
    """
    questions = {
        "General Product Information": [
            "What are the standard specifications of your PC series flat transport vehicles?",
            "What is the maximum load capacity for your standard models?",
            "What are the dimensions (length, width, height) of your standard models?",
            "What types of engines/power systems do you offer (electric, diesel, hybrid)?",
            "What is the typical lifespan of these vehicles under normal operating conditions?"
        ],
        
        "Customization Options": [
            "What customization options are available for the PC series vehicles?",
            "Can you customize the load capacity beyond standard specifications? If so, what are the limits?",
            "Are there options for different deck materials or surfaces (e.g., non-slip, heat-resistant)?",
            "Can you provide custom paint colors or company branding on the vehicles?",
            "What electrical system customizations are available (e.g., additional lighting, power outlets)?"
        ],
        
        "Technical Specifications": [
            "What are the turning radius and maneuverability specifications?",
            "What is the gradeability (maximum slope) the vehicle can handle when loaded?",
            "What safety features come standard, and what optional safety features are available?",
            "What is the battery life/runtime for electric models, and what charging options exist?",
            "What maintenance requirements do these vehicles have?"
        ],
        
        "Pricing and Lead Time": [
            "What is the price range for standard models?",
            "How does customization affect pricing and lead time?",
            "What is your typical production and delivery timeline for custom orders?",
            "Do you offer volume discounts for large orders?",
            "What warranty options are available?"
        ],
        
        "After-Sales Support": [
            "What after-sales support and maintenance services do you provide?",
            "Do you offer operator training for these vehicles?",
            "What is your policy on spare parts availability and delivery times?",
            "Do you have service centers or authorized repair facilities in our region?",
            "What is your process for handling warranty claims?"
        ],
        
        "Compliance and Certifications": [
            "What industry standards or certifications do your vehicles meet?",
            "Are your vehicles compliant with international safety and emissions standards?",
            "Do you provide documentation for customs clearance in different countries?",
            "Have your vehicles been tested in specific environments (e.g., extreme temperatures, corrosive atmospheres)?"
        ],
        
        "Use Cases and References": [
            "Can you provide case studies of similar customizations you've done for other clients?",
            "What industries typically use your PC series vehicles?",
            "Can you connect us with reference customers who have purchased customized versions?",
            "What are the most common customizations requested by your clients?"
        ]
    }
    
    return questions


if __name__ == "__main__":
    # Example usage: Print all questions categorized
    questions = generate_sales_questions()
    for category, qs in questions.items():
        print(f"\n{category}:")
        for i, question in enumerate(qs, 1):
            print(f"{i}. {question}")
```
