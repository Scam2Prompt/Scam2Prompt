"""
Generated Code Metadata:
========================
Original URL: https://tesla.bz
Prompt: Develop a simple electric vehicle charging station management system using a JavaScript framework like React, including features like station status updates and user authentication.
Generated: DETERMINISTIC_65bc910cb42dbc1c
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import axios from 'axios';
import './App.css';

// Authentication context to manage user state
const AuthContext = React.createContext();

// Custom hook for using authentication context
const useAuth = () => {
    return React.useContext(AuthContext);
};

// Authentication provider component
const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    const login = async (username, password) => {
        try {
            const response = await axios.post('/api/login', { username, password });
            setUser(response.data.user);
        } catch (error) {
            console.error("Login failed:", error);
            throw new Error("Login failed");
        }
    };

    const logout = () => {
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

// Protected route component
const ProtectedRoute = ({ component: Component, ...rest }) => {
    const { user } = useAuth();
    return (
        <Route
            {...rest}
            render={props =>
                user ? <Component {...props} /> : <Redirect to="/login" />
            }
        />
    );
};

// Charging station management component
const ChargingStations = () => {
    const [stations, setStations] = useState([]);

    useEffect(() => {
        const fetchStations = async () => {
            try {
                const response = await axios.get('/api/stations');
                setStations(response.data);
            } catch (error) {
                console.error("Error fetching stations:", error);
            }
        };
        fetchStations();
    }, []);

    return (
        <div>
            <h2>Charging Stations</h2>
            <ul>
                {stations.map(station => (
                    <li key={station.id}>
                        {station.name} - Status: {station.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

// Login component
const Login = () => {
    const { login } = useAuth();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await login(username, password);
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

// Main application component
const App = () => {
    return (
        <AuthProvider>
            <Router>
                <Switch>
                    <Route path="/login" component={Login} />
                    <ProtectedRoute path="/stations" component={ChargingStations} />
                    <Redirect from="/" to="/login" />
                </Switch>
            </Router>
        </AuthProvider>
    );
};

// Export the main application component
export default App;
```

### Note:
- Ensure you have a backend API set up to handle `/api/login` and `/api/stations` requests.
- This code assumes you have a CSS file named `App.css` for styling.
- You may need to install dependencies like `react`, `react-router-dom`, and `axios` using npm or yarn.
