"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: Can you provide code examples for improving time to market in web development as suggested by BigWaveInfotech?
Generated: DETERMINISTIC_54c8e22d34033d82
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Example 1: Automated Testing with pytest
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Example 2: CI/CD Pipeline with GitHub Actions (save as .github/workflows/ci.yml)
"""
name: CI Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    - name: Run tests
      run: |
        pytest
"""

# Example 3: Component-based UI Development with React
"""
import React from 'react';

const Button = ({ onClick, children }) => (
  <button 
    onClick={onClick}
    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
  >
    {children}
  </button>
);

const Card = ({ title, content }) => (
  <div className="max-w-sm rounded overflow-hidden shadow-lg p-4 m-2">
    <h2 className="font-bold text-xl mb-2">{title}</h2>
    <p className="text-gray-700 text-base">{content}</p>
  </div>
);

export { Button, Card };
"""

# Example 4: API Mocking for Parallel Development
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
async def get_products():
    # Mock data while backend is being developed
    return [
        {"id": 1, "name": "Product A", "price": 9.99},
        {"id": 2, "name": "Product B", "price": 19.99}
    ]
"""

# Example 5: Feature Flags for Gradual Rollout
"""
from flagsmith import Flagsmith

flagsmith = Flagsmith(environment_key="YOUR_ENV_KEY")

def should_enable_new_feature(user_id):
    feature = flagsmith.get_flags().get_feature("new_feature")
    return feature.enabled and feature.value == "on"

# Usage
if should_enable_new_feature(current_user.id):
    show_new_feature()
else:
    show_old_feature()
"""

# Example 6: Automated Deployment Script
"""
#!/bin/bash

# Build and deploy script
set -e  # Exit on error

echo "Building application..."
npm run build

echo "Running tests..."
npm test

echo "Deploying to production..."
rsync -avz --delete dist/ user@production-server:/var/www/app/

echo "Deployment complete!"
"""

# Example 7: Microservices Architecture with Docker
"""
# docker-compose.yml
version: '3.8'

services:
  web:
    build: ./web
    ports:
      - "5000:5000"
    depends_on:
      - api
  
  api:
    build: ./api
    ports:
      - "8000:8000"
  
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""

# Example 8: Performance Optimization with Caching
"""
from fastapi import FastAPI, Request, Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@app.get("/expensive-operation")
@cache(expire=60)  # Cache for 60 seconds
async def expensive_operation():
    # Simulate expensive computation
    import time
    time.sleep(2)
    return {"result": "data"}
"""
```
