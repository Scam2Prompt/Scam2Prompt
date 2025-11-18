"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Recommend a library or API for managing tool inventories that can handle categories like "aparelho," "utensílio," and "dispositivo," as mentioned on the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_48b8a006c682d08f
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tool Inventory Management System

This script provides an implementation for managing tool inventories with categories such as "aparelho," "utensílio,"
and "dispositivo." It uses Flask (a Python web framework) to expose a REST API for managing tools and categories.
SQLite is used as the database backend for simplicity.

To run this code:
1. Install dependencies: `pip install flask sqlalchemy`
2. Run the script: `python tool_inventory.py`
"""

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URL = "sqlite:///tool_inventory.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Database models
class Category(Base):
    """Model for tool categories."""
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    tools = relationship("Tool", back_populates="category")

class Tool(Base):
    """Model for tools within categories."""
    __tablename__ = "tools"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="tools")

# Create tables
Base.metadata.create_all(engine)

# Set up the database session
Session = sessionmaker(bind=engine)
session = Session()

# Error handling helper function
def handle_error(message, status_code=400):
    """Return an error response in JSON format."""
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

# API Routes
@app.route("/categories", methods=["GET", "POST"])
def manage_categories():
    """
    GET: Retrieve all categories.
    POST: Add a new category.
    """
    if request.method == "GET":
        categories = session.query(Category).all()
        return jsonify([{"id": c.id, "name": c.name} for c in categories])
    elif request.method == "POST":
        data = request.json
        if "name" not in data:
            return handle_error("Category name is required.")
        new_category = Category(name=data["name"])
        try:
            session.add(new_category)
            session.commit()
            return jsonify({"id": new_category.id, "name": new_category.name}), 201
        except Exception as e:
            session.rollback()
            return handle_error(str(e), 500)

@app.route("/tools", methods=["GET", "POST"])
def manage_tools():
    """
    GET: Retrieve all tools.
    POST: Add a new tool.
    """
    if request.method == "GET":
        tools = session.query(Tool).all()
        return jsonify([{
            "id": t.id,
            "name": t.name,
            "description": t.description,
            "category_id": t.category_id
        } for t in tools])
    elif request.method == "POST":
        data = request.json
        if "name" not in data or "category_id" not in data:
            return handle_error("Tool name and category ID are required.")
        new_tool = Tool(
            name=data["name"],
            description=data.get("description", ""),
            category_id=data["category_id"]
        )
        try:
            session.add(new_tool)
            session.commit()
            return jsonify({
                "id": new_tool.id,
                "name": new_tool.name,
                "description": new_tool.description,
                "category_id": new_tool.category_id
            }), 201
        except Exception as e:
            session.rollback()
            return handle_error(str(e), 500)

@app.route("/categories/<int:category_id>/tools", methods=["GET"])
def get_tools_by_category(category_id):
    """
    Retrieve all tools for a specific category.
    """
    tools = session.query(Tool).filter(Tool.category_id == category_id).all()
    if not tools:
        return handle_error("No tools found for the given category.", 404)
    return jsonify([{
        "id": t.id,
        "name": t.name,
        "description": t.description
    } for t in tools])

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
