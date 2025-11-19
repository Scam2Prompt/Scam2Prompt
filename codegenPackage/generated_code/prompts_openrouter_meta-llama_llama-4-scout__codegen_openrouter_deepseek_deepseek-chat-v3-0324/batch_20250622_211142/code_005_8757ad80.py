"""
Generated Code Metadata:
========================
Original URL: https://ideru.com
Prompt: Design a user interface for a web application that provides an intuitive and stress-free user experience, incorporating user-centered design principles and accessibility features.
Generated: DETERMINISTIC_8757ad8066692cf0
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready React-based UI component with accessibility features and user-centered design principles:

```jsx
import React, { useState, useEffect } from 'react';
import './App.css';

/**
 * Main application component with accessible UI elements
 */
function App() {
  const [theme, setTheme] = useState('light');
  const [inputValue, setInputValue] = useState('');
  const [todos, setTodos] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Toggle between light and dark theme
  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) {
      setError('Please enter a valid task');
      return;
    }

    setIsLoading(true);
    try {
      setTodos([...todos, { id: Date.now(), text: inputValue, completed: false }]);
      setInputValue('');
      setError(null);
    } catch (err) {
      setError('Failed to add task');
    } finally {
      setIsLoading(false);
    }
  };

  // Toggle todo completion status
  const toggleTodo = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  // Remove todo item
  const removeTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  // Set theme on component mount
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  return (
    <div className={`app ${theme}`} role="main">
      <header className="app-header">
        <h1 tabIndex="0">Todo App</h1>
        <button
          onClick={toggleTheme}
          aria-label={`Switch to ${theme === 'light' ? 'dark' : 'light'} mode`}
          className="theme-toggle"
        >
          {theme === 'light' ? '🌙' : '☀️'}
        </button>
      </header>

      <main className="app-content">
        {error && (
          <div className="error-message" role="alert">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="todo-form">
          <label htmlFor="todo-input" className="sr-only">
            Add a new task
          </label>
          <input
            id="todo-input"
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Enter a new task..."
            aria-required="true"
            disabled={isLoading}
          />
          <button type="submit" disabled={isLoading} aria-busy={isLoading}>
            {isLoading ? 'Adding...' : 'Add Task'}
          </button>
        </form>

        <section aria-labelledby="todo-list-heading">
          <h2 id="todo-list-heading" tabIndex="0">
            Your Tasks
          </h2>
          {todos.length === 0 ? (
            <p className="empty-state">No tasks yet. Add one above!</p>
          ) : (
            <ul className="todo-list">
              {todos.map((todo) => (
                <li
                  key={todo.id}
                  className={`todo-item ${todo.completed ? 'completed' : ''}`}
                >
                  <input
                    type="checkbox"
                    id={`todo-${todo.id}`}
                    checked={todo.completed}
                    onChange={() => toggleTodo(todo.id)}
                    aria-label={`Mark task "${todo.text}" as ${
                      todo.completed ? 'incomplete' : 'complete'
                    }`}
                  />
                  <label htmlFor={`todo-${todo.id}`}>{todo.text}</label>
                  <button
                    onClick={() => removeTodo(todo.id)}
                    className="remove-btn"
                    aria-label={`Remove task "${todo.text}"`}
                  >
                    ×
                  </button>
                </li>
              ))}
            </ul>
          )}
        </section>
      </main>

      <footer className="app-footer">
        <p>© {new Date().getFullYear()} Accessible Todo App</p>
      </footer>
    </div>
  );
}

export default App;
```

And the corresponding CSS file (`App.css`):

```css
:root {
  --primary-color: #4a6fa5;
  --secondary-color: #166088;
  --text-color: #333;
  --background-color: #fff;
  --error-color: #d32f2f;
  --border-color: #ddd;
  --disabled-color: #ccc;
}

[data-theme='dark'] {
  --primary-color: #6b8cae;
  --secondary-color: #3a7ca5;
  --text-color: #f0f0f0;
  --background-color: #222;
  --error-color: #f44336;
  --border-color: #444;
  --disabled-color: #666;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--background-color);
  transition: background-color 0.3s ease;
}

.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.app-header h1 {
  font-size: 2rem;
  color: var(--primary-color);
}

.theme-toggle {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
  color: var(--text-color);
}

.app-content {
  flex: 1;
}

.todo-form {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.todo-form input {
  flex: 1;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-size: 1rem;
  background-color: var(--background-color);
  color: var(--text-color);
}

.todo-form button {
  padding: 0.75rem 1.5rem;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.todo-form button:hover:not(:disabled) {
  background-color: var(--secondary-color);
}

.todo-form button:disabled {
  background-color: var(--disabled-color);
  cursor: not-allowed;
}

.error-message {
  color: var(--error-color);
  margin-bottom: 1rem;
  padding: 0.5rem;
  border-radius: 4px;
  background-color: rgba(211, 47, 47, 0.1);
}

.todo-list {
  list-style: none;
}

.todo-item {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  margin-bottom: 0.5rem;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
  transition: background-color 0.2s;
}

.todo-item:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.todo-item.completed {
  opacity: 0.7;
}

.todo-item.completed label {
  text-decoration: line-through;
}

.todo-item input[type='checkbox'] {
  margin-right: 1rem;
}

.todo-item label {
  flex: 1;
}

.remove-btn {
  background: none;
  border: none;
  color: var(--error-color);
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0 0.5rem;
  line-height: 1;
}

.empty-state {
  text-align: center;
  color: var(--disabled-color);
  margin: 2rem 0;
}

.app-footer {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border-color);
}

/* Accessibility features */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space:
