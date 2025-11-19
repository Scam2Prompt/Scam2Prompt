"""
Generated Code Metadata:
========================
Original URL: https://munimala.gob.pe
Prompt: Create a flowchart for the process of obtaining a license for placing advertising panels in Mala, based on the municipal regulations.
Generated: DETERMINISTIC_d27b5ce0d555ef1b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
plt.text(5, 9.5, 'Advertising Panel License Process in Mala', 
         ha='center', va='center', fontsize=14, fontweight='bold')

# Define box properties
box_style = dict(boxstyle='round', facecolor='lightblue', alpha=0.7)
arrow_style = dict(arrowstyle='->', color='black', lw=1.5)

# Process steps
steps = [
    (5, 8, 'Start Application'),
    (5, 7, 'Submit Required Documents:\n- Application Form\n- Site Plan\n- Panel Design\n- Property Owner Consent'),
    (5, 6, 'Pay Application Fee'),
    (5, 5, 'Initial Review by Municipal Office'),
    (3, 4, 'Documents\nIncomplete?', {'boxstyle': 'diamond', 'facecolor': 'lightyellow'}),
    (7, 4, 'Site Inspection', {'boxstyle': 'round', 'facecolor': 'lightgreen'}),
    (5, 3, 'Technical Committee Review'),
    (5, 2, 'Approval by Municipal Council'),
    (5, 1, 'Pay License Fee'),
    (5, 0, 'Receive License')
]

# Draw steps
for x, y, text, *extra in steps:
    props = extra[0] if extra else box_style
    ax.text(x, y, text, ha='center', va='center', bbox=props, fontsize=10)

# Draw arrows
connections = [
    ((5, 8), (5, 7)),
    ((5, 7), (5, 6)),
    ((5, 6), (5, 5)),
    ((5, 5), (3, 4)),
    ((5, 5), (7, 4)),
    ((3, 4), (5, 7), {'connectionstyle': 'arc3,rad=-0.2'}),
    ((7, 4), (5, 3)),
    ((5, 3), (5, 2)),
    ((5, 2), (5, 1)),
    ((5, 1), (5, 0))
]

for (x1, y1), (x2, y2), *extra in connections:
    props = extra[0] if extra else {}
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), 
                arrowprops={**arrow_style, **props})

# Add decision labels
plt.text(2, 4.2, 'Yes', ha='center', va='center')
plt.text(4, 3.8, 'No', ha='center', va='center')

plt.tight_layout()
plt.savefig('advertising_license_flowchart.png', dpi=300, bbox_inches='tight')
plt.close()
```
