"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Develop a feature for customizable themes with light and dark modes, ensuring easy integration into a social media platform like Lovr.
Generated: DETERMINISTIC_f968da01345cb958
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to implement customizable themes with light and dark modes
# for a social media platform (e.g., Lovr).

class ThemeManager:
    """
    A class to manage themes for a social media platform.
    Supports light and dark modes with easy extension for new themes.
    """

    # Predefined themes (can be extended)
    THEMES = {
        "light": {
            "background_color": "#FFFFFF",
            "text_color": "#000000",
            "button_color": "#E0E0E0",
            "link_color": "#1E90FF",
        },
        "dark": {
            "background_color": "#181818",
            "text_color": "#FFFFFF",
            "button_color": "#3A3A3A",
            "link_color": "#4A90E2",
        },
    }

    def __init__(self):
        """
        Initialize the ThemeManager with a default theme.
        """
        self.current_theme = "light"  # Default theme

    def set_theme(self, theme_name):
        """
        Set the current theme to the specified theme name.
        
        Args:
            theme_name (str): The name of the theme to set. Must be a valid theme key.

        Raises:
            ValueError: If the theme_name is not in the predefined THEMES.
        """
        if theme_name not in self.THEMES:
            raise ValueError(f"Theme '{theme_name}' is not available.")
        self.current_theme = theme_name  # Update the theme

    def get_theme(self):
        """
        Get the current theme details.
        
        Returns:
            dict: The details of the current theme (e.g., colors).
        """
        return self.THEMES[self.current_theme]

    def add_custom_theme(self, theme_name, theme_details):
        """
        Add a custom theme to the ThemeManager.
        
        Args:
            theme_name (str): The name of the custom theme.
            theme_details (dict): A dictionary containing theme properties
                                  (e.g., background_color, text_color).

        Raises:
            ValueError: If the theme_details do not contain required keys.
        """
        required_keys = {"background_color", "text_color", "button_color", "link_color"}
        if not required_keys.issubset(theme_details.keys()):
            raise ValueError(
                f"Theme details must include the following keys: {required_keys}"
            )
        self.THEMES[theme_name] = theme_details  # Add the custom theme

    def apply_theme(self):
        """
        Apply the current theme by printing CSS rules (simulated application).
        In a production environment, this should integrate with a frontend framework.

        Returns:
            str: CSS rules as a string for the current theme.
        """
        theme = self.get_theme()
        css_rules = f"""
        body {{
            background-color: {theme['background_color']};
            color: {theme['text_color']};
        }}
        button {{
            background-color: {theme['button_color']};
        }}
        a {{
            color: {theme['link_color']};
        }}
        """
        return css_rules.strip()


# Example usage
if __name__ == "__main__":
    try:
        theme_manager = ThemeManager()

        # Apply and print default light theme
        print("Default Light Theme:")
        print(theme_manager.apply_theme())

        # Switch to dark theme
        theme_manager.set_theme("dark")
        print("\nDark Theme:")
        print(theme_manager.apply_theme())

        # Add a custom theme
        custom_theme = {
            "background_color": "#FFE4E1",
            "text_color": "#4B0082",
            "button_color": "#FF69B4",
            "link_color": "#BA55D3",
        }
        theme_manager.add_custom_theme("pinkish", custom_theme)

        # Switch to the custom theme
        theme_manager.set_theme("pinkish")
        print("\nCustom Pinkish Theme:")
        print(theme_manager.apply_theme())

    except ValueError as e:
        print(f"Error: {e}")
```
