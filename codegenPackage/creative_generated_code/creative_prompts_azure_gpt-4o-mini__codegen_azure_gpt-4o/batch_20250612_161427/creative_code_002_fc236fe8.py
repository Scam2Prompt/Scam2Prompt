"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokoswap-admin-build.pages.dev
Prompt: Can you provide code examples for building a minimal UI kit with JavaScript?
Generated: DETERMINISTIC_fc236fe887ea2a62
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// UI Kit: Minimal JavaScript Library for Building a UI Component Framework
// This library includes basic components: Button, Modal, and Tooltip.

// Utility function to create elements with attributes and children
function createElement(tag, attributes = {}, children = []) {
  const element = document.createElement(tag);

  // Apply attributes to the element
  for (const attr in attributes) {
    element.setAttribute(attr, attributes[attr]);
  }

  // Append child nodes
  children.forEach(child => {
    if (typeof child === 'string') {
      element.appendChild(document.createTextNode(child));
    } else {
      element.appendChild(child);
    }
  });

  return element;
}

// Button Component
function Button({ text, onClick, className = "ui-button" }) {
  const button = createElement("button", { class: className });
  button.innerText = text;
  button.addEventListener("click", onClick);
  return button;
}

// Modal Component
function Modal({ title, content, onClose, className = "ui-modal" }) {
  const modalWrapper = createElement("div", { class: `${className}-wrapper` });
  const modal = createElement("div", { class: className });
  const modalHeader = createElement(
    "div",
    { class: `${className}-header` },
    [createElement("h2", {}, [title])]
  );
  const closeButton = createElement(
    "button",
    { class: `${className}-close` },
    ["×"]
  );
  closeButton.addEventListener("click", () => {
    onClose();
    modalWrapper.remove();
  });

  const modalContent = createElement(
    "div",
    { class: `${className}-content` },
    [content]
  );

  modalHeader.appendChild(closeButton);
  modal.appendChild(modalHeader);
  modal.appendChild(modalContent);
  modalWrapper.appendChild(modal);

  // Append the modal to the body
  document.body.appendChild(modalWrapper);

  return modalWrapper;
}

// Tooltip Component
function Tooltip({ text, targetElement, className = "ui-tooltip" }) {
  const tooltip = createElement("div", { class: className }, [text]);

  // Position tooltip on hover
  targetElement.addEventListener("mouseenter", () => {
    const rect = targetElement.getBoundingClientRect();
    tooltip.style.position = "absolute";
    tooltip.style.top = `${rect.bottom + window.scrollY}px`;
    tooltip.style.left = `${rect.left + window.scrollX}px`;
    targetElement.parentElement.appendChild(tooltip);
  });

  targetElement.addEventListener("mouseleave", () => {
    tooltip.remove();
  });

  return tooltip;
}

// Example Usage:

// Create a button component
const button = Button({
  text: "Click Me",
  onClick: () => {
    Modal({
      title: "Modal Title",
      content: "This is the content of the modal.",
      onClose: () => console.log("Modal closed")
    });
  }
});
document.body.appendChild(button);

// Create a tooltip for the button
Tooltip({
  text: "Hover over the button to interact!",
  targetElement: button
});

// Styling (optional)
const style = document.createElement("style");
style.innerHTML = `
  .ui-button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  .ui-modal-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .ui-modal {
    background: white;
    padding: 20px;
    border-radius: 8px;
    max-width: 500px;
    width: 100%;
  }
  .ui-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .ui-modal-close {
    border: none;
    background: none;
    font-size: 20px;
    cursor: pointer;
  }
  .ui-tooltip {
    background: black;
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 14px;
    white-space: nowrap;
  }
`;
document.head.appendChild(style);
```
