"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Write a custom note component for MDX, as discussed on Joe Previte's website.
Generated: DETERMINISTIC_a7b4e7fa234ab9e6
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
/**
 * Custom Note component for MDX.
 *
 * @param {object} props
 * @param {string} props.children
 * @param {string} [props.type="note"]
 * @returns {JSX.Element}
 */
import React from 'react';

const Note = ({ children, type = 'note', ...props }) => {
  const noteTypes = {
    note: 'Note',
    warning: 'Warning',
    danger: 'Danger',
    tip: 'Tip',
  };

  if (!(type in noteTypes)) {
    throw new Error(`Invalid note type: ${type}. Must be one of: ${Object.keys(noteTypes).join(', ')}`);
  }

  return (
    <div
      {...props}
      className={`note note--${type}`}
      role="alert"
    >
      <strong>{noteTypes[type]}</strong>
      <div>{children}</div>
    </div>
  );
};

export default Note;
```

```markdown
// Usage in MDX file
import Note from './Note';

<Note type="warning">
  This is a warning note.
</Note>

<Note>
  This is a default note.
</Note>

<Note type="danger">
  This is a danger note.
</Note>

<Note type="tip">
  This is a tip note.
</Note>
```

```css
/* Add to your CSS file */
.note {
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 0.5em;
  margin: 1em 0;
}

.note strong {
  display: block;
  margin-bottom: 0.5em;
}

.note--note {
  background-color: #f7f7f7;
  border-color: #ddd;
}

.note--warning {
  background-color: #fdf5dc;
  border-color: #ffd700;
}

.note--danger {
  background-color: #fbe6e6;
  border-color: #f44336;
}

.note--tip {
  background-color: #dff0d8;
  border-color: #8bc34a;
}
```
