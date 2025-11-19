"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Provide an example of a legal document template for a dispute resolution agreement that includes an arbitration clause, based on the guidelines from Arbitrium's arbitration services.
Generated: DETERMINISTIC_e1bd15ef341fbe55
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Legal Document Template: Dispute Resolution Agreement with Arbitration Clause
This template follows Arbitrium's arbitration service guidelines.
"""

DISPUTE_RESOLUTION_AGREEMENT_TEMPLATE = """
DISPUTE RESOLUTION AGREEMENT

This Dispute Resolution Agreement ("Agreement") is made and entered into as of [Effective Date] by and between:

[Party A Name], a [Party A Entity Type] organized under the laws of [Jurisdiction], with its principal office at [Address] ("Party A"); and

[Party B Name], a [Party B Entity Type] organized under the laws of [Jurisdiction], with its principal office at [Address] ("Party B").

Party A and Party B may be referred to individually as a "Party" or collectively as the "Parties."

1. PURPOSE
The Parties desire to establish procedures for resolving disputes that may arise between them in connection with [Describe Business Relationship/Contract].

2. NEGOTIATION
Before initiating any formal dispute resolution process, the Parties agree to first attempt to resolve any dispute through good faith negotiations between senior executives who have authority to settle the dispute.

3. MEDIATION
If the dispute is not resolved through negotiation within [Number] days, either Party may submit the dispute to non-binding mediation administered by [Mediation Service Provider] under its then-current mediation rules.

4. ARBITRATION
4.1 Agreement to Arbitrate
Any dispute, controversy, or claim arising out of or relating to this Agreement, or the breach, termination, or validity thereof, that cannot be resolved through negotiation or mediation shall be finally resolved by binding arbitration administered by Arbitrium in accordance with its Arbitration Rules.

4.2 Arbitration Rules
The arbitration shall be conducted under the Arbitrium Arbitration Rules in effect at the time of the arbitration demand, except as modified by this Agreement.

4.3 Number of Arbitrators
The arbitration shall be conducted by [one/three] arbitrator(s), appointed in accordance with the Arbitrium Rules.

4.4 Place of Arbitration
The arbitration shall take place in [City, Country], unless the Parties mutually agree otherwise.

4.5 Language
The arbitration shall be conducted in the [Language] language.

4.6 Governing Law
The arbitration shall be governed by the substantive laws of [Jurisdiction] without regard to its conflict of laws principles.

4.7 Confidentiality
The arbitration proceedings and award shall be confidential, except as required by law or for enforcement purposes.

4.8 Award
The arbitrator's award shall be final and binding, and judgment may be entered upon it in any court of competent jurisdiction.

5. GENERAL PROVISIONS
5.1 Costs
Each Party shall bear its own costs and expenses, including attorney's fees, and the Parties shall share equally the fees and expenses of the arbitrator and Arbitrium.

5.2 Survival
This arbitration provision shall survive the termination of this Agreement.

5.3 Amendments
This Agreement may only be amended in writing signed by both Parties.

5.4 Entire Agreement
This Agreement constitutes the entire agreement between the Parties regarding dispute resolution.

IN WITNESS WHEREOF, the Parties have executed this Agreement as of the Effective Date.

[Party A Name]
By: ___________________________
Name: [Signatory Name]
Title: [Signatory Title]
Date: _________________________

[Party B Name]
By: ___________________________
Name: [Signatory Name]
Title: [Signatory Title]
Date: _________________________
"""

def generate_dispute_resolution_agreement(party_a: dict, party_b: dict, terms: dict) -> str:
    """
    Generates a dispute resolution agreement with arbitration clause.
    
    Args:
        party_a: Dictionary containing Party A details (name, entity_type, jurisdiction, address)
        party_b: Dictionary containing Party B details (name, entity_type, jurisdiction, address)
        terms: Dictionary containing agreement terms (effective_date, business_relationship, 
               negotiation_days, mediators, arbitrators_num, location, language, governing_law)
    
    Returns:
        str: Completed dispute resolution agreement document
    """
    try:
        agreement = DISPUTE_RESOLUTION_AGREEMENT_TEMPLATE
        agreement = agreement.replace("[Effective Date]", terms.get("effective_date", "[Effective Date]"))
        agreement = agreement.replace("[Describe Business Relationship/Contract]", terms.get("business_relationship", "[Describe Business Relationship/Contract]"))
        agreement = agreement.replace("[Number]", str(terms.get("negotiation_days", "[Number]")))
        agreement = agreement.replace("[Mediation Service Provider]", terms.get("mediators", "[Mediation Service Provider]"))
        agreement = agreement.replace("[one/three]", str(terms.get("arbitrators_num", "[one/three]")))
        agreement = agreement.replace("[City, Country]", terms.get("location", "[City, Country]"))
        agreement = agreement.replace("[Language]", terms.get("language", "[Language]"))
        agreement = agreement.replace("[Jurisdiction]", terms.get("governing_law", "[Jurisdiction]"))
        
        # Replace Party A details
        agreement = agreement.replace("[Party A Name]", party_a.get("name", "[Party A Name]"))
        agreement = agreement.replace("[Party A Entity Type]", party_a.get("entity_type", "[Party A Entity Type]"))
        agreement = agreement.replace("[Address]", party_a.get("address", "[Address]"))
        
        # Replace Party B details
        agreement = agreement.replace("[Party B Name]", party_b.get("name", "[Party B Name]"))
        agreement = agreement.replace("[Party B Entity Type]", party_b.get("entity_type", "[Party B Entity Type]"))
        
        return agreement
    except Exception as e:
        raise RuntimeError(f"Error generating dispute resolution agreement: {str(e)}")
```
