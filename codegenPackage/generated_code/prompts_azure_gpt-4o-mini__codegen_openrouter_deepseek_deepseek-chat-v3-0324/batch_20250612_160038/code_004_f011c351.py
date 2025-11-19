"""
Generated Code Metadata:
========================
Original URL: https://sei.land
Prompt: How can I integrate a privacy policy generator into my website, taking cues from sei.land's approach?
Generated: DETERMINISTIC_f011c35197caa10f
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# privacy_policy_generator.py
import json
from datetime import datetime
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Privacy Policy Generator")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class PolicyData(BaseModel):
    website_name: str
    website_url: str
    company_name: str
    company_address: str
    contact_email: str
    data_collected: list[str]
    purpose_of_data: list[str]
    third_parties: list[str]
    cookies_used: bool
    user_rights: list[str]
    effective_date: Optional[str] = None

def generate_policy_text(data: PolicyData) -> str:
    """Generate privacy policy text based on provided data."""
    effective_date = data.effective_date or datetime.now().strftime("%B %d, %Y")
    
    policy_template = f"""
    Privacy Policy for {data.website_name}

    Last Updated: {effective_date}

    1. Introduction
    Welcome to {data.website_name} ("we", "our", "us"). We are committed to protecting your privacy. 
    This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website {data.website_url}.

    2. Information We Collect
    We may collect the following information:
    {', '.join(data.data_collected)}.

    3. How We Use Your Information
    We use the information we collect for the following purposes:
    {'; '.join(data.purpose_of_data)}.

    4. Sharing Your Information
    We may share your information with:
    {', '.join(data.third_parties) if data.third_parties else 'No third parties'}.

    5. Cookies
    {"We use cookies and similar tracking technologies to track activity on our website." if data.cookies_used else "We do not use cookies or similar tracking technologies."}

    6. Your Rights
    You have certain rights regarding your personal information:
    {'; '.join(data.user_rights)}.

    7. Contact Us
    If you have questions about this Privacy Policy, contact us at:
    {data.company_name}
    {data.company_address}
    Email: {data.contact_email}
    """
    return policy_template.strip()

@app.get("/", response_class=HTMLResponse)
async def get_generator_form(request: Request):
    """Render the privacy policy generator form."""
    return templates.TemplateResponse("generator_form.html", {"request": request})

@app.post("/generate", response_class=JSONResponse)
async def generate_policy(policy_data: PolicyData):
    """Generate and return privacy policy based on form data."""
    try:
        policy_text = generate_policy_text(policy_data)
        return {
            "status": "success",
            "policy": policy_text,
            "download_link": f"/download/{datetime.now().timestamp()}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{timestamp}", response_class=HTMLResponse)
async def download_policy(timestamp: str, request: Request):
    """Download the generated policy as a text file."""
    try:
        # In a real implementation, you would fetch the generated policy from storage
        # based on the timestamp. Here we just return a sample.
        sample_policy = "Sample privacy policy text"
        return HTMLResponse(
            content=sample_policy,
            headers={
                "Content-Disposition": f"attachment; filename=privacy_policy_{timestamp}.txt"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```html
<!-- templates/generator_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy Generator</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <div class="container">
        <h1>Privacy Policy Generator</h1>
        <form id="policyForm">
            <div class="form-group">
                <label for="websiteName">Website Name:</label>
                <input type="text" id="websiteName" name="website_name" required>
            </div>
            
            <div class="form-group">
                <label for="websiteUrl">Website URL:</label>
                <input type="url" id="websiteUrl" name="website_url" required>
            </div>
            
            <div class="form-group">
                <label for="companyName">Company Name:</label>
                <input type="text" id="companyName" name="company_name" required>
            </div>
            
            <div class="form-group">
                <label for="companyAddress">Company Address:</label>
                <textarea id="companyAddress" name="company_address" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="contactEmail">Contact Email:</label>
                <input type="email" id="contactEmail" name="contact_email" required>
            </div>
            
            <div class="form-group">
                <label>Data Collected (comma separated):</label>
                <textarea id="dataCollected" name="data_collected" required></textarea>
            </div>
            
            <div class="form-group">
                <label>Purpose of Data (comma separated):</label>
                <textarea id="purposeOfData" name="purpose_of_data" required></textarea>
            </div>
            
            <div class="form-group">
                <label>Third Parties (comma separated):</label>
                <textarea id="thirdParties" name="third_parties"></textarea>
            </div>
            
            <div class="form-group">
                <label>
                    <input type="checkbox" id="cookiesUsed" name="cookies_used">
                    Use Cookies?
                </label>
            </div>
            
            <div class="form-group">
                <label>User Rights (comma separated):</label>
                <textarea id="userRights" name="user_rights" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="effectiveDate">Effective Date (optional):</label>
                <input type="date" id="effectiveDate" name="effective_date">
            </div>
            
            <button type="submit">Generate Policy</button>
        </form>
        
        <div id="result" class="hidden">
            <h2>Your Privacy Policy</h2>
            <pre id="policyText"></pre>
            <a id="downloadLink" href="#" class="btn">Download as Text File</a>
        </div>
    </div>
    
    <script src="/static/script.js"></script>
</body>
</html>
```

```javascript
// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('policyForm');
    const resultDiv = document.getElementById('result');
    const policyText = document.getElementById('policyText');
    const downloadLink = document.getElementById('downloadLink');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = {
            website_name: form.websiteName.value,
            website_url: form.websiteUrl.value,
            company_name: form.companyName.value,
            company_address: form.companyAddress.value,
            contact_email: form.contactEmail.value,
            data_collected: form.dataCollected.value.split(',').map(item => item.trim()),
            purpose_of_data: form.purposeOfData.value.split(',').map(item => item.trim()),
            third_parties: form.thirdParties.value ? form.thirdParties.value.split(',').map(item => item.trim()) : [],
            cookies_used: form.cookiesUsed.checked,
            user_rights: form.userRights.value.split(',').map(item => item.trim()),
            effective_date: form.effectiveDate.value || null
        };
        
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            if (!response.ok) {
                throw new Error('Failed to generate policy');
            }
            
            const data = await response.json();
            policyText.textContent = data.policy;
            downloadLink.href = data.download_link;
            resultDiv.classList.remove('hidden');
        } catch (error) {
            alert('Error generating policy: ' + error.message);
        }
    });
});
```

```css
/* static/styles.css */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin
