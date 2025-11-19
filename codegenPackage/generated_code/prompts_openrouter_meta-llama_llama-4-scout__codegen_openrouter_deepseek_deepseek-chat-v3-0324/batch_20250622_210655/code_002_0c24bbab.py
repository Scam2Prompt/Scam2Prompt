"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Generate a sample HTML page for a hotel website, incorporating essential features like a room gallery, pricing, and contact information, inspired by Vila Vračar's website structure.
Generated: DETERMINISTIC_0c24bbab2a4f43f4
Batch ID: 20250622_210655
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1566073771259-6a85009dce3c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
    <title>Vila Vračar - Luxury Hotel Accommodation</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        /* Header styles */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c3e50;
            text-decoration: none;
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 2rem;
        }
        
        .nav-links a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #e74c3c;
        }
        
        .book-now {
            background-color: #e74c3c;
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 5px;
            font-weight: 600;
            transition: background-color 0.3s;
        }
        
        .book-now:hover {
            background-color: #c0392b;
            color: white;
        }
        
        /* Hero section */
        .hero {
            height: 80vh;
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1566073771259-6a85009dce3c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center/cover;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            padding: 0 2rem;
        }
        
        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin-bottom: 2rem;
        }
        
        /* Rooms section */
        .section-title {
            text-align: center;
            margin: 4rem 0 2rem;
            font-size: 2.5rem;
            color: #2c3e50;
        }
        
        .rooms-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 5%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .room-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .room-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }
        
        .room-img {
            height: 250px;
            width: 100%;
            object-fit: cover;
        }
        
        .room-info {
            padding: 1.5rem;
        }
        
        .room-info h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: #2c3e50;
        }
        
        .room-info p {
            margin-bottom: 1rem;
            color: #7f8c8d;
        }
        
        .room-price {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1rem;
        }
        
        .price {
            font-size: 1.3rem;
            font-weight: 700;
            color: #e74c3c;
        }
        
        /* Amenities section */
        .amenities {
            background-color: #2c3e50;
            color: white;
            padding: 4rem 5%;
            margin: 4rem 0;
        }
        
        .amenities-container {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            text-align: center;
        }
        
        .amenity-item {
            padding: 1.5rem;
        }
        
        .amenity-item i {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #e74c3c;
        }
        
        .amenity-item h3 {
            margin-bottom: 0.5rem;
        }
        
        /* Contact section */
        .contact {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 5% 4rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 3rem;
        }
        
        .contact-info h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: #2c3e50;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .contact-item i {
            margin-right: 1rem;
            color: #e74c3c;
            font-size: 1.2rem;
            width: 20px;
        }
        
        .contact-form h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: #2c3e50;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        .form-group textarea {
            height: 150px;
        }
        
        .submit-btn {
            background-color: #e74c3c;
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .submit-btn:hover {
            background-color: #c0392b;
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 4rem;
        }
        
        .social-links {
            margin-bottom: 1rem;
        }
        
        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.5rem;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: #e74c3c;
        }
        
        .copyright {
            font-size: 0.9rem;
            color: #bdc3c7;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                padding: 1rem;
            }
            
            .nav-links {
