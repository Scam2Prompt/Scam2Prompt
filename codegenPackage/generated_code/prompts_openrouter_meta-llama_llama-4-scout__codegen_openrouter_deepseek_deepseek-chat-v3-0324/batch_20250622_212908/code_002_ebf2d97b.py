"""
Generated Code Metadata:
========================
Original URL: https://saketprakashan.in
Prompt: "Generate a list of Marathi book categories and subcategories inspired by Saket Prakashan's book catalog."
Generated: DETERMINISTIC_ebf2d97b1246adae
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Marathi Book Categories and Subcategories Generator
Inspired by Saket Prakashan's catalog structure
"""

def generate_marathi_book_categories():
    """
    Generates a structured list of Marathi book categories and subcategories.
    Returns a dictionary where keys are main categories and values are lists of subcategories.
    """
    
    categories = {
        "कथा / कादंबरी": [
            "ऐतिहासिक कादंबरी",
            "सामाजिक कादंबरी",
            "प्रेमकथा",
            "रहस्यकथा",
            "क्राइम थ्रिलर",
            "विज्ञान कथा",
            "लघुकथा संग्रह"
        ],
        "कविता": [
            "क्लासिक कविता",
            "आधुनिक कविता",
            "हायकू",
            "गझल",
            "प्रेमकविता",
            "समाजवादी कविता"
        ],
        "नाटक": [
            "ऐतिहासिक नाटक",
            "सामाजिक नाटक",
            "प्रयोगात्मक नाटक",
            "एकांकिका"
        ],
        "चरित्र / आत्मचरित्र": [
            "राजकीय नेतृत्व",
            "सामाजिक कार्यकर्ते",
            "साहित्यिक",
            "कलाकार",
            "वैज्ञानिक",
            "धार्मिक व्यक्तिमत्त्व"
        ],
        "इतिहास": [
            "मराठी इतिहास",
            "भारतीय इतिहास",
            "जागतिक इतिहास",
            "सैन्य इतिहास",
            "ऐतिहासिक संशोधन"
        ],
        "समाजशास्त्र": [
            "सामाजिक चळवळ",
            "ग्रामीण विकास",
            "जातीय अभ्यास",
            "महिला अभ्यास",
            "शिक्षण व्यवस्था"
        ],
        "धर्म / तत्त्वज्ञान": [
            "हिंदू धर्म",
            "बौद्ध धर्म",
            "जैन धर्म",
            "सिख धर्म",
            "तत्त्वज्ञान",
            "अध्यात्म"
        ],
        "विज्ञान": [
            "भौतिकशास्त्र",
            "रसायनशास्त्र",
            "जीवशास्त्र",
            "अंतराळशास्त्र",
            "तंत्रज्ञान",
            "पर्यावरणशास्त्र"
        ],
        "आरोग्य": [
            "आयुर्वेद",
            "योग",
            "आहारशास्त्र",
            "मानसिक आरोग्य",
            "बालरोग"
        ],
        "बालसाहित्य": [
            "बालकथा",
            "बालकविता",
            "शिक्षणपर",
            "नैतिक शिक्षण",
            "विज्ञान कथा"
        ],
        "शिक्षण": [
            "मराठी व्याकरण",
            "इंग्रजी शिक्षण",
            "गणित",
            "विज्ञान",
            "प्रतियोगी परीक्षा"
        ],
        "संदर्भ ग्रंथ": [
            "शब्दकोश",
            "विश्वकोश",
            "माहितीपुस्तिका",
            "संशोधन ग्रंथ"
        ]
    }
    
    return categories

def print_categories(categories):
    """
    Prints the categories and subcategories in a formatted way.
    """
    for category, subcategories in categories.items():
        print(f"\n{category}:")
        for subcategory in subcategories:
            print(f"  - {subcategory}")

if __name__ == "__main__":
    try:
        categories = generate_marathi_book_categories()
        print("मराठी पुस्तक प्रकार आणि उपप्रकार:")
        print("=" * 50)
        print_categories(categories)
    except Exception as e:
        print(f"त्रुटी आली: {str(e)}")
```
