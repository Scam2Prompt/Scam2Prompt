"""
Generated Code Metadata:
========================
Original URL: https://dustbox.netlify.app
Prompt: Generate code to implement a searchable table of contents feature inspired by Dustbox.netlify.app.
Generated: DETERMINISTIC_b8c09e920aa8d664
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Table of Contents Implementation**
=====================================

### TableOfContents.js
```javascript
/**
 * Table of Contents component
 * 
 * @param {object} props - component props
 * @param {array} props.headings - array of headings
 * @param {function} props.onSearch - search callback function
 * @returns {JSX.Element} Table of Contents component
 */
import React, { useState } from 'react';

const TableOfContents = ({ headings, onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredHeadings, setFilteredHeadings] = useState(headings);

  const handleSearch = (event) => {
    const searchTerm = event.target.value.toLowerCase();
    setSearchTerm(searchTerm);
    const filteredHeadings = headings.filter((heading) => {
      return heading.text.toLowerCase().includes(searchTerm);
    });
    setFilteredHeadings(filteredHeadings);
  };

  return (
    <div className="table-of-contents">
      <input
        type="search"
        value={searchTerm}
        onChange={handleSearch}
        placeholder="Search..."
      />
      <ul>
        {filteredHeadings.map((heading, index) => (
          <li key={index}>
            <a href={`#${heading.id}`}>{heading.text}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TableOfContents;
```

### Heading.js
```javascript
/**
 * Heading component
 * 
 * @param {object} props - component props
 * @param {string} props.text - heading text
 * @param {string} props.id - heading id
 * @param {number} props.level - heading level
 * @returns {JSX.Element} Heading component
 */
import React from 'react';

const Heading = ({ text, id, level }) => {
  const HeadingTag = `h${level}`;

  return (
    <HeadingTag id={id}>{text}</HeadingTag>
  );
};

export default Heading;
```

### useHeadings.js
```javascript
/**
 * Custom hook to extract headings from a markdown content
 * 
 * @param {string} content - markdown content
 * @returns {array} array of headings
 */
import { useState, useEffect } from 'react';

const useHeadings = (content) => {
  const [headings, setHeadings] = useState([]);

  useEffect(() => {
    const headings = [];
    const regex = /^(#{1,6}) (.*)$/gm;
    const matches = content.matchAll(regex);

    for (const match of matches) {
      const level = match[1].length;
      const text = match[2];
      const id = text.toLowerCase().replace(/\s+/g, '-');

      headings.push({ text, id, level });
    }

    setHeadings(headings);
  }, [content]);

  return headings;
};

export default useHeadings;
```

### App.js
```javascript
import React from 'react';
import TableOfContents from './TableOfContents';
import Heading from './Heading';
import useHeadings from './useHeadings';

const markdownContent = `
# Introduction
This is an introduction

## Getting Started
This is a getting started section

### Installation
This is an installation section

## Features
This is a features section
`;

const App = () => {
  const headings = useHeadings(markdownContent);

  return (
    <div>
      <TableOfContents headings={headings} />
      <div>
        {headings.map((heading, index) => (
          <Heading
            key={index}
            text={heading.text}
            id={heading.id}
            level={heading.level}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
```

### index.js
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

### styles.css
```css
.table-of-contents {
  position: fixed;
  top: 0;
  left: 0;
  width: 200px;
  height: 100vh;
  padding: 20px;
  background-color: #f0f0f0;
  border-right: 1px solid #ddd;
}

.table-of-contents input[type="search"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
}

.table-of-contents ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.table-of-contents li {
  margin-bottom: 10px;
}

.table-of-contents a {
  text-decoration: none;
  color: #337ab7;
}

.table-of-contents a:hover {
  color: #23527c;
}
```
