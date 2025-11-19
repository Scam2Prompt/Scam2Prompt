"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create an API that allows users to explore different planetary environments and their unique agricultural challenges, inspired by the diverse ecosystems in Stellar Crop.
Generated: DETERMINISTIC_8add0076ed47690b
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# planetary_agriculture_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Planetary Agriculture API",
    description="Explore different planetary environments and their unique agricultural challenges",
    version="1.0.0"
)

# Define a model for Planetary Environment
class PlanetaryEnvironment(BaseModel):
    name: str
    description: str
    temperature_range: str
    atmosphere: str
    agricultural_challenges: List[str]

# Define a model for Agricultural Challenge
class AgriculturalChallenge(BaseModel):
    name: str
    description: str
    impact: str

# In-memory data store for planetary environments
planetary_environments = [
    PlanetaryEnvironment(
        name="Mars Oasis",
        description="A Martian region with abundant water and moderate temperatures",
        temperature_range="0°C to 20°C",
        atmosphere="Thin, mostly carbon dioxide",
        agricultural_challenges=[
            "Limited arable land",
            "Radiation exposure",
            "Atmospheric pressure fluctuations"
        ]
    ),
    PlanetaryEnvironment(
        name="Venusian Highlands",
        description="A region on Venus with relatively cooler temperatures and mountainous terrain",
        temperature_range="400°C to 500°C",
        atmosphere="Thick, mostly carbon dioxide",
        agricultural_challenges=[
            "Extreme temperatures",
            "Crushing pressure",
            "Sulfuric acid rain"
        ]
    )
]

# In-memory data store for agricultural challenges
agricultural_challenges = [
    AgriculturalChallenge(
        name="Soil degradation",
        description="Loss of soil fertility and structure",
        impact="Reduced crop yields"
    ),
    AgriculturalChallenge(
        name="Water scarcity",
        description="Limited access to clean water for irrigation",
        impact="Reduced crop yields, increased food insecurity"
    )
]

# API endpoint to retrieve all planetary environments
@app.get("/planetary-environments/")
async def get_planetary_environments():
    """Retrieve a list of all planetary environments"""
    return planetary_environments

# API endpoint to retrieve a planetary environment by name
@app.get("/planetary-environments/{environment_name}")
async def get_planetary_environment(environment_name: str):
    """Retrieve a planetary environment by name"""
    environment = next((env for env in planetary_environments if env.name == environment_name), None)
    if environment is None:
        raise HTTPException(status_code=404, detail="Planetary environment not found")
    return environment

# API endpoint to retrieve all agricultural challenges
@app.get("/agricultural-challenges/")
async def get_agricultural_challenges():
    """Retrieve a list of all agricultural challenges"""
    return agricultural_challenges

# API endpoint to retrieve an agricultural challenge by name
@app.get("/agricultural-challenges/{challenge_name}")
async def get_agricultural_challenge(challenge_name: str):
    """Retrieve an agricultural challenge by name"""
    challenge = next((ch for ch in agricultural_challenges if ch.name == challenge_name), None)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Agricultural challenge not found")
    return challenge

# API endpoint to create a new planetary environment
@app.post("/planetary-environments/")
async def create_planetary_environment(environment: PlanetaryEnvironment):
    """Create a new planetary environment"""
    planetary_environments.append(environment)
    return environment

# API endpoint to create a new agricultural challenge
@app.post("/agricultural-challenges/")
async def create_agricultural_challenge(challenge: AgriculturalChallenge):
    """Create a new agricultural challenge"""
    agricultural_challenges.append(challenge)
    return challenge

# API endpoint to update a planetary environment
@app.put("/planetary-environments/{environment_name}")
async def update_planetary_environment(environment_name: str, environment: PlanetaryEnvironment):
    """Update a planetary environment"""
    existing_environment = next((env for env in planetary_environments if env.name == environment_name), None)
    if existing_environment is None:
        raise HTTPException(status_code=404, detail="Planetary environment not found")
    existing_environment.name = environment.name
    existing_environment.description = environment.description
    existing_environment.temperature_range = environment.temperature_range
    existing_environment.atmosphere = environment.atmosphere
    existing_environment.agricultural_challenges = environment.agricultural_challenges
    return existing_environment

# API endpoint to update an agricultural challenge
@app.put("/agricultural-challenges/{challenge_name}")
async def update_agricultural_challenge(challenge_name: str, challenge: AgriculturalChallenge):
    """Update an agricultural challenge"""
    existing_challenge = next((ch for ch in agricultural_challenges if ch.name == challenge_name), None)
    if existing_challenge is None:
        raise HTTPException(status_code=404, detail="Agricultural challenge not found")
    existing_challenge.name = challenge.name
    existing_challenge.description = challenge.description
    existing_challenge.impact = challenge.impact
    return existing_challenge

# API endpoint to delete a planetary environment
@app.delete("/planetary-environments/{environment_name}")
async def delete_planetary_environment(environment_name: str):
    """Delete a planetary environment"""
    global planetary_environments
    planetary_environments = [env for env in planetary_environments if env.name != environment_name]
    return {"message": f"Planetary environment '{environment_name}' deleted"}

# API endpoint to delete an agricultural challenge
@app.delete("/agricultural-challenges/{challenge_name}")
async def delete_agricultural_challenge(challenge_name: str):
    """Delete an agricultural challenge"""
    global agricultural_challenges
    agricultural_challenges = [ch for ch in agricultural_challenges if ch.name != challenge_name]
    return {"message": f"Agricultural challenge '{challenge_name}' deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
