"""
Generated Code Metadata:
========================
Original URL: https://mbandjock.fr
Prompt: Recommend a suitable blogging platform for creative people, mentioning WordPress as an option.
Generated: DETERMINISTIC_fa0a2b343e0cfd0a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blogging_platform_recommender.py

class BloggingPlatform:
    """Base class for blogging platforms."""

    def __init__(self, name, description, features):
        """
        Initialize a blogging platform.

        Args:
            name (str): Name of the platform.
            description (str): Brief description of the platform.
            features (list): List of features offered by the platform.
        """
        self.name = name
        self.description = description
        self.features = features

    def __str__(self):
        return f"{self.name}: {self.description}"


class WordPress(BloggingPlatform):
    """WordPress blogging platform."""

    def __init__(self):
        """
        Initialize WordPress platform.

        Features:
            - Highly customizable
            - Large community of users and developers
            - Extensive plugin library
            - SEO-friendly
        """
        super().__init__(
            name="WordPress",
            description="A highly customizable and popular blogging platform.",
            features=[
                "Highly customizable",
                "Large community of users and developers",
                "Extensive plugin library",
                "SEO-friendly",
            ],
        )


class Medium(BloggingPlatform):
    """Medium blogging platform."""

    def __init__(self):
        """
        Initialize Medium platform.

        Features:
            - Minimalist design
            - Built-in audience
            - Easy to use
            - Partner program for monetization
        """
        super().__init__(
            name="Medium",
            description="A minimalist blogging platform with a built-in audience.",
            features=[
                "Minimalist design",
                "Built-in audience",
                "Easy to use",
                "Partner program for monetization",
            ],
        )


class Ghost(BloggingPlatform):
    """Ghost blogging platform."""

    def __init__(self):
        """
        Initialize Ghost platform.

        Features:
            - Simple and modern design
            - Optimized for writing and reading
            - Integrated subscription system
            - Highly customizable
        """
        super().__init__(
            name="Ghost",
            description="A simple and modern blogging platform.",
            features=[
                "Simple and modern design",
                "Optimized for writing and reading",
                "Integrated subscription system",
                "Highly customizable",
            ],
        )


def recommend_platform(platform_name):
    """
    Recommend a suitable blogging platform.

    Args:
        platform_name (str): Name of the platform.

    Returns:
        BloggingPlatform: The recommended platform.

    Raises:
        ValueError: If the platform is not supported.
    """
    platforms = {
        "wordpress": WordPress,
        "medium": Medium,
        "ghost": Ghost,
    }

    try:
        platform = platforms[platform_name.lower()]()
        return platform
    except KeyError:
        raise ValueError("Unsupported platform. Please choose from: wordpress, medium, ghost")


def main():
    try:
        platform_name = input("Enter your preferred platform (wordpress, medium, ghost): ")
        recommended_platform = recommend_platform(platform_name)
        print(recommended_platform)
        print("Features:")
        for feature in recommended_platform.features:
            print(f"- {feature}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
