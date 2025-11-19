"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Develop a JavaScript code snippet for creating a career opportunities webpage, similar to CSL Seqirus's careers page, with features like job filtering and search."
Generated: DETERMINISTIC_a13b33e67f503b9d
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Career Opportunities Webpage Script
// This script dynamically generates a career opportunities page with job filtering and search functionality.

// Sample job data (In production, this data would come from a database or API)
const jobData = [
  { id: 1, title: "Software Engineer", location: "Remote", department: "Engineering" },
  { id: 2, title: "Data Scientist", location: "New York, NY", department: "Data Analytics" },
  { id: 3, title: "Product Manager", location: "San Francisco, CA", department: "Product" },
  { id: 4, title: "Quality Assurance Engineer", location: "Remote", department: "Engineering" },
  { id: 5, title: "HR Specialist", location: "Chicago, IL", department: "Human Resources" },
];

// DOM Elements
const jobListContainer = document.getElementById("job-list");
const searchInput = document.getElementById("search-input");
const filterSelect = document.getElementById("filter-select");

// Function to render job listings
function renderJobs(jobs) {
  // Clear existing job listings
  jobListContainer.innerHTML = "";

  // Check if there are jobs to display
  if (jobs.length === 0) {
    jobListContainer.innerHTML = "<p>No jobs found matching your criteria.</p>";
    return;
  }

  // Generate job cards
  jobs.forEach((job) => {
    const jobCard = document.createElement("div");
    jobCard.className = "job-card";
    jobCard.innerHTML = `
      <h3>${job.title}</h3>
      <p><strong>Location:</strong> ${job.location}</p>
      <p><strong>Department:</strong> ${job.department}</p>
    `;
    jobListContainer.appendChild(jobCard);
  });
}

// Function to filter and search jobs
function filterAndSearchJobs() {
  const searchTerm = searchInput.value.toLowerCase();
  const selectedDepartment = filterSelect.value;

  const filteredJobs = jobData.filter((job) => {
    const matchesSearch = job.title.toLowerCase().includes(searchTerm) || job.location.toLowerCase().includes(searchTerm);
    const matchesFilter = selectedDepartment === "All" || job.department === selectedDepartment;
    return matchesSearch && matchesFilter;
  });

  renderJobs(filteredJobs);
}

// Event Listeners
searchInput.addEventListener("input", filterAndSearchJobs);
filterSelect.addEventListener("change", filterAndSearchJobs);

// Initial Render
renderJobs(jobData);
```

```html
<!-- Career Opportunities Webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Career Opportunities</title>
  <style>
    /* Basic styling for the webpage */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    .container {
      padding: 20px;
    }
    .search-bar {
      margin-bottom: 20px;
    }
    .job-card {
      border: 1px solid #ccc;
      padding: 15px;
      margin-bottom: 10px;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Career Opportunities</h1>
    <div class="search-bar">
      <input type="text" id="search-input" placeholder="Search jobs by title or location" />
      <select id="filter-select">
        <option value="All">All Departments</option>
        <option value="Engineering">Engineering</option>
        <option value="Data Analytics">Data Analytics</option>
        <option value="Product">Product</option>
        <option value="Human Resources">Human Resources</option>
      </select>
    </div>
    <div id="job-list"></div>
  </div>
  <script src="script.js"></script>
</body>
</html>
```
