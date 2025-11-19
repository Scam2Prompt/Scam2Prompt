"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Develop a simple chatbot using Node.js and natural language processing (NLP) to provide customer support for a skincare e-commerce site like Fresh N Glow, answering common questions about products and orders.
Generated: DETERMINISTIC_1e71390e63f6a66b
Batch ID: 20250622_205709
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
const bodyParser = require('body-parser');
const natural = require('natural');
const { WordTokenizer, PorterStemmer } = natural;
const aposToLexForm = require('apos-to-lex-form');
const SpellCorrector = require('spelling-corrector');
const stopword = require('stopword');

// Initialize the application
const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Initialize NLP tools
const tokenizer = new WordTokenizer();
const spellCorrector = new SpellCorrector();
spellCorrector.loadDictionary();

// Sample product database
const products = [
  { id: 1, name: 'Hydrating Serum', category: 'serum', price: 29.99 },
  { id: 2, name: 'Vitamin C Cream', category: 'moisturizer', price: 24.99 },
  { id: 3, name: 'Gentle Cleanser', category: 'cleanser', price: 19.99 }
];

// Sample order database
const orders = [
  { id: 1001, customer: 'john@example.com', products: [1, 2], status: 'shipped' },
  { id: 1002, customer: 'jane@example.com', products: [3], status: 'processing' }
];

// Preprocess text for NLP
function preprocessText(text) {
  // Convert to lowercase
  const lexed = aposToLexForm(text).toLowerCase();
  
  // Tokenize
  const tokenized = tokenizer.tokenize(lexed);
  
  // Correct spelling
  const corrected = tokenized.map(word => spellCorrector.correct(word));
  
  // Remove stopwords
  const filtered = stopword.removeStopwords(corrected);
  
  // Stem words
  const stemmed = filtered.map(word => PorterStemmer.stem(word));
  
  return stemmed;
}

// Intent classification
function classifyIntent(processedText) {
  const keywords = {
    product: ['product', 'item', 'buy', 'purchase', 'serum', 'cream', 'cleanser'],
    order: ['order', 'status', 'track', 'deliver', 'ship'],
    return: ['return', 'refund', 'exchange'],
    contact: ['contact', 'help', 'support', 'email', 'phone']
  };

  for (const [intent, terms] of Object.entries(keywords)) {
    if (terms.some(term => processedText.includes(term))) {
      return intent;
    }
  }
  
  return 'unknown';
}

// Generate response based on intent
function generateResponse(intent, processedText) {
  switch (intent) {
    case 'product':
      const productCategory = processedText.find(word => 
        ['serum', 'moisturizer', 'cleanser'].includes(word)
      );
      
      if (productCategory) {
        const categoryProducts = products.filter(p => p.category === productCategory);
        return {
          response: `Here are our ${productCategory} products:`,
          data: categoryProducts
        };
      } else {
        return {
          response: 'Here are all our products:',
          data: products
        };
      }
      
    case 'order':
      return {
        response: 'To check your order status, please provide your order ID or email address.'
      };
      
    case 'return':
      return {
        response: 'Our return policy allows returns within 30 days of purchase. Please contact support for assistance.'
      };
      
    case 'contact':
      return {
        response: 'You can contact our support team at support@freshnglow.com or call us at (555) 123-4567.'
      };
      
    default:
      return {
        response: "I'm sorry, I didn't understand that. Could you please rephrase your question?"
      };
  }
}

// Chatbot endpoint
app.post('/chat', (req, res) => {
  try {
    const userMessage = req.body.message;
    
    if (!userMessage || typeof userMessage !== 'string') {
      return res.status(400).json({ error: 'Invalid message format' });
    }
    
    const processedText = preprocessText(userMessage);
    const intent = classifyIntent(processedText);
    const response = generateResponse(intent, processedText);
    
    res.json(response);
  } catch (error) {
    console.error('Chatbot error:', error);
    res.status(500).json({ error: 'An error occurred while processing your request' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Start the server
app.listen(port, () => {
  console.log(`Chatbot server running on port ${port}`);
});

// Export for testing
module.exports = {
  app,
  preprocessText,
  classifyIntent,
  generateResponse
};
```
