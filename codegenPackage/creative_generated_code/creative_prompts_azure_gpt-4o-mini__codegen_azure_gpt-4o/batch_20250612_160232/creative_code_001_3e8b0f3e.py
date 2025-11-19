"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: What are the best practices for optimizing latency when using the OpenAI API for real-time applications?
Generated: DETERMINISTIC_3e8b0f3eb57341a2
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import asyncio
import time

# Best practices for optimizing latency when using OpenAI API for real-time applications:
# 1. Use asynchronous programming to handle requests concurrently.
# 2. Implement connection timeout and retries to ensure resilience.
# 3. Cache repeated or predictable responses to reduce API calls.
# 4. Minimize the size of input prompts to reduce processing time.
# 5. Use the appropriate model for your use case (e.g., faster, smaller models when latency is critical).
# 6. Ensure efficient network connectivity to reduce transmission delays.
# 7. Monitor and log performance metrics to optimize further.

# Configuration
openai.api_key = "YOUR_API_KEY"  # Replace with your API key
DEFAULT_TIMEOUT = 10  # Timeout for API requests in seconds

async def fetch_openai_response(prompt: str, model: str = "text-davinci-003") -> str:
    """
    Fetch response from OpenAI API asynchronously.

    :param prompt: The input prompt for the API.
    :param model: The model to use (default is text-davinci-003).
    :return: The response text from the API.
    """
    try:
        start_time = time.time()  # Measure latency
        response = await asyncio.wait_for(
            asyncio.to_thread(openai.Completion.create, model=model, prompt=prompt, max_tokens=100),
            timeout=DEFAULT_TIMEOUT
        )
        elapsed_time = time.time() - start_time
        print(f"API call latency: {elapsed_time:.2f} seconds")
        return response.choices[0].text.strip()
    except asyncio.TimeoutError:
        print("API request timed out.")
        return "Error: Timeout"
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "Error: API failure"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Error: Unexpected issue"

async def main():
    """
    Main entry point for testing API optimization.
    """
    prompt = "What is the best way to optimize latency when using OpenAI APIs?"
    # Example usage of multiple concurrent requests for real-time performance
    tasks = [fetch_openai_response(prompt) for _ in range(5)]
    responses = await asyncio.gather(*tasks)  # Concurrent execution of requests
    for idx, response in enumerate(responses, 1):
        print(f"Response {idx}: {response}")

# Run the program
if __name__ == "__main__":
    asyncio.run(main())
```
