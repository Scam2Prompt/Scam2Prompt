"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Develop a chatbot that uses AI to assist customers in choosing printing services and calculating costs for items like self-inking stamps, die-cut stickers, and product labels, based on ThePrintNan's offerings.
Generated: DETERMINISTIC_a4f88840b6f90b9c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass

# Define data models for printing services
@dataclass
class PrintingService:
    name: str
    description: str
    base_price: float
    price_per_unit: float
    min_quantity: int
    max_quantity: int
    options: Dict[str, List[str]]
    additional_fees: Dict[str, float] = None

# Database of available printing services
PRINTING_SERVICES = {
    "self_inking_stamp": PrintingService(
        name="Self-Inking Stamp",
        description="Custom self-inking stamps with your design",
        base_price=15.99,
        price_per_unit=0.50,
        min_quantity=1,
        max_quantity=1000,
        options={
            "size": ["1x1 inch", "1.5x1.5 inch", "2x2 inch"],
            "color": ["black", "red", "blue", "green"],
            "ink_color": ["black", "red", "blue"]
        },
        additional_fees={
            "express_shipping": 10.00,
            "design_service": 25.00
        }
    ),
    "die_cut_sticker": PrintingService(
        name="Die-Cut Sticker",
        description="Premium quality die-cut stickers",
        base_price=10.00,
        price_per_unit=0.20,
        min_quantity=50,
        max_quantity=5000,
        options={
            "material": ["vinyl", "glossy", "matte"],
            "shape": ["circle", "square", "custom"],
            "finish": ["gloss", "matte"]
        },
        additional_fees={
            "custom_shape": 15.00,
            "waterproof": 5.00
        }
    ),
    "product_label": PrintingService(
        name="Product Label",
        description="Professional product labels for branding",
        base_price=20.00,
        price_per_unit=0.10,
        min_quantity=100,
        max_quantity=10000,
        options={
            "material": ["paper", "vinyl", "polyester"],
            "adhesive": ["permanent", "removable"],
            "finish": ["gloss", "matte", "satin"]
        },
        additional_fees={
            "custom_size": 10.00,
            "variable_data": 30.00
        }
    )
}

class PrintingServiceChatbot:
    def __init__(self):
        self.current_service = None
        self.current_options = {}
        self.current_quantity = 0
    
    def greet(self) -> str:
        """Return welcome message and available services."""
        services_list = "\n".join([f"- {service.name}" for service in PRINTING_SERVICES.values()])
        return (
            "Welcome to ThePrintNan's printing service assistant!\n"
            "I can help you with the following services:\n"
            f"{services_list}\n"
            "Which service are you interested in?"
        )
    
    def select_service(self, service_name: str) -> str:
        """Select a printing service and return its details."""
        service_key = self._normalize_service_name(service_name)
        
        if service_key not in PRINTING_SERVICES:
            return "Sorry, I don't recognize that service. Please choose from our available services."
        
        self.current_service = PRINTING_SERVICES[service_key]
        self.current_options = {}
        self.current_quantity = 0
        
        options_text = "\n".join([
            f"{option}: {', '.join(values)}"
            for option, values in self.current_service.options.items()
        ])
        
        return (
            f"Great choice! Here's what we offer for {self.current_service.name}:\n"
            f"{self.current_service.description}\n"
            f"Base price: ${self.current_service.base_price:.2f}\n"
            f"Price per unit: ${self.current_service.price_per_unit:.2f}\n"
            f"Minimum quantity: {self.current_service.min_quantity}\n"
            f"Maximum quantity: {self.current_service.max_quantity}\n\n"
            f"Available options:\n{options_text}\n\n"
            "What quantity would you like? (Please enter a number)"
        )
    
    def set_quantity(self, quantity_str: str) -> str:
        """Set the quantity and validate it."""
        try:
            quantity = int(quantity_str)
        except ValueError:
            return "Please enter a valid number for the quantity."
        
        if quantity < self.current_service.min_quantity:
            return f"Minimum quantity for this service is {self.current_service.min_quantity}."
        if quantity > self.current_service.max_quantity:
            return f"Maximum quantity for this service is {self.current_service.max_quantity}."
        
        self.current_quantity = quantity
        return (
            f"Quantity set to {quantity}. Now please specify your options.\n"
            "For example: 'size=1x1 inch, color=blue'"
        )
    
    def set_options(self, options_str: str) -> str:
        """Parse and set options for the current service."""
        if not self.current_service:
            return "Please select a service first."
        
        try:
            options = self._parse_options(options_str)
        except ValueError as e:
            return str(e)
        
        for option, value in options.items():
            if option not in self.current_service.options:
                return f"Invalid option: {option}. Available options are: {', '.join(self.current_service.options.keys())}"
            
            if value not in self.current_service.options[option]:
                return f"Invalid value '{value}' for option {option}. Available values are: {', '.join(self.current_service.options[option])}"
            
            self.current_options[option] = value
        
        return (
            "Options set successfully. Would you like to add any additional services?\n"
            f"Available extras: {', '.join(self.current_service.additional_fees.keys())}\n"
            "For example: 'express_shipping, design_service'"
        )
    
    def set_extras(self, extras_str: str) -> str:
        """Parse and set additional services."""
        if not self.current_service:
            return "Please select a service first."
        
        extras = [extra.strip() for extra in extras_str.split(",")]
        selected_extras = {}
        invalid_extras = []
        
        for extra in extras:
            if extra in self.current_service.additional_fees:
                selected_extras[extra] = self.current_service.additional_fees[extra]
            else:
                invalid_extras.append(extra)
        
        if invalid_extras:
            return (
                f"Invalid extras: {', '.join(invalid_extras)}. "
                f"Available extras are: {', '.join(self.current_service.additional_fees.keys())}"
            )
        
        self.current_options["extras"] = selected_extras
        return self._calculate_total()
    
    def _calculate_total(self) -> str:
        """Calculate and return the total cost."""
        if not self.current_service or not self.current_quantity:
            return "Please complete your order selection first."
        
        base_cost = self.current_service.base_price
        unit_cost = self.current_service.price_per_unit * self.current_quantity
        extras_cost = sum(self.current_options.get("extras", {}).values())
        
        total = base_cost + unit_cost + extras_cost
        
        options_text = "\n".join([
            f"{option}: {value}" 
            for option, value in self.current_options.items() 
            if option != "extras"
        ])
        
        extras_text = ", ".join(self.current_options.get("extras", {}).keys()) or "None"
        
        return (
            "Here's your order summary:\n"
            f"Service: {self.current_service.name}\n"
            f"Quantity: {self.current_quantity}\n"
            f"Options:\n{options_text}\n"
            f"Extras: {extras_text}\n\n"
            f"Total cost: ${total:.2f}\n\n"
            "Would you like to proceed with this order? (yes/no)"
        )
    
    def _normalize_service_name(self, name: str) -> str:
        """Normalize service name for lookup."""
        return name.lower().replace(" ", "_").replace("-", "_")
    
    def _parse_options(self, options_str: str) -> Dict[str, str]:
        """Parse options string into a dictionary."""
        options = {}
        for pair in options_str.split(","):
            pair = pair.strip()
            if "=" not in pair:
                raise ValueError(f"Invalid option format: '{pair}'. Please use 'option=value' format.")
            
            key, value = pair.split("=", 1)
            options[key.strip()] = value.strip()
        
        return options
    
    def reset(self) -> None:
        """Reset the current order."""
        self.current_service = None
        self.current_options = {}
        self.current_quantity = 0

def main():
    """Run the chatbot in interactive mode."""
    chatbot = PrintingServiceChatbot()
    print(chatbot.greet())
    
    while True:
        user_input =
