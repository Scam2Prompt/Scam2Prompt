"""
Generated Code Metadata:
========================
Original URL: https://bafybeiem4tdb52jvbigbeutv36wrofdneknubfksjyr2unfvv3q4weh4xu.ipfs.dweb.link
Prompt: What tools does Azuro offer for engaging audiences through prediction applications?
Generated: DETERMINISTIC_f3523d8889eb4ee8
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum

class PredictionTool(Enum):
    """Enum representing different prediction tools offered by Azuro."""
    PREDICTION_MARKETS = "Prediction Markets"
    FANTASY_SPORTS = "Fantasy Sports"
    QUIZZES = "Quizzes"
    BRACKETS = "Brackets"
    POLLS = "Polls"
    TRIVIA = "Trivia"
    WAGERING = "Wagering"
    SOCIAL_PREDICTIONS = "Social Predictions"

class AzuroPredictionTools:
    """Class representing Azuro's tools for audience engagement through predictions."""
    
    def __init__(self):
        """Initialize with default tools."""
        self._available_tools = [
            PredictionTool.PREDICTION_MARKETS,
            PredictionTool.FANTASY_SPORTS,
            PredictionTool.QUIZZES,
            PredictionTool.BRACKETS,
            PredictionTool.POLLS,
            PredictionTool.TRIVIA,
            PredictionTool.WAGERING,
            PredictionTool.SOCIAL_PREDICTIONS
        ]
    
    def get_available_tools(self) -> List[PredictionTool]:
        """Get list of all available prediction tools.
        
        Returns:
            List[PredictionTool]: List of available tools.
        """
        return self._available_tools
    
    def get_tool_details(self, tool: PredictionTool) -> Dict[str, str]:
        """Get details about a specific prediction tool.
        
        Args:
            tool (PredictionTool): The tool to get details for.
            
        Returns:
            Dict[str, str]: Dictionary containing tool details.
            
        Raises:
            ValueError: If the tool is not supported.
        """
        if tool not in self._available_tools:
            raise ValueError(f"Tool {tool} is not supported by Azuro.")
            
        details = {
            "name": tool.value,
            "description": self._get_tool_description(tool),
            "use_case": self._get_tool_use_case(tool)
        }
        return details
    
    def _get_tool_description(self, tool: PredictionTool) -> str:
        """Internal method to get tool description."""
        descriptions = {
            PredictionTool.PREDICTION_MARKETS: "Platform for trading event outcome shares",
            PredictionTool.FANTASY_SPORTS: "Virtual sports team management and competition",
            PredictionTool.QUIZZES: "Interactive quiz games with predictions",
            PredictionTool.BRACKETS: "Tournament bracket prediction challenges",
            PredictionTool.POLLS: "Real-time opinion polling with predictions",
            PredictionTool.TRIVIA: "Knowledge-based prediction games",
            PredictionTool.WAGERING: "Monetary-based prediction contests",
            PredictionTool.SOCIAL_PREDICTIONS: "Community-driven prediction challenges"
        }
        return descriptions.get(tool, "No description available")
    
    def _get_tool_use_case(self, tool: PredictionTool) -> str:
        """Internal method to get tool use case."""
        use_cases = {
            PredictionTool.PREDICTION_MARKETS: "Financial and event outcome predictions",
            PredictionTool.FANTASY_SPORTS: "Sports fan engagement and competition",
            PredictionTool.QUIZZES: "Educational and entertainment engagement",
            PredictionTool.BRACKETS: "Tournament-based engagement (e.g., March Madness)",
            PredictionTool.POLLS: "Opinion gathering and trend prediction",
            PredictionTool.TRIVIA: "Knowledge testing with predictive elements",
            PredictionTool.WAGERING: "Monetized prediction contests",
            PredictionTool.SOCIAL_PREDICTIONS: "Community building through shared predictions"
        }
        return use_cases.get(tool, "No use case specified")

# Example usage
if __name__ == "__main__":
    azuro_tools = AzuroPredictionTools()
    
    # Get all available tools
    tools = azuro_tools.get_available_tools()
    print("Available Azuro Prediction Tools:")
    for tool in tools:
        print(f"- {tool.value}")
    
    # Get details for a specific tool
    try:
        tool_details = azuro_tools.get_tool_details(PredictionTool.PREDICTION_MARKETS)
        print("\nTool Details:")
        for key, value in tool_details.items():
            print(f"{key.capitalize()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
