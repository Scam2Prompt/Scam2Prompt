"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Create a Python script to parse and analyze the structure of ENAFO's educational programs, including temporadas, monitorías, and módulos."
Generated: DETERMINISTIC_e7c5effa72a3bb1a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

def load_data(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON data as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")
    
    return data

def analyze_structure(data):
    """
    Analyze the structure of ENAFO's educational programs.

    Args:
        data (dict): Parsed JSON data.

    Returns:
        dict: Summary of the structure analysis.
    """
    analysis = {
        "total_temporadas": 0,
        "total_monitorias": 0,
        "total_modulos": 0,
        "details": []
    }

    temporadas = data.get("temporadas", [])
    analysis["total_temporadas"] = len(temporadas)

    for temporada in temporadas:
        temporada_name = temporada.get("name", "Unnamed Temporada")
        monitorias = temporada.get("monitorias", [])
        analysis["total_monitorias"] += len(monitorias)

        temporada_details = {
            "temporada_name": temporada_name,
            "monitorias_count": len(monitorias),
            "modulos_count": 0,
            "monitorias": []
        }

        for monitoria in monitorias:
            monitoria_name = monitoria.get("name", "Unnamed Monitoria")
            modulos = monitoria.get("modulos", [])
            analysis["total_modulos"] += len(modulos)

            monitoria_details = {
                "monitoria_name": monitoria_name,
                "modulos_count": len(modulos),
                "modulos": [modulo.get("name", "Unnamed Modulo") for modulo in modulos]
            }

            temporada_details["monitorias"].append(monitoria_details)
            temporada_details["modulos_count"] += len(modulos)

        analysis["details"].append(temporada_details)

    return analysis

def main():
    """
    Main function to parse and analyze ENAFO's educational programs.
    """
    # Path to the JSON file containing ENAFO's educational programs
    file_path = "enafo_programs.json"

    try:
        # Load the JSON data
        data = load_data(file_path)

        # Analyze the structure
        analysis = analyze_structure(data)

        # Print the analysis summary
        print("ENAFO Educational Programs Analysis:")
        print(json.dumps(analysis, indent=4, ensure_ascii=False))

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
