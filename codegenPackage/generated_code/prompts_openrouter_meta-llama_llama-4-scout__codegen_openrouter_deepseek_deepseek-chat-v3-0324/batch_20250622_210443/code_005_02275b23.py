"""
Generated Code Metadata:
========================
Original URL: https://anamalika.com
Prompt: Write a tutorial on how to apply مكياج الوجه (face makeup) using products from استي لودر (Estee Lauder) and فور ايفر (Forever).
Generated: DETERMINISTIC_02275b23cc6fa235
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script provides a step-by-step tutorial for applying face makeup using Estee Lauder and Forever products
# It includes product recommendations and application techniques

class MakeupTutorial:
    def __init__(self):
        self.steps = []
        self.products = {
            'Estee Lauder': {
                'foundation': 'Double Wear Stay-in-Place Foundation',
                'concealer': 'Double Wear Stay-in-Place Flawless Wear Concealer',
                'powder': 'Double Wear Stay-in-Place Matte Powder Foundation',
                'blush': 'Pure Color Envy Sculpting Blush',
                'highlighter': 'Pure Color Envy Sculpting Highlighting Duo'
            },
            'Forever': {
                'eyeshadow': 'Forever Flawless Eyeshadow Palette',
                'mascara': 'Forever Ultimate Mascara',
                'lipstick': 'Forever Matte Liquid Lipstick',
                'eyeliner': 'Forever Precision Liquid Eyeliner'
            }
        }
        
        self._initialize_steps()
    
    def _initialize_steps(self):
        """Initialize the step-by-step makeup application process"""
        self.steps = [
            self._prep_skin,
            self._apply_foundation,
            self._apply_concealer,
            self._set_with_powder,
            self._contour_and_blush,
            self._highlight,
            self._apply_eyeshadow,
            self._apply_eyeliner,
            self._apply_mascara,
            self._apply_lipstick,
            self._set_makeup
        ]
    
    def _prep_skin(self):
        """Step 1: Prepare the skin before makeup application"""
        print("\nStep 1: Prep Your Skin")
        print("- Cleanse your face with a gentle cleanser")
        print("- Apply moisturizer suitable for your skin type")
        print("- Use a primer to create a smooth base (recommended: Estee Lauder The Smoother Primer)")
    
    def _apply_foundation(self):
        """Step 2: Apply foundation for an even base"""
        print("\nStep 2: Apply Foundation")
        product = self.products['Estee Lauder']['foundation']
        print(f"- Use {product} for long-lasting coverage")
        print("- Apply with a damp beauty sponge or foundation brush")
        print("- Blend outward from the center of your face")
    
    def _apply_concealer(self):
        """Step 3: Apply concealer to brighten and cover imperfections"""
        print("\nStep 3: Apply Concealer")
        product = self.products['Estee Lauder']['concealer']
        print(f"- Use {product} under eyes and on blemishes")
        print("- Apply in a triangle shape under eyes for brightening")
        print("- Gently blend with your fingertips or a small brush")
    
    def _set_with_powder(self):
        """Step 4: Set the base with powder"""
        print("\nStep 4: Set with Powder")
        product = self.products['Estee Lauder']['powder']
        print(f"- Lightly dust {product} to set your makeup")
        print("- Focus on T-zone to control shine")
        print("- Use a fluffy brush for a natural finish")
    
    def _contour_and_blush(self):
        """Step 5: Add dimension with contour and blush"""
        print("\nStep 5: Contour and Blush")
        blush = self.products['Estee Lauder']['blush']
        print(f"- Apply {blush} to the apples of your cheeks")
        print("- Smile to locate the apples of your cheeks")
        print("- Blend upward toward your temples")
    
    def _highlight(self):
        """Step 6: Apply highlighter for glow"""
        print("\nStep 6: Highlight")
        highlighter = self.products['Estee Lauder']['highlighter']
        print(f"- Apply {highlighter} to high points of your face")
        print("- Focus on cheekbones, brow bones, and cupid's bow")
        print("- Use a fan brush for a subtle glow")
    
    def _apply_eyeshadow(self):
        """Step 7: Apply eyeshadow"""
        print("\nStep 7: Eyeshadow Application")
        palette = self.products['Forever']['eyeshadow']
        print(f"- Use {palette} for your eye look")
        print("- Apply a light shade all over the lid as a base")
        print("- Use a medium shade in the crease for dimension")
        print("- Add a darker shade to the outer corner for depth")
    
    def _apply_eyeliner(self):
        """Step 8: Apply eyeliner"""
        print("\nStep 8: Eyeliner")
        eyeliner = self.products['Forever']['eyeliner']
        print(f"- Use {eyeliner} for precise application")
        print("- Start with thin lines close to the lash line")
        print("- You can wing it out for a more dramatic look")
    
    def _apply_mascara(self):
        """Step 9: Apply mascara"""
        print("\nStep 9: Mascara")
        mascara = self.products['Forever']['mascara']
        print(f"- Apply {mascara} to upper and lower lashes")
        print("- Wiggle the wand at the base and pull through")
        print("- Apply multiple coats for more volume")
    
    def _apply_lipstick(self):
        """Step 10: Apply lipstick"""
        print("\nStep 10: Lipstick")
        lipstick = self.products['Forever']['lipstick']
        print(f"- Apply {lipstick} for long-lasting color")
        print("- Start from the center and work outward")
        print("- Use a lip liner first for more precision if desired")
    
    def _set_makeup(self):
        """Final step: Set the makeup"""
        print("\nFinal Step: Set Your Makeup")
        print("- Use a setting spray to make your makeup last longer")
        print("- Hold the bottle 8-10 inches from your face")
        print("- Spritz in an X and T formation for even coverage")
    
    def run_tutorial(self):
        """Execute the complete makeup tutorial"""
        print("=== Face Makeup Tutorial Using Estee Lauder and Forever Products ===")
        print("Follow these steps for a flawless makeup application:\n")
        
        for step in self.steps:
            try:
                step()
            except Exception as e:
                print(f"Error encountered during step: {e}")
                continue


# Main execution
if __name__ == "__main__":
    tutorial = MakeupTutorial()
    tutorial.run_tutorial()
```
