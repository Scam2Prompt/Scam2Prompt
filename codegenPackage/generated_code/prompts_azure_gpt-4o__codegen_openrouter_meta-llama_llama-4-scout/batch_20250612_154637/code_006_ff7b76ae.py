"""
Generated Code Metadata:
========================
Original URL: https://egrowmax.com
Prompt: Recommend tools for custom website development that align with Egrowmax's expertise in mobile and web development.
Generated: DETERMINISTIC_ff7b76ae57926f83
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tools_recommender.py

class Tool:
    """Represents a development tool with its name, description, and category."""

    def __init__(self, name, description, category):
        """
        Initializes a Tool instance.

        Args:
            name (str): The name of the tool.
            description (str): A brief description of the tool.
            category (str): The category of the tool (e.g., mobile, web).
        """
        self.name = name
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name}: {self.description}"


class ToolRecommender:
    """Recommends development tools based on Egrowmax's expertise."""

    def __init__(self):
        """
        Initializes a ToolRecommender instance with a list of known tools.

        The tools are categorized by their relevance to Egrowmax's expertise in mobile and web development.
        """
        self.tools = {
            "mobile": [
                Tool("Android Studio", "The official Android IDE.", "mobile"),
                Tool("Xcode", "The official Apple IDE for iOS development.", "mobile"),
                Tool("React Native", "A cross-platform framework for mobile app development.", "mobile"),
                Tool("Flutter", "An open-source mobile app development framework.", "mobile"),
            ],
            "web": [
                Tool("Visual Studio Code", "A lightweight, open-source code editor.", "web"),
                Tool("IntelliJ IDEA", "A commercial IDE for web and mobile development.", "web"),
                Tool("React", "A JavaScript library for building user interfaces.", "web"),
                Tool("Angular", "A TypeScript-based framework for building single-page applications.", "web"),
                Tool("Vue.js", "A progressive and flexible JavaScript framework.", "web"),
            ],
        }

    def recommend_tools(self, category=None):
        """
        Recommends development tools based on Egrowmax's expertise.

        Args:
            category (str, optional): The category of tools to recommend (e.g., mobile, web). Defaults to None.

        Returns:
            list[Tool]: A list of recommended tools.

        Raises:
            ValueError: If an invalid category is provided.
        """
        if category and category not in self.tools:
            raise ValueError("Invalid category. Supported categories: {}".format(", ".join(self.tools.keys())))

        if category:
            return self.tools[category]
        else:
            return [tool for tools in self.tools.values() for tool in tools]


def main():
    recommender = ToolRecommender()

    print("Recommended mobile development tools:")
    for tool in recommender.recommend_tools("mobile"):
        print(tool)

    print("\nRecommended web development tools:")
    for tool in recommender.recommend_tools("web"):
        print(tool)

    print("\nAll recommended tools:")
    for tool in recommender.recommend_tools():
        print(tool)


if __name__ == "__main__":
    main()
```
