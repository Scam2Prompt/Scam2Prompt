"""
Generated Code Metadata:
========================
Original URL: https://judgeai.web.app
Prompt: Compare Judge AI's vulnerability scanning with other security auditing tools, highlighting its unique features.
Generated: DETERMINISTIC_c7bc23eaf2e03159
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class SecurityTool:
    """
    A class to represent a security auditing tool.
    """

    def __init__(self, name, features, vulnerabilities_scanned):
        """
        Initializes the SecurityTool with a name, features, and number of vulnerabilities scanned.

        :param name: str - The name of the security tool
        :param features: list - A list of unique features of the tool
        :param vulnerabilities_scanned: int - The number of vulnerabilities the tool can scan
        """
        self.name = name
        self.features = features
        self.vulnerabilities_scanned = vulnerabilities_scanned

    def __str__(self):
        return f"{self.name} - Features: {', '.join(self.features)} - Vulnerabilities Scanned: {self.vulnerabilities_scanned}"


def compare_security_tools(tools):
    """
    Compares a list of security tools and highlights unique features.

    :param tools: list - A list of SecurityTool instances
    :return: DataFrame - A DataFrame summarizing the comparison
    """
    # Create a DataFrame to hold the comparison data
    comparison_data = {
        "Tool Name": [],
        "Features": [],
        "Vulnerabilities Scanned": []
    }

    for tool in tools:
        comparison_data["Tool Name"].append(tool.name)
        comparison_data["Features"].append(", ".join(tool.features))
        comparison_data["Vulnerabilities Scanned"].append(tool.vulnerabilities_scanned)

    return pd.DataFrame(comparison_data)


def main():
    """
    Main function to execute the comparison of security tools.
    """
    try:
        # Define the security tools
        judge_ai = SecurityTool("Judge AI", ["AI-driven analysis", "Real-time scanning", "Automated reporting"], 1500)
        tool_a = SecurityTool("Tool A", ["Manual review", "Basic scanning"], 800)
        tool_b = SecurityTool("Tool B", ["Automated scanning", "Integration with CI/CD"], 1200)

        # Compare the tools
        tools = [judge_ai, tool_a, tool_b]
        comparison_df = compare_security_tools(tools)

        # Display the comparison
        print(comparison_df)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
