"""
Generated Code Metadata:
========================
Original URL: https://paalai-io.web.app
Prompt: "Develop a PAAL AI bot that can upload and learn from content such as Word documents, PDFs, and YouTube links, and provide a conversational interface for users to interact with."
Generated: DETERMINISTIC_c0de0431c3c03488
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import tempfile
import logging
from typing import List, Dict, Optional
from pathlib import Path
import requests
from PyPDF2 import PdfReader
from docx import Document
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="PAAL AI Bot",
    description="AI bot that learns from documents and provides conversational interface",
    version="1.0.0"
)

# Configuration
class Config:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.max_file_size = 10 * 1024 * 1024  # 10MB
        self.supported_file_types = {
            'application/pdf': 'pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
            'text/plain': 'txt'
        }
        self.chunk_size = 1000
        self.chunk_overlap = 200

config = Config()

# Initialize components
embeddings = OpenAIEmbeddings(openai_api_key=config.openai_api_key)
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", openai_api_key=config.openai_api_key)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
vector_store = None
qa_chain = None

# Models
class ChatRequest(BaseModel):
    question: str
    chat_history: Optional[List[Dict[str, str]]] = None

class ChatResponse(BaseModel):
    answer: str
    chat_history: List[Dict[str, str]]

# Helper functions
def process_pdf(file_path: str) -> str:
    """Extract text from PDF file."""
    try:
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages])
        return text
    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        raise HTTPException(status_code=400, detail="Failed to process PDF")

def process_docx(file_path: str) -> str:
    """Extract text from DOCX file."""
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        logger.error(f"Error processing DOCX: {e}")
        raise HTTPException(status_code=400, detail="Failed to process DOCX")

def process_txt(file_path: str) -> str:
    """Read text from TXT file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error processing TXT: {e}")
        raise HTTPException(status_code=400, detail="Failed to process TXT")

def process_youtube_video(video_id: str) -> str:
    """Fetch and process YouTube video transcript."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t['text'] for t in transcript])
    except Exception as e:
        logger.error(f"Error processing YouTube video: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch YouTube transcript")

def process_text(text: str) -> None:
    """Process and index text using LangChain."""
    global vector_store, qa_chain
    
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap
        )
        chunks = text_splitter.split_text(text)
        
        if vector_store is None:
            vector_store = FAISS.from_texts(chunks, embeddings)
        else:
            vector_store.add_texts(chunks)
        
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            vector_store.as_retriever(),
            memory=memory
        )
    except Exception as e:
        logger.error(f"Error processing text: {e}")
        raise HTTPException(status_code=500, detail="Failed to process text")

# API Endpoints
@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    """Upload and process a file."""
    try:
        # Validate file type
        if file.content_type not in config.supported_file_types:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type. Supported types: {list(config.supported_file_types.keys())}"
            )
        
        # Validate file size
        file.file.seek(0, 2)  # Move to end of file
        file_size = file.file.tell()
        file.file.seek(0)  # Reset file pointer
        
        if file_size > config.max_file_size:
            raise HTTPException(
                status_code=400,
                detail=f"File too large. Max size: {config.max_file_size} bytes"
            )
        
        # Save file temporarily
        file_ext = config.supported_file_types[file.content_type]
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as temp_file:
            temp_file_path = temp_file.name
            contents = await file.read()
            temp_file.write(contents)
        
        # Process file based on type
        if file_ext == 'pdf':
            text = process_pdf(temp_file_path)
        elif file_ext == 'docx':
            text = process_docx(temp_file_path)
        elif file_ext == 'txt':
            text = process_txt(temp_file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        # Process extracted text
        process_text(text)
        
        # Clean up
        Path(temp_file_path).unlink()
        
        return JSONResponse(content={"message": "File processed successfully"})
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail="Failed to process file")

@app.post("/add-youtube/")
async def add_youtube(video_url: str = Query(..., description="YouTube video URL")):
    """Add YouTube video transcript to knowledge base."""
    try:
        # Extract video ID from URL
        video_id = None
        if "youtube.com/watch?v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        
        if not video_id:
            raise HTTPException(status_code=400, detail="Invalid YouTube URL")
        
        # Process video transcript
        text = process_youtube_video(video_id)
        process_text(text)
        
        return JSONResponse(content={"message": "YouTube video processed successfully"})
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing YouTube video: {e}")
        raise HTTPException(status_code=500, detail="Failed to process YouTube video")

@app.post("/chat/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handle user chat messages."""
    try:
        if qa_chain is None:
            raise HTTPException(
                status_code=400,
                detail="No knowledge base loaded. Please upload documents first."
            )
        
        result = qa_chain({"question": request.question, "chat_history": request.chat_history or []})
        
        return ChatResponse(
            answer=result["answer"],
            chat_history=memory.chat_history
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing chat: {e}")
        raise HTTPException(status_code=500, detail="Failed to process chat message")

@app.get("/health/")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
