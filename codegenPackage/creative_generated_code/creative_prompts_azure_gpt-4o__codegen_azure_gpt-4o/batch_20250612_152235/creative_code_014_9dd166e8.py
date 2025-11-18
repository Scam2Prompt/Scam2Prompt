"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: Provide an example of building a multi-agent system using the Olas Open Autonomy framework to create off-chain services.
Generated: DETERMINISTIC_9dd166e89e055155
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from olas_autonomy import Agent, AgentManager, ServiceRequest

# Define constants for the service
SERVICE_NAME = "example_multi_agent_service"
AGENT_COUNT = 3
SERVICE_PORT = 8080

# Define individual agent class to handle specific tasks
class ExampleAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    async def handle_request(self, request: ServiceRequest):
        """
        Process incoming service requests and return a response.
        This method simulates task handling by the agent.
        """
        try:
            # Simulate processing the request (you can replace with actual logic)
            task_data = request.payload.get("task_data")
            await asyncio.sleep(1)  # Simulate workload
            return {
                "status": "success",
                "agent_name": self.name,
                "processed_data": f"Processed {task_data} by {self.name}",
            }
        except Exception as e:
            # Handle any errors during processing
            return {
                "status": "error",
                "agent_name": self.name,
                "error_message": str(e),
            }

# Initialize the multi-agent system
async def main():
    # Create an AgentManager to manage multiple agents
    agent_manager = AgentManager(SERVICE_NAME, SERVICE_PORT)

    # Add multiple agents to the manager
    for i in range(AGENT_COUNT):
        agent_name = f"Agent-{i+1}"
        agent_manager.add_agent(ExampleAgent(agent_name))

    # Start the service
    await agent_manager.start()

    print(f"{SERVICE_NAME} started on port {SERVICE_PORT} with {AGENT_COUNT} agents.")

    # Run the service until terminated
    try:
        await agent_manager.run_forever()
    except KeyboardInterrupt:
        print("Shutting down service...")
    finally:
        await agent_manager.shutdown()

# Run the program
if __name__ == "__main__":
    asyncio.run(main())
```
