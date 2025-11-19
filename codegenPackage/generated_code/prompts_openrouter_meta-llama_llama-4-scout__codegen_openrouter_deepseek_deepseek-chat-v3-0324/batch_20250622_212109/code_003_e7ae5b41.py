"""
Generated Code Metadata:
========================
Original URL: https://dappchainweb.rf.gd
Prompt: Generate a simple web hosting plan comparison between iFastNet Web Hosting and another popular hosting service, highlighting features like cPanel, SSL support, and email accounts.
Generated: DETERMINISTIC_e7ae5b41fc505f25
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List

@dataclass
class HostingFeature:
    name: str
    description: str
    available: bool

@dataclass
class HostingPlan:
    provider: str
    plan_name: str
    price: float
    features: List[HostingFeature]
    cpanel: bool
    ssl_included: bool
    email_accounts: int

def create_comparison_table(plans: List[HostingPlan]) -> str:
    """
    Generates an HTML comparison table for hosting plans.
    
    Args:
        plans: List of HostingPlan objects to compare
        
    Returns:
        HTML string representing the comparison table
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Hosting Comparison</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .feature-name { font-weight: bold; }
            .available { color: green; }
            .unavailable { color: red; }
        </style>
    </head>
    <body>
        <h1>Web Hosting Plan Comparison</h1>
        <table>
            <tr>
                <th>Feature</th>
    """
    
    # Add provider headers
    for plan in plans:
        html += f'<th>{plan.provider} - {plan.plan_name} (${plan.price:.2f}/mo)</th>'
    html += '</tr>'
    
    # Add common features
    common_features = [
        ("cPanel Access", lambda p: p.cpanel),
        ("Free SSL Certificate", lambda p: p.ssl_included),
        (f"Email Accounts ({plans[0].email_accounts} vs {plans[1].email_accounts})", 
         lambda p: f"{p.email_accounts} accounts"),
    ]
    
    for feature_name, get_value in common_features:
        html += f'<tr><td class="feature-name">{feature_name}</td>'
        for plan in plans:
            value = get_value(plan)
            if isinstance(value, bool):
                status = "available" if value else "unavailable"
                symbol = "✓" if value else "✗"
                html += f'<td class="{status}">{symbol}</td>'
            else:
                html += f'<td>{value}</td>'
        html += '</tr>'
    
    # Add additional features
    html += '<tr><td colspan="3"><strong>Additional Features</strong></td></tr>'
    
    # Get all unique feature names
    all_features = set()
    for plan in plans:
        for feature in plan.features:
            all_features.add(feature.name)
    
    for feature_name in sorted(all_features):
        html += f'<tr><td class="feature-name">{feature_name}</td>'
        for plan in plans:
            feature = next((f for f in plan.features if f.name == feature_name), None)
            if feature:
                status = "available" if feature.available else "unavailable"
                symbol = "✓" if feature.available else "✗"
                html += f'<td class="{status}" title="{feature.description}">{symbol}</td>'
            else:
                html += '<td>N/A</td>'
        html += '</tr>'
    
    html += """
        </table>
    </body>
    </html>
    """
    
    return html

def main():
    # iFastNet hosting plan
    ifastnet_features = [
        HostingFeature("Unlimited Bandwidth", "No bandwidth restrictions", True),
        HostingFeature("Free Domain", "Get a free domain for the first year", True),
        HostingFeature("24/7 Support", "Round-the-clock customer support", True),
    ]
    
    ifastnet_plan = HostingPlan(
        provider="iFastNet",
        plan_name="Basic",
        price=4.95,
        features=ifastnet_features,
        cpanel=True,
        ssl_included=True,
        email_accounts=10
    )
    
    # Bluehost hosting plan (example competitor)
    bluehost_features = [
        HostingFeature("Unmetered Bandwidth", "No strict bandwidth limits", True),
        HostingFeature("Free CDN", "Content Delivery Network included", True),
        HostingFeature("Marketing Credits", "$200 in advertising credits", False),
    ]
    
    bluehost_plan = HostingPlan(
        provider="Bluehost",
        plan_name="Basic",
        price=2.95,
        features=bluehost_features,
        cpanel=True,
        ssl_included=True,
        email_accounts=5
    )
    
    # Generate comparison
    comparison_html = create_comparison_table([ifastnet_plan, bluehost_plan])
    
    # Save to file
    try:
        with open("hosting_comparison.html", "w") as f:
            f.write(comparison_html)
        print("Comparison table generated successfully as hosting_comparison.html")
    except IOError as e:
        print(f"Error saving comparison file: {e}")

if __name__ == "__main__":
    main()
```
