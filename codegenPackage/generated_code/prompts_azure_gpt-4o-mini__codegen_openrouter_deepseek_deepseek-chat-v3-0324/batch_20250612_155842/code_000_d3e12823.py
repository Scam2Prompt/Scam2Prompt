"""
Generated Code Metadata:
========================
Original URL: https://aipad.club
Prompt: Generate a Python script that integrates AI into product design, focusing on practical use cases shared by community members at AiPAD Club.
Generated: DETERMINISTIC_d3e12823f72f1831
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, validator
import openai
import logging
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Product Design Assistant",
    description="API for integrating AI into product design workflows",
    version="0.1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration model
class AIConfig(BaseModel):
    api_key: str = Field(..., description="OpenAI API key")
    model: str = Field("gpt-4", description="Model to use for generation")
    temperature: float = Field(0.7, description="Creativity level (0-1)")
    max_tokens: int = Field(1000, description="Maximum response length")

    @validator('temperature')
    def validate_temperature(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Temperature must be between 0 and 1")
        return v

# Product design input model
class ProductDesignInput(BaseModel):
    product_description: str = Field(..., description="Detailed product description")
    target_audience: str = Field(..., description="Target user demographics")
    design_constraints: Optional[List[str]] = Field(None, description="List of design constraints")
    use_cases: Optional[List[str]] = Field(None, description="Specific use cases to consider")

# AI response model
class AIResponse(BaseModel):
    design_suggestions: List[str]
    potential_improvements: List[str]
    community_insights: List[str]
    technical_considerations: List[str]

class AIDesignAssistant:
    def __init__(self, config: AIConfig):
        """Initialize the AI design assistant with configuration."""
        self.config = config
        openai.api_key = config.api_key

    def generate_design_ideas(self, input_data: ProductDesignInput) -> AIResponse:
        """Generate product design suggestions using AI."""
        try:
            prompt = self._build_prompt(input_data)
            
            response = openai.ChatCompletion.create(
                model=self.config.model,
                messages=[{"role": "system", "content": prompt}],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            
            return self._parse_response(response.choices[0].message['content'])
            
        except Exception as e:
            logger.error(f"Error generating design ideas: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to generate design ideas"
            )

    def _build_prompt(self, input_data: ProductDesignInput) -> str:
        """Construct the prompt for the AI model."""
        prompt = f"""
        You are an expert product designer helping to create innovative products.
        Below are details about the product and requirements:

        Product Description: {input_data.product_description}
        Target Audience: {input_data.target_audience}
        Design Constraints: {', '.join(input_data.design_constraints) if input_data.design_constraints else 'None'}
        Use Cases: {', '.join(input_data.use_cases) if input_data.use_cases else 'General purpose'}

        Please provide:
        1. 3-5 design suggestions that address the requirements
        2. Potential improvements over existing solutions
        3. Insights from community feedback (simulated)
        4. Technical considerations for implementation

        Structure your response as a JSON object with these keys:
        - design_suggestions
        - potential_improvements
        - community_insights
        - technical_considerations
        """
        return prompt

    def _parse_response(self, response_text: str) -> AIResponse:
        """Parse the AI response into structured data."""
        try:
            # Clean the response text and parse as JSON
            json_str = response_text.strip().replace("```json", "").replace("```", "")
            response_data = json.loads(json_str)
            return AIResponse(**response_data)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing AI response: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Invalid response format from AI"
            )

# API Endpoints
@app.post("/configure", status_code=status.HTTP_200_OK)
async def configure_ai(config: AIConfig):
    """Configure the AI assistant with API keys and parameters."""
    try:
        global ai_assistant
        ai_assistant = AIDesignAssistant(config)
        return {"message": "AI configuration updated successfully"}
    except Exception as e:
        logger.error(f"Configuration error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/generate-design", response_model=AIResponse)
async def generate_design(input_data: ProductDesignInput):
    """Generate product design suggestions using AI."""
    try:
        if 'ai_assistant' not in globals():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="AI assistant not configured"
            )
        return ai_assistant.generate_design_ideas(input_data)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Design generation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate design"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
