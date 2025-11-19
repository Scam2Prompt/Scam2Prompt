"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://booksinn.com.pk
Prompt: What are the best practices for implementing a search feature on an online bookstore like Books Inn, specifically for Urdu and Islamic books?
Generated: DETERMINISTIC_07e370cf086396d4
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that implements a search feature for an online bookstore like Books Inn, specifically for Urdu and Islamic books. The code uses FastAPI for the backend and follows best practices.

```python
from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional

# Create FastAPI instance
app = FastAPI()

# Sample data to demonstrate search functionality
books = [
    {"id": 1, "title": "اسلام کے اصول", "author": "ابو الاعلیٰ مودودی", "category": "Islamic", "language": "Urdu"},
    {"id": 2, "title": "قرآن پاک", "author": "Unknown", "category": "Islamic", "language": "Urdu"},
    {"id": 3, "title": "Urdu Poetry Collection", "author": "Allama Iqbal", "category": "Urdu Literature", "language": "Urdu"},
    {"id": 4, "title": "The Sealed Nectar", "author": "Safiyur Rahman Mubarakpuri", "category": "Islamic", "language": "English"},
]

@app.get("/search", response_model=List[dict])
async def search_books(
    query: Optional[str] = Query(None, min_length=2, description="Search term"),
    category: Optional[str] = Query(None, description="Filter by category (e.g., 'Islamic', 'Urdu Literature')"),
    language: Optional[str] = Query(None, description="Filter by language (e.g., 'Urdu')")
):
    """
    Search for books in the bookstore.

    Args:
        query (str): Search term for title or author.
        category (str): Category filter (e.g., 'Islamic').
        language (str): Language filter (e.g., 'Urdu').

    Returns:
        List[dict]: List of books matching the search criteria.
    """
    try:
        # Filter books based on search query, category, and language
        search_results = [
            book for book in books
            if (query is None or query.lower() in book["title"].lower() or query.lower() in book["author"].lower())
            and (category is None or category.lower() == book["category"].lower())
            and (language is None or language.lower() == book["language"].lower())
        ]
        
        # Check if results are found
        if not search_results:
            raise HTTPException(status_code=404, detail="No books found matching the search criteria.")

        return search_results

    except Exception as e:
        # Log error in production and provide a generic message
        raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again later.") from e

# Run using: uvicorn filename:app --reload
```

This code demonstrates the construction of a search API endpoint using FastAPI, handling various filters and error cases, and adhering to best practices. You can save this script, install FastAPI and Uvicorn, and run the application for testing.
