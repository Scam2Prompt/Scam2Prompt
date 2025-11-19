"""
Generated Code Metadata:
========================
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Create a form using JavaScript for reporting bugs and feedback in an on-chain governance application, inspired by the functionality described in Optimism Agora.
Generated: DETERMINISTIC_3063f55b43985fb3
Batch ID: 20250612_145706
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
    <title>On-Chain Governance Feedback Form</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }
        input[type="text"],
        input[type="email"],
        textarea,
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }
        textarea {
            min-height: 150px;
            resize: vertical;
        }
        .required {
            color: #e74c3c;
        }
        .submit-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .submit-btn:hover {
            background-color: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
        .success-message {
            display: none;
            background-color: #2ecc71;
            color: white;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Governance Feedback & Bug Report</h1>
        
        <div id="successMessage" class="success-message">
            Thank you for your feedback! Your submission has been received.
        </div>
        
        <form id="feedbackForm">
            <div class="form-group">
                <label for="reportType">Type of Report <span class="required">*</span></label>
                <select id="reportType" name="reportType" required>
                    <option value="">-- Select an option --</option>
                    <option value="bug">Bug Report</option>
                    <option value="feedback">Feature Request</option>
                    <option value="governance">Governance Proposal Issue</option>
                    <option value="other">Other</option>
                </select>
                <div id="reportTypeError" class="error">Please select a report type</div>
            </div>
            
            <div class="form-group">
                <label for="title">Title <span class="required">*</span></label>
                <input type="text" id="title" name="title" required placeholder="Brief description of your report">
                <div id="titleError" class="error">Please enter a title</div>
            </div>
            
            <div class="form-group">
                <label for="description">Description <span class="required">*</span></label>
                <textarea id="description" name="description" required placeholder="Please provide detailed information about the issue or feedback"></textarea>
                <div id="descriptionError" class="error">Please enter a description</div>
            </div>
            
            <div class="form-group">
                <label for="proposalId">Proposal ID (if applicable)</label>
                <input type="text" id="proposalId" name="proposalId" placeholder="Enter the proposal ID this relates to">
            </div>
            
            <div class="form-group">
                <label for="walletAddress">Wallet Address (optional)</label>
                <input type="text" id="walletAddress" name="walletAddress" placeholder="Your wallet address if you'd like us to follow up">
            </div>
            
            <div class="form-group">
                <label for="email">Email (optional)</label>
                <input type="email" id="email" name="email" placeholder="Your email if you'd like us to follow up">
                <div id="emailError" class="error">Please enter a valid email address</div>
            </div>
            
            <div class="form-group">
                <label for="severity">Severity (for bug reports)</label>
                <select id="severity" name="severity">
                    <option value="">-- Select severity --</option>
                    <option value="low">Low - Minor issue</option>
                    <option value="medium">Medium - Significant issue</option>
                    <option value="high">High - Critical issue</option>
                </select>
            </div>
            
            <button type="submit" class="submit-btn">Submit Report</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('feedbackForm');
            const successMessage = document.getElementById('successMessage');
            
            // Form validation
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                document.querySelectorAll('.error').forEach(el => el.style.display = 'none');
                
                let isValid = true;
                
                // Validate required fields
                if (!form.reportType.value) {
                    document.getElementById('reportTypeError').style.display = 'block';
                    isValid = false;
                }
                
                if (!form.title.value.trim()) {
                    document.getElementById('titleError').style.display = 'block';
                    isValid = false;
                }
                
                if (!form.description.value.trim()) {
                    document.getElementById('descriptionError').style.display = 'block';
                    isValid = false;
                }
                
                // Validate email if provided
                if (form.email.value && !validateEmail(form.email.value)) {
                    document.getElementById('emailError').style.display = 'block';
                    isValid = false;
                }
                
                if (isValid) {
                    submitForm();
                }
            });
            
            // Email validation helper
            function validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
            
            // Form submission
            async function submitForm() {
                const formData = {
                    reportType: form.reportType.value,
                    title: form.title.value,
                    description: form.description.value,
                    proposalId: form.proposalId.value,
                    walletAddress: form.walletAddress.value,
                    email: form.email.value,
                    severity: form.severity.value,
                    timestamp: new Date().toISOString()
                };
                
                try {
                    // In a real application, you would send this data to your backend
                    // For demonstration, we'll simulate an API call
                    console.log('Submitting form data:', formData);
                    
                    // Simulate API call delay
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    
                    // Show success message
                    form.style.display = 'none';
                    successMessage.style.display = 'block';
                    
                    // Reset form after submission (optional)
                    setTimeout(() => {
                        form.reset();
                        form.style.display = 'block';
                        successMessage.style.display = 'none';
                    }, 5000);
                    
                } catch (error) {
                    console.error('Error submitting form:', error);
                    alert('There was an error submitting your form. Please try again.');
                }
            }
        });
    </script>
</body>
</html>
```
