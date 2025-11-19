"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Generate a code snippet to create a responsive portfolio layout using CSS Grid, inspired by the portfolio types mentioned on the IMST Telehealth website.
Generated: DETERMINISTIC_240cae9e5f5b94ab
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Portfolio Grid Layout - Responsive Design */
.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem;
  margin: 0 auto;
  max-width: 1200px;
}

/* Portfolio Card Styling */
.portfolio-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.portfolio-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.card-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-content {
  padding: 1.5rem;
}

.card-title {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: #2d3748;
}

.card-description {
  color: #4a5568;
  margin-bottom: 1rem;
}

.card-link {
  display: inline-block;
  color: #4299e1;
  font-weight: 600;
  text-decoration: none;
  transition: color 0.2s ease;
}

.card-link:hover {
  color: #2b6cb0;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .portfolio-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .portfolio-grid {
    grid-template-columns: 1fr;
  }
  
  .card-image {
    height: 180px;
  }
}
```

```html
<!-- Portfolio Grid HTML Structure -->
<div class="portfolio-grid">
  <div class="portfolio-card">
    <img src="project1.jpg" alt="Project 1" class="card-image">
    <div class="card-content">
      <h3 class="card-title">Telehealth Platform</h3>
      <p class="card-description">A comprehensive telehealth solution for remote consultations.</p>
      <a href="#" class="card-link">View Project →</a>
    </div>
  </div>
  
  <div class="portfolio-card">
    <img src="project2.jpg" alt="Project 2" class="card-image">
    <div class="card-content">
      <h3 class="card-title">Patient Portal</h3>
      <p class="card-description">Secure patient portal for medical records and appointments.</p>
      <a href="#" class="card-link">View Project →</a>
    </div>
  </div>
  
  <div class="portfolio-card">
    <img src="project3.jpg" alt="Project 3" class="card-image">
    <div class="card-content">
      <h3 class="card-title">Mobile Health App</h3>
      <p class="card-description">iOS/Android app for on-the-go health monitoring.</p>
      <a href="#" class="card-link">View Project →</a>
    </div>
  </div>
</div>
```
