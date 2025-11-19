"""
Generated Code Metadata:
========================
Original URL: https://arcofaurora.com
Prompt: Create an API that allows users to access information about "Etheric Surgery" and its benefits, as described on the Arc of AurorA website.
Generated: DETERMINISTIC_fb9cbfc3da99b2e6
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Etheric Surgery API",
    description="API for accessing information about Etheric Surgery and its benefits",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for Etheric Surgery information
class EthericSurgeryInfo(BaseModel):
    title: str
    description: str
    benefits: list[str]
    procedure_steps: Optional[list[str]] = None
    faqs: Optional[list[dict[str, str]]] = None

# Mock database
ETHERIC_SURGERY_DATA = EthericSurgeryInfo(
    title="Etheric Surgery",
    description="Etheric Surgery is a revolutionary energy healing technique that works on the subtle energy bodies to remove blockages and restore balance.",
    benefits=[
        "Removes energetic blockages",
        "Restores balance to the chakra system",
        "Enhances spiritual growth",
        "Promotes emotional healing",
        "Improves physical well-being"
    ],
    procedure_steps=[
        "Initial energy assessment",
        "Identification of blockages",
        "Energetic realignment",
        "Chakra balancing",
        "Post-session integration"
    ],
    faqs=[
        {
            "question": "Is Etheric Surgery safe?",
            "answer": "Yes, it's completely non-invasive and works only with your energy field."
        },
        {
            "question": "How many sessions are needed?",
            "answer": "This varies by individual, but most people see benefits after 3-5 sessions."
        }
    ]
)

@app.get("/", response_model=EthericSurgeryInfo, summary="Get all Etheric Surgery information")
async def get_all_info():
    """
    Returns complete information about Etheric Surgery including:
    - Description
    - Benefits
    - Procedure steps
    - FAQs
    """
    return ETHERIC_SURGERY_DATA

@app.get("/description", summary="Get Etheric Surgery description")
async def get_description():
    """Returns the description of Etheric Surgery"""
    return {"description": ETHERIC_SURGERY_DATA.description}

@app.get("/benefits", summary="Get Etheric Surgery benefits")
async def get_benefits():
    """Returns the list of benefits from Etheric Surgery"""
    return {"benefits": ETHERIC_SURGERY_DATA.benefits}

@app.get("/procedure", summary="Get Etheric Surgery procedure steps")
async def get_procedure():
    """Returns the steps involved in the Etheric Surgery procedure"""
    if not ETHERIC_SURGERY_DATA.procedure_steps:
        raise HTTPException(status_code=404, detail="Procedure steps not available")
    return {"procedure_steps": ETHERIC_SURGERY_DATA.procedure_steps}

@app.get("/faqs", summary="Get Etheric Surgery FAQs")
async def get_faqs():
    """Returns frequently asked questions about Etheric Surgery"""
    if not ETHERIC_SURGERY_DATA.faqs:
        raise HTTPException(status_code=404, detail="FAQs not available")
    return {"faqs": ETHERIC_SURGERY_DATA.faqs}

@app.get("/search")
async def search_info(query: str):
    """
    Search across all Etheric Surgery information.
    
    Parameters:
    - query: str - Search term to look for in the content
    
    Returns:
    - Dictionary with matching content from all sections
    """
    results = {}
    
    if query.lower() in ETHERIC_SURGERY_DATA.description.lower():
        results["description"] = ETHERIC_SURGERY_DATA.description
    
    matching_benefits = [b for b in ETHERIC_SURGERY_DATA.benefits if query.lower() in b.lower()]
    if matching_benefits:
        results["benefits"] = matching_benefits
    
    if ETHERIC_SURGERY_DATA.procedure_steps:
        matching_steps = [s for s in ETHERIC_SURGERY_DATA.procedure_steps if query.lower() in s.lower()]
        if matching_steps:
            results["procedure_steps"] = matching_steps
    
    if ETHERIC_SURGERY_DATA.faqs:
        matching_faqs = []
        for faq in ETHERIC_SURGERY_DATA.faqs:
            if (query.lower() in faq["question"].lower()) or (query.lower() in faq["answer"].lower()):
                matching_faqs.append(faq)
        if matching_faqs:
            results["faqs"] = matching_faqs
    
    if not results:
        raise HTTPException(status_code=404, detail=f"No results found for '{query}'")
    
    return results
```
