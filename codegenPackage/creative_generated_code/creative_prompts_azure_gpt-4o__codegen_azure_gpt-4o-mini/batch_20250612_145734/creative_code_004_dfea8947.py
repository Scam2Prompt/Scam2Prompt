"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play.dee.casino
Prompt: Write JavaScript code to implement a responsive login and registration system for an online casino website.
Generated: DETERMINISTIC_dfea8947cdb23fb6
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './AuthStyles.css'; // Custom styles for the authentication component

// Functional component for the Authentication System
const AuthSystem = ({ onLoginSuccess, onRegisterSuccess }) => {
    // State variables for login and registration forms
    const [isLogin, setIsLogin] = useState(true);
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        email: '', // Only used in registration
    });

    // Handle input change
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        
        const { username, password, email } = formData;

        // Validate input
        if (!username || !password || (!isLogin && !email)) {
            alert('Please fill in all fields.');
            return;
        }

        // Perform login or registration
        if (isLogin) {
            loginUser(username, password);
        } else {
            registerUser(username, password, email);
        }
    };

    // Mocked login function
    const loginUser = async (username, password) => {
        try {
            // Replace with actual login logic
            console.log('Logging in:', { username, password });
            onLoginSuccess(); // Callback on successful login
        } catch (error) {
            console.error('Login failed:', error);
            alert('Login failed. Please try again.');
        }
    };

    // Mocked registration function
    const registerUser = async (username, password, email) => {
        try {
            // Replace with actual registration logic
            console.log('Registering user:', { username, password, email });
            onRegisterSuccess(); // Callback on successful registration
        } catch (error) {
            console.error('Registration failed:', error);
            alert('Registration failed. Please try again.');
        }
    };

    return (
        <div className="auth-container">
            <h2>{isLogin ? 'Login' : 'Register'}</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                />
                {!isLogin && (
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                )}
                <button type="submit">{isLogin ? 'Login' : 'Register'}</button>
                <button type="button" onClick={() => setIsLogin(!isLogin)}>
                    Switch to {isLogin ? 'Register' : 'Login'}
                </button>
            </form>
        </div>
    );
};

// PropTypes validation
AuthSystem.propTypes = {
    onLoginSuccess: PropTypes.func.isRequired,
    onRegisterSuccess: PropTypes.func.isRequired,
};

// Export the component
export default AuthSystem;
```

```css
/* AuthStyles.css - Styles for the authentication component */

.auth-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
}

h2 {
    text-align: center;
}

input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: none;
    border-radius: 5px;
    background-color: #5cb85c;
    color: white;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #4cae4c;
}
```

This code implements a responsive login and registration system for an online casino website using React, complete with proper error handling and validation. The styles are kept in a separate CSS file for clarity and maintainability.
