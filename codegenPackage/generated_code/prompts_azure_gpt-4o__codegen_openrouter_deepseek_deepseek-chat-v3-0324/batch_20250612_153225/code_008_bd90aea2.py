"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write code to generate a dynamic FAQ section for a website, including questions about polygraph test accuracy, procedure, and use cases, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_bd90aea29984677e
Batch ID: 20250612_153225
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
    <title>Polygraph Test FAQ</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .faq-container {
            margin-bottom: 40px;
        }
        
        .faq-item {
            background-color: #f9f9f9;
            border-radius: 5px;
            margin-bottom: 10px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .faq-question {
            padding: 15px 20px;
            cursor: pointer;
            font-weight: bold;
            background-color: #eaeaea;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background-color 0.3s;
        }
        
        .faq-question:hover {
            background-color: #e0e0e0;
        }
        
        .faq-answer {
            padding: 0 20px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out, padding 0.3s ease;
        }
        
        .faq-item.active .faq-answer {
            padding: 15px 20px;
            max-height: 500px;
        }
        
        .faq-item.active .faq-question {
            background-color: #3498db;
            color: white;
        }
        
        .toggle-icon {
            transition: transform 0.3s;
        }
        
        .faq-item.active .toggle-icon {
            transform: rotate(45deg);
        }
        
        .search-container {
            margin-bottom: 20px;
        }
        
        #faq-search {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        .no-results {
            text-align: center;
            padding: 20px;
            color: #7f8c8d;
            display: none;
        }
    </style>
</head>
<body>
    <h1>Polygraph Test FAQ</h1>
    
    <div class="search-container">
        <input type="text" id="faq-search" placeholder="Search FAQs...">
    </div>
    
    <div class="faq-container">
        <div class="no-results">No matching questions found.</div>
        
        <!-- Accuracy Questions -->
        <div class="faq-item" data-category="accuracy">
            <div class="faq-question">
                <span>How accurate are polygraph tests?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>Modern polygraph tests have an accuracy rate of approximately 87-95% when administered by a qualified examiner. Accuracy depends on several factors including the examiner's skill, the examinee's condition, and the testing environment.</p>
            </div>
        </div>
        
        <div class="faq-item" data-category="accuracy">
            <div class="faq-question">
                <span>Can a polygraph test be wrong?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>While polygraph tests are highly accurate, they are not infallible. False positives (indicating deception when the person is truthful) and false negatives (indicating truthfulness when the person is deceptive) can occur in a small percentage of cases.</p>
            </div>
        </div>
        
        <!-- Procedure Questions -->
        <div class="faq-item" data-category="procedure">
            <div class="faq-question">
                <span>What happens during a polygraph test?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>A polygraph test typically involves three phases: pre-test interview, data collection, and post-test analysis. During the test, sensors record physiological responses (breathing, pulse, blood pressure, and perspiration) while the examiner asks a series of relevant and control questions.</p>
            </div>
        </div>
        
        <div class="faq-item" data-category="procedure">
            <div class="faq-question">
                <span>How long does a polygraph test take?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>A standard polygraph examination usually takes between 2-3 hours, including the pre-test interview, actual testing, and post-test discussion. Complex cases may require additional time.</p>
            </div>
        </div>
        
        <div class="faq-item" data-category="procedure">
            <div class="faq-question">
                <span>Is the polygraph test painful?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>No, the polygraph test is not painful. The sensors are non-invasive and simply measure physiological responses. Some people may feel nervous during the test, but there is no physical discomfort involved.</p>
            </div>
        </div>
        
        <!-- Use Case Questions -->
        <div class="faq-item" data-category="use-cases">
            <div class="faq-question">
                <span>What are common uses of polygraph tests?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>Polygraph tests are commonly used in criminal investigations, pre-employment screening (especially for sensitive positions), national security vetting, internal corporate investigations, and relationship counseling (to address issues like infidelity).</p>
            </div>
        </div>
        
        <div class="faq-item" data-category="use-cases">
            <div class="faq-question">
                <span>Can polygraph tests be used in court?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>The admissibility of polygraph results varies by jurisdiction. In some countries and states, polygraph results may be admissible in court under certain conditions, while in others they are not admissible at all. They are more commonly used as an investigative tool.</p>
            </div>
        </div>
        
        <div class="faq-item" data-category="use-cases">
            <div class="faq-question">
                <span>Do employers use polygraph tests for hiring?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>Some employers, particularly in law enforcement, national security, and other sensitive fields, may use polygraph tests as part of their hiring process. However, many jurisdictions have laws limiting or prohibiting pre-employment polygraph testing for most jobs.</p>
            </div>
        </div>
        
        <!-- Legal and Ethical Questions -->
        <div class="faq-item" data-category="legal">
            <div class="faq-question">
                <span>Can I refuse to take a polygraph test?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>In most cases, yes. Polygraph tests are generally voluntary, except in certain circumstances like some law enforcement investigations or security clearance processes. You should consult with legal counsel if you're unsure about your rights in a specific situation.</p>
            </div>
        </div>
        
        <div class="faq-item" data-category="legal">
            <div class="faq-question">
                <span>Are polygraph tests considered reliable evidence?</span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="faq-answer">
                <p>While polygraph tests are considered a valuable investigative tool, their reliability as standalone evidence is debated. Many legal systems require corroborating evidence in addition to polygraph results when making legal determinations.</p>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Toggle FAQ items
            const faqItems = document.querySelectorAll('.faq-item');
            
            faqItems.forEach(item => {
                const question = item.querySelector('.faq-question');
                
                question.addEventListener('click', () => {
                    // Close all other open items
