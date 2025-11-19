"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleoplan.com
Prompt: Develop a user interface in React that allows users to log in to their Aleo Plan account, incorporating language options as mentioned on the site.
Generated: DETERMINISTIC_254bd5a20f3e48a3
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';
import './LoginPage.css'; // Assuming there's a CSS file for styling

const LoginPage = ({ languages, onLoginSuccess }) => {
    // State variables for storing user inputs and error messages
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [selectedLanguage, setSelectedLanguage] = useState(languages[0]);
    const [errorMessage, setErrorMessage] = useState('');

    // Handler for login form submission
    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent page reload

        // Clear previous error messages
        setErrorMessage('');

        try {
            // Send login request to the server
            const response = await axios.post('/api/login', { username, password });

            // Check if login was successful
            if (response.data.success) {
                onLoginSuccess(response.data.user); // Call success callback
            } else {
                throw new Error(response.data.message); // Throw error for handling
            }
        } catch (error) {
            // Handle errors (network or server)
            setErrorMessage(error.message || 'Login failed. Please try again.');
        }
    };

    return (
        <div className="login-container">
            <h2>{selectedLanguage === 'en' ? 'Login to your Aleo Plan Account' : 'Iniciar sesión en su cuenta de Aleo Plan'}</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="username">{selectedLanguage === 'en' ? 'Username' : 'Nombre de usuario'}</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">{selectedLanguage === 'en' ? 'Password' : 'Contraseña'}</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="language-select">{selectedLanguage === 'en' ? 'Select Language' : 'Seleccionar idioma'}</label>
                    <select
                        id="language-select"
                        value={selectedLanguage}
                        onChange={(e) => setSelectedLanguage(e.target.value)}
                    >
                        {languages.map((lang) => (
                            <option key={lang} value={lang}>
                                {lang}
                            </option>
                        ))}
                    </select>
                </div>
                {errorMessage && <div className="error-message">{errorMessage}</div>}
                <button type="submit">{selectedLanguage === 'en' ? 'Login' : 'Iniciar sesión'}</button>
            </form>
        </div>
    );
};

// PropTypes validation for component props
LoginPage.propTypes = {
    languages: PropTypes.arrayOf(PropTypes.string).isRequired,
    onLoginSuccess: PropTypes.func.isRequired,
};

export default LoginPage;
```
