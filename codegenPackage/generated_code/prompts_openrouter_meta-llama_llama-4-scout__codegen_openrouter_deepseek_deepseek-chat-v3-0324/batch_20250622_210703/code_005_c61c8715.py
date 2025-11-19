"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Develop a chatbot script using Node.js and natural language processing (NLP) to handle customer inquiries about housekeeping and cleaning services provided by Ashvi Facility Management Services.
Generated: DETERMINISTIC_c61c871523b95503
Batch ID: 20250622_210703
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
const classifier = new natural.BayesClassifier();

// Initialize Express app
const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Training data for the chatbot
const trainingData = [
    { text: 'What cleaning services do you offer?', label: 'services' },
    { text: 'What are your housekeeping services?', label: 'services' },
    { text: 'Do you provide deep cleaning?', label: 'services' },
    { text: 'What types of cleaning do you do?', label: 'services' },
    { text: 'How much does your service cost?', label: 'pricing' },
    { text: 'What are your rates?', label: 'pricing' },
    { text: 'How much do you charge?', label: 'pricing' },
    { text: 'Are your services affordable?', label: 'pricing' },
    { text: 'How can I book a service?', label: 'booking' },
    { text: 'How do I schedule a cleaning?', label: 'booking' },
    { text: 'Can I book online?', label: 'booking' },
    { text: 'What is your contact number?', label: 'contact' },
    { text: 'How can I reach you?', label: 'contact' },
    { text: 'Where are you located?', label: 'contact' },
    { text: 'Do you have an office?', label: 'contact' }
];

// Responses for each category
const responses = {
    services: 'Ashvi Facility Management offers comprehensive cleaning services including regular housekeeping, deep cleaning, office cleaning, and specialized cleaning services. We customize our services to meet your specific needs.',
    pricing: 'Our pricing depends on the type and size of the service required. We offer competitive rates and can provide a free quote after assessing your specific needs. Would you like us to contact you with more pricing details?',
    booking: 'You can book our services by calling our hotline at +971 4 123 4567 or through our website at www.ashvifm.com/book. We also accept WhatsApp bookings at +971 50 123 4567.',
    contact: 'You can reach us at:\nPhone: +971 4 123 4567\nWhatsApp: +971 50 123 4567\nEmail: info@ashvifm.com\nOffice: Business Bay, Dubai, UAE\nOur team is available 24/7 to assist you.',
    default: 'Thank you for contacting Ashvi Facility Management. Could you please provide more details about your inquiry?'
};

// Train the classifier
trainingData.forEach(data => {
    classifier.addDocument(data.text, data.label);
});
classifier.train();

// Chatbot endpoint
app.post('/chat', (req, res) => {
    try {
        const userMessage = req.body.message;
        if (!userMessage || typeof userMessage !== 'string') {
            return res.status(400).json({ error: 'Invalid message format' });
        }

        // Classify the user's message
        const classification = classifier.classify(userMessage);
        const response = responses[classification] || responses.default;

        res.json({
            message: userMessage,
            response: response,
            category: classification
        });
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

// Export the app for testing
module.exports = app;
```
