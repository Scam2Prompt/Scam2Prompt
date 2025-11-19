"""
Generated Code Metadata:
========================
Original URL: https://rb.itsmeplabon.xyz
Prompt: Develop a form using Bootstrap that allows users to request withdrawals by selecting a method (e.g., Mobile Recharge, Bkash, Rocket, Nogod) and entering an amount and withdrawal address, with validation for required fields.
Generated: DETERMINISTIC_daa97b884a650ab1
Batch ID: 20250612_150246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Withdrawal Request Form</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <style>
        .form-container {
            max-width: 600px;
            margin: 30px auto;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        .form-title {
            text-align: center;
            margin-bottom: 20px;
            color: #0d6efd;
        }
        .error-message {
            color: #dc3545;
            font-size: 0.875em;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form-container bg-white">
            <h2 class="form-title">Withdrawal Request</h2>
            <form id="withdrawalForm" novalidate>
                <!-- Withdrawal Method -->
                <div class="mb-3">
                    <label for="withdrawalMethod" class="form-label">Withdrawal Method *</label>
                    <select class="form-select" id="withdrawalMethod" required>
                        <option value="" selected disabled>Select a method</option>
                        <option value="Mobile Recharge">Mobile Recharge</option>
                        <option value="Bkash">Bkash</option>
                        <option value="Rocket">Rocket</option>
                        <option value="Nogod">Nogod</option>
                    </select>
                    <div class="error-message" id="methodError">Please select a withdrawal method</div>
                </div>

                <!-- Amount -->
                <div class="mb-3">
                    <label for="amount" class="form-label">Amount *</label>
                    <input type="number" class="form-control" id="amount" placeholder="Enter amount" min="1" required>
                    <div class="error-message" id="amountError">Please enter a valid amount (minimum 1)</div>
                </div>

                <!-- Withdrawal Address -->
                <div class="mb-3">
                    <label for="address" class="form-label">Withdrawal Address *</label>
                    <input type="text" class="form-control" id="address" placeholder="Enter withdrawal address" required>
                    <div class="error-message" id="addressError">Please enter a withdrawal address</div>
                </div>

                <!-- Submit Button -->
                <div class="d-grid">
                    <button type="submit" class="btn btn-primary">Request Withdrawal</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Custom JavaScript for form validation -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('withdrawalForm');
            
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                event.stopPropagation();
                
                // Reset error messages
                document.querySelectorAll('.error-message').forEach(el => el.style.display = 'none');
                
                // Validate form
                let isValid = true;
                
                // Validate withdrawal method
                const method = document.getElementById('withdrawalMethod');
                if (!method.value) {
                    document.getElementById('methodError').style.display = 'block';
                    isValid = false;
                }
                
                // Validate amount
                const amount = document.getElementById('amount');
                if (!amount.value || amount.value < 1) {
                    document.getElementById('amountError').style.display = 'block';
                    isValid = false;
                }
                
                // Validate address
                const address = document.getElementById('address');
                if (!address.value.trim()) {
                    document.getElementById('addressError').style.display = 'block';
                    isValid = false;
                }
                
                // If form is valid, submit it
                if (isValid) {
                    // Here you would typically send the data to the server
                    alert('Withdrawal request submitted successfully!');
                    form.reset();
                }
            });
            
            // Add real-time validation for better UX
            document.getElementById('withdrawalMethod').addEventListener('change', function() {
                if (this.value) {
                    document.getElementById('methodError').style.display = 'none';
                }
            });
            
            document.getElementById('amount').addEventListener('input', function() {
                if (this.value && this.value >= 1) {
                    document.getElementById('amountError').style.display = 'none';
                }
            });
            
            document.getElementById('address').addEventListener('input', function() {
                if (this.value.trim()) {
                    document.getElementById('addressError').style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
```
