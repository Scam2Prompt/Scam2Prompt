"""
Generated Code Metadata:
========================
Original URL: https://aipad.club
Prompt: Create a tutorial for using popular AI tools mentioned in the AiPAD Club, aimed at new users looking to enhance their skills.
Generated: DETERMINISTIC_bfa6162942706ff1
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
AI Tools Tutorial for AiPAD Club Members

This script provides a hands-on tutorial for new users to explore popular AI tools.
It covers basic usage of tools like OpenAI's GPT, Hugging Face Transformers, and LangChain.
"""

import os
import openai
from transformers import pipeline
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AIToolsTutorial:
    def __init__(self):
        """Initialize AI tools with API keys from environment variables."""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
        
        if not self.openai_api_key or not self.huggingface_token:
            raise ValueError("API keys not found in environment variables")
            
        openai.api_key = self.openai_api_key

    def openai_gpt_demo(self, prompt):
        """
        Demonstrate basic usage of OpenAI's GPT model.
        
        Args:
            prompt (str): Input prompt for the model
            
        Returns:
            str: Generated response from GPT
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error in OpenAI GPT demo: {e}")
            return None

    def huggingface_demo(self, text):
        """
        Demonstrate sentiment analysis using Hugging Face transformers.
        
        Args:
            text (str): Input text for sentiment analysis
            
        Returns:
            dict: Sentiment analysis results
        """
        try:
            classifier = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
            return classifier(text)
        except Exception as e:
            print(f"Error in Hugging Face demo: {e}")
            return None

    def langchain_demo(self, template, input_variables):
        """
        Demonstrate LangChain for chaining prompts and LLM calls.
        
        Args:
            template (str): Template for the prompt
            input_variables (dict): Variables to fill in the template
            
        Returns:
            str: Generated response from the chain
        """
        try:
            llm = OpenAI(temperature=0.7)
            prompt = PromptTemplate(
                input_variables=list(input_variables.keys()),
                template=template
            )
            chain = LLMChain(llm=llm, prompt=prompt)
            return chain.run(input_variables)
        except Exception as e:
            print(f"Error in LangChain demo: {e}")
            return None

def run_tutorial():
    """Run interactive tutorial for AI tools."""
    tutorial = AIToolsTutorial()
    
    print("Welcome to the AiPAD Club AI Tools Tutorial!\n")
    
    # OpenAI GPT Demo
    print("\n=== OpenAI GPT Demo ===")
    gpt_prompt = "Explain how AI is transforming education in simple terms."
    gpt_response = tutorial.openai_gpt_demo(gpt_prompt)
    print(f"\nPrompt: {gpt_prompt}")
    print(f"Response: {gpt_response}")
    
    # Hugging Face Demo
    print("\n=== Hugging Face Transformers Demo ===")
    hf_text = "I'm really excited about learning AI tools!"
    hf_result = tutorial.huggingface_demo(hf_text)
    print(f"\nText: {hf_text}")
    print(f"Sentiment: {hf_result}")
    
    # LangChain Demo
    print("\n=== LangChain Demo ===")
    lc_template = "Create a short poem about {topic} in the style of {style}."
    lc_vars = {"topic": "artificial intelligence", "style": "Shakespeare"}
    lc_response = tutorial.langchain_demo(lc_template, lc_vars)
    print(f"\nTemplate: {lc_template}")
    print(f"Variables: {lc_vars}")
    print(f"Response: {lc_response}")
    
    print("\nTutorial completed! Explore these tools further to enhance your AI skills.")

if __name__ == "__main__":
    run_tutorial()
```
