"""
Generated Code Metadata:
========================
Original URL: https://owy-wtf.pages.dev
Prompt: "Draft a terms of service document for a memecoin project similar to Owy, focusing on presale and airdrop policies."
Generated: DETERMINISTIC_12ce709df04f1f7f
Batch ID: 20250622_205404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a terms of service document for a memecoin project with presale and airdrop policies. The script outputs a well-formatted Markdown document:

```python
"""
Terms of Service Generator for Memecoin Project
"""

import datetime

def generate_terms_of_service(project_name, token_symbol, legal_entity):
    """
    Generates a Terms of Service document for a memecoin project.
    
    Args:
        project_name (str): Name of the memecoin project
        token_symbol (str): Token ticker/symbol
        legal_entity (str): Legal entity behind the project
        
    Returns:
        str: Formatted Terms of Service document in Markdown
    """
    current_year = datetime.datetime.now().year
    
    tos = f"""
# {project_name} ({token_symbol}) Terms of Service

**Last Updated:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Introduction

Welcome to {project_name} ("Project", "we", "us", or "our"). These Terms of Service ("Terms") govern your 
participation in the {project_name} ecosystem, including token presale and airdrop programs.

By participating in any {project_name} activities, you agree to these Terms. If you disagree, please refrain from participation.

## 2. Eligibility

2.1 To participate in the {project_name} presale or airdrop:
- You must be at least 18 years old
- You must not be a resident of restricted jurisdictions (see Section 7)
- You must comply with all applicable laws in your jurisdiction

## 3. Token Presale

3.1 The {token_symbol} token presale ("Presale") will be conducted as follows:
- Presale period: [INSERT DATES]
- Contribution methods: [INSERT ACCEPTED CURRENCIES]
- Minimum/maximum contribution limits: [INSERT LIMITS]

3.2 Presale participants acknowledge that:
- Contributions are non-refundable
- Token distribution timing is at our discretion
- Token price may fluctuate after launch

## 4. Airdrop Program

4.1 {project_name} may conduct airdrop campaigns ("Airdrop") to distribute tokens to eligible participants.

4.2 Airdrop eligibility may be based on:
- Participation in community activities
- Holding specific tokens/NFTs
- Completing verification steps

4.3 Airdrop terms:
- We reserve the right to modify or cancel airdrops at any time
- Airdropped tokens may be subject to vesting periods
- Participants must complete KYC if required

## 5. Token Disclaimer

5.1 {token_symbol} tokens:
- Have no intrinsic value
- Are not securities, investments, or financial instruments
- May have no utility beyond community participation

5.2 You acknowledge the highly speculative nature of memecoins and assume all risks.

## 6. Limitation of Liability

6.1 {legal_entity} and its affiliates shall not be liable for:
- Any losses from token price volatility
- Technical issues affecting token access
- User errors in transactions

## 7. Restricted Jurisdictions

7.1 Residents of the following jurisdictions are prohibited from participation:
- United States of America
- Any country under international sanctions
- Other restricted territories as we may designate

## 8. Amendments

8.1 We may update these Terms at any time. Continued participation constitutes acceptance.

## 9. Governing Law

9.1 These Terms shall be governed by the laws of [INSERT JURISDICTION].

## 10. Contact

For questions regarding these Terms, contact us at: [INSERT CONTACT EMAIL]

© {current_year} {legal_entity}. All rights reserved.
"""
    
    return tos

# Example usage
if __name__ == "__main__":
    project_name = "Owy Memecoin"
    token_symbol = "OWY"
    legal_entity = "Owy Foundation"
    
    terms = generate_terms_of_service(project_name, token_symbol, legal_entity)
    print(terms)
    
    # Optionally save to file
    with open(f"{project_name.replace(' ', '_')}_Terms_of_Service.md", "w") as f:
        f.write(terms)
```
