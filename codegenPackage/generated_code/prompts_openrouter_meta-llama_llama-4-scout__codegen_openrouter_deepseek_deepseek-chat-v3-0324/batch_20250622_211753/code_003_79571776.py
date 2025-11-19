"""
Generated Code Metadata:
========================
Original URL: https://www.icursor.ai
Prompt: Compare the features of iCursor with other AI-powered writing tools, highlighting its unique use cases and benefits.
Generated: DETERMINISTIC_7957177678d4354e
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class WritingToolFeature:
    """
    Represents a feature of a writing tool with its description and supported status.
    """
    def __init__(self, name: str, description: str, is_supported: bool):
        self.name = name
        self.description = description
        self.is_supported = is_supported

    def to_dict(self) -> Dict:
        """Convert the feature to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "is_supported": self.is_supported
        }

class WritingTool:
    """
    Represents a writing tool with its features and metadata.
    """
    def __init__(self, name: str, description: str, features: List[WritingToolFeature]):
        self.name = name
        self.description = description
        self.features = features

    def to_dict(self) -> Dict:
        """Convert the writing tool to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "features": [feature.to_dict() for feature in self.features]
        }

class WritingToolComparator:
    """
    Compares features of multiple writing tools and highlights unique use cases.
    """
    def __init__(self, tools: List[WritingTool]):
        self.tools = tools

    def compare_features(self) -> Dict:
        """
        Compare features across all tools and return a summary.
        
        Returns:
            Dict: A dictionary with tool names as keys and their unique features.
        """
        comparison = {}
        for tool in self.tools:
            unique_features = []
            for feature in tool.features:
                is_unique = True
                for other_tool in self.tools:
                    if other_tool.name != tool.name:
                        for other_feature in other_tool.features:
                            if other_feature.name == feature.name and other_feature.is_supported:
                                is_unique = False
                                break
                    if not is_unique:
                        break
                if is_unique and feature.is_supported:
                    unique_features.append(feature.to_dict())
            comparison[tool.name] = {
                "description": tool.description,
                "unique_features": unique_features
            }
        return comparison

    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate a JSON report of the comparison.
        
        Args:
            output_file (Optional[str]): Path to save the report. If None, return as string.
        
        Returns:
            str: JSON string if output_file is None, else confirmation message.
        
        Raises:
            IOError: If there's an issue writing to the file.
        """
        report = self.compare_features()
        report_json = json.dumps(report, indent=2)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(report_json)
                return f"Report saved to {output_file}"
            except IOError as e:
                raise IOError(f"Failed to write report to file: {e}")
        return report_json

# Example usage
if __name__ == "__main__":
    # Define features for iCursor
    i_cursor_features = [
        WritingToolFeature("Contextual Suggestions", "Provides suggestions based on the context of the document.", True),
        WritingToolFeature("Multi-language Support", "Supports multiple languages for writing and editing.", True),
        WritingToolFeature("Code Assistance", "Helps with writing and debugging code snippets.", True),
        WritingToolFeature("Collaborative Editing", "Allows real-time collaboration with other users.", False)
    ]

    # Define features for Tool B
    tool_b_features = [
        WritingToolFeature("Contextual Suggestions", "Provides suggestions based on the context of the document.", True),
        WritingToolFeature("Grammar Checking", "Advanced grammar and style checking.", True),
        WritingToolFeature("Code Assistance", "Helps with writing and debugging code snippets.", False),
        WritingToolFeature("Templates", "Provides pre-built templates for various document types.", True)
    ]

    # Define features for Tool C
    tool_c_features = [
        WritingToolFeature("Grammar Checking", "Advanced grammar and style checking.", True),
        WritingToolFeature("Plagiarism Checker", "Checks for plagiarism in the document.", True),
        WritingToolFeature("Multi-language Support", "Supports multiple languages for writing and editing.", False),
        WritingToolFeature("Templates", "Provides pre-built templates for various document types.", True)
    ]

    # Create writing tool instances
    i_cursor = WritingTool("iCursor", "AI-powered writing tool with advanced contextual suggestions and code assistance.", i_cursor_features)
    tool_b = WritingTool("Tool B", "Comprehensive writing assistant with grammar checking and templates.", tool_b_features)
    tool_c = WritingTool("Tool C", "Writing tool focused on grammar and plagiarism checking.", tool_c_features)

    # Compare tools
    comparator = WritingToolComparator([i_cursor, tool_b, tool_c])
    
    # Generate and print the report
    try:
        print(comparator.generate_report())
        # To save to a file:
        # print(comparator.generate_report("writing_tools_comparison.json"))
    except Exception as e:
        print(f"Error generating report: {e}")
```
