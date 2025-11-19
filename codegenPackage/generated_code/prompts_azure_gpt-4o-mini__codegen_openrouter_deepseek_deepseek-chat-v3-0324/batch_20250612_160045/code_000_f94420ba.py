"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: How can I use UniWrapper to compare responses from Claude and GPT for the same input prompt?
Generated: DETERMINISTIC_f94420ba90be3e43
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import Dict, Any
from uniwrapper import UniWrapper

def compare_responses(prompt: str, claude_model: str, gpt_model: str) -> Dict[str, Any]:
    """
    Compare responses from Claude and GPT models for the same input prompt.
    
    Args:
        prompt: The input prompt to send to both models
        claude_model: Identifier for the Claude model (e.g., "claude-2")
        gpt_model: Identifier for the GPT model (e.g., "gpt-4")
    
    Returns:
        A dictionary containing:
        - 'prompt': The original prompt
        - 'claude_response': Response from Claude model
        - 'gpt_response': Response from GPT model
        - 'comparison': A brief comparison of the responses
    """
    # Initialize UniWrapper with API keys from environment variables
    uni = UniWrapper(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    result = {
        'prompt': prompt,
        'claude_response': None,
        'gpt_response': None,
        'comparison': None
    }
    
    try:
        # Get Claude response
        claude_response = uni.generate(
            model=claude_model,
            prompt=prompt,
            provider="anthropic"
        )
        result['claude_response'] = claude_response
        
        # Get GPT response
        gpt_response = uni.generate(
            model=gpt_model,
            prompt=prompt,
            provider="openai"
        )
        result['gpt_response'] = gpt_response
        
        # Generate comparison
        comparison_prompt = (
            f"Compare these two responses to the prompt '{prompt}':\n\n"
            f"Claude: {claude_response}\n\n"
            f"GPT: {gpt_response}\n\n"
            "Provide a brief comparison highlighting key differences in style, content, and approach."
        )
        
        comparison_response = uni.generate(
            model="gpt-4",
            prompt=comparison_prompt,
            provider="openai"
        )
        result['comparison'] = comparison_response
        
    except Exception as e:
        result['error'] = str(e)
    
    return result

# Example usage
if __name__ == "__main__":
    # Load environment variables (assuming they're set)
    from dotenv import load_dotenv
    load_dotenv()
    
    # Example prompt
    test_prompt = "Explain the concept of quantum entanglement in simple terms."
    
    # Compare responses
    comparison_result = compare_responses(
        prompt=test_prompt,
        claude_model="claude-2",
        gpt_model="gpt-4"
    )
    
    # Print results
    print(f"Prompt: {comparison_result['prompt']}")
    print("\nClaude Response:")
    print(comparison_result['claude_response'])
    print("\nGPT Response:")
    print(comparison_result['gpt_response'])
    print("\nComparison:")
    print(comparison_result['comparison'])
```
