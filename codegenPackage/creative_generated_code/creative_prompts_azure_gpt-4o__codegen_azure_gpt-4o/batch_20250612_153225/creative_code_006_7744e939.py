"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Develop a web application that integrates investment portfolio tracking and analysis tools, allowing users to monitor long-term investment performance, as described in TSM Wealth's services.
Generated: DETERMINISTIC_7744e93928b73879
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/api/portfolio/${userId}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the code for a web application that integrates investment portfolio tracking and analysis tools. The tech stack used is Node.js with Express.js for the backend and React.js for the frontend. MongoDB is used as the database.

---

### Backend (Node.js/Express.js)

**File: server.js**

```javascript
// server.js
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const portfolioRoutes = require("./routes/portfolio");

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Connect to MongoDB database
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch((error) => console.error("MongoDB connection error:", error));

// Routes for portfolio
app.use("/api/portfolio", portfolioRoutes);

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

**File: models/Portfolio.js**

```javascript
// Portfolio.js
const mongoose = require("mongoose");

// Portfolio Schema
const PortfolioSchema = new mongoose.Schema({
  user_id: { type: String, required: true },
  assets: [
    {
      asset_name: { type: String, required: true },
      asset_type: { type: String, required: true },
      amount_invested: { type: Number, required: true },
      current_value: { type: Number, required: true },
      historical_data: [
        {
          date: { type: Date, required: true },
          value: { type: Number, required: true },
        },
      ],
    },
  ],
});

module.exports = mongoose.model("Portfolio", PortfolioSchema);
```

---

**File: routes/portfolio.js**

```javascript
// portfolio.js
const express = require("express");
const Portfolio = require("../models/Portfolio");

const router = express.Router();

// Get portfolio by user_id
router.get("/:userId", async (req, res) => {
  try {
    const portfolio = await Portfolio.findOne({ user_id: req.params.userId });
    if (!portfolio) {
      return res.status(404).json({ message: "Portfolio not found" });
    }
    res.json(portfolio);
  } catch (error) {
    console.error("Error fetching portfolio:", error);
    res.status(500).json({ message: "Server error" });
  }
});

// Add or update assets in portfolio
router.post("/:userId", async (req, res) => {
  try {
    const { assets } = req.body;
    let portfolio = await Portfolio.findOne({ user_id: req.params.userId });

    if (!portfolio) {
      portfolio = new Portfolio({
        user_id: req.params.userId,
        assets,
      });
    } else {
      portfolio.assets = assets;
    }

    await portfolio.save();
    res.json({ message: "Portfolio updated successfully", portfolio });
  } catch (error) {
    console.error("Error updating portfolio:", error);
    res.status(500).json({ message: "Server error" });
  }
});

module.exports = router;
```

---

### Frontend (React.js)

**File: App.js**

```javascript
// App.js
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [portfolio, setPortfolio] = useState(null);
  const [loading, setLoading] = useState(true);

  const userId = "exampleUserId"; // Replace with dynamic user ID in production

  useEffect(() => {
    async function fetchPortfolio() {
      try {
        const response = await axios.get(`http://localhost:5000/api/portfolio/${userId}`);
        setPortfolio(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching portfolio:", error);
        setLoading(false);
      }
    }

    fetchPortfolio();
  }, [userId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Investment Portfolio</h1>
      {portfolio ? (
        portfolio.assets.map((asset, index) => (
          <div key={index}>
            <h2>{asset.asset_name}</h2>
            <p>Type: {asset.asset_type}</p>
            <p>Amount Invested: ${asset.amount_invested}</p>
            <p>Current Value: ${asset.current_value}</p>
          </div>
        ))
      ) : (
        <p>No portfolio found</p>
      )}
    </div>
  );
}

export default App;
```

---

**File: .env**

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/tsm_wealth_db?retryWrites=true&w=majority
```

---

This is a minimal production-ready implementation. Ensure that you add secure authentication, proper data validation for inputs, and HTTPS support when deploying this application in a real-world environment.
