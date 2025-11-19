"""
Generated Code Metadata:
========================
Original URL: https://alwan.om
Prompt: Write code to implement a wishlist feature for an e-commerce platform, allowing users to create, find, manage, and view lists, similar to the functionality described on Alwan's website.
Generated: DETERMINISTIC_b15bda63fb7fad9b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from datetime import datetime
from uuid import uuid4
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="E-Commerce Wishlist API",
    description="API for managing user wishlists in an e-commerce platform",
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

# Mock authentication (in a real app, this would connect to an auth service)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Mock authentication function"""
    # In a real app, validate the token and return user info
    return {"user_id": "user123", "username": "testuser"}

# Database models
class WishlistItem(BaseModel):
    """Represents an item in a wishlist"""
    product_id: str = Field(..., description="Unique identifier for the product")
    name: str = Field(..., description="Name of the product")
    price: float = Field(..., description="Current price of the product")
    image_url: Optional[str] = Field(None, description="URL of the product image")
    added_at: datetime = Field(default_factory=datetime.utcnow, description="When the item was added")

class Wishlist(BaseModel):
    """Represents a user's wishlist"""
    id: str = Field(default_factory=lambda: str(uuid4()), description="Unique wishlist ID")
    user_id: str = Field(..., description="ID of the user who owns this wishlist")
    name: str = Field(..., description="Name of the wishlist")
    description: Optional[str] = Field(None, description="Optional description")
    items: List[WishlistItem] = Field(default_factory=list, description="List of items in the wishlist")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="When the wishlist was created")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update time")

# In-memory database (replace with real DB in production)
wishlists_db: Dict[str, Wishlist] = {}

# API Endpoints
@app.post("/wishlists/", response_model=Wishlist, status_code=status.HTTP_201_CREATED)
async def create_wishlist(
    name: str,
    description: Optional[str] = None,
    current_user: Dict = Depends(get_current_user)
):
    """Create a new wishlist for the current user"""
    wishlist = Wishlist(
        user_id=current_user["user_id"],
        name=name,
        description=description
    )
    wishlists_db[wishlist.id] = wishlist
    return wishlist

@app.get("/wishlists/", response_model=List[Wishlist])
async def get_user_wishlists(current_user: Dict = Depends(get_current_user)):
    """Get all wishlists for the current user"""
    return [wl for wl in wishlists_db.values() if wl.user_id == current_user["user_id"]]

@app.get("/wishlists/{wishlist_id}", response_model=Wishlist)
async def get_wishlist(
    wishlist_id: str,
    current_user: Dict = Depends(get_current_user)
):
    """Get a specific wishlist by ID"""
    if wishlist_id not in wishlists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wishlist not found"
        )
    
    wishlist = wishlists_db[wishlist_id]
    if wishlist.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this wishlist"
        )
    
    return wishlist

@app.put("/wishlists/{wishlist_id}", response_model=Wishlist)
async def update_wishlist(
    wishlist_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    current_user: Dict = Depends(get_current_user)
):
    """Update wishlist metadata (name, description)"""
    if wishlist_id not in wishlists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wishlist not found"
        )
    
    wishlist = wishlists_db[wishlist_id]
    if wishlist.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this wishlist"
        )
    
    if name is not None:
        wishlist.name = name
    if description is not None:
        wishlist.description = description
    wishlist.updated_at = datetime.utcnow()
    
    return wishlist

@app.delete("/wishlists/{wishlist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wishlist(
    wishlist_id: str,
    current_user: Dict = Depends(get_current_user)
):
    """Delete a wishlist"""
    if wishlist_id not in wishlists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wishlist not found"
        )
    
    wishlist = wishlists_db[wishlist_id]
    if wishlist.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this wishlist"
        )
    
    del wishlists_db[wishlist_id]

@app.post("/wishlists/{wishlist_id}/items", response_model=Wishlist)
async def add_item_to_wishlist(
    wishlist_id: str,
    item: WishlistItem,
    current_user: Dict = Depends(get_current_user)
):
    """Add an item to a wishlist"""
    if wishlist_id not in wishlists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wishlist not found"
        )
    
    wishlist = wishlists_db[wishlist_id]
    if wishlist.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this wishlist"
        )
    
    # Check if item already exists
    for existing_item in wishlist.items:
        if existing_item.product_id == item.product_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Item already exists in wishlist"
            )
    
    wishlist.items.append(item)
    wishlist.updated_at = datetime.utcnow()
    return wishlist

@app.delete("/wishlists/{wishlist_id}/items/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_item_from_wishlist(
    wishlist_id: str,
    product_id: str,
    current_user: Dict = Depends(get_current_user)
):
    """Remove an item from a wishlist"""
    if wishlist_id not in wishlists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wishlist not found"
        )
    
    wishlist = wishlists_db[wishlist_id]
    if wishlist.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this wishlist"
        )
    
    # Find and remove the item
    for i, item in enumerate(wishlist.items):
        if item.product_id == product_id:
            wishlist.items.pop(i)
            wishlist.updated_at = datetime.utcnow()
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found in wishlist"
    )
```
