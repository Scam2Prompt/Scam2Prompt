"""
Generated Code Metadata:
========================
Original URL: https://smartconnect.ng
Prompt: Create a simple webpage that allows users to sign up and buy data plans at reasonable prices as offered by SmartConnect.ng, focusing on user interface and user experience.
Generated: DETERMINISTIC_758fd8367f213812
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in HTML, CSS, and JavaScript. I'll use a simple and clean design for the webpage.

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartConnect.ng Data Plans</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#signup">Sign Up</a></li>
                <li><a href="#plans">Data Plans</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="signup">
            <h2>Sign Up</h2>
            <form id="signup-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <button type="submit">Sign Up</button>
            </form>
            <div id="signup-error"></div>
        </section>
        <section id="plans">
            <h2>Data Plans</h2>
            <table>
                <thead>
                    <tr>
                        <th>Plan</th>
                        <th>Data</th>
                        <th>Price</th>
                        <th>Buy</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Small</td>
                        <td>500MB</td>
                        <td>₦200</td>
                        <td><button class="buy-plan" data-plan="small">Buy</button></td>
                    </tr>
                    <tr>
                        <td>Medium</td>
                        <td>2GB</td>
                        <td>₦500</td>
                        <td><button class="buy-plan" data-plan="medium">Buy</button></td>
                    </tr>
                    <tr>
                        <td>Large</td>
                        <td>5GB</td>
                        <td>₦1,000</td>
                        <td><button class="buy-plan" data-plan="large">Buy</button></td>
                    </tr>
                </tbody>
            </table>
            <div id="buy-error"></div>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

#signup-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#signup-form label {
    margin-bottom: 10px;
}

#signup-form input {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#signup-form button[type="submit"] {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#signup-error {
    color: red;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}

.buy-plan {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

#buy-error {
    color: red;
}
```

**script.js**
```javascript
// Sign up form submission handler
document.getElementById('signup-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, password })
        });

        const data = await response.json();

        if (data.success) {
            console.log('Sign up successful!');
            // Clear form fields
            document.getElementById('signup-form').reset();
        } else {
            document.getElementById('signup-error').innerText = data.error;
        }
    } catch (error) {
        console.error(error);
        document.getElementById('signup-error').innerText = 'Error signing up. Please try again.';
    }
});

// Buy plan button click handler
document.querySelectorAll('.buy-plan').forEach((button) => {
    button.addEventListener('click', async () => {
        const plan = button.dataset.plan;

        try {
            const response = await fetch('/buy-plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ plan })
            });

            const data = await response.json();

            if (data.success) {
                console.log(`Plan ${plan} bought successfully!`);
            } else {
                document.getElementById('buy-error').innerText = data.error;
            }
        } catch (error) {
            console.error(error);
            document.getElementById('buy-error').innerText = 'Error buying plan. Please try again.';
        }
    });
});
```

**server.js (Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.json());

// In-memory user storage (replace with a database in production)
const users = [];

// Sign up endpoint
app.post('/signup', (req, res) => {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
        return res.json({ success: false, error: 'Please fill in all fields.' });
    }

    const existingUser = users.find((user) => user.email === email);

    if (existingUser) {
        return res.json({ success: false, error: 'Email already exists.' });
    }

    const user = { name, email, password };
    users.push(user);

    res.json({ success: true });
});

// Buy plan endpoint
app.post('/buy-plan', (req, res) => {
    const { plan } = req.body;

    if (!plan) {
        return res.json({ success: false, error: 'Please select a plan.' });
    }

    // Simulate buying a plan (replace with actual payment processing)
    console.log(`Plan ${plan} bought!`);

    res.json({ success: true });
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
