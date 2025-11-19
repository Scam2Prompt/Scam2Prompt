"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Write a program to generate a detailed árajánlat (price quote) for műanyag ablakcsere (plastic window replacement) based on the dimensions and specifications provided by the user.
Generated: DETERMINISTIC_16a1c3addd7774bf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class WindowSpecs:
    width: float  # in meters
    height: float  # in meters
    type: str  # e.g., "single", "double", "triple"
    color: str  # e.g., "white", "wood", "custom"
    has_mosquito_net: bool
    has_blinds: bool
    has_handle: bool
    quantity: int = 1

@dataclass
class PriceQuote:
    base_price: float
    size_surcharge: float
    type_surcharge: float
    color_surcharge: float
    mosquito_net_price: float
    blinds_price: float
    handle_price: float
    quantity: int
    subtotal: float
    tax: float
    total: float

class WindowQuoteGenerator:
    BASE_PRICE_PER_SQM = 25000  # HUF per square meter
    SIZE_SURCHARGE_THRESHOLD = 1.5  # sqm
    SIZE_SURCHARGE_RATE = 0.1  # 10% surcharge for large windows
    
    TYPE_SURCHARGES = {
        "single": 0.0,
        "double": 0.15,
        "triple": 0.25
    }
    
    COLOR_SURCHARGES = {
        "white": 0.0,
        "wood": 0.12,
        "custom": 0.2
    }
    
    MOSQUITO_NET_PRICE = 5000  # HUF
    BLINDS_PRICE = 8000  # HUF
    HANDLE_PRICE = 2000  # HUF
    TAX_RATE = 0.27  # 27% VAT
    
    def calculate_quote(self, specs: WindowSpecs) -> PriceQuote:
        try:
            # Validate inputs
            if specs.width <= 0 or specs.height <= 0:
                raise ValueError("Window dimensions must be positive")
            if specs.type not in self.TYPE_SURCHARGES:
                raise ValueError(f"Invalid window type: {specs.type}")
            if specs.color not in self.COLOR_SURCHARGES:
                raise ValueError(f"Invalid color: {specs.color}")
            if specs.quantity <= 0:
                raise ValueError("Quantity must be at least 1")
            
            # Calculate area
            area = specs.width * specs.height
            
            # Base price calculation
            base_price = area * self.BASE_PRICE_PER_SQM
            
            # Size surcharge
            size_surcharge = 0.0
            if area > self.SIZE_SURCHARGE_THRESHOLD:
                size_surcharge = base_price * self.SIZE_SURCHARGE_RATE
            
            # Type surcharge
            type_surcharge = base_price * self.TYPE_SURCHARGES[specs.type]
            
            # Color surcharge
            color_surcharge = base_price * self.COLOR_SURCHARGES[specs.color]
            
            # Additional features
            mosquito_net_price = self.MOSQUITO_NET_PRICE if specs.has_mosquito_net else 0
            blinds_price = self.BLINDS_PRICE if specs.has_blinds else 0
            handle_price = self.HANDLE_PRICE if specs.has_handle else 0
            
            # Calculate subtotal
            subtotal = (base_price + size_surcharge + type_surcharge + color_surcharge + 
                       mosquito_net_price + blinds_price + handle_price) * specs.quantity
            
            # Calculate tax and total
            tax = subtotal * self.TAX_RATE
            total = subtotal + tax
            
            return PriceQuote(
                base_price=base_price,
                size_surcharge=size_surcharge,
                type_surcharge=type_surcharge,
                color_surcharge=color_surcharge,
                mosquito_net_price=mosquito_net_price,
                blinds_price=blinds_price,
                handle_price=handle_price,
                quantity=specs.quantity,
                subtotal=subtotal,
                tax=tax,
                total=total
            )
        
        except ValueError as e:
            print(f"Error in calculation: {e}")
            raise

def get_user_input() -> WindowSpecs:
    print("Műanyag ablakcsere árajánlat készítése")
    print("Kérem adja meg az ablak adatait:")
    
    try:
        width = float(input("Szélesség (m): "))
        height = float(input("Magasság (m): "))
        type_ = input("Ablak típusa (single/double/triple): ").lower()
        color = input("Szín (white/wood/custom): ").lower()
        mosquito_net = input("Szúnyogháló (igen/nem): ").lower() == "igen"
        blinds = input("Redőny (igen/nem): ").lower() == "igen"
        handle = input("Különleges fogantyú (igen/nem): ").lower() == "igen"
        quantity = int(input("Mennyiség: "))
        
        return WindowSpecs(
            width=width,
            height=height,
            type=type_,
            color=color,
            has_mosquito_net=mosquito_net,
            has_blinds=blinds,
            has_handle=handle,
            quantity=quantity
        )
    except ValueError as e:
        print(f"Hibás adatbevitel: {e}")
        raise

def format_quote(quote: PriceQuote) -> str:
    formatted = "\n=== ÁRAJÁNLAT ===\n"
    formatted += f"Alapár: {quote.base_price:,.0f} HUF\n"
    formatted += f"Méret felár: {quote.size_surcharge:,.0f} HUF\n"
    formatted += f"Típus felár: {quote.type_surcharge:,.0f} HUF\n"
    formatted += f"Szín felár: {quote.color_surcharge:,.0f} HUF\n"
    
    if quote.mosquito_net_price > 0:
        formatted += f"Szúnyogháló: {quote.mosquito_net_price:,.0f} HUF\n"
    if quote.blinds_price > 0:
        formatted += f"Redőny: {quote.blinds_price:,.0f} HUF\n"
    if quote.handle_price > 0:
        formatted += f"Különleges fogantyú: {quote.handle_price:,.0f} HUF\n"
    
    formatted += f"Mennyiség: {quote.quantity}\n"
    formatted += f"Részösszeg: {quote.subtotal:,.0f} HUF\n"
    formatted += f"ÁFA (27%): {quote.tax:,.0f} HUF\n"
    formatted += f"Végösszeg: {quote.total:,.0f} HUF\n"
    formatted += "=================\n"
    
    return formatted

def main():
    try:
        generator = WindowQuoteGenerator()
        specs = get_user_input()
        quote = generator.calculate_quote(specs)
        print(format_quote(quote))
    except Exception as e:
        print(f"Hiba történt: {e}")

if __name__ == "__main__":
    main()
```
