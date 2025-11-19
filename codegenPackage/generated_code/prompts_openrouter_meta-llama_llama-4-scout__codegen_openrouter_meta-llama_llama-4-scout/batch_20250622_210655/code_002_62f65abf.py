"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Design a community manager tool using Node.js and Express.js that integrates with social media platforms, inspired by moOve's social media marketing services.
Generated: DETERMINISTIC_62f65abf6658a38d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const passport = require('passport');
const FacebookStrategy = require('passport-facebook').Strategy;
const TwitterStrategy = require('passport-twitter').Strategy;
const InstagramStrategy = require('passport-instagram').Strategy;
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for social media accounts
const socialMediaAccountSchema = new mongoose.Schema({
  platform: String,
  username: String,
  accessToken: String,
  refreshToken: String,
});

// Define schema for community manager
const communityManagerSchema = new mongoose.Schema({
  name: String,
  email: String,
  socialMediaAccounts: [socialMediaAccountSchema],
});

// Compile schemas into models
const SocialMediaAccount = mongoose.model('SocialMediaAccount', socialMediaAccountSchema);
const CommunityManager = mongoose.model('CommunityManager', communityManagerSchema);

// Configure Passport.js
passport.use(new FacebookStrategy({
  clientID: process.env.FACEBOOK_APP_ID,
  clientSecret: process.env.FACEBOOK_APP_SECRET,
  callbackURL: '/auth/facebook/callback',
}, (accessToken, refreshToken, profile, cb) => {
  // Find or create Facebook account
  SocialMediaAccount.findOne({ platform: 'facebook', username: profile.username }, (err, account) => {
    if (err) return cb(err);
    if (!account) {
      account = new SocialMediaAccount({
        platform: 'facebook',
        username: profile.username,
        accessToken,
        refreshToken,
      });
      account.save((err) => {
        if (err) return cb(err);
        cb(null, account);
      });
    } else {
      account.accessToken = accessToken;
      account.refreshToken = refreshToken;
      account.save((err) => {
        if (err) return cb(err);
        cb(null, account);
      });
    }
  });
}));

passport.use(new TwitterStrategy({
  consumerKey: process.env.TWITTER_CONSUMER_KEY,
  consumerSecret: process.env.TWITTER_CONSUMER_SECRET,
  callbackURL: '/auth/twitter/callback',
}, (token, tokenSecret, profile, cb) => {
  // Find or create Twitter account
  SocialMediaAccount.findOne({ platform: 'twitter', username: profile.username }, (err, account) => {
    if (err) return cb(err);
    if (!account) {
      account = new SocialMediaAccount({
        platform: 'twitter',
        username: profile.username,
        accessToken: token,
        refreshToken: tokenSecret,
      });
      account.save((err) => {
        if (err) return cb(err);
        cb(null, account);
      });
    } else {
      account.accessToken = token;
      account.refreshToken = tokenSecret;
      account.save((err) => {
        if (err) return cb(err);
        cb(null, account);
      });
    }
  });
}));

passport.use(new InstagramStrategy({
  clientID: process.env.INSTAGRAM_CLIENT_ID,
  clientSecret: process.env.INSTAGRAM_CLIENT_SECRET,
  callbackURL: '/auth/instagram/callback',
}, (accessToken, refreshToken, profile, cb) => {
  // Find or create Instagram account
  SocialMediaAccount.findOne({ platform: 'instagram', username: profile.username }, (err, account) => {
    if (err) return cb(err);
    if (!account) {
      account = new SocialMediaAccount({
        platform: 'instagram',
        username: profile.username,
        accessToken,
        refreshToken,
      });
      account.save((err) => {
        if (err) return cb(err);
        cb(null, account);
      });
    } else {
      account.accessToken = accessToken;
      account.refreshToken = refreshToken;
      account.save((err) => {
        if (err) return cb(err);
        cb(null, account);
      });
    }
  });
}));

// Serialize and deserialize user
passport.serializeUser((user, cb) => {
  cb(null, user.id);
});

passport.deserializeUser((id, cb) => {
  CommunityManager.findById(id, (err, user) => {
    cb(err, user);
  });
});

// Express middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(passport.initialize());
app.use(passport.session());

// Routes
app.get('/auth/facebook', passport.authenticate('facebook'));
app.get('/auth/facebook/callback', passport.authenticate('facebook', { failureRedirect: '/login' }), (req, res) => {
  res.redirect('/');
});

app.get('/auth/twitter', passport.authenticate('twitter'));
app.get('/auth/twitter/callback', passport.authenticate('twitter', { failureRedirect: '/login' }), (req, res) => {
  res.redirect('/');
});

app.get('/auth/instagram', passport.authenticate('instagram'));
app.get('/auth/instagram/callback', passport.authenticate('instagram', { failureRedirect: '/login' }), (req, res) => {
  res.redirect('/');
});

app.get('/community-manager', (req, res) => {
  CommunityManager.find().populate('socialMediaAccounts').exec((err, communityManagers) => {
    if (err) return res.status(500).send({ message: 'Error fetching community managers' });
    res.send(communityManagers);
  });
});

app.post('/community-manager', (req, res) => {
  const communityManager = new CommunityManager(req.body);
  communityManager.save((err) => {
    if (err) return res.status(400).send({ message: 'Error creating community manager' });
    res.send({ message: 'Community manager created successfully' });
  });
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
