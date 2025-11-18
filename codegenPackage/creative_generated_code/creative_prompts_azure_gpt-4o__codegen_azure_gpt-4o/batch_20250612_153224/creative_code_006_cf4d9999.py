"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Write JavaScript code to implement a dynamic product carousel for showcasing Ecoplast sheets, such as "ECOPLAST GREY GALAXY STARS-S6" and "ECOPLAST WHISPER GALAXY STARS-S8."
Generated: DETERMINISTIC_cf4d9999792aa885
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product Carousel for Ecoplast Sheets
// This script dynamically creates a product carousel for showcasing Ecoplast products.
// It includes basic functionality for navigating through the carousel, error handling, and responsiveness.

// Products array holding product names and images (replace image URLs with actual paths)
const products = [
  {
    name: "ECOPLAST GREY GALAXY STARS-S6",
    image: "images/grey-galaxy-stars-s6.jpg", // Replace with your actual image URL
  },
  {
    name: "ECOPLAST WHISPER GALAXY STARS-S8",
    image: "images/whisper-galaxy-stars-s8.jpg", // Replace with your actual image URL
  },
  // Add more products as needed
];

// Initialize carousel container
const carouselContainer = document.getElementById("product-carousel");

// Error handling: Ensure the carousel container exists
if (!carouselContainer) {
  console.error("Carousel container not found. Ensure the container ID matches.");
  return;
}

// Create carousel elements
const carouselTrack = document.createElement("div");
carouselTrack.id = "carousel-track";
carouselTrack.style.display = "flex";
carouselTrack.style.overflow = "hidden";
carouselTrack.style.width = "100%";

products.forEach((product, index) => {
  const productSlide = document.createElement("div");
  productSlide.className = "product-slide";
  productSlide.style.flex = "0 0 100%";
  productSlide.style.textAlign = "center";

  const productImage = document.createElement("img");
  productImage.src = product.image;
  productImage.alt = product.name;
  productImage.style.maxWidth = "100%";
  productImage.style.height = "auto";

  const productName = document.createElement("h3");
  productName.textContent = product.name;

  productSlide.appendChild(productImage);
  productSlide.appendChild(productName);
  carouselTrack.appendChild(productSlide);
});

carouselContainer.appendChild(carouselTrack);

// Navigation buttons
const prevButton = document.createElement("button");
prevButton.textContent = "Previous";
prevButton.id = "prev-button";
prevButton.style.position = "absolute";
prevButton.style.left = "10px";
prevButton.style.top = "50%";
prevButton.style.transform = "translateY(-50%)";

const nextButton = document.createElement("button");
nextButton.textContent = "Next";
nextButton.id = "next-button";
nextButton.style.position = "absolute";
nextButton.style.right = "10px";
nextButton.style.top = "50%";
nextButton.style.transform = "translateY(-50%)";

carouselContainer.appendChild(prevButton);
carouselContainer.appendChild(nextButton);

// Carousel functionality
let currentIndex = 0;

const updateCarousel = () => {
  const offset = currentIndex * -100;
  carouselTrack.style.transform = `translateX(${offset}%)`;
};

prevButton.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
    updateCarousel();
  } else {
    console.warn("Already at the first product.");
  }
});

nextButton.addEventListener("click", () => {
  if (currentIndex < products.length - 1) {
    currentIndex++;
    updateCarousel();
  } else {
    console.warn("Already at the last product.");
  }
});

// Styling (optional, for better visuals; consider moving this to a CSS file for production)
document.head.insertAdjacentHTML(
  "beforeend",
  `<style>
    #product-carousel {
      position: relative;
      width: 80%;
      margin: auto;
      border: 1px solid #ddd;
      overflow: hidden;
    }
    .product-slide img {
      max-width: 100%;
      height: auto;
      border-radius: 8px;
    }
    button {
      background-color: #007BFF;
      color: white;
      border: none;
      padding: 10px;
      cursor: pointer;
      border-radius: 4px;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>`
);
```
