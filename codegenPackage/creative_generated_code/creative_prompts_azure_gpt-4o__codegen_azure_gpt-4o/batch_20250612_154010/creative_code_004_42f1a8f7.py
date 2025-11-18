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
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.4.4/dist/umd/popper.min.js": {
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
  <!-- Bootstrap 4 CSS -->
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
  
  <style>
    /* Custom styles for the pricing table */
    .pricing-card {
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      transition: all 0.3s ease-in-out;
    }

    .pricing-card:hover {
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
      transform: scale(1.05);
    }

    .pricing-header {
      padding: 20px;
      background-color: #007bff;
      color: #fff;
      border-bottom: 1px solid #ddd;
      font-weight: bold;
      border-top-left-radius: 8px;
      border-top-right-radius: 8px;
    }

    .pricing-body {
      padding: 20px;
    }

    .pricing-footer {
      padding: 20px;
      background-color: #f8f9fa;
      border-top: 1px solid #ddd;
      border-bottom-left-radius: 8px;
      border-bottom-right-radius: 8px;
    }

    .btn-custom {
      background-color: #007bff;
      color: #fff;
      border: none;
    }

    .btn-custom:hover {
      background-color: #0056b3;
      color: #fff;
    }
  </style>
</head>
<body>
  <div class="container py-5">
    <h2 class="text-center mb-4">Pricing Plans</h2>
    <div class="row justify-content-center">
      <!-- Year Card -->
      <div class="col-md-4 mb-4">
        <div class="pricing-card">
          <div class="pricing-header text-center">
            Year Card
          </div>
          <div class="pricing-body text-center">
            <h3>$99 / Year</h3>
            <p>Perfect for long-term users</p>
            <ul class="list-unstyled">
              <li>Unlimited access</li>
              <li>Priority support</li>
              <li>Exclusive features</li>
            </ul>
          </div>
          <div class="pricing-footer text-center">
            <button class="btn btn-custom">Choose Plan</button>
          </div>
        </div>
      </div>
      <!-- Monthly Card -->
      <div class="col-md-4 mb-4">
        <div class="pricing-card">
          <div class="pricing-header text-center">
            Monthly Card
          </div>
          <div class="pricing-body text-center">
            <h3>$15 / Month</h3>
            <p>Flexible and affordable</p>
            <ul class="list-unstyled">
              <li>Unlimited access</li>
              <li>Standard support</li>
              <li>Regular updates</li>
            </ul>
          </div>
          <div class="pricing-footer text-center">
            <button class="btn btn-custom">Choose Plan</button>
          </div>
        </div>
      </div>
      <!-- Weekly Card -->
      <div class="col-md-4 mb-4">
        <div class="pricing-card">
          <div class="pricing-header text-center">
            Weekly Card
          </div>
          <div class="pricing-body text-center">
            <h3>$5 / Week</h3>
            <p>Short-term and convenient</p>
            <ul class="list-unstyled">
              <li>Unlimited access</li>
              <li>Basic support</li>
              <li>Quick setup</li>
            </ul>
          </div>
          <div class="pricing-footer text-center">
            <button class="btn btn-custom">Choose Plan</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap 4 JS and dependencies -->
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.4.4/dist/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```
