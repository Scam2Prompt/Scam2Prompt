"""
Generated Code Metadata:
========================
Original URL: https://www.igadvocacia.com
Prompt: Write a brief description of the services offered by IG Advocacia in the areas of previdenciária and trabalhista law.
Generated: DETERMINISTIC_467159fbb48400fb
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def get_services_description():
    """
    Returns a description of IG Advocacia's services in Previdenciária and Trabalhista law areas.
    
    Returns:
        dict: A dictionary with two keys ('previdenciaria', 'trabalhista') containing service descriptions.
    """
    services = {
        'previdenciaria': (
            "IG Advocacia specializes in Previdenciária (Social Security) law, offering comprehensive "
            "services including retirement planning, disability benefit claims, pension reviews, "
            "and appeals against INSS decisions. We ensure clients receive all entitled benefits "
            "through expert legal guidance and representation."
        ),
        'trabalhista': (
            "In Trabalhista (Labor) law, IG Advocacia provides robust representation for employees "
            "and employers. Services include contract reviews, wrongful termination cases, labor "
            "rights enforcement, compensation claims, and defense against labor lawsuits. We aim to "
            "protect our clients' rights while ensuring compliance with labor regulations."
        )
    }
    
    return services

# Example usage
if __name__ == "__main__":
    services = get_services_description()
    print("Previdenciária Services:")
    print(services['previdenciaria'])
    print("\nTrabalhista Services:")
    print(services['trabalhista'])
```
