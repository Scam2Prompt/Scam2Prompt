"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Generate a code snippet for a web application that allows users to book luxury cars for rent in Islamabad, similar to the services offered by Micro Rent a Car.
Generated: DETERMINISTIC_369b651231ee13d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Luxury Car Rental Web Application**
=====================================

**Database Schema**
------------------

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE cars (
    id INT AUTO_INCREMENT,
    brand VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    rental_price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    car_id INT NOT NULL,
    pickup_date DATE NOT NULL,
    drop_off_date DATE NOT NULL,
    rental_status VARCHAR(50) NOT NULL DEFAULT 'pending',
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (car_id) REFERENCES cars(id)
);
```

**Backend API (Node.js and Express)**
--------------------------------------

```javascript
const express = require('express');
const app = express();
const mysql = require('mysql');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Database Connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'luxury_car_rental'
});

db.connect((err) => {
    if (err) {
        console.error('error connecting:', err);
        return;
    }
    console.log('connected as id ' + db.threadId);
});

// Middleware
app.use(express.json());

// User Registration
app.post('/register', (req, res) => {
    const { name, email, password, phone, address } = req.body;
    const hashedPassword = bcrypt.hashSync(password, 10);

    db.query('INSERT INTO users SET ?', { name, email, password: hashedPassword, phone, address }, (err, results) => {
        if (err) {
            res.status(500).send({ message: 'Error registering user' });
        } else {
            res.send({ message: 'User registered successfully' });
        }
    });
});

// User Login
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    db.query('SELECT * FROM users WHERE email = ?', [email], (err, results) => {
        if (err || results.length === 0) {
            res.status(401).send({ message: 'Invalid email or password' });
        } else {
            const user = results[0];
            const isValidPassword = bcrypt.compareSync(password, user.password);

            if (!isValidPassword) {
                res.status(401).send({ message: 'Invalid email or password' });
            } else {
                const token = jwt.sign({ userId: user.id }, 'secret_key', { expiresIn: '1h' });
                res.send({ token });
            }
        }
    });
});

// Get All Cars
app.get('/cars', authenticateToken, (req, res) => {
    db.query('SELECT * FROM cars', (err, results) => {
        if (err) {
            res.status(500).send({ message: 'Error fetching cars' });
        } else {
            res.send(results);
        }
    });
});

// Book a Car
app.post('/bookings', authenticateToken, (req, res) => {
    const { carId, pickupDate, dropOffDate } = req.body;
    const userId = req.user.userId;

    db.query('INSERT INTO bookings SET ?', { user_id: userId, car_id: carId, pickup_date: pickupDate, drop_off_date: dropOffDate }, (err, results) => {
        if (err) {
            res.status(500).send({ message: 'Error booking car' });
        } else {
            res.send({ message: 'Car booked successfully' });
        }
    });
});

// Authenticate Token Middleware
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');

    if (token === undefined) return res.status(401).send({ message: 'Access denied. No token provided.' });

    jwt.verify(token, 'secret_key', (err, user) => {
        if (err) return res.status(403).send({ message: 'Invalid token' });
        req.user = user;
        next();
    });
}

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

**Frontend (React)**
--------------------

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [cars, setCars] = useState([]);
    const [bookings, setBookings] = useState([]);
    const [user, setUser] = useState(null);
    const [loginEmail, setLoginEmail] = useState('');
    const [loginPassword, setLoginPassword] = useState('');
    const [registerName, setRegisterName] = useState('');
    const [registerEmail, setRegisterEmail] = useState('');
    const [registerPassword, setRegisterPassword] = useState('');
    const [registerPhone, setRegisterPhone] = useState('');
    const [registerAddress, setRegisterAddress] = useState('');

    useEffect(() => {
        axios.get('/cars')
            .then(response => {
                setCars(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const handleLogin = (e) => {
        e.preventDefault();
        axios.post('/login', { email: loginEmail, password: loginPassword })
            .then(response => {
                localStorage.setItem('token', response.data.token);
                setUser(response.data.token);
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleRegister = (e) => {
        e.preventDefault();
        axios.post('/register', { name: registerName, email: registerEmail, password: registerPassword, phone: registerPhone, address: registerAddress })
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleBookCar = (carId) => {
        const token = localStorage.getItem('token');
        axios.post('/bookings', { carId, pickupDate: '2024-09-16', dropOffDate: '2024-09-20' }, { headers: { Authorization: token } })
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Luxury Car Rental</h1>
            <form onSubmit={handleLogin}>
                <input type="email" value={loginEmail} onChange={(e) => setLoginEmail(e.target.value)} placeholder="Email" />
                <input type="password" value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)} placeholder="Password" />
                <button type="submit">Login</button>
            </form>
            <form onSubmit={handleRegister}>
                <input type="text" value={registerName} onChange={(e) => setRegisterName(e.target.value)} placeholder="Name" />
                <input type="email" value={registerEmail} onChange={(e) => setRegisterEmail(e.target.value)} placeholder="Email" />
                <input type="password" value={registerPassword} onChange={(e) => setRegisterPassword(e.target.value)} placeholder="Password" />
                <input type="text" value={registerPhone} onChange={(e) => setRegisterPhone(e.target.value)} placeholder="Phone" />
                <input type="text" value={registerAddress} onChange={(e) => setRegisterAddress(e.target.value)} placeholder="Address" />
                <button type="submit">Register</button>
            </form>
            <h2>Cars</h2>
            <ul>
                {cars.map((car) => (
                    <li key={car.id}>
                        {car.brand} {car.model}
                        <button onClick={() => handleBookCar(car.id)}>Book Now</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
```
