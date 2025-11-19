"""
Generated Code Metadata:
========================
Original URL: https://ton-org.vercel.app
Prompt: Design an API for accessing mirrored websites, inspired by the architecture of TON and HTTrack Website Copier.
Generated: DETERMINISTIC_021f652c11625d76
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pathlib import Path
import aiofiles
import aiohttp
import asyncio
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Website Mirroring API",
    description="API for accessing mirrored websites inspired by TON and HTTrack",
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

# Configuration
MIRROR_DIR = "mirrors"
os.makedirs(MIRROR_DIR, exist_ok=True)

class MirrorManager:
    """
    Handles website mirroring operations including download, storage, and retrieval.
    """
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    def _get_mirror_path(self, url: str) -> str:
        """Generate a filesystem-safe path for the mirrored website."""
        url_hash = hashlib.sha256(url.encode()).hexdigest()
        return os.path.join(MIRROR_DIR, url_hash)

    async def _download_resource(self, url: str, mirror_path: str) -> None:
        """Download and save a single resource from the web."""
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    os.makedirs(os.path.dirname(mirror_path), exist_ok=True)
                    async with aiofiles.open(mirror_path, 'wb') as f:
                        await f.write(content)
        except Exception as e:
            logger.error(f"Failed to download {url}: {str(e)}")

    async def _mirror_website(self, url: str, max_depth: int = 2) -> str:
        """Recursively mirror a website up to a specified depth."""
        mirror_path = self._get_mirror_path(url)
        if os.path.exists(mirror_path):
            return mirror_path

        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')

                    # Save main page
                    os.makedirs(mirror_path, exist_ok=True)
                    index_path = os.path.join(mirror_path, "index.html")
                    async with aiofiles.open(index_path, 'w', encoding='utf-8') as f:
                        await f.write(html)

                    # Find and download all linked resources
                    base_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
                    resources = set()

                    for tag in soup.find_all(['a', 'link', 'script', 'img', 'style']):
                        attr = 'href' if tag.name in ['a', 'link'] else 'src'
                        if tag.has_attr(attr):
                            resource_url = urljoin(base_url, tag[attr])
                            if urlparse(resource_url).netloc == urlparse(url).netloc:
                                resources.add(resource_url)

                    # Download resources with limited depth
                    if max_depth > 0:
                        tasks = []
                        for resource_url in resources:
                            resource_path = os.path.join(
                                mirror_path,
                                urlparse(resource_url).path.lstrip('/')
                            )
                            tasks.append(
                                self._download_resource(resource_url, resource_path)
                            )
                        await asyncio.gather(*tasks)

                    return mirror_path
        except Exception as e:
            logger.error(f"Failed to mirror {url}: {str(e)}")
            raise

    async def mirror_website(self, url: str) -> str:
        """Public method to mirror a website."""
        try:
            return await self._mirror_website(url)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to mirror website: {str(e)}"
            )

    def get_mirror(self, url: str, path: str = "") -> Optional[str]:
        """Get the path to a mirrored resource."""
        mirror_path = self._get_mirror_path(url)
        full_path = os.path.join(mirror_path, path.lstrip('/'))

        if not os.path.exists(full_path):
            return None

        if os.path.isdir(full_path):
            full_path = os.path.join(full_path, "index.html")
            if not os.path.exists(full_path):
                return None

        return full_path

# Initialize mirror manager
mirror_manager = MirrorManager()

@app.on_event("shutdown")
async def shutdown_event():
    await mirror_manager.close()

@app.post("/mirror")
async def create_mirror(url: str):
    """Endpoint to create a new website mirror."""
    try:
        mirror_path = await mirror_manager.mirror_website(url)
        return JSONResponse(
            status_code=200,
            content={"message": "Mirror created successfully", "mirror_id": os.path.basename(mirror_path)}
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )

@app.get("/mirror/{mirror_id}")
@app.get("/mirror/{mirror_id}/{path:path}")
async def get_mirrored_content(mirror_id: str, path: str = ""):
    """Endpoint to retrieve mirrored content."""
    # Reconstruct the URL (in a real system, you'd store the original URL)
    # This is a simplified version for demonstration
    mirror_path = os.path.join(MIRROR_DIR, mirror_id)
    full_path = os.path.join(mirror_path, path.lstrip('/'))

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Mirror not found")

    if os.path.isdir(full_path):
        full_path = os.path.join(full_path, "index.html")
        if not os.path.exists(full_path):
            raise HTTPException(status_code=404, detail="Index not found")

    return FileResponse(full_path)

@app.get("/mirrors")
async def list_mirrors():
    """Endpoint to list all available mirrors."""
    try:
        mirrors = []
        for entry in os.listdir(MIRROR_DIR):
            full_path = os.path.join(MIRROR_DIR, entry)
            if os.path.isdir(full_path):
                mirrors.append({
                    "id": entry,
                    "created_at": datetime.fromtimestamp(os.path.getctime(full_path)).isoformat()
                })
        return JSONResponse(status_code=200, content={"mirrors": mirrors})
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to list mirrors: {str(e)}"
        )
```
