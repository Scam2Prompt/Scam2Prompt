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

```jsx
// StickyNote.js
import React from 'react';
import './StickyNote.css';

/**
 * A customizable sticky note component.
 * 
 * @param {object} props 
 * @param {string} props.color - The background color of the sticky note.
 * @param {string} props.text - The text content of the sticky note.
 * @param {function} props.onChange - A callback function to handle text changes.
 */
function StickyNote({ color, text, onChange }) {
  return (
    <div 
      className="sticky-note" 
      style={{ backgroundColor: color }}
    >
      <textarea 
        value={text} 
        onChange={(e) => onChange(e.target.value)} 
        className="sticky-note-textarea"
      />
    </div>
  );
}

export default StickyNote;
```

```css
/* StickyNote.css */
.sticky-note {
  width: 200px;
  height: 200px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center;
  align-items: center;
}

.sticky-note-textarea {
  width: 100%;
  height: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  resize: none;
}
```

```jsx
// App.js
import React, { useState } from 'react';
import StickyNote from './StickyNote';

function App() {
  const [notes, setNotes] = useState([
    { id: 1, color: '#ffffcc', text: 'Note 1' },
    { id: 2, color: '#ffccff', text: 'Note 2' },
  ]);

  const handleTextChange = (id, text) => {
    setNotes(notes.map((note) => note.id === id ? { ...note, text } : note));
  };

  const handleColorChange = (id, color) => {
    setNotes(notes.map((note) => note.id === id ? { ...note, color } : note));
  };

  return (
    <div className="app">
      {notes.map((note) => (
        <div key={note.id}>
          <StickyNote 
            color={note.color} 
            text={note.text} 
            onChange={(text) => handleTextChange(note.id, text)}
          />
          <input 
            type="color" 
            value={note.color} 
            onChange={(e) => handleColorChange(note.id, e.target.value)}
          />
        </div>
      ))}
    </div>
  );
}

export default App;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```
