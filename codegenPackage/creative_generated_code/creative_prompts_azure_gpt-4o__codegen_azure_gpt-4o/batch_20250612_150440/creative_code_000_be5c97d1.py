"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: Write a MERN stack web application that includes a responsive design using React for the front-end, Node.js for the back-end, and MongoDB for the database. Reference the skills and expertise described on Muhammed Ashkar's portfolio website.
Generated: DETERMINISTIC_be5c97d14d3a9789
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Project Structure
```
mern-portfolio/
├── backend/
│   ├── server.js
│   ├── routes/
│   │   └── skillsRoutes.js
│   ├── models/
│   │   └── Skill.js
│   ├── controllers/
│       └── skillsController.js
│   └── config/
│       └── db.js
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.js
│   │   │   └── SkillList.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── styles.css
├── .env
└── package.json
```

---

### Backend Code

#### `backend/server.js`
```javascript
const express = require("express");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
const skillsRoutes = require("./routes/skillsRoutes");

// Load environment variables
dotenv.config();

// Connect to MongoDB
connectDB();

const app = express();

// Middleware
app.use(express.json());

// Routes
app.use("/api/skills", skillsRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.message);
  res.status(500).json({ error: "Server Error" });
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

#### `backend/config/db.js`
```javascript
const mongoose = require("mongoose");

const connectDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log(`MongoDB connected: ${conn.connection.host}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1); // Exit process with failure
  }
};

module.exports = connectDB;
```

#### `backend/models/Skill.js`
```javascript
const mongoose = require("mongoose");

const skillSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String, required: true },
});

module.exports = mongoose.model("Skill", skillSchema);
```

#### `backend/controllers/skillsController.js`
```javascript
const Skill = require("../models/Skill");

// @desc Get all skills
// @route GET /api/skills
// @access Public
const getSkills = async (req, res) => {
  try {
    const skills = await Skill.find();
    res.json(skills);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch skills" });
  }
};

// @desc Add a new skill
// @route POST /api/skills
// @access Public
const addSkill = async (req, res) => {
  const { name, description } = req.body;

  if (!name || !description) {
    return res.status(400).json({ error: "All fields are required" });
  }

  try {
    const skill = new Skill({ name, description });
    await skill.save();
    res.status(201).json(skill);
  } catch (error) {
    res.status(500).json({ error: "Failed to add skill" });
  }
};

module.exports = { getSkills, addSkill };
```

#### `backend/routes/skillsRoutes.js`
```javascript
const express = require("express");
const { getSkills, addSkill } = require("../controllers/skillsController");

const router = express.Router();

router.route("/").get(getSkills).post(addSkill);

module.exports = router;
```

---

### Frontend Code

#### `frontend/src/index.js`
```javascript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

#### `frontend/src/App.js`
```javascript
import React from "react";
import Header from "./components/Header";
import SkillList from "./components/SkillList";

function App() {
  return (
    <div>
      <Header />
      <div className="container">
        <SkillList />
      </div>
    </div>
  );
}

export default App;
```

#### `frontend/src/components/Header.js`
```javascript
import React from "react";

function Header() {
  return (
    <header className="header">
      <h1>Muhammed Ashkar's Skills</h1>
    </header>
  );
}

export default Header;
```

#### `frontend/src/components/SkillList.js`
```javascript
import React, { useEffect, useState } from "react";

function SkillList() {
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    const fetchSkills = async () => {
      try {
        const response = await fetch("/api/skills");
        const data = await response.json();
        setSkills(data);
      } catch (error) {
        console.error("Error fetching skills:", error);
      }
    };

    fetchSkills();
  }, []);

  return (
    <div className="skills">
      <h2>My Skills</h2>
      <ul>
        {skills.map((skill) => (
          <li key={skill._id}>
            <strong>{skill.name}</strong>: {skill.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SkillList;
```

#### `frontend/src/styles.css`
```css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.header {
  background: #333;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}

.container {
  margin: 20px auto;
  max-width: 800px;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.skills ul {
  list-style-type: none;
  padding: 0;
}

.skills li {
  border-bottom: 1px solid #ddd;
  padding: 10px 0;
}

.skills li:last-child {
  border-bottom: none;
}
```

---

### `.env`
```
MONGO_URI=your_mongodb_connection_string
```

---

### Notes
1. Install dependencies:
   - Backend: `npm install express mongoose dotenv`
   - Frontend: `npm install`

2. Run the backend server: `node server.js`
3. Start the frontend with `npm start` in the `frontend/` directory.
