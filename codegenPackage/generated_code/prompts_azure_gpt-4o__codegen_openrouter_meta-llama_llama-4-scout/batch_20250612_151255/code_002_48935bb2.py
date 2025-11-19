"""
Generated Code Metadata:
========================
Original URL: https://staketelegramapp.com
Prompt: Create a pricing table using Bootstrap that matches the structure and features described in the Avenger template, including options for Basic, Plus, Premium, and Ultimate plans.
Generated: DETERMINISTIC_48935bb2ad0ed90f
Batch ID: 20250612_151255
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js": {
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
    <title>Pricing Table</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        .pricing-table {
            text-align: center;
        }
        .pricing-table .card {
            margin: 20px;
        }
    </style>
</head>
<body>

<div class="container pricing-table">
    <div class="row">
        <div class="col-lg-3 col-md-6">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h4>Basic</h4>
                </div>
                <div class="card-body">
                    <h1 class="price">$9.99 <span>/month</span></h1>
                    <ul>
                        <li>1 User</li>
                        <li>100MB Storage</li>
                        <li>Basic Support</li>
                    </ul>
                    <button class="btn btn-primary">Sign Up</button>
                </div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h4>Plus</h4>
                </div>
                <div class="card-body">
                    <h1 class="price">$19.99 <span>/month</span></h1>
                    <ul>
                        <li>5 Users</li>
                        <li>1GB Storage</li>
                        <li>Priority Support</li>
                    </ul>
                    <button class="btn btn-success">Sign Up</button>
                </div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6">
            <div class="card">
                <div class="card-header bg-warning text-white">
                    <h4>Premium</h4>
                </div>
                <div class="card-body">
                    <h1 class="price">$29.99 <span>/month</span></h1>
                    <ul>
                        <li>10 Users</li>
                        <li>5GB Storage</li>
                        <li>Dedicated Support</li>
                    </ul>
                    <button class="btn btn-warning">Sign Up</button>
                </div>
            </div>
        </div>
        <div class="col-lg-3 col-md-6">
            <div class="card">
                <div class="card-header bg-danger text-white">
                    <h4>Ultimate</h4>
                </div>
                <div class="card-body">
                    <h1 class="price">$49.99 <span>/month</span></h1>
                    <ul>
                        <li>Unlimited Users</li>
                        <li>Unlimited Storage</li>
                        <li>Personalized Support</li>
                    </ul>
                    <button class="btn btn-danger">Sign Up</button>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>
</html>
```
