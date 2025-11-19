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

```typescript
import React from 'react';
import { MDXProvider } from '@mdx-js/react';

type NoteType = 'info' | 'warning' | 'error' | 'success';

interface NoteProps {
  type?: NoteType;
  title?: string;
  children: React.ReactNode;
}

const Note: React.FC<NoteProps> = ({ type = 'info', title, children }) => {
  const getNoteStyles = (noteType: NoteType) => {
    const baseStyles = 'p-4 rounded-lg my-4 border-l-4';
    switch (noteType) {
      case 'info':
        return `${baseStyles} bg-blue-50 border-blue-500`;
      case 'warning':
        return `${baseStyles} bg-yellow-50 border-yellow-500`;
      case 'error':
        return `${baseStyles} bg-red-50 border-red-500`;
      case 'success':
        return `${baseStyles} bg-green-50 border-green-500`;
      default:
        return `${baseStyles} bg-gray-50 border-gray-500`;
    }
  };

  const getTitle = () => {
    if (title) return title;
    switch (type) {
      case 'info':
        return 'Info';
      case 'warning':
        return 'Warning';
      case 'error':
        return 'Error';
      case 'success':
        return 'Success';
      default:
        return 'Note';
    }
  };

  return (
    <div className={getNoteStyles(type)}>
      <div className="font-bold mb-2">{getTitle()}</div>
      <div className="note-content">{children}</div>
    </div>
  );
};

const MDXComponents = {
  Note,
};

interface MDXNoteProviderProps {
  children: React.ReactNode;
}

const MDXNoteProvider: React.FC<MDXNoteProviderProps> = ({ children }) => {
  return <MDXProvider components={MDXComponents}>{children}</MDXProvider>;
};

export { Note, MDXNoteProvider };
```
