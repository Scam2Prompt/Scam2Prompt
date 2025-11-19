"""
Generated Code Metadata:
========================
Original URL: https://sushiswap-suhii.weebly.com
Prompt: Generate code for a webpage that allows users to edit text directly on the site, drag and drop elements, and customize templates, similar to the functionality described on the Sushiswap-Suhii website.
Generated: DETERMINISTIC_2b27e25b91ae3310
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in JavaScript, HTML, and CSS. I'll be using React for this task.

**package.json**
```json
{
  "name": "editable-webpage",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-draggable": "^4.0.0",
    "@material-ui/core": "^4.12.4"
  },
  "scripts": {
    "start": "parcel index.html"
  }
}
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editable Webpage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="root"></div>
    <script src="index.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

.editable-text {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.draggable-element {
    position: absolute;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: move;
}

.template-container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: auto;
}
```

**Template.js**
```javascript
// Template.js
import React from 'react';
import Draggable from 'react-draggable';

const Template = ({ children, onSave }) => {
    const [template, setTemplate] = React.useState(children);

    const handleDrag = (e, data) => {
        const newTemplate = [...template];
        newTemplate.forEach((child, index) => {
            if (child.type === 'text') {
                child.x = data.x;
                child.y = data.y;
            }
        });
        setTemplate(newTemplate);
    };

    const handleSave = () => {
        onSave(template);
    };

    return (
        <div className="template-container">
            {template.map((child, index) => {
                if (child.type === 'text') {
                    return (
                        <Draggable
                            key={index}
                            bounds={{ top: 0, left: 0, bottom: 0, right: 0 }}
                            onStart={handleDrag}
                            onDrag={handleDrag}
                            onStop={handleDrag}
                        >
                            <div
                                className="editable-text draggable-element"
                                style={{ left: child.x, top: child.y }}
                            >
                                {child.content}
                            </div>
                        </Draggable>
                    );
                } else {
                    return child;
                }
            })}
            <button onClick={handleSave}>Save Template</button>
        </div>
    );
};

export default Template;
```

**TextEditor.js**
```javascript
// TextEditor.js
import React from 'react';

const TextEditor = ({ value, onChange }) => {
    const [editing, setEditing] = React.useState(false);
    const [text, setText] = React.useState(value);

    const handleEdit = () => {
        setEditing(true);
    };

    const handleBlur = () => {
        setEditing(false);
        onChange(text);
    };

    const handleChange = (e) => {
        setText(e.target.value);
    };

    return (
        <div>
            {editing ? (
                <textarea
                    value={text}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    autoFocus
                />
            ) : (
                <div onClick={handleEdit}>{value}</div>
            )}
        </div>
    );
};

export default TextEditor;
```

**App.js**
```javascript
// App.js
import React, { useState } from 'react';
import Template from './Template';
import TextEditor from './TextEditor';

const App = () => {
    const [template, setTemplate] = useState([
        { type: 'text', content: 'Hello, World!', x: 100, y: 100 },
    ]);

    const handleSaveTemplate = (template) => {
        setTemplate(template);
        console.log('Template saved:', template);
    };

    const handleAddText = () => {
        setTemplate([...template, { type: 'text', content: '', x: 0, y: 0 }]);
    };

    return (
        <div>
            <Template onSave={handleSaveTemplate}>
                {template.map((child, index) => {
                    if (child.type === 'text') {
                        return (
                            <TextEditor
                                key={index}
                                value={child.content}
                                onChange={(text) => {
                                    setTemplate(
                                        template.map((c, i) => {
                                            if (i === index) {
                                                return { ...c, content: text };
                                            }
                                            return c;
                                        })
                                    );
                                }}
                            />
                        );
                    } else {
                        return child;
                    }
                })}
            </Template>
            <button onClick={handleAddText}>Add Text</button>
        </div>
    );
};

export default App;
```

**index.js**
```javascript
// index.js
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
