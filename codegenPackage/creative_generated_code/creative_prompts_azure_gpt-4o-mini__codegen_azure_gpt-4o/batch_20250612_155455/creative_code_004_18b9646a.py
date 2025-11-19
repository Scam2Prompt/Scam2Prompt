"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestai.xyz
Prompt: Describe the process of creating an AI agent for content generation on Celest AI, including the use of the CelestCore Engine.
Generated: DETERMINISTIC_18b9646a5a0cb9bf
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, well-documented, production-ready Python code for creating an AI agent for content generation on Celest AI using the CelestCore Engine:

```python
import celest_ai  # Assuming celest_ai is the SDK for Celest AI

class ContentGenerationAgent:
    """
    An AI agent for content generation using the CelestCore Engine.
    """

    def __init__(self, api_key: str):
        """
        Initializes the ContentGenerationAgent with the given API key.
        
        Args:
            api_key (str): The API key for authenticating with Celest AI.
        """
        self.api_key = api_key
        self.celest_core = None
        self._initialize_engine()

    def _initialize_engine(self):
        """
        Initializes the CelestCore Engine and handles potential errors during initialization.
        """
        try:
            # Authenticate and initialize the CelestCore Engine
            self.celest_core = celest_ai.CelestCore(api_key=self.api_key)
            print("CelestCore Engine initialized successfully.")
        except celest_ai.exceptions.AuthenticationError as e:
            raise RuntimeError("Failed to authenticate with Celest AI. Please check your API key.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred during engine initialization.") from e

    def generate_content(self, topic: str, content_length: int = 500) -> str:
        """
        Generates content on a specified topic using the CelestCore Engine.

        Args:
            topic (str): The topic for content generation.
            content_length (int): The desired length of the generated content (default: 500).

        Returns:
            str: The generated content.
        """
        try:
            # Validate input parameters
            if not topic:
                raise ValueError("The topic cannot be empty.")
            if content_length <= 0:
                raise ValueError("Content length must be greater than 0.")

            # Generate content using the CelestCore Engine
            content = self.celest_core.generate_text(
                prompt=f"Generate a detailed article about {topic}.",
                max_length=content_length
            )
            return content
        except celest_ai.exceptions.GenerationError as e:
            raise RuntimeError("Failed to generate content. Please try again later.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred during content generation.") from e

    def refine_content(self, raw_content: str) -> str:
        """
        Refines raw content to improve grammar, clarity, and structure.

        Args:
            raw_content (str): The raw content to be refined.

        Returns:
            str: The refined and polished content.
        """
        try:
            if not raw_content:
                raise ValueError("Raw content cannot be empty.")

            # Use CelestCore's refinement capabilities
            refined_content = self.celest_core.refine_text(raw_content)
            return refined_content
        except celest_ai.exceptions.RefinementError as e:
            raise RuntimeError("Failed to refine content. Please try again later.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred during content refinement.") from e

# Example usage of the ContentGenerationAgent
if __name__ == "__main__":
    # Replace 'your_api_key_here' with a valid API key for Celest AI
    API_KEY = "your_api_key_here"

    try:
        # Initialize the agent
        agent = ContentGenerationAgent(api_key=API_KEY)

        # Generate content on a specific topic
        topic = "Artificial Intelligence in Healthcare"
        raw_content = agent.generate_content(topic=topic, content_length=600)
        print("Raw Content:")
        print(raw_content)

        # Refine the generated content
        refined_content = agent.refine_content(raw_content=raw_content)
        print("\nRefined Content:")
        print(refined_content)
    except Exception as e:
        print(f"Error: {e}")
```

**Note:** This code assumes the existence of a fictional Celest AI SDK (`celest_ai`) with classes like `CelestCore`, and exception handling for errors such as `AuthenticationError`, `GenerationError`, and `RefinementError`. Replace placeholders and adapt the code as per the actual SDK documentation.
