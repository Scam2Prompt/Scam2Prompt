"""
Generated Code Metadata:
========================
Original URL: https://www.icursor.ai
Prompt: How can I create a writing tool that allows real-time collaboration with AI assistance, similar to the features of iCursor?
Generated: DETERMINISTIC_882376b66b129893
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import os
from typing import Dict, List, Optional

import websockets
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Serve static files for the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize AI models
text_generator = pipeline("text-generation", model="gpt2")
text_completer = pipeline("text2text-generation", model="t5-small")

class DocumentUpdate(BaseModel):
    content: str
    cursor_position: int

class AISuggestionRequest(BaseModel):
    context: str
    suggestion_type: str  # "completion" or "generation"

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.document_states: Dict[str, str] = {}

    async def connect(self, websocket: WebSocket, doc_id: str):
        await websocket.accept()
        self.active_connections[doc_id] = websocket
        if doc_id not in self.document_states:
            self.document_states[doc_id] = ""

    def disconnect(self, doc_id: str):
        if doc_id in self.active_connections:
            del self.active_connections[doc_id]

    async def broadcast_update(self, doc_id: str, update: DocumentUpdate):
        if doc_id in self.active_connections:
            self.document_states[doc_id] = update.content
            await self.active_connections[doc_id].send_text(
                json.dumps({
                    "type": "update",
                    "content": update.content,
                    "cursor_position": update.cursor_position
                })
            )

    async def send_ai_suggestion(self, doc_id: str, suggestion: str):
        if doc_id in self.active_connections:
            await self.active_connections[doc_id].send_text(
                json.dumps({
                    "type": "ai_suggestion",
                    "content": suggestion
                })
            )

manager = ConnectionManager()

@app.websocket("/ws/{doc_id}")
async def websocket_endpoint(websocket: WebSocket, doc_id: str):
    await manager.connect(websocket, doc_id)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            if message["type"] == "update":
                update = DocumentUpdate(
                    content=message["content"],
                    cursor_position=message["cursor_position"]
                )
                await manager.broadcast_update(doc_id, update)
            
            elif message["type"] == "ai_request":
                request = AISuggestionRequest(
                    context=message["context"],
                    suggestion_type=message["suggestion_type"]
                )
                # Process AI request in background to not block
                asyncio.create_task(handle_ai_request(doc_id, request))
                
    except WebSocketDisconnect:
        manager.disconnect(doc_id)

async def handle_ai_request(doc_id: str, request: AISuggestionRequest):
    try:
        if request.suggestion_type == "completion":
            result = text_completer(request.context, max_length=50)
            suggestion = result[0]["generated_text"]
        else:
            result = text_generator(request.context, max_length=50)
            suggestion = result[0]["generated_text"]
        
        await manager.send_ai_suggestion(doc_id, suggestion)
    except Exception as e:
        print(f"AI processing error: {e}")

@app.get("/")
async def read_root():
    return {"message": "Collaborative Writing Tool API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```html
<!-- static/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Collaborative Writing Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        #editor {
            min-height: 300px;
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 20px;
            outline: none;
        }
        .ai-suggestion {
            background-color: #f0f7ff;
            padding: 10px;
            border-left: 3px solid #4a90e2;
            margin: 10px 0;
            cursor: pointer;
        }
        .toolbar {
            margin-bottom: 15px;
            display: flex;
            gap: 10px;
        }
        button {
            padding: 8px 12px;
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #3a7bc8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Collaborative Writing Tool</h1>
        <div class="toolbar">
            <button id="completeBtn">Get AI Completion</button>
            <button id="suggestBtn">Get AI Suggestion</button>
        </div>
        <div id="editor" contenteditable="true"></div>
        <div id="suggestions"></div>
    </div>

    <script>
        const docId = window.location.pathname.split('/').pop() || 'default-doc';
        const editor = document.getElementById('editor');
        const suggestionsDiv = document.getElementById('suggestions');
        const completeBtn = document.getElementById('completeBtn');
        const suggestBtn = document.getElementById('suggestBtn');
        
        let socket = new WebSocket(`ws://${window.location.host}/ws/${docId}`);
        let cursorPosition = 0;

        // Handle WebSocket messages
        socket.onmessage = (event) => {
            const message = JSON.parse(event.data);
            
            if (message.type === 'update') {
                if (editor.innerHTML !== message.content) {
                    editor.innerHTML = message.content;
                    setCursorPosition(message.cursor_position);
                }
            } 
            else if (message.type === 'ai_suggestion') {
                const suggestion = document.createElement('div');
                suggestion.className = 'ai-suggestion';
                suggestion.textContent = message.content;
                suggestion.onclick = () => {
                    insertSuggestion(message.content);
                };
                suggestionsDiv.appendChild(suggestion);
            }
        };

        // Send updates to server
        editor.addEventListener('input', () => {
            cursorPosition = getCursorPosition();
            const message = {
                type: 'update',
                content: editor.innerHTML,
                cursor_position: cursorPosition
            };
            socket.send(JSON.stringify(message));
        });

        // Request AI completion
        completeBtn.addEventListener('click', () => {
            const context = getTextAroundCursor(100);
            const message = {
                type: 'ai_request',
                context: context,
                suggestion_type: 'completion'
            };
            socket.send(JSON.stringify(message));
        });

        // Request AI suggestion
        suggestBtn.addEventListener('click', () => {
            const context = getTextAroundCursor(200);
            const message = {
                type: 'ai_request',
                context: context,
                suggestion_type: 'generation'
            };
            socket.send(JSON.stringify(message));
        });

        // Helper functions
        function getCursorPosition() {
            const selection = window.getSelection();
            const range = selection.getRangeAt(0);
            const preCaretRange = range.cloneRange();
            preCaretRange.selectNodeContents(editor);
            preCaretRange.setEnd(range.endContainer, range.endOffset);
            return preCaretRange.toString().length;
        }

        function setCursorPosition(position) {
            const selection = window.getSelection();
            const range = document.createRange();
            
            let charCount = 0;
            let nodeStack = [editor], node, foundStart = false, stop = false;
            
            while (!stop && (node = nodeStack.pop())) {
                if (node.nodeType === 3) {
                    const nextCharCount = charCount + node.length;
                    if (!foundStart && position >= charCount && position <= nextCharCount) {
                        range.setStart(node, position - charCount);
                        foundStart = true;
                    }
                    if (foundStart && position <= nextCharCount) {
                        range.setEnd(node, position - charCount);
                        stop = true;
                    }
                    charCount = nextCharCount;
                } else {
                    let i = node.childNodes.length;
                    while (i--) {
                        nodeStack.push(node.childNodes[i]);
