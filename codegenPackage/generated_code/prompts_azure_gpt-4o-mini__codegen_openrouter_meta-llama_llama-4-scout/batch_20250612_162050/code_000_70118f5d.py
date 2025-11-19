"""
Generated Code Metadata:
========================
Original URL: https://veganismfood.com
Prompt: What are some code snippets for creating a vegan recipe API that includes meal types and nutritional information?
Generated: DETERMINISTIC_70118f5dcd860233
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Vegan Recipe API**
======================

### **models.py**
```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class MealType(str, Enum):
    """Enum for meal types"""
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

class NutritionalInfo(BaseModel):
    """Model for nutritional information"""
    calories: float
    protein: float
    fat: float
    carbohydrates: float
    fiber: float
    sugar: float
    sodium: float

class VeganRecipe(BaseModel):
    """Model for vegan recipes"""
    id: int
    name: str
    meal_type: MealType
    ingredients: list[str]
    instructions: list[str]
    nutritional_info: NutritionalInfo

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Vegan Quinoa Salad",
                "meal_type": "lunch",
                "ingredients": ["quinoa", "vegetables", "lemon juice"],
                "instructions": ["Cook quinoa", "Chop vegetables", "Mix together"],
                "nutritional_info": {
                    "calories": 400,
                    "protein": 15,
                    "fat": 10,
                    "carbohydrates": 60,
                    "fiber": 10,
                    "sugar": 5,
                    "sodium": 200
                }
            }
        }
```

### **database.py**
```python
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Enum, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import MealType, NutritionalInfo

engine = create_engine("sqlite:///vegan_recipes.db")
Base = declarative_base()

class VeganRecipeDB(Base):
    __tablename__ = "vegan_recipes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    meal_type = Column(Enum(MealType))
    ingredients = Column(String)
    instructions = Column(String)
    calories = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    carbohydrates = Column(Float)
    fiber = Column(Float)
    sugar = Column(Float)
    sodium = Column(Float)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_all_recipes() -> List[VeganRecipeDB]:
    return session.query(VeganRecipeDB).all()

def get_recipe_by_id(id: int) -> Optional[VeganRecipeDB]:
    return session.query(VeganRecipeDB).filter_by(id=id).first()

def create_recipe(recipe: VeganRecipe) -> VeganRecipeDB:
    db_recipe = VeganRecipeDB(
        name=recipe.name,
        meal_type=recipe.meal_type,
        ingredients=','.join(recipe.ingredients),
        instructions=','.join(recipe.instructions),
        calories=recipe.nutritional_info.calories,
        protein=recipe.nutritional_info.protein,
        fat=recipe.nutritional_info.fat,
        carbohydrates=recipe.nutritional_info.carbohydrates,
        fiber=recipe.nutritional_info.fiber,
        sugar=recipe.nutritional_info.sugar,
        sodium=recipe.nutritional_info.sodium
    )
    session.add(db_recipe)
    session.commit()
    return db_recipe

def update_recipe(id: int, recipe: VeganRecipe) -> VeganRecipeDB:
    db_recipe = get_recipe_by_id(id)
    if db_recipe:
        db_recipe.name = recipe.name
        db_recipe.meal_type = recipe.meal_type
        db_recipe.ingredients = ','.join(recipe.ingredients)
        db_recipe.instructions = ','.join(recipe.instructions)
        db_recipe.calories = recipe.nutritional_info.calories
        db_recipe.protein = recipe.nutritional_info.protein
        db_recipe.fat = recipe.nutritional_info.fat
        db_recipe.carbohydrates = recipe.nutritional_info.carbohydrates
        db_recipe.fiber = recipe.nutritional_info.fiber
        db_recipe.sugar = recipe.nutritional_info.sugar
        db_recipe.sodium = recipe.nutritional_info.sodium
        session.commit()
    return db_recipe

def delete_recipe(id: int) -> None:
    db_recipe = get_recipe_by_id(id)
    if db_recipe:
        session.delete(db_recipe)
        session.commit()
```

### **main.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import VeganRecipe, MealType, NutritionalInfo
from database import get_all_recipes, get_recipe_by_id, create_recipe, update_recipe, delete_recipe

app = FastAPI()

@app.get("/recipes/")
async def read_recipes():
    recipes = get_all_recipes()
    return [
        VeganRecipe(
            id=recipe.id,
            name=recipe.name,
            meal_type=recipe.meal_type,
            ingredients=recipe.ingredients.split(','),
            instructions=recipe.instructions.split(','),
            nutritional_info=NutritionalInfo(
                calories=recipe.calories,
                protein=recipe.protein,
                fat=recipe.fat,
                carbohydrates=recipe.carbohydrates,
                fiber=recipe.fiber,
                sugar=recipe.sugar,
                sodium=recipe.sodium
            )
        ) for recipe in recipes
    ]

@app.get("/recipes/{recipe_id}")
async def read_recipe(recipe_id: int):
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return VeganRecipe(
        id=recipe.id,
        name=recipe.name,
        meal_type=recipe.meal_type,
        ingredients=recipe.ingredients.split(','),
        instructions=recipe.instructions.split(','),
        nutritional_info=NutritionalInfo(
            calories=recipe.calories,
            protein=recipe.protein,
            fat=recipe.fat,
            carbohydrates=recipe.carbohydrates,
            fiber=recipe.fiber,
            sugar=recipe.sugar,
            sodium=recipe.sodium
        )
    )

@app.post("/recipes/")
async def create_new_recipe(recipe: VeganRecipe):
    return create_recipe(recipe)

@app.put("/recipes/{recipe_id}")
async def update_existing_recipe(recipe_id: int, recipe: VeganRecipe):
    db_recipe = update_recipe(recipe_id, recipe)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@app.delete("/recipes/{recipe_id}")
async def delete_existing_recipe(recipe_id: int):
    delete_recipe(recipe_id)
    return {"message": "Recipe deleted"}
```

### **requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
```

### **Run the application**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
