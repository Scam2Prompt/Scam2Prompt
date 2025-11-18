"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orlandoplasmacenters.com
Prompt: Generate code for a step-by-step plasma donation guide on a website, including interactive elements for each step outlined by Orlando Plasma Centers.
Generated: DETERMINISTIC_465a53d4dfcb6894
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Step-by-step plasma donation guide by Orlando Plasma Centers">
  <title>Plasma Donation Guide</title>
  <style>
    /* Base styling */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f8f9fa;
    }

    .header {
      text-align: center;
      background-color: #007bff;
      color: white;
      padding: 1rem;
    }

    .step-container {
      padding: 2rem;
      max-width: 800px;
      margin: auto;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .step {
      margin-bottom: 2rem;
    }

    .step-title {
      font-size: 1.25rem;
      font-weight: bold;
      margin-bottom: 0.5rem;
    }

    .step-description {
      margin-bottom: 1rem;
    }

    .step-actions {
      display: flex;
      justify-content: center;
    }

    .step-actions button {
      padding: 0.5rem 1rem;
      margin: 0 0.5rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button.active {
      background-color: #007bff;
      color: white;
    }

    button.inactive {
      background-color: #6c757d;
      color: white;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <h1>Plasma Donation Guide</h1>
    <p>Follow these simple steps to donate plasma at Orlando Plasma Centers!</p>
  </header>

  <!-- Step-by-Step Guide -->
  <main class="step-container">
    <!-- Step 1 -->
    <div class="step" id="step-1">
      <div class="step-title">Step 1: Registration</div>
      <div class="step-description">Fill out a registration form with your personal details and medical history.</div>
      <div class="step-actions">
        <button class="inactive" onclick="prevStep(1)">Previous</button>
        <button class="active" onclick="nextStep(1)">Next</button>
      </div>
    </div>

    <!-- Step 2 -->
    <div class="step" id="step-2" style="display: none;">
      <div class="step-title">Step 2: Health Screening</div>
      <div class="step-description">Undergo a health screening to ensure you meet eligibility requirements.</div>
      <div class="step-actions">
        <button class="active" onclick="prevStep(2)">Previous</button>
        <button class="active" onclick="nextStep(2)">Next</button>
      </div>
    </div>

    <!-- Step 3 -->
    <div class="step" id="step-3" style="display: none;">
      <div class="step-title">Step 3: Plasma Collection</div>
      <div class="step-description">Donate plasma through a safe and sterile process.</div>
      <div class="step-actions">
        <button class="active" onclick="prevStep(3)">Previous</button>
        <button class="active" onclick="nextStep(3)">Next</button>
      </div>
    </div>

    <!-- Step 4 -->
    <div class="step" id="step-4" style="display: none;">
      <div class="step-title">Step 4: Post-Donation Care</div>
      <div class="step-description">Receive post-donation care instructions and enjoy refreshments provided.</div>
      <div class="step-actions">
        <button class="active" onclick="prevStep(4)">Previous</button>
        <button class="inactive" onclick="nextStep(4)">Next</button>
      </div>
    </div>
  </main>

  <script>
    /**
     * Navigate to the next step.
     * @param {number} currentStep - The current step number.
     */
    function nextStep(currentStep) {
      const current = document.getElementById(`step-${currentStep}`);
      const next = document.getElementById(`step-${currentStep + 1}`);

      if (next) {
        current.style.display = 'none';
        next.style.display = 'block';
      }
    }

    /**
     * Navigate to the previous step.
     * @param {number} currentStep - The current step number.
     */
    function prevStep(currentStep) {
      const current = document.getElementById(`step-${currentStep}`);
      const prev = document.getElementById(`step-${currentStep - 1}`);

      if (prev) {
        current.style.display = 'none';
        prev.style.display = 'block';
      }
    }
  </script>
</body>
</html>
```
