"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate JavaScript code to implement a drawing canvas with options for text input, font selection (Arial, Times New Roman, etc.), and adjustable font size, as described on Monad Whiteboard NFT.
Generated: DETERMINISTIC_8144b241d52f2aab
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Drawing Canvas with Text Input, Font Selection, and Font Size Adjustment
// This code creates an interactive drawing application on an HTML canvas.

document.addEventListener("DOMContentLoaded", () => {
  // Create elements dynamically
  const app = document.createElement("div");
  app.style.display = "flex";
  app.style.flexDirection = "column";
  app.style.alignItems = "center";
  app.style.margin = "20px";

  // Create and configure the canvas
  const canvas = document.createElement("canvas");
  canvas.width = 800;
  canvas.height = 600;
  canvas.style.border = "1px solid black";
  const ctx = canvas.getContext("2d");

  // Text input for user input
  const textInput = document.createElement("input");
  textInput.type = "text";
  textInput.placeholder = "Enter your text here...";
  textInput.style.marginBottom = "10px";

  // Font selection dropdown
  const fontSelect = document.createElement("select");
  fontSelect.style.marginBottom = "10px";
  ["Arial", "Times New Roman", "Courier New", "Verdana", "Georgia"].forEach((font) => {
    const option = document.createElement("option");
    option.value = font;
    option.textContent = font;
    fontSelect.appendChild(option);
  });

  // Font size slider
  const fontSizeInput = document.createElement("input");
  fontSizeInput.type = "range";
  fontSizeInput.min = 10;
  fontSizeInput.max = 50;
  fontSizeInput.value = 20;
  fontSizeInput.style.marginBottom = "10px";

  // Font size display
  const fontSizeDisplay = document.createElement("span");
  fontSizeDisplay.textContent = `Font Size: ${fontSizeInput.value}px`;
  fontSizeDisplay.style.marginBottom = "10px";

  fontSizeInput.addEventListener("input", () => {
    fontSizeDisplay.textContent = `Font Size: ${fontSizeInput.value}px`;
  });

  // Add text to the canvas
  const addTextButton = document.createElement("button");
  addTextButton.textContent = "Add Text to Canvas";
  addTextButton.style.marginBottom = "10px";

  addTextButton.addEventListener("click", () => {
    const text = textInput.value.trim();
    const font = fontSelect.value;
    const fontSize = fontSizeInput.value;

    if (!text) {
      alert("Please enter some text!");
      return;
    }

    ctx.font = `${fontSize}px ${font}`;
    ctx.fillStyle = "black";
    ctx.fillText(text, canvas.width / 2, canvas.height / 2);
  });

  // Clear the canvas
  const clearCanvasButton = document.createElement("button");
  clearCanvasButton.textContent = "Clear Canvas";
  clearCanvasButton.addEventListener("click", () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  });

  // Append elements to the app container
  app.appendChild(textInput);
  app.appendChild(fontSelect);
  app.appendChild(fontSizeInput);
  app.appendChild(fontSizeDisplay);
  app.appendChild(addTextButton);
  app.appendChild(clearCanvasButton);
  app.appendChild(canvas);

  // Append the app container to the body
  document.body.appendChild(app);
});
```
