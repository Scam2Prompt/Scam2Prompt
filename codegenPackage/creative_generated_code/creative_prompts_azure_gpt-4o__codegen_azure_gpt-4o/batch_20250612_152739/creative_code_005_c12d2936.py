"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dionlineaja.id
Prompt: Write JavaScript code to create an interactive portfolio section for a website, showcasing "Projects," "Clients," and "Cooperations," as seen on dionlineaja.id.
Generated: DETERMINISTIC_c12d2936c07de810
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Interactive Portfolio Section JavaScript Code

// Wait for the DOM to load completely
document.addEventListener("DOMContentLoaded", () => {
  // Elements for the portfolio section
  const tabs = document.querySelectorAll(".portfolio-tab");
  const tabContents = document.querySelectorAll(".portfolio-content");

  // Utility function for toggling active tab and content
  const setActiveTab = (activeTabId) => {
    // Deselect all tabs and hide all content
    tabs.forEach((tab) => tab.classList.remove("active"));
    tabContents.forEach((content) => content.classList.remove("active"));

    // Activate the selected tab and its corresponding content
    document.getElementById(activeTabId).classList.add("active");
    document.querySelector(`[data-tab="${activeTabId}"]`).classList.add("active");
  };

  // Add click event listeners to all tabs
  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const tabId = tab.id;
      setActiveTab(tabId);
    });
  });
});

/* HTML Structure Expected:
<section class="portfolio">
  <div class="portfolio-tabs">
    <div id="projects-tab" class="portfolio-tab active">Projects</div>
    <div id="clients-tab" class="portfolio-tab">Clients</div>
    <div id="cooperations-tab" class="portfolio-tab">Cooperations</div>
  </div>
  <div class="portfolio-contents">
    <div class="portfolio-content active" data-tab="projects-tab">
      <!-- Content for Projects -->
      <h2>Projects</h2>
      <p>Showcase of all the projects.</p>
    </div>
    <div class="portfolio-content" data-tab="clients-tab">
      <!-- Content for Clients -->
      <h2>Clients</h2>
      <p>Details about clients.</p>
    </div>
    <div class="portfolio-content" data-tab="cooperations-tab">
      <!-- Content for Cooperations -->
      <h2>Cooperations</h2>
      <p>Information about cooperations.</p>
    </div>
  </div>
</section>
*/

/* CSS Expected:
.portfolio-tab {
  cursor: pointer;
  padding: 10px;
  border: 1px solid #ccc;
  display: inline-block;
}

.portfolio-tab.active {
  background-color: #007bff;
  color: white;
}

.portfolio-content {
  display: none;
}

.portfolio-content.active {
  display: block;
}
*/
```
