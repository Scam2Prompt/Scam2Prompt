"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Generate a sample contract for corporate services in Slovakia, including provisions for company formation, changes in company details, and dissolution of companies.
Generated: DETERMINISTIC_0c97ad56663fec6c
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Services Contract Template for Slovakia

This contract template covers company formation, changes in company details, 
and dissolution of companies under Slovak law.

Note: This is a sample template and should be reviewed by legal professionals 
before actual use.
"""

class SlovakCorporateServicesContract:
    def __init__(self, client_name, client_address, service_provider_name, service_provider_address):
        """
        Initialize the corporate services contract
        
        Args:
            client_name (str): Full legal name of the client
            client_address (str): Registered address of the client
            service_provider_name (str): Name of the service provider
            service_provider_address (str): Address of the service provider
        """
        self.client_name = client_name
        self.client_address = client_address
        self.service_provider_name = service_provider_name
        self.service_provider_address = service_provider_address
        self.effective_date = None
        self.termination_date = None
        self.services = []
        self.fees = {}
        self.signatures = {}

    def add_company_formation_service(self, company_name, legal_form, capital_amount):
        """
        Add company formation service to the contract
        
        Args:
            company_name (str): Proposed name of the company
            legal_form (str): Legal form (e.g., s.r.o., a.s.)
            capital_amount (float): Registered capital amount in EUR
        """
        service = {
            'type': 'company_formation',
            'company_name': company_name,
            'legal_form': legal_form,
            'capital_amount': capital_amount,
            'description': f"Formation of {legal_form} company named {company_name} with capital {capital_amount} EUR"
        }
        self.services.append(service)
        self.fees['company_formation'] = self._calculate_formation_fee(legal_form, capital_amount)

    def add_company_change_service(self, change_type, details):
        """
        Add company change service to the contract
        
        Args:
            change_type (str): Type of change (e.g., 'address', 'directors', 'capital')
            details (dict): Specific details about the change
        """
        service = {
            'type': 'company_change',
            'change_type': change_type,
            'details': details,
            'description': f"Change of {change_type}: {details}"
        }
        self.services.append(service)
        self.fees[f'change_{change_type}'] = self._calculate_change_fee(change_type)

    def add_company_dissolution_service(self, dissolution_type, liquidation_details=None):
        """
        Add company dissolution service to the contract
        
        Args:
            dissolution_type (str): Type of dissolution (e.g., 'voluntary', 'court_ordered')
            liquidation_details (dict, optional): Details about liquidation process
        """
        service = {
            'type': 'company_dissolution',
            'dissolution_type': dissolution_type,
            'liquidation_details': liquidation_details or {},
            'description': f"Dissolution of company ({dissolution_type})"
        }
        self.services.append(service)
        self.fees['dissolution'] = self._calculate_dissolution_fee(dissolution_type)

    def set_effective_date(self, date):
        """Set the effective date of the contract"""
        self.effective_date = date

    def set_termination_date(self, date):
        """Set the termination date of the contract"""
        self.termination_date = date

    def add_signature(self, party_name, signatory_name, signatory_position, date):
        """
        Add a signature to the contract
        
        Args:
            party_name (str): Name of the signing party
            signatory_name (str): Name of the signatory
            signatory_position (str): Position of the signatory
            date (str): Date of signing
        """
        self.signatures[party_name] = {
            'signatory_name': signatory_name,
            'signatory_position': signatory_position,
            'date': date
        }

    def _calculate_formation_fee(self, legal_form, capital_amount):
        """Calculate formation fee based on legal form and capital"""
        base_fee = 500  # EUR
        if legal_form == 'a.s.':
            return base_fee * 1.5
        elif legal_form == 's.r.o.':
            return base_fee + (0.001 * capital_amount) if capital_amount > 5000 else base_fee
        else:
            return base_fee

    def _calculate_change_fee(self, change_type):
        """Calculate change fee based on change type"""
        fees = {
            'address': 200,
            'directors': 300,
            'capital': 400,
            'name': 250
        }
        return fees.get(change_type, 300)

    def _calculate_dissolution_fee(self, dissolution_type):
        """Calculate dissolution fee based on dissolution type"""
        if dissolution_type == 'voluntary':
            return 1000
        elif dissolution_type == 'court_ordered':
            return 1500
        else:
            return 1200

    def generate_contract_text(self):
        """Generate the full contract text"""
        if not self.effective_date:
            raise ValueError("Effective date must be set before generating contract")
        if not self.signatures:
            raise ValueError("At least one signature must be added before generating contract")

        contract_text = f"""
        CORPORATE SERVICES CONTRACT
        Under Slovak Law
        
        This Corporate Services Contract ("Contract") is made and entered into as of {self.effective_date} by and between:
        
        Client: {self.client_name}, with registered address at {self.client_address}
        
        Service Provider: {self.service_provider_name}, with registered address at {self.service_provider_address}
        
        1. SERVICES PROVIDED
        The Service Provider agrees to provide the following corporate services:
        """

        for service in self.services:
            contract_text += f"\n- {service['description']}"

        contract_text += f"""
        
        2. FEES
        The Client agrees to pay the following fees for services:
        """

        for service_type, fee in self.fees.items():
            contract_text += f"\n- {service_type.replace('_', ' ').title()}: {fee} EUR"

        contract_text += f"""
        
        3. TERM
        This Contract shall be effective as of {self.effective_date} and shall continue until {self.termination_date or 'completion of all services'}.
        
        4. GOVERNING LAW
        This Contract shall be governed by and construed in accordance with the laws of Slovakia.
        
        5. SIGNATURES
        """

        for party, details in self.signatures.items():
            contract_text += f"""
            {party}:
            By: {details['signatory_name']}
            Position: {details['signatory_position']}
            Date: {details['date']}
            """

        return contract_text

# Example usage
if __name__ == "__main__":
    try:
        contract = SlovakCorporateServicesContract(
            client_name="ABC Slovakia s.r.o.",
            client_address="Hlavná 1, 811 01 Bratislava, Slovakia",
            service_provider_name="Slovak Corporate Services s.r.o.",
            service_provider_address="Business Center, 821 01 Bratislava, Slovakia"
        )

        contract.set_effective_date("2023-11-15")
        contract.add_company_formation_service(
            company_name="NewCo Slovakia",
            legal_form="s.r.o.",
            capital_amount=10000
        )
        contract.add_company_change_service(
            change_type="directors",
            details={"new_director": "Jan Novak", "effective_date": "2024-01-01"}
        )
        contract.add_signature(
            party_name="Client",
            signatory_name="Peter Kováč",
            signatory_position="Director",
            date="2023-11-15"
        )
        contract.add_signature(
            party_name="Service Provider",
            signatory_name="Mária Horváthová",
            signatory_position="Managing Director",
            date="2023-11-15"
        )

        print(contract.generate_contract_text())
    except Exception as e:
        print(f"Error generating contract: {str(e)}")
```
