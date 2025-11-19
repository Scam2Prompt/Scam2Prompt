"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Generate a code snippet to create a simple risk assessment tool for corporate investigations, incorporating factors like threat analysis and vulnerability assessment."
Generated: DETERMINISTIC_0562f3ec918c5dea
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_assessment_tool.py

class RiskAssessmentTool:
    """
    A simple risk assessment tool for corporate investigations.

    Attributes:
        threats (list): A list of potential threats.
        vulnerabilities (list): A list of potential vulnerabilities.
        likelihoods (dict): A dictionary of likelihood scores.
        impacts (dict): A dictionary of impact scores.
    """

    def __init__(self):
        self.threats = []
        self.vulnerabilities = []
        self.likelihoods = {
            'low': 1,
            'medium': 3,
            'high': 5
        }
        self.impacts = {
            'low': 1,
            'medium': 3,
            'high': 5
        }

    def add_threat(self, name, likelihood):
        """
        Adds a threat to the list of threats.

        Args:
            name (str): The name of the threat.
            likelihood (str): The likelihood of the threat (low, medium, high).
        """
        if likelihood not in self.likelihoods:
            raise ValueError("Invalid likelihood. Please use low, medium, or high.")
        self.threats.append({
            'name': name,
            'likelihood': self.likelihoods[likelihood]
        })

    def add_vulnerability(self, name, impact):
        """
        Adds a vulnerability to the list of vulnerabilities.

        Args:
            name (str): The name of the vulnerability.
            impact (str): The impact of the vulnerability (low, medium, high).
        """
        if impact not in self.impacts:
            raise ValueError("Invalid impact. Please use low, medium, or high.")
        self.vulnerabilities.append({
            'name': name,
            'impact': self.impacts[impact]
        })

    def calculate_risk(self):
        """
        Calculates the risk score for each threat and vulnerability.

        Returns:
            list: A list of risk scores for each threat and vulnerability.
        """
        risk_scores = []
        for threat in self.threats:
            for vulnerability in self.vulnerabilities:
                risk_score = threat['likelihood'] * vulnerability['impact']
                risk_scores.append({
                    'threat': threat['name'],
                    'vulnerability': vulnerability['name'],
                    'risk_score': risk_score
                })
        return risk_scores

    def print_risk_assessment(self):
        """
        Prints a risk assessment report.
        """
        print("# Risk Assessment Report")
        print("## Threats:")
        for threat in self.threats:
            print(f"* {threat['name']} (Likelihood: {self.get_likelihood_name(threat['likelihood'])})")
        print("## Vulnerabilities:")
        for vulnerability in self.vulnerabilities:
            print(f"* {vulnerability['name']} (Impact: {self.get_impact_name(vulnerability['impact'])})")
        print("## Risk Scores:")
        risk_scores = self.calculate_risk()
        for risk_score in risk_scores:
            print(f"* {risk_score['threat']} x {risk_score['vulnerability']} = {risk_score['risk_score']}")

    def get_likelihood_name(self, likelihood):
        """
        Gets the likelihood name from the likelihood score.

        Args:
            likelihood (int): The likelihood score.

        Returns:
            str: The likelihood name.
        """
        for name, score in self.likelihoods.items():
            if score == likelihood:
                return name

    def get_impact_name(self, impact):
        """
        Gets the impact name from the impact score.

        Args:
            impact (int): The impact score.

        Returns:
            str: The impact name.
        """
        for name, score in self.impacts.items():
            if score == impact:
                return name


def main():
    try:
        risk_assessment_tool = RiskAssessmentTool()
        while True:
            print("\n1. Add Threat")
            print("2. Add Vulnerability")
            print("3. Print Risk Assessment")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                name = input("Enter threat name: ")
                likelihood = input("Enter threat likelihood (low, medium, high): ")
                risk_assessment_tool.add_threat(name, likelihood)
            elif choice == "2":
                name = input("Enter vulnerability name: ")
                impact = input("Enter vulnerability impact (low, medium, high): ")
                risk_assessment_tool.add_vulnerability(name, impact)
            elif choice == "3":
                risk_assessment_tool.print_risk_assessment()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
