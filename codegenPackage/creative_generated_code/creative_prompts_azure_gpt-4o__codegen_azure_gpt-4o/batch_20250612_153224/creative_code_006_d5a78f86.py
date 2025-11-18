"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Develop a function to showcase Bollé's 130-year history and technological advancements in a timeline format on a website.
Generated: DETERMINISTIC_d5a78f86b89699f3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bollé 130-Year History Timeline</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    /* Basic styling for the timeline */
    .timeline {
      position: relative;
      max-width: 800px;
      margin: 0 auto;
    }

    .timeline::after {
      content: '';
      position: absolute;
      width: 6px;
      background-color: #3498db;
      top: 0;
      bottom: 0;
      left: 50%;
      margin-left: -3px;
    }

    .timeline-item {
      padding: 10px 40px;
      position: relative;
      background-color: #f4f4f4;
      border-radius: 8px;
      width: 45%;
    }

    .timeline-item.left {
      left: calc(50% - 45%);
    }

    .timeline-item.right {
      left: 50%;
    }

    .timeline-item::after {
      content: '';
      position: absolute;
      width: 10px;
      height: 10px;
      background-color: #3498db;
      top: 15px;
      border-radius: 50%;
      left: -6px;
    }

    .timeline-item.right::after {
      left: auto;
      right: -6px;
    }

    .timeline-year {
      font-weight: bold;
      color: #222;
    }

    .timeline-description {
      margin-top: 8px;
      font-size: 0.9em;
      color: #555;
    }
  </style>
</head>
<body>
  <header>
    <h1>Bollé - 130 Years of Innovation</h1>
  </header>
  <section class="timeline">
    <!-- Each timeline item represents a key event -->
    <div class="timeline-item left">
      <span class="timeline-year">1888</span>
      <p class="timeline-description">Bollé was founded in France, producing combs and hair accessories made of horn.</p>
    </div>
    <div class="timeline-item right">
      <span class="timeline-year">1936</span>
      <p class="timeline-description">Bollé began manufacturing eyewear, leveraging advanced molding techniques.</p>
    </div>
    <div class="timeline-item left">
      <span class="timeline-year">1960</span>
      <p class="timeline-description">Introduction of safety glasses, marking Bollé's foray into protective eyewear.</p>
    </div>
    <div class="timeline-item right">
      <span class="timeline-year">1986</span>
      <p class="timeline-description">Launch of performance sunglasses, opening a new chapter for athletes and outdoor enthusiasts.</p>
    </div>
    <div class="timeline-item left">
      <span class="timeline-year">2007</span>
      <p class="timeline-description">Bollé adopted advanced anti-fog and anti-scratch lens technologies.</p>
    </div>
    <div class="timeline-item right">
      <span class="timeline-year">2023</span>
      <p class="timeline-description">Celebrating 130 years of innovation, Bollé continues to lead in eyewear technology.</p>
    </div>
  </section>
  <footer>
    <p>&copy; 2023 Bollé. All rights reserved.</p>
  </footer>
</body>
</html>
```
