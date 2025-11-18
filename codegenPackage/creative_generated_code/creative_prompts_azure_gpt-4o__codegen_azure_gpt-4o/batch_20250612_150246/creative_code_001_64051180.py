"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create a code snippet using Bootstrap to design a dashboard that shows user earnings, task progress (completed, remaining, and percentage), and withdrawal options with personal charges for each method.
Generated: DETERMINISTIC_64051180956287eb
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

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <div class="container mt-5">
        <!-- Dashboard Header -->
        <div class="text-center mb-4">
            <h1>User Dashboard</h1>
        </div>

        <!-- Dashboard Content -->
        <div class="row">
            <!-- User Earnings Card -->
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-header bg-primary text-white">
                        Earnings
                    </div>
                    <div class="card-body">
                        <h5>Total Earnings:</h5>
                        <p>$5,430.00</p>
                        <h5>Pending Payments:</h5>
                        <p>$320.00</p>
                    </div>
                </div>
            </div>

            <!-- Task Progress Card -->
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-header bg-success text-white">
                        Task Progress
                    </div>
                    <div class="card-body">
                        <h6>Completed Tasks:</h6>
                        <p>45</p>
                        <h6>Remaining Tasks:</h6>
                        <p>10</p>
                        <h6>Progress Percentage:</h6>
                        <p>82%</p>
                        <!-- Progress Bar -->
                        <div class="progress">
                            <div class="progress-bar bg-success" role="progressbar" style="width: 82%" aria-valuenow="82" aria-valuemin="0" aria-valuemax="100">82%</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Withdrawal Options Card -->
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-header bg-warning text-dark">
                        Withdrawal Options
                    </div>
                    <div class="card-body">
                        <h6>Bank Transfer:</h6>
                        <p>Charge: $15</p>
                        <h6>PayPal:</h6>
                        <p>Charge: $10</p>
                        <h6>Crypto:</h6>
                        <p>Charge: $5</p>
                        <!-- Withdrawal Button -->
                        <button class="btn btn-warning">Withdraw Funds</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
```
