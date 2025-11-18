"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tylos.click
Prompt: Write HTML and CSS code for a spa website using the Energen Bootstrap 4 template, including a pricing table for treatments like face, nail, and medical therapies.
Generated: DETERMINISTIC_9ed7ea233baeaa06
Batch ID: 20250612_154010
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css": {
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
    <meta name="description" content="Spa Website">
    <meta name="author" content="Your Name">
    <title>Spa Website</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <!-- Custom CSS -->
    <style>
        /* Custom Styling for the Spa Website */

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f5f5f5;
        }

        .navbar {
            background-color: #6c757d;
        }

        .navbar-brand {
            color: #ffffff !important;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .pricing-table {
            padding: 3rem 0;
        }

        .pricing-table h2 {
            text-align: center;
            margin-bottom: 2rem;
            color: #333;
        }

        .pricing-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }

        .pricing-card:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .pricing-card .card-header {
            background-color: #6c757d;
            color: #fff;
            font-size: 1.25rem;
            text-align: center;
        }

        .pricing-card .card-body {
            text-align: center;
        }

        .pricing-card .price {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        .pricing-card ul {
            list-style: none;
            padding: 0;
            margin-bottom: 1rem;
        }

        .pricing-card ul li {
            padding: 0.5rem 0;
        }

        .btn-custom {
            background-color: #6c757d;
            color: #ffffff;
        }

        .btn-custom:hover {
            background-color: #5a6268;
            color: #ffffff;
        }

        footer {
            background-color: #6c757d;
            color: #ffffff;
            padding: 1rem 0;
            text-align: center;
        }

        footer a {
            color: #ffffff;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Energen Spa</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item"><a class="nav-link" href="#services">Services</a></li>
                    <li class="nav-item"><a class="nav-link" href="#pricing">Pricing</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Pricing Section -->
    <section id="pricing" class="pricing-table">
        <div class="container">
            <h2>Pricing Table</h2>
            <div class="row">
                <!-- Face Therapy Card -->
                <div class="col-md-4 mb-4">
                    <div class="card pricing-card">
                        <div class="card-header">Face Therapy</div>
                        <div class="card-body">
                            <p class="price">$50</p>
                            <ul>
                                <li>Deep Cleansing</li>
                                <li>Hydrating Mask</li>
                                <li>Organic Products</li>
                            </ul>
                            <a href="#" class="btn btn-custom">Book Now</a>
                        </div>
                    </div>
                </div>
                <!-- Nail Therapy Card -->
                <div class="col-md-4 mb-4">
                    <div class="card pricing-card">
                        <div class="card-header">Nail Therapy</div>
                        <div class="card-body">
                            <p class="price">$40</p>
                            <ul>
                                <li>Manicure</li>
                                <li>Pedicure</li>
                                <li>Gel Polish</li>
                            </ul>
                            <a href="#" class="btn btn-custom">Book Now</a>
                        </div>
                    </div>
                </div>
                <!-- Medical Therapy Card -->
                <div class="col-md-4 mb-4">
                    <div class="card pricing-card">
                        <div class="card-header">Medical Therapy</div>
                        <div class="card-body">
                            <p class="price">$80</p>
                            <ul>
                                <li>Physiotherapy</li>
                                <li>Massage</li>
                                <li>Pain Relief</li>
                            </ul>
                            <a href="#" class="btn btn-custom">Book Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Energen Spa | <a href="#">Privacy Policy</a></p>
        </div>
    </footer>

    <!-- Bootstrap JS and dependencies (Optional for dynamic elements) -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
```
