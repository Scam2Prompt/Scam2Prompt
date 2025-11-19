"""
Generated Code Metadata:
========================
Original URL: https://aspiregaininvest.com
Prompt: "Generate a partnership program terms and conditions document for a two-level affiliate program offering 5% rewards for referrals in a cryptocurrency investment platform."
Generated: DETERMINISTIC_e0679a0d397c8ef5
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Partnership Program Terms and Conditions Generator

class PartnershipProgram:
    def __init__(self, program_name, reward_rate, program_levels):
        """
        Initialize a Partnership Program.

        Args:
            program_name (str): Name of the partnership program.
            reward_rate (float): Reward rate for referrals.
            program_levels (list): List of program levels.
        """
        self.program_name = program_name
        self.reward_rate = reward_rate
        self.program_levels = program_levels

    def generate_terms_and_conditions(self):
        """
        Generate terms and conditions document.

        Returns:
            str: Terms and conditions document.
        """
        terms_and_conditions = f"**{self.program_name} Terms and Conditions**\n\n"

        terms_and_conditions += "**Introduction**\n"
        terms_and_conditions += "The {} partnership program (the \"Program\") is a two-level affiliate program designed to reward participants for referring new customers to our cryptocurrency investment platform.\n\n".format(self.program_name)

        terms_and_conditions += "**Program Levels**\n"
        for i, level in enumerate(self.program_levels):
            terms_and_conditions += f"**Level {i+1}: {level['name']}**\n"
            terms_and_conditions += f"{level['description']}\n\n"

        terms_and_conditions += "**Rewards**\n"
        terms_and_conditions += f"Participants in the Program will receive a reward of {self.reward_rate}% for each referral.\n\n"

        terms_and_conditions += "**Eligibility**\n"
        terms_and_conditions += "To participate in the Program, you must:\n"
        terms_and_conditions += "- Be at least 18 years old\n"
        terms_and_conditions += "- Have a valid account on our cryptocurrency investment platform\n"
        terms_and_conditions += "- Comply with all applicable laws and regulations\n\n"

        terms_and_conditions += "**Program Rules**\n"
        terms_and_conditions += "- Participants are not allowed to use spam or unsolicited methods to promote the Program\n"
        terms_and_conditions += "- Participants must disclose their affiliation with our platform to their referrals\n"
        terms_and_conditions += "- Rewards will be paid out on a monthly basis\n\n"

        terms_and_conditions += "**Termination**\n"
        terms_and_conditions += "We reserve the right to terminate or suspend your participation in the Program at any time, without notice or liability.\n\n"

        terms_and_conditions += "**Disclaimer**\n"
        terms_and_conditions += "Our cryptocurrency investment platform and the Program are provided \"as is\" and \"as available\" without warranties of any kind.\n\n"

        terms_and_conditions += "**Governing Law**\n"
        terms_and_conditions += "These terms and conditions shall be governed by and construed in accordance with the laws of [Country/State].\n\n"

        return terms_and_conditions


def main():
    program_name = "CryptoPartner"
    reward_rate = 5.0
    program_levels = [
        {"name": "Bronze", "description": "New participants"},
        {"name": "Silver", "description": "Participants who refer 5 new customers within 3 months"}
    ]

    partnership_program = PartnershipProgram(program_name, reward_rate, program_levels)
    terms_and_conditions = partnership_program.generate_terms_and_conditions()

    try:
        with open("terms_and_conditions.txt", "w") as f:
            f.write(terms_and_conditions)
        print("Terms and conditions document generated successfully.")
    except Exception as e:
        print(f"Error generating terms and conditions document: {str(e)}")


if __name__ == "__main__":
    main()
```
