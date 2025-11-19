"""
Generated Code Metadata:
========================
Original URL: https://forgemints.store
Prompt: Design a user interface for an NFT marketplace similar to Forgemint, incorporating features such as search filtering, sorting, and recommendations, and ensuring a seamless user experience across various devices and browsers.
Generated: DETERMINISTIC_62b8350a4fdda123
Batch ID: 20250622_212813
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
  <title>NFT Marketplace</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">NFT Marketplace</h1>
      <nav class="nav">
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Explore</a></li>
          <li><a href="#">My Collection</a></li>
          <li><a href="#">Profile</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content -->
  <main class="main">
    <div class="container">
      <!-- Search and Filter Section -->
      <section class="search-filter">
        <input type="text" id="search" placeholder="Search NFTs..." />
        <select id="filter">
          <option value="all">All</option>
          <option value="art">Art</option>
          <option value="music">Music</option>
          <option value="domain">Domain Names</option>
        </select>
        <select id="sort">
          <option value="popular">Most Popular</option>
          <option value="recent">Recently Added</option>
          <option value="price_low_high">Price: Low to High</option>
          <option value="price_high_low">Price: High to Low</option>
        </select>
      </section>

      <!-- Recommendations Section -->
      <section class="recommendations">
        <h2>Recommended NFTs</h2>
        <div id="recommendations-list" class="nft-grid">
          <!-- Dynamic NFT cards will be inserted here -->
        </div>
      </section>

      <!-- NFT Listing Section -->
      <section class="nft-listing">
        <h2>Explore NFTs</h2>
        <div id="nft-list" class="nft-grid">
          <!-- Dynamic NFT cards will be inserted here -->
        </div>
      </section>
    </div>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 NFT Marketplace. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, input, select {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f9f9f9;
  color: #333;
}

/* Header Styling */
.header {
  background-color: #222;
  color: #fff;
  padding: 1rem 0;
}

.header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header .logo {
  font-size: 1.5rem;
}

.header .nav ul {
  list-style: none;
  display: flex;
}

.header .nav ul li {
  margin: 0 1rem;
}

.header .nav ul li a {
  color: #fff;
  text-decoration: none;
}

/* Main Content Styling */
.main .container {
  padding: 2rem;
}

.search-filter {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-filter input, .search-filter select {
  padding: 0.5rem;
  font-size: 1rem;
}

.nft-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.nft-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
}

.nft-card img {
  max-width: 100%;
  border-radius: 8px;
}

.nft-card h3 {
  margin: 0.5rem 0;
}

.nft-card p {
  font-size: 0.9rem;
  color: #666;
}

/* Footer Styling */
.footer {
  background-color: #222;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```

```javascript
// app.js

// Mock Data for NFTs
const mockNFTs = [
  { id: 1, name: "Digital Art #1", category: "art", price: 0.5, image: "art1.jpg" },
  { id: 2, name: "Music NFT #1", category: "music", price: 1.2, image: "music1.jpg" },
  { id: 3, name: "Domain Name #1", category: "domain", price: 0.8, image: "domain1.jpg" },
  { id: 4, name: "Digital Art #2", category: "art", price: 0.3, image: "art2.jpg" },
  { id: 5, name: "Music NFT #2", category: "music", price: 1.5, image: "music2.jpg" },
];

// Function to Render NFTs
function renderNFTs(nfts, containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = ""; // Clear previous content

  nfts.forEach(nft => {
    const card = document.createElement("div");
    card.className = "nft-card";
    card.innerHTML = `
      <img src="${nft.image}" alt="${nft.name}">
      <h3>${nft.name}</h3>
      <p>Category: ${nft.category}</p>
      <p>Price: ${nft.price} ETH</p>
    `;
    container.appendChild(card);
  });
}

// Initial Render
renderNFTs(mockNFTs, "nft-list");
renderNFTs(mockNFTs.slice(0, 3), "recommendations-list");

// Search and Filter Logic
document.getElementById("search").addEventListener("input", (e) => {
  const searchTerm = e.target.value.toLowerCase();
  const filteredNFTs = mockNFTs.filter(nft => nft.name.toLowerCase().includes(searchTerm));
  renderNFTs(filteredNFTs, "nft-list");
});

document.getElementById("filter").addEventListener("change", (e) => {
  const category = e.target.value;
  const filteredNFTs = category === "all" ? mockNFTs : mockNFTs.filter(nft => nft.category === category);
  renderNFTs(filteredNFTs, "nft-list");
});

document.getElementById("sort").addEventListener("change", (e) => {
  const sortOption = e.target.value;
  let sortedNFTs = [...mockNFTs];

  if (sortOption === "price_low_high") {
    sortedNFTs.sort((a, b) => a.price - b.price);
  } else if (sortOption === "price_high_low") {
    sortedNFTs.sort((a, b) => b.price - a.price);
  } else if (sortOption === "recent") {
    sortedNFTs = mockNFTs; // Assuming mockNFTs are already sorted by recent
  }

  renderNFTs(sortedNFTs, "nft-list");
});
```
