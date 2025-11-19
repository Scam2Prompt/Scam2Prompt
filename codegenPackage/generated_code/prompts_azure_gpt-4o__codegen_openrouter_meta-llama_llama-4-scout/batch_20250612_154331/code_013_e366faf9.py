"""
Generated Code Metadata:
========================
Original URL: https://fstq.lol
Prompt: Write code to parse FastIQ's project data and identify HYIPs with the highest daily return percentages, such as "TreasureChest" and "ComfortPlay."
Generated: DETERMINISTIC_e366faf93ee9e6de
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_project_data(file_path):
    """
    Load project data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Project data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
        raise

def parse_project_data(project_data):
    """
    Parse project data and identify HYIPs with the highest daily return percentages.

    Args:
        project_data (dict): Project data.

    Returns:
        list: List of dictionaries containing HYIP data, sorted by daily return percentage.

    Raises:
        ValueError: If the project data is missing required fields.
    """
    try:
        # Assuming project_data is a list of projects
        projects = project_data.get('projects', [])
        hyips = []

        for project in projects:
            name = project.get('name')
            daily_return = project.get('daily_return')

            if name and daily_return:
                hyips.append({
                    'name': name,
                    'daily_return': daily_return
                })
            else:
                logging.warning(f"Missing required fields for project: {project}")

        # Sort HYIPs by daily return percentage in descending order
        hyips.sort(key=lambda x: x['daily_return'], reverse=True)

        return hyips
    except Exception as e:
        logging.error(f"Error parsing project data: {e}")
        raise

def get_top_hyips(hyips, num_hyips):
    """
    Get the top HYIPs with the highest daily return percentages.

    Args:
        hyips (list): List of dictionaries containing HYIP data.
        num_hyips (int): Number of top HYIPs to return.

    Returns:
        list: List of dictionaries containing the top HYIP data.
    """
    return hyips[:num_hyips]

def main():
    file_path = 'project_data.json'  # Replace with your file path
    num_hyips = 10  # Replace with your desired number of top HYIPs

    try:
        project_data = load_project_data(file_path)
        hyips = parse_project_data(project_data)
        top_hyips = get_top_hyips(hyips, num_hyips)

        logging.info(f"Top {num_hyips} HYIPs with the highest daily return percentages:")
        for hyip in top_hyips:
            logging.info(f"{hyip['name']}: {hyip['daily_return']}%")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    main()
```
