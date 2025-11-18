"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.insectshieldzoro.com
Prompt: Write JavaScript code to implement a contact form that dynamically updates based on user queries about products like UPVC mosquito nets or stainless steel mesh, as described on the Insect Shield ZORO website.
Generated: DETERMINISTIC_f224359890f47be9
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Contact Form Script for Dynamic Product Queries

// HTML structure assumed:
// <form id="contactForm">
//   <label for="name">Name:</label>
//   <input type="text" id="name" name="name" required>
//   
//   <label for="email">Email:</label>
//   <input type="email" id="email" name="email" required>
//
//   <label for="productQuery">Query about:</label>
//   <select id="productQuery" name="productQuery" required>
//     <option value="">Select a product</option>
//     <option value="upvcMosquitoNets">UPVC Mosquito Nets</option>
//     <option value="stainlessSteelMesh">Stainless Steel Mesh</option>
//   </select>
//
//   <div id="dynamicFields"></div>
//
//   <button type="submit">Submit</button>
// </form>

// JavaScript Code
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const productQuerySelect = document.getElementById('productQuery');
  const dynamicFieldsContainer = document.getElementById('dynamicFields');

  // Function to clear dynamic fields
  const clearDynamicFields = () => {
    dynamicFieldsContainer.innerHTML = '';
  };

  // Function to generate dynamic fields based on product selection
  const generateDynamicFields = (selectedProduct) => {
    clearDynamicFields(); // Ensure no leftover fields from previous selections

    if (selectedProduct === 'upvcMosquitoNets') {
      // Add fields specific to UPVC Mosquito Nets
      const questionLabel = document.createElement('label');
      questionLabel.setAttribute('for', 'meshColor');
      questionLabel.textContent = 'Preferred Mesh Color:';
      
      const questionInput = document.createElement('input');
      questionInput.setAttribute('type', 'text');
      questionInput.setAttribute('id', 'meshColor');
      questionInput.setAttribute('name', 'meshColor');
      questionInput.setAttribute('placeholder', 'e.g., White, Black');
      
      dynamicFieldsContainer.appendChild(questionLabel);
      dynamicFieldsContainer.appendChild(questionInput);
    } else if (selectedProduct === 'stainlessSteelMesh') {
      // Add fields specific to Stainless Steel Mesh
      const sizeLabel = document.createElement('label');
      sizeLabel.setAttribute('for', 'meshSize');
      sizeLabel.textContent = 'Preferred Mesh Size:';
      
      const sizeInput = document.createElement('input');
      sizeInput.setAttribute('type', 'text');
      sizeInput.setAttribute('id', 'meshSize');
      sizeInput.setAttribute('name', 'meshSize');
      sizeInput.setAttribute('placeholder', 'e.g., 1mm, 2mm');
      
      dynamicFieldsContainer.appendChild(sizeLabel);
      dynamicFieldsContainer.appendChild(sizeInput);
    }
  };

  // Event listener for product selection change
  productQuerySelect.addEventListener('change', (event) => {
    const selectedProduct = event.target.value;
    generateDynamicFields(selectedProduct);
  });

  // Form submission handler
  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent page reload

    // Validate form inputs
    const formData = new FormData(form);
    const name = formData.get('name');
    const email = formData.get('email');
    const productQuery = formData.get('productQuery');
    const dynamicFields = {};

    // Collect dynamic fields if applicable
    if (productQuery === 'upvcMosquitoNets') {
      dynamicFields.meshColor = formData.get('meshColor');
    } else if (productQuery === 'stainlessSteelMesh') {
      dynamicFields.meshSize = formData.get('meshSize');
    }

    // Basic error handling
    if (!name || !email || !productQuery) {
      alert('Please fill in all required fields.');
      return;
    }

    // Simulate form submission (could integrate with an API here)
    const submissionData = {
      name,
      email,
      productQuery,
      ...dynamicFields,
    };

    console.log('Form submitted:', submissionData);
    alert('Thank you for your query! We will get back to you soon.');
    form.reset(); // Clear the form after submission
    clearDynamicFields(); // Reset dynamic fields
  });
});
```
