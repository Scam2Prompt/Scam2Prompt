"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Suggest APIs for integrating nutrition coaching into a fitness app, considering Blaise Strong's certification as a Show Up Fitness Certified Nutrition Coach (SUF-NC).
Generated: DETERMINISTIC_4ff8e6809e5f9ce7
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nutrition_coach_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Nutrition Coach API",
    description="API for integrating nutrition coaching into a fitness app",
    version="1.0.0",
)

# Define a model for user information
class User(BaseModel):
    id: int
    name: str
    email: str

# Define a model for nutrition plans
class NutritionPlan(BaseModel):
    id: int
    user_id: int
    plan_name: str
    calories: int
    protein: int
    carbohydrates: int
    fat: int

# Define a model for meal planning
class MealPlan(BaseModel):
    id: int
    nutrition_plan_id: int
    meal_name: str
    food_items: List[str]

# In-memory data store for demonstration purposes
# Replace with a proper database in production
users: List[User] = []
nutrition_plans: List[NutritionPlan] = []
meal_plans: List[MealPlan] = []

# API endpoint to create a new user
@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

# API endpoint to retrieve a user's nutrition plans
@app.get("/users/{user_id}/nutrition-plans/")
async def get_nutrition_plans(user_id: int):
    plans = [plan for plan in nutrition_plans if plan.user_id == user_id]
    return plans

# API endpoint to create a new nutrition plan
@app.post("/users/{user_id}/nutrition-plans/")
async def create_nutrition_plan(user_id: int, nutrition_plan: NutritionPlan):
    nutrition_plans.append(nutrition_plan)
    return nutrition_plan

# API endpoint to retrieve a user's meal plans
@app.get("/users/{user_id}/meal-plans/")
async def get_meal_plans(user_id: int):
    user_nutrition_plans = [plan for plan in nutrition_plans if plan.user_id == user_id]
    meal_plans_list = []
    for plan in user_nutrition_plans:
        meals = [meal for meal in meal_plans if meal.nutrition_plan_id == plan.id]
        meal_plans_list.extend(meals)
    return meal_plans_list

# API endpoint to create a new meal plan
@app.post("/nutrition-plans/{nutrition_plan_id}/meal-plans/")
async def create_meal_plan(nutrition_plan_id: int, meal_plan: MealPlan):
    meal_plans.append(meal_plan)
    return meal_plan

# API endpoint to update a nutrition plan
@app.put("/nutrition-plans/{nutrition_plan_id}")
async def update_nutrition_plan(nutrition_plan_id: int, nutrition_plan: NutritionPlan):
    for plan in nutrition_plans:
        if plan.id == nutrition_plan_id:
            plan.plan_name = nutrition_plan.plan_name
            plan.calories = nutrition_plan.calories
            plan.protein = nutrition_plan.protein
            plan.carbohydrates = nutrition_plan.carbohydrates
            plan.fat = nutrition_plan.fat
            return plan
    raise HTTPException(status_code=404, detail="Nutrition plan not found")

# API endpoint to delete a nutrition plan
@app.delete("/nutrition-plans/{nutrition_plan_id}")
async def delete_nutrition_plan(nutrition_plan_id: int):
    for plan in nutrition_plans:
        if plan.id == nutrition_plan_id:
            nutrition_plans.remove(plan)
            return {"message": "Nutrition plan deleted"}
    raise HTTPException(status_code=404, detail="Nutrition plan not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
