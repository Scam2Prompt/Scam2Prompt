"""
Generated Code Metadata:
========================
Original URL: https://artstrid-app-git-mm-943-phantom-confirm-tr-c95731-mintmyne-team.vercel.app
Prompt: Generate code for a "Help Center" page with FAQ functionality for a digital art platform like Artstrid.
Generated: DETERMINISTIC_4c9fae51d7df775f
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
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
    <title>Artstrid - Help Center</title>
    <style>
        :root {
            --primary-color: #6a5acd;
            --secondary-color: #9370db;
            --text-color: #333;
            --light-gray: #f5f5f5;
            --white: #ffffff;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            color: var(--text-color);
            line-height: 1.6;
            background-color: var(--light-gray);
        }

        header {
            background-color: var(--white);
            box-shadow: var(--shadow);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: var(--primary-color);
        }

        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .help-center-header {
            text-align: center;
            margin-bottom: 2rem;
        }

        .help-center-header h1 {
            font-size: 2.5rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .search-bar {
            max-width: 600px;
            margin: 0 auto;
            position: relative;
        }

        .search-bar input {
            width: 100%;
            padding: 0.8rem 1rem;
            border: 1px solid #ddd;
            border-radius: 30px;
            font-size: 1rem;
            outline: none;
            transition: all 0.3s ease;
        }

        .search-bar input:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(106, 90, 205, 0.2);
        }

        .search-bar button {
            position: absolute;
            right: 5px;
            top: 5px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 0.5rem 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .search-bar button:hover {
            background-color: var(--secondary-color);
        }

        .faq-section {
            background-color: var(--white);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .faq-section h2 {
            color: var(--primary-color);
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }

        .faq-item {
            margin-bottom: 1rem;
            border-bottom: 1px solid #eee;
            padding-bottom: 1rem;
        }

        .faq-item:last-child {
            border-bottom: none;
        }

        .faq-question {
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            padding: 0.5rem 0;
            font-weight: 600;
        }

        .faq-question:hover {
            color: var(--primary-color);
        }

        .faq-answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            padding-left: 1rem;
        }

        .faq-answer.active {
            max-height: 500px;
            padding-top: 1rem;
        }

        .toggle-icon {
            transition: transform 0.3s ease;
        }

        .toggle-icon.active {
            transform: rotate(180deg);
        }

        .contact-section {
            background-color: var(--white);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 2rem;
            text-align: center;
        }

        .contact-section h2 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .contact-section p {
            margin-bottom: 1.5rem;
        }

        .contact-btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .contact-btn:hover {
            background-color: var(--secondary-color);
        }

        footer {
            text-align: center;
            padding: 2rem;
            background-color: var(--white);
            margin-top: 2rem;
        }

        @media (max-width: 768px) {
            .container {
                padding: 0 1rem;
            }
            
            .help-center-header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Artstrid</div>
    </header>

    <div class="container">
        <section class="help-center-header">
            <h1>Help Center</h1>
            <p>Find answers to common questions about using Artstrid</p>
            <div class="search-bar">
                <input type="text" placeholder="Search help articles..." id="searchInput">
                <button id="searchButton">Search</button>
            </div>
        </section>

        <section class="faq-section">
            <h2>Frequently Asked Questions</h2>
            
            <div class="faq-item">
                <div class="faq-question">
                    <span>How do I create an account on Artstrid?</span>
                    <svg class="toggle-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="faq-answer">
                    <p>To create an account, click on the "Sign Up" button at the top right corner of the page. You can sign up using your email address or connect with your Google or Facebook account. Follow the prompts to complete your profile.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">
                    <span>How do I upload my artwork?</span>
                    <svg class="toggle-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="faq-answer">
                    <p>After logging in, click on the "Upload" button in the navigation bar. Select the files you want to upload from your device. Add a title, description, and relevant tags to help others discover your work. Choose whether to make it public or private, then click "Publish".</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">
                    <span>What file formats does Artstrid support?</span>
                    <svg class="toggle-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="faq-answer">
                    <p>Artstrid supports JPEG, PNG, GIF, and SVG for images. For videos, we support MP4, MOV, and WEBM formats. The maximum file size is 50MB for images and 500MB for videos.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">
                    <span>How do I sell my artwork on Artstrid?</span>
                    <svg class="toggle-icon" width="16" height="16" viewBox="
