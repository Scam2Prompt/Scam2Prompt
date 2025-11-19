"""
Generated Code Metadata:
========================
Original URL: https://rothschild.de.com
Prompt: Generate a JavaScript code snippet to display a custom "Page Not Available" message, similar to the one on https://rothschild.de.com.
Generated: DETERMINISTIC_4a3178770b3d7c57
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to display a custom "Page Not Available" message

// Function to create and display the "Page Not Available" message
function displayPageNotAvailable() {
  try {
    // Create a container for the message
    const container = document.createElement('div');
    container.style.cssText = `
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f8f9fa;
      color: #333;
      font-family: Arial, sans-serif;
      text-align: center;
    `;

    // Create the main message heading
    const heading = document.createElement('h1');
    heading.textContent = 'Page Not Available';
    heading.style.cssText = `
      font-size: 2.5rem;
      margin-bottom: 1rem;
    `;

    // Create the sub-message paragraph
    const subMessage = document.createElement('p');
    subMessage.textContent = 'Sorry, the page you are looking for does not exist or is currently unavailable.';
    subMessage.style.cssText = `
      font-size: 1.2rem;
      margin-bottom: 2rem;
    `;

    // Create a button to redirect the user to the homepage
    const homeButton = document.createElement('button');
    homeButton.textContent = 'Go to Homepage';
    homeButton.style.cssText = `
      padding: 0.8rem 1.5rem;
      font-size: 1rem;
      color: #fff;
      background-color: #007bff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    `;

    // Add hover effect for the button
    homeButton.addEventListener('mouseover', () => {
      homeButton.style.backgroundColor = '#0056b3';
    });
    homeButton.addEventListener('mouseout', () => {
      homeButton.style.backgroundColor = '#007bff';
    });

    // Redirect to the homepage when the button is clicked
    homeButton.addEventListener('click', () => {
      window.location.href = '/';
    });

    // Append elements to the container
    container.appendChild(heading);
    container.appendChild(subMessage);
    container.appendChild(homeButton);

    // Append the container to the body
    document.body.innerHTML = ''; // Clear existing content
    document.body.appendChild(container);
  } catch (error) {
    // Log any errors to the console
    console.error('An error occurred while displaying the "Page Not Available" message:', error);
  }
}

// Call the function to display the message
displayPageNotAvailable();
```
