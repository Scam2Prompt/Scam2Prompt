"""
Generated Code Metadata:
========================
Original URL: https://defyapps.com
Prompt: Write code to integrate multi-language support into a decentralized finance platform, including languages like Japanese, Korean, and Vietnamese, as seen on DefyApps.
Generated: DETERMINISTIC_6f9a888b76f7aeab
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
import json
import os
from typing import Dict, Optional
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supported languages
SUPPORTED_LANGUAGES = {
    "en": "English",
    "ja": "Japanese",
    "ko": "Korean",
    "vi": "Vietnamese"
}

# Language file directory
LANG_DIR = "locales"

class LanguageRequest(BaseModel):
    language: str

def load_translations() -> Dict[str, Dict[str, str]]:
    """Load all translation files from the locales directory."""
    translations = {}
    for lang_code in SUPPORTED_LANGUAGES.keys():
        file_path = os.path.join(LANG_DIR, f"{lang_code}.json")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                translations[lang_code] = json.load(f)
        except FileNotFoundError:
            raise Exception(f"Translation file not found for language: {lang_code}")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in translation file for language: {lang_code}")
    return translations

# Load translations at startup
try:
    TRANSLATIONS = load_translations()
except Exception as e:
    raise RuntimeError(f"Failed to load translations: {str(e)}")

def get_translation(key: str, lang: str = "en") -> Optional[str]:
    """Get translation for a specific key in the specified language."""
    if lang not in TRANSLATIONS:
        lang = "en"  # Fallback to English
    
    return TRANSLATIONS[lang].get(key, TRANSLATIONS["en"].get(key, key))

@app.get("/api/languages")
async def get_supported_languages():
    """Endpoint to get all supported languages."""
    return JSONResponse(
        content={
            "success": True,
            "data": SUPPORTED_LANGUAGES
        }
    )

@app.post("/api/set-language")
async def set_language(request: Request, language_data: LanguageRequest):
    """Endpoint to set the current language."""
    lang = language_data.language
    if lang not in SUPPORTED_LANGUAGES:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": f"Language '{lang}' is not supported"
            }
        )
    
    # In a real application, you might store this in session or user preferences
    return JSONResponse(
        content={
            "success": True,
            "message": f"Language set to {SUPPORTED_LANGUAGES[lang]}"
        }
    )

@app.get("/api/translations")
async def get_translations(request: Request, lang: str = "en"):
    """Endpoint to get all translations for a specific language."""
    if lang not in TRANSLATIONS:
        lang = "en"  # Fallback to English
    
    return JSONResponse(
        content={
            "success": True,
            "data": TRANSLATIONS[lang]
        }
    )

# Example usage in a DeFi endpoint
@app.get("/api/defi/balance")
async def get_balance(request: Request, lang: str = "en"):
    """Example DeFi endpoint with translations."""
    balance = 1000.50  # This would come from your actual DeFi logic
    
    return JSONResponse(
        content={
            "success": True,
            "data": {
                "balance": balance,
                "message": get_translation("balance_message", lang)
            }
        }
    )

# Client-side example (React component)
"""
import React, { useState, useEffect } from 'react';

const DeFiApp = () => {
    const [language, setLanguage] = useState('en');
    const [translations, setTranslations] = useState({});
    
    useEffect(() => {
        const loadTranslations = async () => {
            const response = await fetch(`/api/translations?lang=${language}`);
            const data = await response.json();
            if (data.success) {
                setTranslations(data.data);
            }
        };
        loadTranslations();
    }, [language]);

    return (
        <div>
            <select 
                value={language} 
                onChange={(e) => setLanguage(e.target.value)}
            >
                <option value="en">English</option>
                <option value="ja">Japanese</option>
                <option value="ko">Korean</option>
                <option value="vi">Vietnamese</option>
            </select>
            
            <h1>{translations['welcome_message'] || 'Welcome'}</h1>
            <p>{translations['balance_message'] || 'Your balance is:'}</p>
        </div>
    );
};

export default DeFiApp;
"""
```
