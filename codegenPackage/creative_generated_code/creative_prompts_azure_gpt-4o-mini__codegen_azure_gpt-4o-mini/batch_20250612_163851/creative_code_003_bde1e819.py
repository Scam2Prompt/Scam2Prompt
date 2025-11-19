"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krnas.com
Prompt: Generate a code snippet for handling Gmail sign-in errors in a web application.
Generated: DETERMINISTIC_bde1e81972dff32b
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { auth } from 'firebase/app';
import 'firebase/auth';

// Function to handle Gmail sign-in
async function signInWithGmail() {
    try {
        // Create a new instance of the Google provider
        const provider = new auth.GoogleAuthProvider();

        // Sign in with popup
        const result = await auth().signInWithPopup(provider);
        
        // User successfully signed in
        const user = result.user;
        console.log('User signed in:', user);
        
        // Here you can handle user data, e.g., store user info
    } catch (error) {
        // Handle errors during sign-in
        handleSignInError(error);
    }
}

// Function to handle sign-in errors
function handleSignInError(error) {
    // Log error details for debugging
    console.error('Sign-in error:', error);

    // Extract error code and message
    const errorCode = error.code;
    const errorMessage = error.message;

    // Display user-friendly error messages based on error code
    switch (errorCode) {
        case 'auth/popup-closed-by-user':
            alert('Sign-in popup was closed before completing the sign-in. Please try again.');
            break;
        case 'auth/cancelled-popup-request':
            alert('Popup sign-in was cancelled. Please try again.');
            break;
        case 'auth/user-disabled':
            alert('This user account has been disabled. Please contact support.');
            break;
        case 'auth/invalid-email':
            alert('The email address is not valid. Please check your input.');
            break;
        case 'auth/user-not-found':
            alert('No user found for the provided email. Please sign up.');
            break;
        case 'auth/wrong-password':
            alert('Invalid password. Please try again.');
            break;
        default:
            alert(`An error occurred: ${errorMessage}`);
            break;
    }
}

// Example usage: Call the sign-in function when a button is clicked
document.getElementById('gmailSignInButton').addEventListener('click', signInWithGmail);
```
