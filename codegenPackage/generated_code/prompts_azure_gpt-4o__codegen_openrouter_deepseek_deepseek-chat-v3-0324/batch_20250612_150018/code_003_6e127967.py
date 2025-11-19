"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Write code to automate the generation of contact forms for a packaging manufacturer, including fields for product inquiries about ABS Atlas trays and bakery trays, as described on Isoplas Corporation's website.
Generated: DETERMINISTIC_6e127967ec31037f
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto

class ProductType(Enum):
    """Enumeration of product types available for inquiry."""
    ABS_ATLAS_TRAY = auto()
    BAKERY_TRAY = auto()

@dataclass
class FormField:
    """Represents a single field in the contact form."""
    name: str
    label: str
    field_type: str  # 'text', 'email', 'select', 'textarea', etc.
    required: bool = True
    options: Optional[List[str]] = None
    placeholder: Optional[str] = None

@dataclass
class ProductInquiry:
    """Represents a product inquiry section in the form."""
    product_type: ProductType
    fields: List[FormField]

class ContactFormGenerator:
    """Generates contact forms for packaging product inquiries."""
    
    def __init__(self):
        self.base_fields = [
            FormField(
                name="name",
                label="Full Name",
                field_type="text",
                placeholder="John Doe"
            ),
            FormField(
                name="company",
                label="Company Name",
                field_type="text",
                placeholder="ACME Corp"
            ),
            FormField(
                name="email",
                label="Email Address",
                field_type="email",
                placeholder="your.email@example.com"
            ),
            FormField(
                name="phone",
                label="Phone Number",
                field_type="tel",
                required=False,
                placeholder="+1 (123) 456-7890"
            ),
            FormField(
                name="message",
                label="Additional Information",
                field_type="textarea",
                required=False,
                placeholder="Your message here..."
            )
        ]
        
        self.product_inquiries = {
            ProductType.ABS_ATLAS_TRAY: ProductInquiry(
                product_type=ProductType.ABS_ATLAS_TRAY,
                fields=[
                    FormField(
                        name="quantity",
                        label="Estimated Quantity Needed",
                        field_type="text",
                        placeholder="e.g., 1000 units/month"
                    ),
                    FormField(
                        name="color",
                        label="Preferred Color",
                        field_type="select",
                        options=["Black", "White", "Custom"]
                    ),
                    FormField(
                        name="dimensions",
                        label="Required Dimensions (L x W x H)",
                        field_type="text",
                        placeholder="e.g., 12x8x4 inches"
                    )
                ]
            ),
            ProductType.BAKERY_TRAY: ProductInquiry(
                product_type=ProductType.BAKERY_TRAY,
                fields=[
                    FormField(
                        name="quantity",
                        label="Estimated Quantity Needed",
                        field_type="text",
                        placeholder="e.g., 500 units/week"
                    ),
                    FormField(
                        name="material",
                        label="Material Preference",
                        field_type="select",
                        options=["PP", "PET", "PS", "Other"]
                    ),
                    FormField(
                        name="special_requirements",
                        label="Special Requirements",
                        field_type="textarea",
                        required=False,
                        placeholder="e.g., venting, stacking, etc."
                    )
                ]
            )
        }
    
    def generate_form(self, product_types: List[ProductType]) -> dict:
        """
        Generates a contact form JSON structure for the specified product types.
        
        Args:
            product_types: List of ProductType enums for which to generate form fields
            
        Returns:
            dict: The complete form structure including base fields and product-specific fields
        """
        if not product_types:
            raise ValueError("At least one product type must be specified")
            
        form_structure = {
            "base_fields": [field.__dict__ for field in self.base_fields],
            "product_inquiries": []
        }
        
        for product_type in product_types:
            if product_type not in self.product_inquiries:
                raise ValueError(f"Unsupported product type: {product_type}")
                
            inquiry = self.product_inquiries[product_type]
            form_structure["product_inquiries"].append({
                "product_type": inquiry.product_type.name,
                "fields": [field.__dict__ for field in inquiry.fields]
            })
            
        return form_structure
    
    def generate_html_form(self, product_types: List[ProductType]) -> str:
        """
        Generates an HTML contact form for the specified product types.
        
        Args:
            product_types: List of ProductType enums for which to generate form fields
            
        Returns:
            str: HTML string of the generated form
        """
        form_json = self.generate_form(product_types)
        html = ['<form id="packaging-inquiry-form" method="POST">']
        
        # Add base fields
        html.append('<fieldset><legend>Contact Information</legend>')
        for field in form_json["base_fields"]:
            html.append(self._render_field(field))
        html.append('</fieldset>')
        
        # Add product inquiries
        for inquiry in form_json["product_inquiries"]:
            html.append(f'<fieldset><legend>{inquiry["product_type"].replace("_", " ").title()} Inquiry</legend>')
            for field in inquiry["fields"]:
                html.append(self._render_field(field))
            html.append('</fieldset>')
        
        html.append('<button type="submit">Submit Inquiry</button>')
        html.append('</form>')
        
        return '\n'.join(html)
    
    def _render_field(self, field: dict) -> str:
        """Helper method to render a single form field as HTML."""
        required_attr = " required" if field["required"] else ""
        placeholder_attr = f' placeholder="{field["placeholder"]}"' if field["placeholder"] else ""
        
        if field["field_type"] == "select":
            options = ''.join(f'<option value="{opt}">{opt}</option>' for opt in field["options"])
            return f'''
            <div class="form-group">
                <label for="{field["name"]}">{field["label"]}</label>
                <select id="{field["name"]}" name="{field["name"]}"{required_attr}>
                    <option value="">Select an option</option>
                    {options}
                </select>
            </div>
            '''
        elif field["field_type"] == "textarea":
            return f'''
            <div class="form-group">
                <label for="{field["name"]}">{field["label"]}</label>
                <textarea id="{field["name"]}" name="{field["name"]}"{required_attr}{placeholder_attr}></textarea>
            </div>
            '''
        else:
            return f'''
            <div class="form-group">
                <label for="{field["name"]}">{field["label"]}</label>
                <input type="{field["field_type"]}" id="{field["name"]}" name="{field["name"]}"{required_attr}{placeholder_attr}>
            </div>
            '''

# Example usage
if __name__ == "__main__":
    generator = ContactFormGenerator()
    
    # Generate form for both product types
    form_json = generator.generate_form([ProductType.ABS_ATLAS_TRAY, ProductType.BAKERY_TRAY])
    print(json.dumps(form_json, indent=2))
    
    # Generate HTML form for ABS Atlas trays only
    html_form = generator.generate_html_form([ProductType.ABS_ATLAS_TRAY])
    print(html_form)
```
