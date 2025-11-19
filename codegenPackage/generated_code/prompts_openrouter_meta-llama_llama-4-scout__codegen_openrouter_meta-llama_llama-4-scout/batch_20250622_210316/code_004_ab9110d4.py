"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Develop a Node.js application to handle customer requests for test drives and car sales inquiries, like those on Suzuki Capital Motors' website.
Generated: DETERMINISTIC_ab9110d4739c0622
Batch ID: 20250622_210316
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
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/suzuki-capital-motors', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for test drive requests
const testDriveSchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String,
    carModel: String,
    preferredDate: Date,
    preferredTime: String
});

// Define schema for car sales inquiries
const carInquirySchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String,
    carModel: String,
    inquiry: String
});

// Create models
const TestDriveRequest = mongoose.model('TestDriveRequest', testDriveSchema);
const CarInquiry = mongoose.model('CarInquiry', carInquirySchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle test drive requests
app.post('/test-drive', async (req, res) => {
    try {
        const { name, email, phone, carModel, preferredDate, preferredTime } = req.body;
        if (!name || !email || !phone || !carModel || !preferredDate || !preferredTime) {
            return res.status(400).send({ message: 'All fields are required' });
        }

        const testDriveRequest = new TestDriveRequest({
            name,
            email,
            phone,
            carModel,
            preferredDate: new Date(preferredDate),
            preferredTime
        });

        await testDriveRequest.save();

        // Send confirmation email
        const transporter = nodemailer.createTransport({
            host: 'smtp.example.com',
            port: 587,
            auth: {
                user: 'username',
                pass: 'password'
            }
        });

        const mailOptions = {
            from: 'suzuki-capital-motors@example.com',
            to: email,
            subject: 'Test Drive Confirmation',
            text: `Dear ${name},\n\nThank you for requesting a test drive. We will contact you soon.\n\nBest regards,\nSuzuki Capital Motors`
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(error);
            } else {
                console.log('Email sent: ' + info.response);
            }
        });

        res.send({ message: 'Test drive request received successfully' });
    } catch (error) {
        console.log(error);
        res.status(500).send({ message: 'Internal Server Error' });
    }
});

// Route to handle car sales inquiries
app.post('/car-inquiry', async (req, res) => {
    try {
        const { name, email, phone, carModel, inquiry } = req.body;
        if (!name || !email || !phone || !carModel || !inquiry) {
            return res.status(400).send({ message: 'All fields are required' });
        }

        const carInquiry = new CarInquiry({
            name,
            email,
            phone,
            carModel,
            inquiry
        });

        await carInquiry.save();

        // Send confirmation email
        const transporter = nodemailer.createTransport({
            host: 'smtp.example.com',
            port: 587,
            auth: {
                user: 'username',
                pass: 'password'
            }
        });

        const mailOptions = {
            from: 'suzuki-capital-motors@example.com',
            to: email,
            subject: 'Inquiry Confirmation',
            text: `Dear ${name},\n\nThank you for your inquiry. We will contact you soon.\n\nBest regards,\nSuzuki Capital Motors`
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(error);
            } else {
                console.log('Email sent: ' + info.response);
            }
        });

        res.send({ message: 'Inquiry received successfully' });
    } catch (error) {
        console.log(error);
        res.status(500).send({ message: 'Internal Server Error' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
