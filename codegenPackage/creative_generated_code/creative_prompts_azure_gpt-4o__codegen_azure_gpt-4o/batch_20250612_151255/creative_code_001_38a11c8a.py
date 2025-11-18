"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staketelegramapp.com
Prompt: Generate a Bootstrap-based portfolio section with collapsible project descriptions, as outlined in the Avenger template.
Generated: DETERMINISTIC_38a11c8a3142faba
Batch ID: 20250612_151255
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
  <title>Portfolio Section</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <section id="portfolio" class="py-5">
    <div class="container">
      <h2 class="text-center mb-4">My Portfolio</h2>
      <div class="row">
        <!-- Project Card -->
        <div class="col-md-6 col-lg-4 mb-4">
          <div class="card">
            <img src="project1.jpg" class="card-img-top" alt="Project 1">
            <div class="card-body">
              <h5 class="card-title">Project 1</h5>
              <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#project1Description" aria-expanded="false" aria-controls="project1Description">
                View Description
              </button>
              <div class="collapse mt-3" id="project1Description">
                <div class="card card-body">
                  <p>A detailed description of Project 1 goes here. Explain the features, technologies used, and purpose of the project.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Project Card -->
        <div class="col-md-6 col-lg-4 mb-4">
          <div class="card">
            <img src="project2.jpg" class="card-img-top" alt="Project 2">
            <div class="card-body">
              <h5 class="card-title">Project 2</h5>
              <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#project2Description" aria-expanded="false" aria-controls="project2Description">
                View Description
              </button>
              <div class="collapse mt-3" id="project2Description">
                <div class="card card-body">
                  <p>A detailed description of Project 2 goes here. Explain the features, technologies used, and purpose of the project.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Project Card -->
        <div class="col-md-6 col-lg-4 mb-4">
          <div class="card">
            <img src="project3.jpg" class="card-img-top" alt="Project 3">
            <div class="card-body">
              <h5 class="card-title">Project 3</h5>
              <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#project3Description" aria-expanded="false" aria-controls="project3Description">
                View Description
              </button>
              <div class="collapse mt-3" id="project3Description">
                <div class="card card-body">
                  <p>A detailed description of Project 3 goes here. Explain the features, technologies used, and purpose of the project.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Bootstrap JS and Dependencies -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
