"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Develop a script to handle DG/HAZ goods packaging and labeling, ensuring compliance with international shipping regulations, as offered by Alexa Shipping.
Generated: DETERMINISTIC_541edc8ef7d90978
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# goods_packaging.py

import logging
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GoodsType(str, Enum):
    """Enum for goods type"""
    DG = "DG"
    HAZ = "HAZ"
    NON_DG = "NON_DG"

class PackagingMaterial(str, Enum):
    """Enum for packaging material"""
    PLASTIC = "PLASTIC"
    WOOD = "WOOD"
    METAL = "METAL"
    PAPER = "PAPER"

class Label:
    """Class to represent a shipping label"""
    def __init__(self, goods_type: GoodsType, packaging_material: PackagingMaterial, 
                 label_text: str, label_barcode: str):
        self.goods_type = goods_type
        self.packaging_material = packaging_material
        self.label_text = label_text
        self.label_barcode = label_barcode

class GoodsPackaging:
    """Class to handle goods packaging and labeling"""
    def __init__(self):
        self.goods_types = {
            GoodsType.DG: self.handle_dg_goods,
            GoodsType.HAZ: self.handle_haz_goods,
            GoodsType.NON_DG: self.handle_non_dg_goods
        }

    def handle_dg_goods(self, packaging_material: PackagingMaterial, 
                       label_text: str, label_barcode: str) -> Label:
        """Handle DG goods packaging and labeling"""
        # DG goods require special handling and labeling
        if packaging_material not in [PackagingMaterial.PLASTIC, PackagingMaterial.METAL]:
            raise ValueError("DG goods require PLASTIC or METAL packaging material")
        
        # Add DG specific label text
        label_text = f"DG - {label_text}"
        
        return Label(GoodsType.DG, packaging_material, label_text, label_barcode)

    def handle_haz_goods(self, packaging_material: PackagingMaterial, 
                        label_text: str, label_barcode: str) -> Label:
        """Handle HAZ goods packaging and labeling"""
        # HAZ goods require special handling and labeling
        if packaging_material not in [PackagingMaterial.PLASTIC, PackagingMaterial.WOOD]:
            raise ValueError("HAZ goods require PLASTIC or WOOD packaging material")
        
        # Add HAZ specific label text
        label_text = f"HAZ - {label_text}"
        
        return Label(GoodsType.HAZ, packaging_material, label_text, label_barcode)

    def handle_non_dg_goods(self, packaging_material: PackagingMaterial, 
                            label_text: str, label_barcode: str) -> Label:
        """Handle NON DG goods packaging and labeling"""
        return Label(GoodsType.NON_DG, packaging_material, label_text, label_barcode)

    def package_and_label_goods(self, goods_type: GoodsType, 
                               packaging_material: PackagingMaterial, 
                               label_text: str, label_barcode: str) -> Label:
        """Package and label goods based on goods type"""
        try:
            return self.goods_types[goods_type](packaging_material, label_text, label_barcode)
        except KeyError:
            logging.error(f"Unsupported goods type: {goods_type}")
            raise ValueError(f"Unsupported goods type: {goods_type}")

def main():
    goods_packaging = GoodsPackaging()
    
    # Example usage:
    dg_label = goods_packaging.package_and_label_goods(
        GoodsType.DG, PackagingMaterial.PLASTIC, "DG Goods", "DG123456"
    )
    print(f"DG Label: {dg_label.label_text} - {dg_label.label_barcode}")
    
    haz_label = goods_packaging.package_and_label_goods(
        GoodsType.HAZ, PackagingMaterial.WOOD, "HAZ Goods", "HAZ789012"
    )
    print(f"HAZ Label: {haz_label.label_text} - {haz_label.label_barcode}")
    
    non_dg_label = goods_packaging.package_and_label_goods(
        GoodsType.NON_DG, PackagingMaterial.PAPER, "NON DG Goods", "NON_DG345678"
    )
    print(f"NON DG Label: {non_dg_label.label_text} - {non_dg_label.label_barcode}")

if __name__ == "__main__":
    main()
```
