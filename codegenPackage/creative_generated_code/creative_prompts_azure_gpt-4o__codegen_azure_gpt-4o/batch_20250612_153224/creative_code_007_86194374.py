"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Generate a detailed CSS stylesheet for designing banners that align with the aesthetic principles mentioned in ChurchProWeb's banner design services.
Generated: DETERMINISTIC_8619437427f5ea52
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* ChurchProWeb Banner Design CSS Stylesheet */
/* This stylesheet is designed to create banners that align with the aesthetic principles of ChurchProWeb's services */

/* General Reset for Consistent Styling Across Browsers */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Main Banner Container */
.banner {
  width: 100%;
  max-width: 1200px; /* Responsive design cap */
  margin: 0 auto; /* Center container */
  padding: 20px 40px;
  background-color: #f5f5f5; /* Neutral background for banners */
  border-radius: 8px; /* Soft corners for elegant design */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  display: flex;
  flex-direction: column; /* Allow stacking of content */
  align-items: center; /* Align content centrally */
  transition: transform 0.3s ease; /* Smooth hover effect */
}

/* Banner Hover Effect */
.banner:hover {
  transform: scale(1.03); /* Slight zoom effect */
}

/* Banner Title */
.banner-title {
  font-size: 2rem; /* Large, prominent title */
  font-family: 'Helvetica Neue', Arial, sans-serif; /* Clean and modern font */
  color: #333333; /* Dark gray for readability */
  text-align: center; /* Center text */
  margin-bottom: 10px;
}

/* Banner Subtitle */
.banner-subtitle {
  font-size: 1.25rem; /* Secondary emphasis */
  font-family: 'Georgia', serif; /* Add a touch of elegance */
  color: #555555; /* Medium gray */
  text-align: center;
  margin-bottom: 20px;
}

/* Banner Call-to-Action Button */
.banner-button {
  font-size: 1rem;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #ffffff; /* White text for emphasis */
  background-color: #007BFF; /* Primary blue for action */
  padding: 10px 20px;
  border: none;
  border-radius: 4px; /* Rounded corners for modern design */
  cursor: pointer;
  text-transform: uppercase; /* Bold and clear action text */
  text-decoration: none; /* Remove underline for button-like appearance */
  display: inline-block;
  transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effects */
}

/* Button Hover Effect */
.banner-button:hover {
  background-color: #0056b3; /* Darker shade of blue */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); /* Slight shadow for hover feedback */
}

/* Banner Image Styling */
.banner-image {
  width: 100%;
  height: auto; /* Maintain aspect ratio */
  border-radius: 8px; /* Rounded corners */
  margin-bottom: 20px; /* Space below the image */
  object-fit: cover; /* Ensure image fills the container proportionally */
}

/* Responsive Design for Smaller Screens */
@media (max-width: 768px) {
  .banner {
    padding: 15px 20px; /* Adjust padding for smaller screens */
  }

  .banner-title {
    font-size: 1.75rem; /* Scale down title size */
  }

  .banner-subtitle {
    font-size: 1rem; /* Scale down subtitle size */
  }

  .banner-button {
    font-size: 0.875rem; /* Scale down button text */
    padding: 8px 16px; /* Adjust button padding */
  }
}

/* Accessibility Enhancements */
/* Ensure focus is clearly visible for keyboard users */
.banner-button:focus {
  outline: 3px solid #FFD700; /* Gold color for focus outline */
  outline-offset: 2px; /* Space between button and focus outline */
}

/* End of ChurchProWeb Banner Stylesheet */
```
