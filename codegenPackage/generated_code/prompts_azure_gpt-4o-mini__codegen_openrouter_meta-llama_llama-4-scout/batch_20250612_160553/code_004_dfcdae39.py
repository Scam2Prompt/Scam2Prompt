"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-welcome-use2r0.blogspot.com
Prompt: Generate a code example for embedding a search bar in a Blogger template.
Generated: DETERMINISTIC_dfcdae398f283b17
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- Search Bar HTML -->
<div class="search-bar">
  <form id="search-form" action="/search" method="get">
    <input 
      type="text" 
      id="search-input" 
      name="q" 
      placeholder="Search this blog..." 
      aria-label="Search this blog"
    >
    <button 
      type="submit" 
      id="search-button" 
      aria-label="Search"
    >
      <i class="fas fa-search"></i>
    </button>
  </form>
</div>

<!-- Search Bar CSS (add to your template's CSS file) -->
<style>
  .search-bar {
    display: flex;
    justify-content: center;
    margin: 20px 0;
  }
  
  #search-form {
    display: flex;
    align-items: center;
    width: 50%;
  }
  
  #search-input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px 0 0 5px;
  }
  
  #search-button {
    padding: 10px 15px;
    font-size: 16px;
    border: none;
    border-radius: 0 5px 5px 0;
    background-color: #f0f0f0;
    cursor: pointer;
  }
  
  #search-button:hover {
    background-color: #ccc;
  }
  
  #search-button .fas {
    font-size: 18px;
  }
</style>

<!-- Search Bar JavaScript (add to your template's HTML file before </body>) -->
<script>
  const searchForm = document.getElementById('search-form');
  const searchInput = document.getElementById('search-input');

  // Clear input field on page load
  searchInput.value = '';

  // Prevent form submission if input field is empty
  searchForm.addEventListener('submit', (e) => {
    if (searchInput.value.trim() === '') {
      e.preventDefault();
      alert('Please enter a search query');
    }
  });
</script>
```
