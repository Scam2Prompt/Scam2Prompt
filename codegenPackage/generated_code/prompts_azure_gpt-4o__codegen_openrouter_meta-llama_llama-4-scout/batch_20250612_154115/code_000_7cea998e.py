"""
Generated Code Metadata:
========================
Original URL: https://infinitiai.in
Prompt: Write code to create a drag-and-drop survey form using InfinitiAI's platform features. Include integration with a page builder for lead capture.
Generated: DETERMINISTIC_7cea998e5a737a96
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState } from 'react';
import { Draggable, Droppable } from 'react-beautiful-dnd';
import { Form, Input, Button } from 'antd';

// Define the survey form component
const SurveyForm = () => {
  // State to store form data
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
  });

  // State to store survey questions
  const [questions, setQuestions] = useState([
    { id: 'question-1', text: 'What is your name?' },
    { id: 'question-2', text: 'What is your email?' },
    { id: 'question-3', text: 'What is your phone number?' },
  ]);

  // Handle form data changes
  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // Integrate with InfinitiAI's platform features for lead capture
    // For demonstration purposes, log form data to console
    console.log(formData);
  };

  // Define droppable area for survey questions
  const droppableId = 'survey-questions';

  // Define draggable survey questions
  const draggableQuestions = questions.map((question) => (
    <Draggable key={question.id} draggableId={question.id} index={questions.indexOf(question)}>
      {(provided) => (
        <div
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
        >
          {question.text}
        </div>
      )}
    </Draggable>
  ));

  // Render survey form
  return (
    <Form onSubmit={handleSubmit}>
      <Droppable droppableId={droppableId}>
        {(provided) => (
          <div ref={provided.innerRef} {...provided.droppableProps}>
            {draggableQuestions}
            {provided.placeholder}
          </div>
        )}
      </Droppable>
      <Form.Item label="Name">
        <Input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </Form.Item>
      <Form.Item label="Email">
        <Input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
      </Form.Item>
      <Form.Item label="Phone">
        <Input
          type="tel"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          required
        />
      </Form.Item>
      <Button type="primary" htmlType="submit">
        Submit
      </Button>
    </Form>
  );
};

// Integrate with page builder for lead capture
const PageBuilderIntegration = () => {
  // Render survey form within page builder
  return (
    <div>
      <SurveyForm />
    </div>
  );
};

export default PageBuilderIntegration;
```

```css
/* Add basic styling for survey form */
.ant-form {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.ant-form-item {
  margin-bottom: 20px;
}

.ant-form-item-label {
  font-weight: bold;
}

.ant-input {
  width: 100%;
  height: 40px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
}

.ant-btn {
  width: 100%;
  height: 40px;
  padding: 10px;
  font-size: 16px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.ant-btn:hover {
  background-color: #3e8e41;
}
```

```html
<!-- Example usage within an HTML file -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Survey Form</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```
