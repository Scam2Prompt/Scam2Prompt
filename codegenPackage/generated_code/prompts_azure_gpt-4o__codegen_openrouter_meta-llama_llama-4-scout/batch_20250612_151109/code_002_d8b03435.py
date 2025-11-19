"""
Generated Code Metadata:
========================
Original URL: https://gn-connect.com
Prompt: Develop a program using AI to generate personalized restaurant menus based on customer preferences, inspired by the trends discussed at gn connect.
Generated: DETERMINISTIC_d8b03435d0771f46
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.exceptions import ConvergenceWarning
import warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

class MenuGenerator:
    """
    A class used to generate personalized restaurant menus based on customer preferences.

    Attributes:
    ----------
    menu_data : pandas.DataFrame
        A DataFrame containing menu item data with columns 'item_name', 'description', and 'cuisine'.
    customer_preferences : dict
        A dictionary containing customer preferences with keys 'food_type', 'cuisine', and 'allergies'.

    Methods:
    -------
    generate_menu(customer_preferences)
        Generates a personalized menu based on customer preferences.
    """

    def __init__(self, menu_data):
        """
        Initializes the MenuGenerator class.

        Parameters:
        ----------
        menu_data : pandas.DataFrame
            A DataFrame containing menu item data with columns 'item_name', 'description', and 'cuisine'.
        """
        self.menu_data = menu_data

    def generate_menu(self, customer_preferences):
        """
        Generates a personalized menu based on customer preferences.

        Parameters:
        ----------
        customer_preferences : dict
            A dictionary containing customer preferences with keys 'food_type', 'cuisine', and 'allergies'.

        Returns:
        -------
        personalized_menu : list
            A list of menu items that match the customer's preferences.
        """
        # Filter menu data based on customer preferences
        filtered_menu = self.filter_menu(customer_preferences)

        # Use TF-IDF to vectorize menu item descriptions
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_vectors = vectorizer.fit_transform(filtered_menu['description'])

        # Get customer preference vector
        preference_vector = self.get_preference_vector(customer_preferences, vectorizer)

        # Calculate cosine similarity between menu items and customer preferences
        similarities = cosine_similarity(tfidf_vectors, preference_vector)

        # Get top 5 similar menu items
        top_indices = similarities.argsort()[0, -5:][::-1]
        personalized_menu = filtered_menu.iloc[top_indices].to_dict('records')

        return personalized_menu

    def filter_menu(self, customer_preferences):
        """
        Filters the menu data based on customer preferences.

        Parameters:
        ----------
        customer_preferences : dict
            A dictionary containing customer preferences with keys 'food_type', 'cuisine', and 'allergies'.

        Returns:
        -------
        filtered_menu : pandas.DataFrame
            A DataFrame containing filtered menu items.
        """
        filtered_menu = self.menu_data

        if 'cuisine' in customer_preferences:
            filtered_menu = filtered_menu[filtered_menu['cuisine'] == customer_preferences['cuisine']]

        if 'food_type' in customer_preferences:
            filtered_menu = filtered_menu[filtered_menu['item_name'].str.contains(customer_preferences['food_type'], case=False)]

        if 'allergies' in customer_preferences:
            for allergy in customer_preferences['allergies']:
                filtered_menu = filtered_menu[~filtered_menu['description'].str.contains(allergy, case=False)]

        return filtered_menu

    def get_preference_vector(self, customer_preferences, vectorizer):
        """
        Gets the customer preference vector.

        Parameters:
        ----------
        customer_preferences : dict
            A dictionary containing customer preferences with keys 'food_type', 'cuisine', and 'allergies'.
        vectorizer : TfidfVectorizer
            A TF-IDF vectorizer.

        Returns:
        -------
        preference_vector : scipy.sparse.csr_matrix
            A sparse matrix representing the customer preference vector.
        """
        preference_text = ''

        if 'food_type' in customer_preferences:
            preference_text += customer_preferences['food_type'] + ' '

        if 'cuisine' in customer_preferences:
            preference_text += customer_preferences['cuisine'] + ' '

        if 'allergies' in customer_preferences:
            for allergy in customer_preferences['allergies']:
                preference_text += 'no ' + allergy + ' '

        preference_vector = vectorizer.transform([preference_text])

        return preference_vector


def main():
    # Sample menu data
    menu_data = pd.DataFrame({
        'item_name': ['Pizza', 'Burger', 'Salad', 'Sushi', 'Tacos'],
        'description': ['Italian dish with cheese and sauce', 'American burger with beef and lettuce', 'Healthy salad with vegetables and dressing', 'Japanese sushi with raw fish and rice', 'Mexican tacos with beef and salsa'],
        'cuisine': ['Italian', 'American', 'International', 'Japanese', 'Mexican']
    })

    # Sample customer preferences
    customer_preferences = {
        'food_type': 'Italian',
        'cuisine': 'Italian',
        'allergies': ['gluten']
    }

    # Create a MenuGenerator instance
    menu_generator = MenuGenerator(menu_data)

    try:
        # Generate a personalized menu
        personalized_menu = menu_generator.generate_menu(customer_preferences)
        print("Personalized Menu:")
        for item in personalized_menu:
            print(item['item_name'])
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```
