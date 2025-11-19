"""
Generated Code Metadata:
========================
Original URL: https://micmarktrade.com
Prompt: Write code to integrate a multilingual customer service chatbot for a trading platform, inspired by MIC markets' multilingual support team.
Generated: DETERMINISTIC_f19316b9f4d13e53
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import Dict, List, Optional
import json
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import openai
from langdetect import detect
from pydantic import BaseModel, Field
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Multilingual Trading Platform Chatbot",
    description="API for multilingual customer service chatbot for trading platform",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Supported languages with their ISO codes
SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ar": "Arabic"
}

# Chatbot system prompts for different languages
SYSTEM_PROMPTS = {
    "en": "You are a professional customer support agent for a trading platform. Provide clear, accurate and helpful responses.",
    "es": "Eres un agente de soporte al cliente profesional para una plataforma de trading. Proporciona respuestas claras, precisas y útiles.",
    "fr": "Vous êtes un agent de support client professionnel pour une plateforme de trading. Fournissez des réponses claires, précises et utiles.",
    "de": "Sie sind ein professioneller Kundensupportmitarbeiter für eine Trading-Plattform. Geben Sie klare, präzise und hilfreiche Antworten.",
    "it": "Sei un agente di supporto clienti professionale per una piattaforma di trading. Fornisci risposte chiare, accurate e utili.",
    "pt": "Você é um agente de suporte ao cliente profissional para uma plataforma de negociação. Forneça respostas claras, precisas e úteis.",
    "ru": "Вы профессиональный агент службы поддержки клиентов торговой платформы. Давайте четкие, точные и полезные ответы.",
    "zh": "您是一名专业的交易平台客户支持代理。提供清晰、准确和有用的回复。",
    "ja": "あなたは取引プラットフォームのプロフェッショナルなカスタマーサポートエージェントです。明確で正確かつ役立つ回答を提供してください。",
    "ar": "أنت وكيل دعم عملاء محترف لمنصة تداول. قدم إجابات واضحة ودقيقة ومفيدة."
}

# Common trading FAQs
TRADING_FAQS = {
    "account": {
        "en": "For account-related questions, please visit our account management section.",
        "es": "Para preguntas relacionadas con la cuenta, visite nuestra sección de gestión de cuentas.",
        "fr": "Pour les questions relatives au compte, veuillez visiter notre section de gestion de compte.",
        "de": "Für kontobezogene Fragen besuchen Sie bitte unseren Kontoverwaltungsbereich.",
        "it": "Per domande relative all'account, visita la nostra sezione di gestione dell'account.",
        "pt": "Para perguntas relacionadas à conta, visite nossa seção de gerenciamento de contas.",
        "ru": "По вопросам, связанным с учетной записью, посетите наш раздел управления учетной записью.",
        "zh": "有关账户问题，请访问我们的账户管理部分。",
        "ja": "アカウントに関する質問については、アカウント管理セクションをご覧ください。",
        "ar": "للأسئلة المتعلقة بالحساب ، يرجى زيارة قسم إدارة الحساب لدينا."
    },
    "deposit": {
        "en": "Deposit methods include bank transfer, credit card, and e-wallets. Processing time varies by method.",
        "es": "Los métodos de depósito incluyen transferencia bancaria, tarjeta de crédito y billeteras electrónicas. El tiempo de procesamiento varía según el método.",
        "fr": "Les méthodes de dépôt comprennent le virement bancaire, la carte de crédit et les portefeuilles électroniques. Le temps de traitement varie selon la méthode.",
        "de": "Einzahlungsmethoden umfassen Banküberweisung, Kreditkarte und E-Wallets. Die Bearbeitungszeit variiert je nach Methode.",
        "it": "I metodi di deposito includono bonifico bancario, carta di credito e portafogli elettronici. Il tempo di elaborazione varia a seconda del metodo.",
        "pt": "Os métodos de depósito incluem transferência bancária, cartão de crédito e carteiras eletrônicas. O tempo de processamento varia de acordo com o método.",
        "ru": "Методы депозита включают банковский перевод, кредитную карту и электронные кошельки. Время обработки зависит от метода.",
        "zh": "存款方式包括银行转账、信用卡和电子钱包。处理时间因方法而异。",
        "ja": "入金方法には、銀行振込、クレジットカード、電子ウォレットが含まれます。処理時間は方法によって異なります。",
        "ar": "تشمل طرق الإيداع التحويل البنكي وبطاقة الائتمام والمحافظ الإلكترونية. يختلف وقت المعالجة حسب الطريقة."
    }
}

class ChatRequest(BaseModel):
    message: str = Field(..., description="User's message to the chatbot")
    language: Optional[str] = Field(
        None,
        description="Preferred language for response (ISO code). Auto-detected if not provided."
    )
    session_id: Optional[str] = Field(
        None,
        description="Session ID for maintaining conversation context"
    )

class ChatResponse(BaseModel):
    response: str = Field(..., description="Chatbot's response message")
    detected_language: Optional[str] = Field(
        None,
        description="Detected language of user message (ISO code)"
    )
    used_language: str = Field(..., description="Language used for response (ISO code)")
    session_id: Optional[str] = Field(
        None,
        description="Session ID for maintaining conversation context"
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An unexpected error occurred. Please try again later."}
    )

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        return lang if lang in SUPPORTED_LANGUAGES else "en"
    except:
        return "en"

def get_system_prompt(language: str) -> str:
    return SYSTEM_PROMPTS.get(language, SYSTEM_PROMPTS["en"])

def get_faq_response(intent: str, language: str) -> Optional[str]:
    if intent in TRADING_FAQS:
        return TRADING_FAQS[intent].get(language, TRADING_FAQS[intent]["en"])
    return None

async def generate_chat_response(
    message: str,
    language: str,
    session_id: Optional[str] = None
) -> Dict:
    # Check for FAQ matches first
    message_lower = message.lower()
    for intent in TRADING_FAQS:
        if intent in message_lower:
            faq_response = get_faq_response(intent, language)
            if faq_response:
                return {
                    "response": faq_response,
                    "used_language": language
                }

    # Generate response using OpenAI
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": get_system_prompt(language)},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return {
            "response": response.choices[0].message.content,
            "used_language":
