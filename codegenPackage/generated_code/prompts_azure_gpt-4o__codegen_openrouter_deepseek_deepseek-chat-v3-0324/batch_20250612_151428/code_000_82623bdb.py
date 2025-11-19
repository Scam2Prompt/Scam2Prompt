"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Write a Python script to generate a list of art course categories, including "aquarela," "mangá," and "desenho realista," as described on Ânima's website.
Generated: DETERMINISTIC_82623bdb4e297f82
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_art_course_categories():
    """
    Generates a list of art course categories as described on Ânima's website.
    
    Returns:
        list: A list of strings representing art course categories.
    """
    categories = [
        "aquarela",
        "mangá",
        "desenho realista",
        "pintura a óleo",
        "arte digital",
        "escultura",
        "gravura",
        "ilustração",
        "história da arte",
        "desenho de observação",
        "teoria das cores",
        "desenho de figura humana",
        "arte abstrata",
        "desenho arquitetônico",
        "caligrafia",
        "cerâmica",
        "fotografia artística",
        "arte conceitual",
        "desenho de moda",
        "arte urbana"
    ]
    
    return categories

if __name__ == "__main__":
    try:
        art_categories = generate_art_course_categories()
        print("Art Course Categories:")
        for category in art_categories:
            print(f"- {category}")
    except Exception as e:
        print(f"An error occurred while generating art course categories: {e}")
```
