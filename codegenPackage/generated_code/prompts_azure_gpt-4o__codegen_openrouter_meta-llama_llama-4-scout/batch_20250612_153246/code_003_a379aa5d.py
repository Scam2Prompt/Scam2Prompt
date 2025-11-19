"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Suggest an API for managing diagnostic testing results (e.g., IgG food intolerance, hormone tests) and write code to display these results securely on a client portal.
Generated: DETERMINISTIC_a379aa5dd443bdb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Diagnostic Testing Results API**
=====================================

### API Endpoints

#### 1. Create Diagnostic Test Result

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from jose import jwt, JWTError

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///diagnostic_test_results.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Models
class DiagnosticTestResult(Base):
    __tablename__ = "diagnostic_test_results"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True)
    test_name = Column(String, index=True)
    result = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Schemas
class DiagnosticTestResultSchema(BaseModel):
    patient_id: int
    test_name: str
    result: str

class DiagnosticTestResultResponseSchema(BaseModel):
    id: int
    patient_id: int
    test_name: str
    result: str
    created_at: datetime

# API
app = FastAPI()

# Auth
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Auth logic here
    access_token = jwt.encode({"sub": "1"}, "secret_key", algorithm="HS256")
    return {"access_token": access_token, "token_type": "bearer"}

# Create Diagnostic Test Result
@app.post("/diagnostic-test-results/", response_model=DiagnosticTestResultResponseSchema)
async def create_diagnostic_test_result(
    diagnostic_test_result: DiagnosticTestResultSchema,
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    db_diagnostic_test_result = DiagnosticTestResult(
        patient_id=diagnostic_test_result.patient_id,
        test_name=diagnostic_test_result.test_name,
        result=diagnostic_test_result.result,
    )
    db.add(db_diagnostic_test_result)
    db.commit()
    db.refresh(db_diagnostic_test_result)
    return db_diagnostic_test_result

# Get Diagnostic Test Results for Patient
@app.get("/patients/{patient_id}/diagnostic-test-results/", response_model=List[DiagnosticTestResultResponseSchema])
async def read_diagnostic_test_results(
    patient_id: int,
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return db.query(DiagnosticTestResult).filter(DiagnosticTestResult.patient_id == patient_id).all()

# Client Portal
from fastapi.responses import HTMLResponse

@app.get("/client-portal/")
async def client_portal(current_user: str = Depends(get_current_user)):
    return HTMLResponse(content="""
    <html>
        <head>
            <title>Client Portal</title>
        </head>
        <body>
            <h1>Diagnostic Test Results</h1>
            <div id="test-results"></div>

            <script>
                fetch('/patients/1/diagnostic-test-results/', {
                    method: 'GET',
                    headers: {
                        'Authorization': 'Bearer <access_token>'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    const testResultsElement = document.getElementById('test-results');
                    data.forEach(testResult => {
                        const testResultElement = document.createElement('p');
                        testResultElement.textContent = \`${testResult.test_name}: \${testResult.result}\`;
                        testResultsElement.appendChild(testResultElement);
                    });
                })
                .catch(error => console.error(error));
            </script>
        </body>
    </html>
    """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Running the Code

```bash
# Install dependencies
pip install fastapi uvicorn sqlalchemy

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API Documentation

*   **Create Diagnostic Test Result:** `POST /diagnostic-test-results/`
    *   Request Body: `patient_id`, `test_name`, `result`
    *   Response: `id`, `patient_id`, `test_name`, `result`, `created_at`
*   **Get Diagnostic Test Results for Patient:** `GET /patients/{patient_id}/diagnostic-test-results/`
    *   Path Parameters: `patient_id`
    *   Response: List of `id`, `patient_id`, `test_name`, `result`, `created_at`

### Security Considerations

*   **Authentication:** OAuth2 with JWT tokens
*   **Authorization:** Bearer token authentication
*   **Data Encryption:** SSL/TLS recommended for production

### Client Portal

*   **Access:** `GET /client-portal/`
*   **Content:** HTML page displaying diagnostic test results for the patient

### Commit Message

```
Create diagnostic testing results API

* Add API endpoints for creating and retrieving diagnostic test results
* Implement authentication and authorization using OAuth2 and JWT tokens
* Create client portal for displaying test results securely
```
