"""
Generated Code Metadata:
========================
Original URL: https://cfdiplus.com
Prompt: How can I customize the appearance of sticky notes in a React application?
Generated: DETERMINISTIC_3ee83c3a36dd5f05
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import './StickyNote.css'; // Importing CSS for styling

// StickyNote component
const StickyNote = ({ initialText, initialColor }) => {
  // State to manage the text and color of the sticky note
  const [text, setText] = useState(initialText || 'New Note');
  const [color, setColor] = useState(initialColor || '#ffeb3b');

  // Handler for text change
  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  // Handler for color change
  const handleColorChange = (event) => {
    setColor(event.target.value);
  };

  return (
    <div className="sticky-note" style={{ backgroundColor: color }}>
      <textarea
        value={text}
        onChange={handleTextChange}
        className="sticky-note-text"
      />
      <div className="color-picker">
        <label htmlFor="color">Choose Color:</label>
        <input
          type="color"
          id="color"
          value={color}
          onChange={handleColorChange}
        />
      </div>
    </div>
  );
};

// Main App component
const App = () => {
  return (
    <div className="app">
      <h1>Sticky Notes</h1>
      <StickyNote initialText="My first note!" initialColor="#ffeb3b" />
      <StickyNote initialText="Another note!" initialColor="#ffcc80" />
    </div>
  );
};

export default App;
```

```css
/* StickyNote.css */
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

.sticky-note {
  width: 200px;
  height: 200px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 10px;
  position: relative;
}

.sticky-note-text {
  width: 100%;
  height: 80%;
  border: none;
  outline: none;
  resize: none;
  background: transparent;
  font-size: 16px;
}

.color-picker {
  position: absolute;
  bottom: 10px;
  left: 10px;
}
```

This code provides a simple React application with customizable sticky notes. Each sticky note allows the user to change its text and background color. The CSS styles ensure a clean and visually appealing layout.
