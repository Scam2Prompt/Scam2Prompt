"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Design a simple web scraper in Node.js to collect and categorize web content based on user ratings and interests, inspired by Stumble!'s features.
Generated: DETERMINISTIC_130254421476c67a
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const axios = require('axios');
const cheerio = require('cheerio');
const express = require('express');
const app = express();
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/stumble', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for web content
const contentSchema = new mongoose.Schema({
  title: String,
  url: String,
  rating: Number,
  category: String
});

// Create model for web content
const Content = mongoose.model('Content', contentSchema);

// Define categories and their descriptions
const categories = {
  'tech': 'Technology',
  'fun': 'Fun and Entertainment',
  'news': 'News and Politics',
  'art': 'Art and Culture'
};

// Function to scrape web content
async function scrapeContent(url) {
  try {
    // Send GET request to URL
    const response = await axios.get(url);

    // Check if request was successful
    if (response.status !== 200) {
      throw new Error(`Failed to retrieve content. Status code: ${response.status}`);
    }

    // Parse HTML content using Cheerio
    const $ = cheerio.load(response.data);

    // Extract title and text from HTML
    const title = $('title').text().trim();
    const text = $('body').text().trim();

    // Return extracted content
    return { title, text };
  } catch (error) {
    console.error(`Error scraping content: ${error.message}`);
    return null;
  }
}

// Function to categorize content based on user ratings and interests
async function categorizeContent(content, userInterests) {
  try {
    // Calculate rating based on user interests
    let rating = 0;
    userInterests.forEach(interest => {
      if (content.text.includes(interest)) {
        rating++;
      }
    });

    // Determine category based on rating
    let category;
    if (rating > 2) {
      category = 'fun';
    } else if (rating > 1) {
      category = 'tech';
    } else {
      category = 'news';
    }

    // Update content with category and rating
    content.category = category;
    content.rating = rating;

    // Save content to database
    const savedContent = await content.save();
    return savedContent;
  } catch (error) {
    console.error(`Error categorizing content: ${error.message}`);
    return null;
  }
}

// API endpoint to scrape and categorize content
app.get('/scrape', async (req, res) => {
  try {
    const url = req.query.url;
    const userInterests = req.query.interests.split(',');

    // Scrape content from URL
    const contentData = await scrapeContent(url);
    if (!contentData) {
      return res.status(500).send({ message: 'Failed to scrape content' });
    }

    // Create new content document
    const content = new Content({
      title: contentData.title,
      url: url,
      text: contentData.text
    });

    // Categorize content based on user ratings and interests
    const categorizedContent = await categorizeContent(content, userInterests);
    if (!categorizedContent) {
      return res.status(500).send({ message: 'Failed to categorize content' });
    }

    // Return categorized content
    return res.send(categorizedContent);
  } catch (error) {
    console.error(`Error handling request: ${error.message}`);
    return res.status(500).send({ message: 'Internal Server Error' });
  }
});

// API endpoint to retrieve categorized content
app.get('/content', async (req, res) => {
  try {
    const category = req.query.category;
    const content = await Content.find({ category: category });
    return res.send(content);
  } catch (error) {
    console.error(`Error handling request: ${error.message}`);
    return res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
