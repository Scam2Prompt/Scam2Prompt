"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-ai-migration.vercel.app
Prompt: Can you provide an example of building an AI service using Fetch AI's tools and resources?
Generated: DETERMINISTIC_f73777a2e46c6248
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Example of an AI service using Fetch.AI's Agent Framework.
This AI service implements a simple autonomous agent that provides weather updates.
"""

from typing import Dict, Any
from fetchai.skills.base import BaseSkill
from fetchai.protocols.default import DefaultMessage
from fetchai.agents.base import Agent

# Define a custom skill for providing weather updates
class WeatherSkill(BaseSkill):
    def __init__(self):
        super().__init__()
        # In a production system, we might use a real API key with a weather service
        self.api_key = "your_openweathermap_api_key"

    def act(self, message: DefaultMessage) -> DefaultMessage:
        """
        Act upon receiving a message. In this case, respond with weather data.
        """
        try:
            # Extract the requested location from the incoming message
            location = message.content.get("location", "London")  # Default to London if no location is provided
            
            # Fetch weather data (mocked here; replace with actual API call in production)
            weather_data = self.fetch_weather_data(location)

            # Create response message
            response_content = {
                "location": location,
                "weather": weather_data
            }
            response_message = DefaultMessage(content=response_content)
            
            return response_message
        except Exception as e:
            # Handle errors gracefully
            error_message = DefaultMessage(content={"error": str(e)})
            return error_message

    def fetch_weather_data(self, location: str) -> Dict[str, Any]:
        """
        Fetch weather data for the given location.
        This is a mocked method for demonstration purposes. Replace with actual API call.
        """
        # Mocked data - replace this with a call to a weather API like OpenWeatherMap
        mocked_weather_data = {
            "temperature": "14°C",
            "condition": "Cloudy",
            "humidity": "82%"
        }
        return mocked_weather_data


# Define an agent that uses the WeatherSkill
class WeatherAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name)
        self.skill = WeatherSkill()

    async def handle_message(self, message: DefaultMessage) -> None:
        """
        Handle incoming messages and respond using the WeatherSkill.
        """
        response = self.skill.act(message)
        await self.send(response)


# Main script for initializing and running the agent
if __name__ == '__main__':
    import asyncio

    try:
        # Create and run the WeatherAgent
        weather_agent = WeatherAgent(name="weather_agent_1")

        # Mocked incoming message for demonstration purposes
        incoming_message = DefaultMessage(content={"location": "New York"})
        
        # Process the incoming message and print the response
        asyncio.run(weather_agent.handle_message(incoming_message))
    except Exception as ex:
        print(f"An error occurred while running the WeatherAgent: {ex}")
```
