"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Develop a CSS style for a fullscreen slider that aligns with the design aesthetics of the IMST Telehealth homepage, focusing on visual clarity and simplicity.
Generated: DETERMINISTIC_52a32f29279dcc3f
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Fullscreen Slider Styles for IMST Telehealth Homepage */

/* General container for the slider */
.fullscreen-slider {
  position: relative; /* Ensures positioning for child elements */
  width: 100vw; /* Full viewport width */
  height: 100vh; /* Full viewport height */
  overflow: hidden; /* Prevents content overflow */
  display: flex; /* Enables flexbox for alignment */
  align-items: center; /* Centers items vertically */
  justify-content: center; /* Centers items horizontally */
  background-color: #f9f9f9; /* Neutral background for clarity */
}

/* Individual slide styling */
.slide {
  position: absolute; /* Allows stacking of slides */
  width: 100%; /* Full width of the slider */
  height: 100%; /* Full height of the slider */
  background-size: cover; /* Ensures background image covers the slide */
  background-position: center; /* Centers the background image */
  transition: opacity 0.5s ease-in-out; /* Smooth fade transition */
  opacity: 0; /* Default state is hidden */
}

/* Active slide */
.slide.active {
  opacity: 1; /* Makes the active slide visible */
}

/* Navigation buttons */
.slider-nav {
  position: absolute; /* Positioned relative to the slider */
  top: 50%; /* Vertically centered */
  transform: translateY(-50%); /* Adjusts for centering */
  display: flex; /* Enables flexbox for alignment */
  justify-content: space-between; /* Positions buttons on opposite sides */
  width: 100%; /* Full width of the slider */
  pointer-events: none; /* Prevents interference with slide content */
}

.slider-nav button {
  pointer-events: auto; /* Enables button interaction */
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  color: #fff; /* White text for contrast */
  border: none; /* Removes default button border */
  border-radius: 50%; /* Circular buttons */
  width: 50px; /* Fixed width */
  height: 50px; /* Fixed height */
  display: flex; /* Enables flexbox for alignment */
  align-items: center; /* Centers icon vertically */
  justify-content: center; /* Centers icon horizontally */
  cursor: pointer; /* Changes cursor to pointer on hover */
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

.slider-nav button:hover {
  background-color: rgba(0, 0, 0, 0.7); /* Darker background on hover */
}

/* Pagination dots */
.slider-pagination {
  position: absolute; /* Positioned relative to the slider */
  bottom: 20px; /* Positioned near the bottom */
  width: 100%; /* Full width of the slider */
  display: flex; /* Enables flexbox for alignment */
  justify-content: center; /* Centers dots horizontally */
  gap: 10px; /* Adds spacing between dots */
}

.slider-pagination .dot {
  width: 12px; /* Fixed width */
  height: 12px; /* Fixed height */
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  border-radius: 50%; /* Circular dots */
  cursor: pointer; /* Changes cursor to pointer on hover */
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

.slider-pagination .dot.active {
  background-color: #0078d7; /* Highlighted color for active dot */
}

.slider-pagination .dot:hover {
  background-color: rgba(0, 0, 0, 0.7); /* Darker background on hover */
}
```
