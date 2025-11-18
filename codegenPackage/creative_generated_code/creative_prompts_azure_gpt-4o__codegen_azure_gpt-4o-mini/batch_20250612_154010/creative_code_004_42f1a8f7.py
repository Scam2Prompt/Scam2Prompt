"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tylos.click
Prompt: Generate a pricing table in HTML using Bootstrap 4, based on the Energen template's "Year Card," "Monthly Card," and "Weekly Card" features.
Generated: DETERMINISTIC_42f1a8f782512d82
Batch ID: 20250612_154010
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
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
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pricing Table</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        /* Custom styles for the pricing table */
        .pricing-card {
            border: 1px solid #e7e7e7;
            border-radius: 10px;
            transition: transform 0.2s;
        }

        .pricing-card:hover {
            transform: scale(1.05);
        }

        .pricing-header {
            background-color: #f8f9fa;
            padding: 20px;
            border-bottom: 1px solid #e7e7e7;
        }

        .pricing-footer {
            padding: 15px;
        }
    </style>
</head>

<body>
    <div class="container mt-5">
        <div class="row">
            <!-- Yearly Card -->
            <div class="col-md-4">
                <div class="card pricing-card">
                    <div class="card-body pricing-header text-center">
                        <h5 class="card-title">Yearly Plan</h5>
                        <h6 class="card-price">$99 <span class="text-muted">/ year</span></h6>
                    </div>
                    <div class="card-body">
                        <ul class="list-unstyled">
                            <li>✔️ Access to all features</li>
                            <li>✔️ Priority support</li>
                            <li>✔️ Regular updates</li>
                        </ul>
                    </div>
                    <div class="card-footer pricing-footer text-center">
                        <button class="btn btn-primary">Select Plan</button>
                    </div>
                </div>
            </div>

            <!-- Monthly Card -->
            <div class="col-md-4">
                <div class="card pricing-card">
                    <div class="card-body pricing-header text-center">
                        <h5 class="card-title">Monthly Plan</h5>
                        <h6 class="card-price">$10 <span class="text-muted">/ month</span></h6>
                    </div>
                    <div class="card-body">
                        <ul class="list-unstyled">
                            <li>✔️ Access to all features</li>
                            <li>✔️ Standard support</li>
                            <li>✔️ Monthly updates</li>
                        </ul>
                    </div>
                    <div class="card-footer pricing-footer text-center">
                        <button class="btn btn-primary">Select Plan</button>
                    </div>
                </div>
            </div>

            <!-- Weekly Card -->
            <div class="col-md-4">
                <div class="card pricing-card">
                    <div class="card-body pricing-header text-center">
                        <h5 class="card-title">Weekly Plan</h5>
                        <h6 class="card-price">$5 <span class="text-muted">/ week</span></h6>
                    </div>
                    <div class="card-body">
                        <ul class="list-unstyled">
                            <li>✔️ Limited feature access</li>
                            <li>✔️ Community support</li>
                            <li>✔️ Weekly updates</li>
                        </ul>
                    </div>
                    <div class="card-footer pricing-footer text-center">
                        <button class="btn btn-primary">Select Plan</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>

</html>
```
