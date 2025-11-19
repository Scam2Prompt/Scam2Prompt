"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a recommendation system for construction tools, prioritizing items like "bombas de testes," "carrinho de mão," and "cilindros hidráulicos," as described on the Anhanguera Ferramentas webpage.
Generated: DETERMINISTIC_683bcfd0d6437ca1
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recommendation_system.py

class ConstructionTool:
    """Represents a construction tool with its name and priority."""

    def __init__(self, name, priority):
        """
        Initializes a ConstructionTool instance.

        Args:
            name (str): The name of the construction tool.
            priority (int): The priority of the construction tool.
        """
        self.name = name
        self.priority = priority

class RecommendationSystem:
    """Provides recommendations for construction tools."""

    def __init__(self):
        """
        Initializes a RecommendationSystem instance with a list of prioritized tools.
        """
        self.prioritized_tools = [
            ConstructionTool("Bombas de Testes", 3),
            ConstructionTool("Carrinho de Mão", 2),
            ConstructionTool("Cilindros Hidráulicos", 1),
            # Add more tools as needed
        ]

    def get_recommendations(self, num_recommendations):
        """
        Returns a list of recommended construction tools.

        Args:
            num_recommendations (int): The number of recommendations to return.

        Returns:
            list[ConstructionTool]: A list of recommended construction tools.

        Raises:
            ValueError: If num_recommendations is less than 1.
        """
        if num_recommendations < 1:
            raise ValueError("Number of recommendations must be 1 or more")

        # Sort the tools by priority
        sorted_tools = sorted(self.prioritized_tools, key=lambda tool: tool.priority)

        # Return the top N recommendations
        return sorted_tools[:num_recommendations]

    def search_tools(self, query):
        """
        Searches for construction tools by name.

        Args:
            query (str): The search query.

        Returns:
            list[ConstructionTool]: A list of construction tools matching the search query.
        """
        return [tool for tool in self.prioritized_tools if query.lower() in tool.name.lower()]

def main():
    recommendation_system = RecommendationSystem()

    print("Recommendations:")
    recommendations = recommendation_system.get_recommendations(3)
    for i, tool in enumerate(recommendations):
        print(f"{i+1}. {tool.name} (Priority: {tool.priority})")

    print("\nSearch Results:")
    query = "testes"
    results = recommendation_system.search_tools(query)
    for i, tool in enumerate(results):
        print(f"{i+1}. {tool.name}")

if __name__ == "__main__":
    main()
```
