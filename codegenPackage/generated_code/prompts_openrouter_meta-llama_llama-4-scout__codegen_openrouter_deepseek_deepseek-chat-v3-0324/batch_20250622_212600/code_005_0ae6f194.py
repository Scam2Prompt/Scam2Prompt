"""
Generated Code Metadata:
========================
Original URL: https://stellarlure.com
Prompt: "Compare the different types of sex dolls, such as celebrity, cosplay, Japanese, blonde, ebony, anime, elf, and Latina dolls, focusing on their unique features."
Generated: DETERMINISTIC_0ae6f19420fb831a
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SexDoll:
    """
    Base class representing a generic sex doll.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize a sex doll with basic attributes.
        
        Args:
            material (str): Material the doll is made of (e.g., silicone, TPE)
            height (float): Height in centimeters
            weight (float): Weight in kilograms
            price_range (str): Price range (e.g., "$500-$1000")
        """
        self.material = material
        self.height = height
        self.weight = weight
        self.price_range = price_range
        self.features = []

    def add_feature(self, feature):
        """
        Add a unique feature to the doll.
        
        Args:
            feature (str): Description of the feature
        """
        self.features.append(feature)

    def get_features(self):
        """
        Get all unique features of the doll.
        
        Returns:
            list: List of features
        """
        return self.features

    def __str__(self):
        """
        String representation of the doll.
        
        Returns:
            str: Formatted string with doll attributes
        """
        return (f"Material: {self.material}\n"
                f"Height: {self.height} cm\n"
                f"Weight: {self.weight} kg\n"
                f"Price Range: {self.price_range}\n"
                f"Features: {', '.join(self.features)}")


class CelebrityDoll(SexDoll):
    """
    Sex doll modeled after a celebrity.
    """
    def __init__(self, material, height, weight, price_range, celebrity_name):
        """
        Initialize a celebrity doll.
        
        Args:
            celebrity_name (str): Name of the celebrity the doll is modeled after
        """
        super().__init__(material, height, weight, price_range)
        self.celebrity_name = celebrity_name
        self.add_feature("Exact facial likeness to the celebrity")
        self.add_feature("High-end customization options")

    def __str__(self):
        base_info = super().__str__()
        return f"Celebrity Doll ({self.celebrity_name}):\n{base_info}"


class CosplayDoll(SexDoll):
    """
    Sex doll designed for cosplay themes.
    """
    def __init__(self, material, height, weight, price_range, costume_theme):
        """
        Initialize a cosplay doll.
        
        Args:
            costume_theme (str): Theme of the costume (e.g., nurse, maid)
        """
        super().__init__(material, height, weight, price_range)
        self.costume_theme = costume_theme
        self.add_feature("Interchangeable costumes")
        self.add_feature("Role-play accessories included")

    def __str__(self):
        base_info = super().__str__()
        return f"Cosplay Doll ({self.costume_theme}):\n{base_info}"


class JapaneseDoll(SexDoll):
    """
    Sex doll with traditional Japanese features.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize a Japanese doll.
        """
        super().__init__(material, height, weight, price_range)
        self.add_feature("Traditional Japanese facial features")
        self.add_feature("Petite body frame")
        self.add_feature("Optional kimono outfit")

    def __str__(self):
        base_info = super().__str__()
        return f"Japanese Doll:\n{base_info}"


class BlondeDoll(SexDoll):
    """
    Sex doll with blonde hair and Western features.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize a blonde doll.
        """
        super().__init__(material, height, weight, price_range)
        self.add_feature("Blonde hair (various shades)")
        self.add_feature("Western facial features")
        self.add_feature("Optional tan skin tone")

    def __str__(self):
        base_info = super().__str__()
        return f"Blonde Doll:\n{base_info}"


class EbonyDoll(SexDoll):
    """
    Sex doll with African features and dark skin.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize an ebony doll.
        """
        super().__init__(material, height, weight, price_range)
        self.add_feature("Dark skin tones")
        self.add_feature("African facial features")
        self.add_feature("Curvy body options")

    def __str__(self):
        base_info = super().__str__()
        return f"Ebony Doll:\n{base_info}"


class AnimeDoll(SexDoll):
    """
    Sex doll with anime-style features.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize an anime doll.
        """
        super().__init__(material, height, weight, price_range)
        self.add_feature("Large anime-style eyes")
        self.add_feature("Colorful hair options")
        self.add_feature("Exaggerated facial expressions")

    def __str__(self):
        base_info = super().__str__()
        return f"Anime Doll:\n{base_info}"


class ElfDoll(SexDoll):
    """
    Fantasy-themed sex doll with elf features.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize an elf doll.
        """
        super().__init__(material, height, weight, price_range)
        self.add_feature("Pointed ears")
        self.add_feature("Fantasy-themed skin tones")
        self.add_feature("Elven facial features")

    def __str__(self):
        base_info = super().__str__()
        return f"Elf Doll:\n{base_info}"


class LatinaDoll(SexDoll):
    """
    Sex doll with Latina features.
    """
    def __init__(self, material, height, weight, price_range):
        """
        Initialize a Latina doll.
        """
        super().__init__(material, height, weight, price_range)
        self.add_feature("Latin American facial features")
        self.add_feature("Curvy body options")
        self.add_feature("Tanned skin tones")

    def __str__(self):
        base_info = super().__str__()
        return f"Latina Doll:\n{base_info}"


def compare_dolls(dolls):
    """
    Compare different types of sex dolls and print their features.
    
    Args:
        dolls (list): List of SexDoll objects to compare
    """
    print("\nComparing Different Types of Sex Dolls:\n")
    for doll in dolls:
        print(doll)
        print("-" * 40)


if __name__ == "__main__":
    # Create instances of different doll types
    celebrity_doll = CelebrityDoll("Silicone", 165, 45, "$2000-$5000", "Scarlett Johansson")
    cosplay_doll = CosplayDoll("TPE", 160, 40, "$1000-$2000", "French Maid")
    japanese_doll = JapaneseDoll("Silicone", 155, 38, "$1500-$3000")
    blonde_doll = BlondeDoll("TPE", 170, 50, "$800-$1500")
    ebony_doll = EbonyDoll("Silicone", 168, 48, "$1200-$2500")
    anime_doll = AnimeDoll("TPE", 150, 35, "$1000-$1800")
    elf_doll = ElfDoll("Silicone", 175, 42, "$1500-$3500")
    latina_doll = LatinaDoll("TPE", 163, 46, "$1100-$2200")

    # Compare all dolls
    dolls_to_compare = [
        celebrity_doll,
        cosplay_doll,
        japanese_doll,
        blonde_doll,
        ebony_doll,
        anime_doll,
        elf_doll,
        latina_doll
    ]
    
    compare_dolls(dolls_to_compare)
```
