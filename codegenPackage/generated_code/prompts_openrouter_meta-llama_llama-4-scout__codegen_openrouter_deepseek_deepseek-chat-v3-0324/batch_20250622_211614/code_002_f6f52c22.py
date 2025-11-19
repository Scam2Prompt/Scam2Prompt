"""
Generated Code Metadata:
========================
Original URL: https://hamsterboost.io
Prompt: "Generate code to integrate Telegram Mini App with Hamster Boost for quest participation and bounty claiming."
Generated: DETERMINISTIC_f6f52c220bcda62b
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import Optional, Dict, Any
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import httpx
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HAMSTER_BOOST_API_URL = os.getenv("HAMSTER_BOOST_API_URL")
HAMSTER_BOOST_API_KEY = os.getenv("HAMSTER_BOOST_API_KEY")

if not all([TELEGRAM_BOT_TOKEN, HAMSTER_BOOST_API_URL, HAMSTER_BOOST_API_KEY]):
    raise ValueError("Missing required environment variables")

# Initialize FastAPI app
app = FastAPI(title="Telegram Mini App - Hamster Boost Integration")

# Telegram bot setup
telegram_bot = Bot(token=TELEGRAM_BOOST_API_KEY)

# Pydantic models for request/response validation
class QuestParticipationRequest(BaseModel):
    user_id: int
    quest_id: str
    wallet_address: str

class BountyClaimRequest(BaseModel):
    user_id: int
    bounty_id: str
    wallet_address: str

class HamsterBoostResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

async def call_hamster_boost_api(endpoint: str, payload: Dict[str, Any]) -> HamsterBoostResponse:
    """
    Helper function to make API calls to Hamster Boost
    """
    headers = {
        "Authorization": f"Bearer {HAMSTER_BOOST_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{HAMSTER_BOOST_API_URL}/{endpoint}",
                headers=headers,
                json=payload,
                timeout=10.0
            )
            response.raise_for_status()
            return HamsterBoostResponse(**response.json())
    except httpx.HTTPStatusError as e:
        logger.error(f"Hamster Boost API error: {e}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Hamster Boost API error: {e.response.text}"
        )
    except Exception as e:
        logger.error(f"Unexpected error calling Hamster Boost API: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

@app.post("/participate-in-quest")
async def participate_in_quest(request: QuestParticipationRequest):
    """
    Endpoint to handle quest participation
    """
    try:
        payload = {
            "user_id": request.user_id,
            "quest_id": request.quest_id,
            "wallet_address": request.wallet_address
        }
        
        response = await call_hamster_boost_api("quests/participate", payload)
        
        if response.success:
            # Notify user via Telegram
            await telegram_bot.send_message(
                chat_id=request.user_id,
                text=f"🎉 Successfully participated in quest {request.quest_id}!"
            )
        
        return response.dict()
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f"Error in quest participation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/claim-bounty")
async def claim_bounty(request: BountyClaimRequest):
    """
    Endpoint to handle bounty claiming
    """
    try:
        payload = {
            "user_id": request.user_id,
            "bounty_id": request.bounty_id,
            "wallet_address": request.wallet_address
        }
        
        response = await call_hamster_boost_api("bounties/claim", payload)
        
        if response.success:
            # Notify user via Telegram
            await telegram_bot.send_message(
                chat_id=request.user_id,
                text=f"💰 Successfully claimed bounty {request.bounty_id}!"
            )
        
        return response.dict()
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f"Error in bounty claim: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/telegram-webhook")
async def telegram_webhook(update: Update):
    """
    Telegram webhook handler for Mini App interactions
    """
    try:
        if not update.message or not update.message.text:
            return JSONResponse(content={"status": "ignored"})
        
        text = update.message.text.lower()
        user_id = update.message.from_user.id
        
        if text.startswith("/start quest_"):
            quest_id = text.split("_")[1]
            return await participate_in_quest(QuestParticipationRequest(
                user_id=user_id,
                quest_id=quest_id,
                wallet_address="user_wallet_address"  # Should be obtained from Mini App
            ))
        elif text.startswith("/claim bounty_"):
            bounty_id = text.split("_")[1]
            return await claim_bounty(BountyClaimRequest(
                user_id=user_id,
                bounty_id=bounty_id,
                wallet_address="user_wallet_address"  # Should be obtained from Mini App
            ))
        
        return JSONResponse(content={"status": "unknown_command"})
    except Exception as e:
        logger.error(f"Error in Telegram webhook: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

async def setup_telegram_bot():
    """
    Setup Telegram bot handlers
    """
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", telegram_webhook))
    application.add_handler(CommandHandler("claim", telegram_webhook))
    
    return application

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
