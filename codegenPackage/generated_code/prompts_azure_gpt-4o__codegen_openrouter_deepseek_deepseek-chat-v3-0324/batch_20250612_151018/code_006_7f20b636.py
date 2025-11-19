"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: Create a Docusaurus blog post using MDX that includes embedded JSX components.
Generated: DETERMINISTIC_7f20b6360174764c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```mdx
---
title: "Interactive Blog Post with JSX Components"
author: "John Doe"
date: "2023-11-15"
description: "A blog post demonstrating embedded JSX components in MDX"
tags: ["react", "mdx", "docusaurus"]
---

import { useState } from 'react';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import CodeBlock from '@theme/CodeBlock';

# Interactive Blog Post with JSX Components

This post demonstrates how to embed interactive JSX components within a Docusaurus MDX blog post.

## Counter Component Example

Here's a simple counter component embedded directly in the post:

```jsx live
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: '1rem', border: '1px solid #ddd', borderRadius: '4px' }}>
      <p>Current count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

## Tabbed Code Examples

<Tabs>
  <TabItem value="js" label="JavaScript">
    <CodeBlock language="js">
      {`function greet(name) {
  return \`Hello, \${name}!\`;
}`}
    </CodeBlock>
  </TabItem>
  <TabItem value="py" label="Python">
    <CodeBlock language="py">
      {`def greet(name):
    return f"Hello, {name}!"`}
    </CodeBlock>
  </TabItem>
</Tabs>

## Interactive Quiz Component

```jsx live
function Quiz() {
  const [selected, setSelected] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  const questions = [
    {
      question: "What is the capital of France?",
      options: ["London", "Paris", "Berlin", "Madrid"],
      answer: "Paris"
    },
    {
      question: "Which language is used for Docusaurus?",
      options: ["Python", "JavaScript", "Ruby", "Go"],
      answer: "JavaScript"
    }
  ];

  const currentQuestion = questions[0];

  const handleSubmit = () => {
    setSubmitted(true);
  };

  return (
    <div style={{ margin: '1rem 0', padding: '1rem', border: '1px solid #eee', borderRadius: '4px' }}>
      <h3>{currentQuestion.question}</h3>
      {currentQuestion.options.map((option) => (
        <div key={option}>
          <label>
            <input
              type="radio"
              name="quiz"
              checked={selected === option}
              onChange={() => setSelected(option)}
            />
            {option}
          </label>
        </div>
      ))}
      <button onClick={handleSubmit} style={{ marginTop: '0.5rem' }}>
        Submit
      </button>
      {submitted && (
        <p style={{ color: selected === currentQuestion.answer ? 'green' : 'red' }}>
          {selected === currentQuestion.answer ? 'Correct!' : 'Incorrect!'}
        </p>
      )}
    </div>
  );
}
```

## Conclusion

As shown above, MDX allows seamless integration of JSX components within your blog content, making it possible to create rich, interactive documentation.
```
