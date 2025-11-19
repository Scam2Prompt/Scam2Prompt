"""
Generated Code Metadata:
========================
Original URL: https://foxmask.net
Prompt: Generate a Terms of Service (T.O.S) template in Swedish for a company that provides services and has specific rules for users and non-users.
Generated: DETERMINISTIC_3b592857413e77a5
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to generate a Terms of Service (T.O.S) template in Swedish
# This script creates a T.O.S template for a company providing services with specific rules for users and non-users.

def generate_tos_template(company_name, service_name):
    """
    Generates a Terms of Service (T.O.S) template in Swedish for a given company and service.

    Args:
        company_name (str): Name of the company.
        service_name (str): Name of the service provided by the company.

    Returns:
        str: A formatted T.O.S template in Swedish.
    """
    try:
        # Template for Terms of Service in Swedish
        tos_template = f"""
        VILLKOR FÖR ANVÄNDNING

        Välkommen till {company_name}! Genom att använda vår tjänst, {service_name}, godkänner du följande villkor.

        1. ALLMÄNT
        Dessa villkor reglerar din användning av {service_name}, som tillhandahålls av {company_name}. Genom att använda tjänsten accepterar du dessa villkor i sin helhet.

        2. ANVÄNDARANSVAR
        - Du måste vara minst 18 år gammal för att använda {service_name}.
        - Du får inte använda tjänsten för olagliga eller otillåtna ändamål.
        - Du ansvarar för att hålla dina inloggningsuppgifter säkra och konfidentiella.

        3. TJÄNSTENS TILLGÄNGLIGHET
        {company_name} förbehåller sig rätten att ändra, avbryta eller avsluta {service_name} när som helst utan föregående meddelande.

        4. IMMATERIELLA RÄTTIGHETER
        Allt innehåll och material som tillhandahålls via {service_name} är skyddat av immateriella rättigheter och tillhör {company_name}.

        5. ANSVARSBEGRÄNSNING
        {company_name} ansvarar inte för direkta, indirekta eller följdskador som uppstår vid användning av {service_name}.

        6. FÖR ICKE-ANVÄNDARE
        - Icke-användare får inte försöka få obehörig åtkomst till {service_name}.
        - Allt missbruk av tjänsten kommer att rapporteras till relevanta myndigheter.

        7. ÄNDRINGAR AV VILLKOR
        {company_name} förbehåller sig rätten att ändra dessa villkor när som helst. Ändringar träder i kraft vid publicering på vår webbplats.

        8. KONTAKT
        Om du har frågor om dessa villkor, vänligen kontakta oss på support@{company_name.lower()}.com.

        Tack för att du använder {service_name}!
        """
        return tos_template
    except Exception as e:
        # Handle any unexpected errors
        return f"Ett fel uppstod vid generering av villkoren: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Replace with your company and service name
    company_name = "Exempelbolaget AB"
    service_name = "ExempelTjänst"
    
    # Generate the T.O.S template
    tos = generate_tos_template(company_name, service_name)
    
    # Print the generated template
    print(tos)
```
