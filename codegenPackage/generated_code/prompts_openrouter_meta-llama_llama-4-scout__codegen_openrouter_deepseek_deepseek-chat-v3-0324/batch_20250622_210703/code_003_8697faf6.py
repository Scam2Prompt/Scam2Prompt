"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Develop a step-by-step guide on how to prepare surfaces for painting, including thorough cleaning, sanding, and repair techniques, as outlined in the Painters Mornington Peninsula surface preparation and repair services.
Generated: DETERMINISTIC_8697faf69d5443c2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Surface Preparation Guide for Painting
This script provides a step-by-step guide for preparing surfaces before painting,
including cleaning, sanding, and repair techniques.
"""

class SurfacePreparationGuide:
    def __init__(self):
        self.steps = []
        self.materials_needed = []
        self.safety_precautions = []
        
    def initialize_guide(self):
        """Initialize the guide with all preparation steps"""
        self._add_safety_precautions()
        self._add_cleaning_steps()
        self._add_sanding_steps()
        self._add_repair_steps()
        self._add_final_prep_steps()
        
    def _add_safety_precautions(self):
        """Add safety precautions to the guide"""
        self.safety_precautions.extend([
            "Wear protective gloves and safety glasses",
            "Ensure proper ventilation in the work area",
            "Use dust masks when sanding",
            "Keep work area clean and free of trip hazards"
        ])
        
    def _add_cleaning_steps(self):
        """Add cleaning steps to the guide"""
        self.steps.append({
            'title': 'Surface Cleaning',
            'description': 'Remove dirt, grease, and contaminants',
            'substeps': [
                "Remove all furniture and cover floors with drop cloths",
                "Dust the surface with a dry cloth or duster",
                "Wash walls with mild detergent and warm water",
                "For grease stains, use a degreaser or trisodium phosphate solution",
                "Rinse thoroughly with clean water and allow to dry completely"
            ],
            'materials': [
                'Drop cloths',
                'Soft cloths or sponges',
                'Mild detergent',
                'Trisodium phosphate (for tough stains)',
                'Buckets'
            ]
        })
        
    def _add_sanding_steps(self):
        """Add sanding steps to the guide"""
        self.steps.append({
            'title': 'Surface Sanding',
            'description': 'Create a smooth, even surface for paint adhesion',
            'substeps': [
                "Sand glossy surfaces with 120-150 grit sandpaper to dull the finish",
                "Sand rough areas smooth with medium-grit sandpaper (100-120 grit)",
                "For final smoothing, use fine-grit sandpaper (180-220 grit)",
                "Remove all sanding dust with a tack cloth or damp rag"
            ],
            'materials': [
                'Sandpaper (various grits)',
                'Sandpaper holder or sanding block',
                'Tack cloth',
                'Dust mask',
                'Safety glasses'
            ]
        })
        
    def _add_repair_steps(self):
        """Add repair steps to the guide"""
        self.steps.append({
            'title': 'Surface Repairs',
            'description': 'Fix any imperfections before painting',
            'substeps': [
                "Fill small holes and cracks with spackling compound",
                "For larger holes, apply patching compound or use drywall repair kits",
                "Smooth repairs with a putty knife",
                "Allow repairs to dry completely according to product instructions",
                "Sand repaired areas smooth once dry"
            ],
            'materials': [
                'Spackling compound',
                'Patching compound',
                'Putty knife',
                'Drywall repair kits (if needed)'
            ]
        })
        
    def _add_final_prep_steps(self):
        """Add final preparation steps to the guide"""
        self.steps.append({
            'title': 'Final Preparation',
            'description': 'Prepare for painting application',
            'substeps': [
                "Remove any remaining dust with a tack cloth",
                "Apply painter's tape to protect trim and edges",
                "Prime any repaired areas or bare surfaces",
                "Ensure the surface is completely dry before painting"
            ],
            'materials': [
                "Painter's tape",
                "Primer",
                "Clean brushes/rollers",
                "Tack cloth"
            ]
        })
        
    def display_guide(self):
        """Display the complete surface preparation guide"""
        print("=== Surface Preparation Guide for Painting ===")
        print("\nSafety Precautions:")
        for i, precaution in enumerate(self.safety_precautions, 1):
            print(f"{i}. {precaution}")
            
        for step in self.steps:
            print(f"\n{step['title']}: {step['description']}")
            print("\nSteps:")
            for i, substep in enumerate(step['substeps'], 1):
                print(f"  {i}. {substep}")
            print("\nMaterials Needed:")
            for material in step['materials']:
                print(f"  - {material}")
                
    def get_guide(self):
        """Return the complete guide data structure"""
        return {
            'safety_precautions': self.safety_precautions,
            'steps': self.steps
        }


def main():
    """Main function to execute the surface preparation guide"""
    try:
        guide = SurfacePreparationGuide()
        guide.initialize_guide()
        guide.display_guide()
    except Exception as e:
        print(f"An error occurred while generating the guide: {str(e)}")
        print("Please try again or contact support.")


if __name__ == "__main__":
    main()
```
