"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: Explain how to use Sui’s zkLogin authentication for secure user login and provide code examples for integration into a Web3 application.
Generated: DETERMINISTIC_cd6439a3c8ee939f
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { zkLogin } from 'sui-zklogin'; // Assuming 'sui-zklogin' is the library for zkLogin
import { useEffect, useState } from 'react';

// Define a functional component for the Web3 application
const Web3Login = () => {
    // State to manage user authentication status
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [error, setError] = useState(null);

    // Function to handle user login
    const handleLogin = async () => {
        try {
            // Initiate zkLogin process
            const user = await zkLogin.login();
            // Check if user is successfully authenticated
            if (user) {
                setIsAuthenticated(true);
                console.log('User authenticated:', user);
                // You can store user information in local storage or state management
                localStorage.setItem('user', JSON.stringify(user));
            }
        } catch (err) {
            // Handle any errors during the login process
            console.error('Login failed:', err);
            setError('Login failed. Please try again.');
        }
    };

    // Function to handle user logout
    const handleLogout = () => {
        // Clear user data and update authentication status
        localStorage.removeItem('user');
        setIsAuthenticated(false);
        console.log('User logged out');
    };

    // Effect to check if user is already logged in on component mount
    useEffect(() => {
        const user = localStorage.getItem('user');
        if (user) {
            setIsAuthenticated(true);
            console.log('User is already logged in:', JSON.parse(user));
        }
    }, []);

    return (
        <div>
            <h1>Web3 Application Login</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {isAuthenticated ? (
                <div>
                    <p>Welcome back!</p>
                    <button onClick={handleLogout}>Logout</button>
                </div>
            ) : (
                <button onClick={handleLogin}>Login with zkLogin</button>
            )}
        </div>
    );
};

export default Web3Login;
```

### Notes:
- Ensure that you have the `sui-zklogin` library installed in your project.
- This code is a React functional component that handles user authentication using Sui's zkLogin.
- Proper error handling is included to manage login failures.
- User authentication status is managed using React's state and local storage.
