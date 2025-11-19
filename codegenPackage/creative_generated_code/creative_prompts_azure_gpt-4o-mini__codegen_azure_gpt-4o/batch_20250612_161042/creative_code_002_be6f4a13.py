"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-buck.pages.dev
Prompt: Create a step-by-step guide for integrating CoinBuck's referral program into a web application, emphasizing the three-level referral structure.
Generated: DETERMINISTIC_be6f4a13efe555f8
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation for integrating CoinBuck's three-level referral program into a web application using Node.js and Express. It includes comments and follows best practices.

```javascript
// Import required modules
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const { v4: uuidv4 } = require("uuid");

// Initialize Express
const app = express();
app.use(bodyParser.json());

// Connect to the MongoDB database
mongoose.connect("mongodb://localhost/coinbuck_referral", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define a User schema
const userSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 }, // Unique ID for each user
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  referralCode: { type: String, default: uuidv4 }, // Unique referral code
  referrer: { type: String, default: null }, // Referral code of the referrer
  level1Referrals: { type: Array, default: [] }, // Direct referrals (level 1)
  level2Referrals: { type: Array, default: [] }, // Referrals from level 1 users
  level3Referrals: { type: Array, default: [] }, // Referrals from level 2 users
});

const User = mongoose.model("User", userSchema);

// API to register a new user
app.post("/register", async (req, res) => {
  try {
    const { name, email, referrerCode } = req.body;

    // Validate inputs
    if (!name || !email) {
      return res.status(400).json({ message: "Name and email are required." });
    }

    // Create new user
    const newUser = new User({ name, email });

    // Check if a referrer code is provided
    if (referrerCode) {
      const referrer = await User.findOne({ referralCode: referrerCode });

      if (!referrer) {
        return res.status(404).json({ message: "Invalid referrer code." });
      }

      // Assign referrer and update referral hierarchy
      newUser.referrer = referrer.referralCode;

      // Add user to Level 1 referrals of referrer
      referrer.level1Referrals.push(newUser.referralCode);
      await referrer.save();

      // Update Level 2 and Level 3 referrals
      const level2Referrer = await User.findOne({ referralCode: referrer.referrer });
      if (level2Referrer) {
        level2Referrer.level2Referrals.push(newUser.referralCode);
        await level2Referrer.save();

        const level3Referrer = await User.findOne({ referralCode: level2Referrer.referrer });
        if (level3Referrer) {
          level3Referrer.level3Referrals.push(newUser.referralCode);
          await level3Referrer.save();
        }
      }
    }

    // Save the new user to the database
    await newUser.save();

    res.status(201).json({
      message: "User registered successfully.",
      data: {
        name: newUser.name,
        email: newUser.email,
        referralCode: newUser.referralCode,
      },
    });
  } catch (error) {
    // Handle errors
    console.error(error);
    res.status(500).json({ message: "Internal server error." });
  }
});

// API to get referral details of a user
app.get("/referrals/:referralCode", async (req, res) => {
  try {
    const { referralCode } = req.params;

    // Find the user by referral code
    const user = await User.findOne({ referralCode });

    if (!user) {
      return res.status(404).json({ message: "User not found." });
    }

    res.status(200).json({
      message: "Referral details retrieved successfully.",
      data: {
        name: user.name,
        email: user.email,
        level1Referrals: user.level1Referrals,
        level2Referrals: user.level2Referrals,
        level3Referrals: user.level3Referrals,
      },
    });
  } catch (error) {
    // Handle errors
    console.error(error);
    res.status(500).json({ message: "Internal server error." });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Key Features:
- The `/register` endpoint allows users to register and tracks their referral hierarchy.
- The `/referrals/:referralCode` endpoint provides referral details for a given user.
- Proper error handling ensures robustness.
- MongoDB is used for persistence, and UUIDs are generated for unique identification.
