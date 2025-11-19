"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: Generate a Python script to create a simple website structure similar to jkpcrnica.rs, including sections for ПОЧЕТНА, О НАМА, and КОНТАКТ.
Generated: DETERMINISTIC_427effd7b01436e5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from pathlib import Path

def create_website_structure(base_dir):
    """
    Creates a simple website structure with sections for ПОЧЕТНА, О НАМА, and КОНТАКТ.
    
    Args:
        base_dir (str): The base directory where the website will be created.
    """
    try:
        # Create base directory if it doesn't exist
        Path(base_dir).mkdir(parents=True, exist_ok=True)
        
        # Create directories for each section
        sections = ['pocetna', 'o-nama', 'kontakt']
        for section in sections:
            os.makedirs(os.path.join(base_dir, section), exist_ok=True)
        
        # Create index.html in the root directory
        with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JKP Crnica</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        header { background-color: #0066cc; color: white; padding: 20px; text-align: center; }
        nav { background-color: #f1f1f1; padding: 10px; }
        nav ul { list-style-type: none; margin: 0; padding: 0; display: flex; justify-content: center; }
        nav li { margin: 0 15px; }
        nav a { text-decoration: none; color: #333; font-weight: bold; }
        main { padding: 20px; }
        footer { background-color: #0066cc; color: white; text-align: center; padding: 10px; position: fixed; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <header>
        <h1>JKP Crnica</h1>
    </header>
    <nav>
        <ul>
            <li><a href="pocetna/index.html">ПОЧЕТНА</a></li>
            <li><a href="o-nama/index.html">О НАМА</a></li>
            <li><a href="kontakt/index.html">КОНТАКТ</a></li>
        </ul>
    </nav>
    <main>
        <h2>Добродошли на сајт ЈКП Црница</h2>
        <p>Ово је главна страница нашег сајта.</p>
    </main>
    <footer>
        <p>&copy; 2023 JKP Crnica. Сва права задржана.</p>
    </footer>
</body>
</html>""")
        
        # Create content for each section
        section_contents = {
            'pocetna': """<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ПОЧЕТНА - JKP Crnica</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <header>
        <h1>JKP Crnica</h1>
    </header>
    <nav>
        <ul>
            <li><a href="../pocetna/index.html">ПОЧЕТНА</a></li>
            <li><a href="../o-nama/index.html">О НАМА</a></li>
            <li><a href="../kontakt/index.html">КОНТАКТ</a></li>
        </ul>
    </nav>
    <main>
        <h2>ПОЧЕТНА</h2>
        <p>Ово је почетна страница нашег сајта.</p>
    </main>
    <footer>
        <p>&copy; 2023 JKP Crnica. Сва права задржана.</p>
    </footer>
</body>
</html>""",
            'o-nama': """<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>О НАМА - JKP Crnica</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <header>
        <h1>JKP Crnica</h1>
    </header>
    <nav>
        <ul>
            <li><a href="../pocetna/index.html">ПОЧЕТНА</a></li>
            <li><a href="../o-nama/index.html">О НАМА</a></li>
            <li><a href="../kontakt/index.html">КОНТАКТ</a></li>
        </ul>
    </nav>
    <main>
        <h2>О НАМА</h2>
        <p>Информације о нашој компанији и услугама које пружамо.</p>
    </main>
    <footer>
        <p>&copy; 2023 JKP Crnica. Сва права задржана.</p>
    </footer>
</body>
</html>""",
            'kontakt': """<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>КОНТАКТ - JKP Crnica</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <header>
        <h1>JKP Crnica</h1>
    </header>
    <nav>
        <ul>
            <li><a href="../pocetna/index.html">ПОЧЕТНА</a></li>
            <li><a href="../o-nama/index.html">О НАМА</a></li>
            <li><a href="../kontakt/index.html">КОНТАКТ</a></li>
        </ul>
    </nav>
    <main>
        <h2>КОНТАКТ</h2>
        <p>Контакт информације за ЈКП Црница.</p>
        <address>
            Адреса: Улица Краља Петра I, Црница<br>
            Телефон: +381 123 4567<br>
            Е-пошта: info@jkpcrnica.rs
        </address>
    </main>
    <footer>
        <p>&copy; 2023 JKP Crnica. Сва права задржана.</p>
    </footer>
</body>
</html>"""
        }
        
        # Write section content to respective index.html files
        for section, content in section_contents.items():
            with open(os.path.join(base_dir, section, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(content)
        
        # Create a CSS file
        with open(os.path.join(base_dir, 'styles.css'), 'w', encoding='utf-8') as f:
            f.write("""body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #0066cc;
    color: white;
    padding: 20px;
    text-align: center;
}

nav {
    background-color: #f1f1f1;
    padding: 10px;
}

nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
}

nav li {
    margin: 0 15px;
}

nav a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
}

main {
    padding: 20px;
    margin-bottom: 60px; /* To prevent footer from overlapping content */
}

footer {
    background-color: #0066cc;
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;
}""")
        
        print(f"Website structure successfully created at: {base_dir}")
    
    except Exception as e:
        print(f"Error creating website structure: {str(e)}")

if __name__ == "__main__":
    create_website_structure("jkp_crnica_website")
```
