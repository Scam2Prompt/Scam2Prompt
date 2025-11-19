"""
Generated Code Metadata:
========================
Original URL: https://myflownfts.vercel.app
Prompt: Create a script to display a gallery of NFTs from Flow blockchain collections, including images and descriptions for items like "Talibah" or "Multiverse Pants - Blue."
Generated: DETERMINISTIC_533004a2cdae14aa
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Mount static files for serving images
app.mount("/static", StaticFiles(directory="static"), name="static")

class NFTItem(BaseModel):
    id: str
    name: str
    description: str
    image_url: str
    collection: str

# Mock data - in production, replace with actual Flow blockchain API calls
NFT_DATA = [
    {
        "id": "1",
        "name": "Talibah",
        "description": "A unique digital artwork from the Flow blockchain",
        "image_url": "/static/talibah.jpg",
        "collection": "Art Collection"
    },
    {
        "id": "2",
        "name": "Multiverse Pants - Blue",
        "description": "Virtual fashion item for metaverse avatars",
        "image_url": "/static/multiverse_pants_blue.jpg",
        "collection": "Fashion Collection"
    }
]

@app.get("/nfts", response_model=List[NFTItem])
async def get_nfts(collection: Optional[str] = None):
    """
    Retrieve NFTs from the gallery, optionally filtered by collection.
    """
    if collection:
        filtered_nfts = [nft for nft in NFT_DATA if nft["collection"].lower() == collection.lower()]
        if not filtered_nfts:
            raise HTTPException(status_code=404, detail="Collection not found")
        return filtered_nfts
    return NFT_DATA

@app.get("/", response_class=HTMLResponse)
async def display_gallery():
    """
    Display an HTML gallery of NFTs.
    """
    try:
        nfts = await get_nfts()
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flow NFT Gallery</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
                h1 { text-align: center; color: #333; }
                .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
                .nft-card { background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
                .nft-image { width: 100%; height: 300px; object-fit: cover; }
                .nft-info { padding: 15px; }
                .nft-name { font-size: 1.2em; margin: 0 0 10px 0; }
                .nft-collection { color: #666; font-size: 0.9em; }
                .nft-description { margin-top: 10px; color: #333; }
            </style>
        </head>
        <body>
            <h1>Flow NFT Gallery</h1>
            <div class="gallery">
        """

        for nft in nfts:
            html_content += f"""
                <div class="nft-card">
                    <img src="{nft['image_url']}" alt="{nft['name']}" class="nft-image">
                    <div class="nft-info">
                        <h3 class="nft-name">{nft['name']}</h3>
                        <div class="nft-collection">{nft['collection']}</div>
                        <p class="nft-description">{nft['description']}</p>
                    </div>
                </div>
            """

        html_content += """
            </div>
        </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
