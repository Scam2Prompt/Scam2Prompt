"""
Generated Code Metadata:
========================
Original URL: https://akaan.com.tr
Prompt: Create a sample project structure for a corporate website that is both mobile and SEO-friendly, as described by Akaan.
Generated: DETERMINISTIC_c4bd3c324ff52244
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Project Structure:**
```markdown
# Project Structure
- config/
  - db.js
  - env.js
- controllers/
  - home.js
  - about.js
  - services.js
- models/
  - user.js
  - page.js
- public/
  - index.html
  - favicon.ico
  - images/
  - styles/
    - global.css
  - scripts/
    - main.js
- routes/
  - index.js
  - home.js
  - about.js
- services/
  - database.js
  - mail.js
- utils/
  - auth.js
  - helpers.js
- app.js
- package.json
```

**package.json:**
```json
{
  "name": "corporate-website",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "morgan": "^1.10.0",
    "nodemon": "^2.0.7"
  }
}
```

**app.js:**
```javascript
// Import required modules
const express = require('express');
const morgan = require('morgan');
const mongoose = require('mongoose');
const homeRoutes = require('./routes/home');
const aboutRoutes = require('./routes/about');

// Create Express app
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/corporate-website', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Middlewares
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Routes
app.use('/', homeRoutes);
app.use('/about', aboutRoutes);

// Error handling
app.use((req, res, next) => {
  const error = new Error('Not found');
  error.status = 404;
  next(error);
});

app.use((error, req, res, next) => {
  console.error(error);
  res.status(error.status || 500);
  res.json({ error: error.message });
});

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```

**routes/home.js:**
```javascript
// Import required modules
const express = require('express');
const router = express.Router();
const homeController = require('../controllers/home');

// Routes
router.get('/', homeController.getHome);
router.get('/services', homeController.getServices);

module.exports = router;
```

**controllers/home.js:**
```javascript
// Import required modules
const pageModel = require('../models/page');

// Home controller
exports.getHome = async (req, res, next) => {
  try {
    const page = await pageModel.findOne({ slug: 'home' });
    res.render('index', { page });
  } catch (error) {
    next(error);
  }
};

exports.getServices = async (req, res, next) => {
  try {
    const page = await pageModel.findOne({ slug: 'services' });
    res.json({ page });
  } catch (error) {
    next(error);
  }
};
```

**models/page.js:**
```javascript
// Import required modules
const mongoose = require('mongoose');

// Page schema
const pageSchema = new mongoose.Schema({
  slug: String,
  title: String,
  content: String,
});

// Page model
const Page = mongoose.model('Page', pageSchema);

module.exports = Page;
```

**public/index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Corporate Website</title>
  <link rel="stylesheet" href="styles/global.css">
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <h1>{{ page.title }}</h1>
    <p>{{ page.content }}</p>
  </main>
  <script src="scripts/main.js"></script>
</body>
</html>
```

**public/styles/global.css:**
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

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

nav li {
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2em;
}
```
