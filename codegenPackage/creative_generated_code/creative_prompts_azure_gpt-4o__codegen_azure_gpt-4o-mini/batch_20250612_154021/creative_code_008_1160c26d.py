"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: How can I enable code verification for secure user authentication in a Firebase-hosted web app? Provide example code using the Firebase SDK.
Generated: DETERMINISTIC_1160c26d444bafc6
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Firebase modules
import { initializeApp } from "firebase/app";
import { getAuth, signInWithPhoneNumber, RecaptchaVerifier } from "firebase/auth";

// Firebase configuration object
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Function to set up reCAPTCHA
function setupRecaptcha() {
    // Create an instance of RecaptchaVerifier
    window.recaptchaVerifier = new RecaptchaVerifier('recaptcha-container', {
        'size': 'invisible', // Use 'invisible' for user experience
        'callback': (response) => {
            // ReCAPTCHA solved - will proceed with phone verification
            console.log('ReCAPTCHA solved, proceed with phone verification');
        }
    }, auth);
}

// Function to send SMS verification code
async function sendVerificationCode(phoneNumber) {
    try {
        setupRecaptcha(); // Set up reCAPTCHA

        // Use signInWithPhoneNumber to send the verification code
        const confirmationResult = await signInWithPhoneNumber(auth, phoneNumber, window.recaptchaVerifier);
        
        // Confirmation result contains the verification ID
        window.confirmationResult = confirmationResult;
        console.log('Verification code sent to:', phoneNumber);
        
    } catch (error) {
        console.error("Error during SMS verification code sending:", error);
        alert("Error sending verification code: " + error.message);
    }
}

// Function to confirm the code and sign in the user
async function verifyCode(verificationCode) {
    try {
        // Use the confirmation result to verify the code
        const result = await window.confirmationResult.confirm(verificationCode);
        
        // User signed in successfully
        const user = result.user;
        console.log('User signed in:', user);
        
    } catch (error) {
        console.error("Error verifying code:", error);
        alert("Error verifying code: " + error.message);
    }
}

// HTML Element to attach reCAPTCHA
// <div id="recaptcha-container"></div>

// Example usage:
// sendVerificationCode('+1234567890'); // Replace with the user's phone number
// verifyCode('123456'); // Replace with the code input by the user
```

**Note:** Replace placeholders in the `firebaseConfig` object with your actual Firebase project credentials. Also, ensure to include Firebase SDK scripts in your HTML file or use a bundler for the Firebase SDK.
