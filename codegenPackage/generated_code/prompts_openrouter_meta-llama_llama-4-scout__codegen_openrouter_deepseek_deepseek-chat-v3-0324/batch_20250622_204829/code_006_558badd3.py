"""
Generated Code Metadata:
========================
Original URL: https://jwzt-dashboard-inqubeta.pages.dev
Prompt: Create a basic AI start-up application form using HTML, CSS, and JavaScript, integrating with the InQubeta platform's API for listing and fundraising.
Generated: DETERMINISTIC_558badd35cb1f197
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Startup Application - InQubeta</title>
    <style>
        /* CSS Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            text-align: center;
            margin-bottom: 2rem;
        }

        h1 {
            color: #4a6bff;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            color: #666;
            font-size: 1.1rem;
        }

        .form-container {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #444;
        }

        input[type="text"],
        input[type="email"],
        input[type="url"],
        input[type="number"],
        textarea,
        select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input:focus,
        textarea:focus,
        select:focus {
            outline: none;
            border-color: #4a6bff;
        }

        textarea {
            min-height: 120px;
            resize: vertical;
        }

        .btn {
            background-color: #4a6bff;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 600;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #3a5bef;
        }

        .btn-block {
            display: block;
            width: 100%;
        }

        .error {
            color: #e74c3c;
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }

        .success-message {
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
            display: none;
        }

        .loading {
            display: none;
            text-align: center;
            margin: 1rem 0;
        }

        .spinner {
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            border-top: 4px solid #4a6bff;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .form-container {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Startup Application</h1>
            <p class="subtitle">Join the InQubeta platform for fundraising and listing your AI startup</p>
        </header>

        <div class="success-message" id="successMessage">
            Your application has been submitted successfully! We'll review your information and get back to you soon.
        </div>

        <div class="loading" id="loadingIndicator">
            <div class="spinner"></div>
            <p>Submitting your application...</p>
        </div>

        <div class="form-container">
            <form id="startupForm">
                <div class="form-group">
                    <label for="companyName">Company Name *</label>
                    <input type="text" id="companyName" name="companyName" required>
                    <div class="error" id="companyNameError"></div>
                </div>

                <div class="form-group">
                    <label for="founderName">Founder Name *</label>
                    <input type="text" id="founderName" name="founderName" required>
                    <div class="error" id="founderNameError"></div>
                </div>

                <div class="form-group">
                    <label for="email">Email Address *</label>
                    <input type="email" id="email" name="email" required>
                    <div class="error" id="emailError"></div>
                </div>

                <div class="form-group">
                    <label for="website">Website URL</label>
                    <input type="url" id="website" name="website">
                    <div class="error" id="websiteError"></div>
                </div>

                <div class="form-group">
                    <label for="fundingAmount">Funding Amount Needed (USD) *</label>
                    <input type="number" id="fundingAmount" name="fundingAmount" min="10000" step="1000" required>
                    <div class="error" id="fundingAmountError"></div>
                </div>

                <div class="form-group">
                    <label for="aiFocus">AI Focus Area *</label>
                    <select id="aiFocus" name="aiFocus" required>
                        <option value="">Select an area</option>
                        <option value="machine_learning">Machine Learning</option>
                        <option value="computer_vision">Computer Vision</option>
                        <option value="natural_language">Natural Language Processing</option>
                        <option value="robotics">Robotics</option>
                        <option value="healthcare">Healthcare AI</option>
                        <option value="finance">Financial AI</option>
                        <option value="other">Other</option>
                    </select>
                    <div class="error" id="aiFocusError"></div>
                </div>

                <div class="form-group">
                    <label for="description">Company Description *</label>
                    <textarea id="description" name="description" required></textarea>
                    <div class="error" id="descriptionError"></div>
                </div>

                <div class="form-group">
                    <label for="pitchDeck">Pitch Deck URL (Google Drive, Dropbox, etc.)</label>
                    <input type="url" id="pitchDeck" name="pitchDeck">
                    <div class="error" id="pitchDeckError"></div>
                </div>

                <button type="submit" class="btn btn-block">Submit Application</button>
            </form>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('startupForm');
            const loadingIndicator = document.getElementById('loadingIndicator');
            const successMessage = document.getElementById('successMessage');

            form.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                // Reset error messages
                clearErrors();
                
                // Validate form
                if (!validateForm()) {
                    return;
                }

                // Show loading indicator
                loadingIndicator.style.display = 'block';
                
                try {
                    // Prepare form data
                    const formData = {
                        companyName: document.getElementById('companyName').value,
                        founderName: document.getElementById('founderName').value,
                        email: document.getElementById('email').value,
                        website: document.getElementById('website').value || null,
                        fundingAmount: parseFloat(document.getElementById('fundingAmount').value),
                        aiFocus: document.getElementById('aiFocus').value,
                        description: document.getElementById('description').value,
                        pitchDeck: document.getElementById('pitchDeck').value || null
                    };

                    // Simulate API call to InQubeta (replace with actual API integration)
                    const response = await submitToInQubetaAPI(formData);
                    
                    if (response.success) {
                        // Show success message
                        successMessage.style.display = 'block';
                        form.reset();
                    } else {
                        // Show API error
                        showError('form', response.message || 'Submission failed. Please try again.');
                    }
                } catch (error) {
                    console.error('Error:', error);
                    showError('form', 'An error
