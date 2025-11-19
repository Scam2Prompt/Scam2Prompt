"""
Generated Code Metadata:
========================
Original URL: https://aptoslive.com
Prompt: "Create an infographic illustrating the benefits of using Aptos ONE POS for retailers, including its impact on customer engagement, inventory management, and sales growth."
Generated: DETERMINISTIC_da2e368044aaea24
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Title
title = "Benefits of Aptos ONE POS for Retailers"
plt.title(title, fontsize=18, pad=20, fontweight='bold')

# Main sections
sections = [
    ("Customer Engagement", 0.7, 0.7, "#4E79A7"),
    ("Inventory Management", 0.3, 0.7, "#F28E2B"),
    ("Sales Growth", 0.7, 0.3, "#E15759")
]

# Benefits for each section
benefits = {
    "Customer Engagement": [
        "Personalized promotions",
        "Faster checkout",
        "Customer loyalty programs",
        "Seamless omnichannel experience"
    ],
    "Inventory Management": [
        "Real-time stock tracking",
        "Automated reordering",
        "Reduced overstock/out-of-stock",
        "Advanced analytics"
    ],
    "Sales Growth": [
        "Data-driven decisions",
        "Upsell/cross-sell opportunities",
        "Improved staff efficiency",
        "24/7 business insights"
    ]
}

# Draw sections
for section, x, y, color in sections:
    ax.add_patch(Rectangle((x-0.2, y-0.15), 0.4, 0.3, 
                          facecolor=color, alpha=0.7,
                          edgecolor='black', linewidth=1))
    ax.text(x, y, section, ha='center', va='center', 
            fontsize=14, fontweight='bold', color='white')
    
    # Add benefits
    for i, benefit in enumerate(benefits[section]):
        ax.text(x, y - 0.05 - i*0.05, f"• {benefit}", 
                ha='center', va='center', fontsize=10)

# Central Aptos ONE POS logo/circle
central_circle = plt.Circle((0.5, 0.5), 0.15, 
                          facecolor='#59A14F', alpha=0.9)
ax.add_patch(central_circle)
ax.text(0.5, 0.5, "Aptos\nONE POS", 
        ha='center', va='center', 
        fontsize=14, fontweight='bold', color='white')

# Connecting lines
for section, x, y, _ in sections:
    ax.plot([0.5, x], [0.5, y], color='gray', linestyle='--', alpha=0.5)

# Footer
footer_text = "Transform your retail business with Aptos ONE POS - The all-in-one solution for modern retailers"
ax.text(0.5, 0.05, footer_text, ha='center', va='center', 
        fontsize=10, style='italic')

# Save the infographic
plt.tight_layout()
plt.savefig('aptos_one_pos_benefits.png', dpi=300, bbox_inches='tight')
plt.close()
```
