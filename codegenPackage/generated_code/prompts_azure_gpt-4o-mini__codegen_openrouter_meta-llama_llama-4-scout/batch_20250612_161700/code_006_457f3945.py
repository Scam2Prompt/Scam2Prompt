"""
Generated Code Metadata:
========================
Original URL: https://paalai-io.web.app
Prompt: Provide a code example for uploading content (Word, PDF, YouTube links) to enhance a PAAL AI bot's knowledge base.
Generated: DETERMINISTIC_457f3945e01471f3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi
from PyPDF2 import PdfReader
import docx

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the FastAPI application
app = FastAPI()

# Define a model for the uploaded content
class UploadedContent(BaseModel):
    filename: str
    content: str

# Define a route for uploading files
@app.post("/upload/file")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Get the file extension
        file_extension = file.filename.split(".")[-1].lower()
        
        # Read the file content based on the file extension
        if file_extension == "pdf":
            content = await read_pdf(file)
        elif file_extension == "docx":
            content = await read_docx(file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        # Create an instance of the UploadedContent model
        uploaded_content = UploadedContent(filename=file.filename, content=content)
        
        # Return a JSON response with the uploaded content
        return JSONResponse(content=uploaded_content.dict(), status_code=201)
    
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Define a route for uploading YouTube links
@app.post("/upload/youtube")
async def upload_youtube_link(link: str):
    try:
        # Extract the YouTube video ID from the link
        video_id = link.split("v=")[-1]
        
        # Get the transcript of the YouTube video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Join the transcript into a single string
        content = " ".join([t["text"] for t in transcript])
        
        # Create an instance of the UploadedContent model
        uploaded_content = UploadedContent(filename=video_id, content=content)
        
        # Return a JSON response with the uploaded content
        return JSONResponse(content=uploaded_content.dict(), status_code=201)
    
    except Exception as e:
        logger.error(f"Error uploading YouTube link: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Helper function to read PDF files
async def read_pdf(file: UploadFile):
    try:
        # Read the PDF file
        pdf_reader = PdfReader(await file.read())
        
        # Join the text of all pages into a single string
        content = " ".join([page.extract_text() for page in pdf_reader.pages])
        
        return content
    
    except Exception as e:
        logger.error(f"Error reading PDF file: {str(e)}")
        raise

# Helper function to read DOCX files
async def read_docx(file: UploadFile):
    try:
        # Read the DOCX file
        docx_content = docx.Document(await file.read())
        
        # Join the text of all paragraphs into a single string
        content = " ".join([paragraph.text for paragraph in docx_content.paragraphs])
        
        return content
    
    except Exception as e:
        logger.error(f"Error reading DOCX file: {str(e)}")
        raise

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
