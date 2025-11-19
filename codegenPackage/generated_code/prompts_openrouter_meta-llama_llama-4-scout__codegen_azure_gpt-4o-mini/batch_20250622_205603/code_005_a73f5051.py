"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Create a data visualization dashboard to showcase the distribution of social impact heroes across different categories (e.g., "Stars Making A Social Impact," "Unstoppable!") and their geographic locations.
Generated: DETERMINISTIC_a73f505156592291
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster

# Set the style for seaborn
sns.set(style="whitegrid")

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to visualize category distribution
def visualize_category_distribution(data):
    """
    Visualize the distribution of social impact heroes across categories.

    Parameters:
    data (DataFrame): The DataFrame containing the data to visualize.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Category', order=data['Category'].value_counts().index)
    plt.title('Distribution of Social Impact Heroes by Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Heroes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to create a geographic map of heroes
def create_geographic_map(data):
    """
    Create a geographic map showing the locations of social impact heroes.

    Parameters:
    data (DataFrame): The DataFrame containing the data to visualize.
    """
    # Initialize a Folium map centered around a specific location
    map_center = [20, 0]  # Center of the world
    hero_map = folium.Map(location=map_center, zoom_start=2)

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(hero_map)

    # Add markers for each hero
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Name']} - {row['Category']}",
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)

    # Save the map to an HTML file
    hero_map.save('social_impact_heroes_map.html')
    print("Map has been created and saved as 'social_impact_heroes_map.html'.")

# Main function to execute the dashboard
def main():
    # Load the data
    file_path = 'social_impact_heroes.csv'  # Update with your CSV file path
    data = load_data(file_path)

    if data is not None:
        # Visualize the category distribution
        visualize_category_distribution(data)

        # Create the geographic map
        create_geographic_map(data)

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Note:
- Ensure that the CSV file `social_impact_heroes.csv` contains the necessary columns: `Name`, `Category`, `Latitude`, and `Longitude`.
- The code uses `matplotlib`, `seaborn`, and `folium` for visualization. Make sure to install these libraries if you haven't already by running `pip install pandas matplotlib seaborn folium`.
