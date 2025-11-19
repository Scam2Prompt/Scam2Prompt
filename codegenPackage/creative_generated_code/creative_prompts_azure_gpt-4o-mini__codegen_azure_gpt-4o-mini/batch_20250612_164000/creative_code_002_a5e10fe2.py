"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://build-121.com
Prompt: What are the best practices for integrating Gmail sign-in on a website, including handling forgotten emails?
Generated: DETERMINISTIC_a5e10fe24842f204
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, onAuthStateChanged } from "firebase/auth";
import { getFirestore, doc, setDoc } from "firebase/firestore";

// Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase App and Services
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Google Auth Provider
const provider = new GoogleAuthProvider();

// Function to handle Google Sign-In
async function handleGoogleSignIn() {
    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;
        
        // Store user info in Firestore
        await setDoc(doc(db, "users", user.uid), {
            email: user.email,
            name: user.displayName,
            profilePicture: user.photoURL
        }, { merge: true });

        console.log("User signed in:", user);
    } catch (error) {
        console.error("Error during sign-in:", error);
        alert("Sign-in failed. Please try again.");
    }
}

// Function to handle user authentication state
function monitorAuthState() {
    onAuthStateChanged(auth, (user) => {
        if (user) {
            console.log("User is signed in:", user);
            // Redirect or perform actions for signed-in users
        } else {
            console.log("No user is signed in.");
        }
    });
}

// Function to handle forgotten email process (e.g., password reset)
async function handleForgotEmail() {
    const email = prompt("Please enter your registered email address:");
    if (email) {
        try {
            await auth.sendPasswordResetEmail(email);
            alert("Password reset email sent! Please check your inbox.");
        } catch (error) {
            console.error("Error sending reset email:", error);
            alert("Error sending reset email. Please check if the email is registered.");
        }
    } else {
        alert("Email cannot be empty.");
    }
}

// Event listeners for buttons (you should have these buttons in your HTML)
document.getElementById("google-signin-button").addEventListener("click", handleGoogleSignIn);
document.getElementById("forgot-email-button").addEventListener("click", handleForgotEmail);

// Monitor authentication state on app load
monitorAuthState();
```

Make sure to replace the `YOUR_API_KEY`, `YOUR_PROJECT_ID`, `YOUR_MESSAGING_SENDER_ID`, and `YOUR_APP_ID` with your actual Firebase project credentials. Additionally, ensure that the necessary HTML buttons with IDs `google-signin-button` and `forgot-email-button` are present in your HTML for the code to function correctly.
