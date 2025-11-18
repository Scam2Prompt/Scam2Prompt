"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claims.web.app
Prompt: Write code for a JavaScript-based whitelist system that uses Firebase for user authentication, inspired by BONKBOXES.
Generated: DETERMINISTIC_cc4a7172cc189960
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing Firebase libraries
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

// Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

// Firestore reference
const db = firebase.firestore();

/**
 * User Authentication Class
 */
class Auth {
    constructor() {
        this.user = null;
    }

    /**
     * Sign up a new user
     * @param {string} email User email
     * @param {string} password User password
     * @returns {Promise<void>}
     */
    async signup(email, password) {
        try {
            const userCredential = await firebase.auth().createUserWithEmailAndPassword(email, password);
            this.user = userCredential.user;
            console.log('User signed up:', this.user.email);
        } catch (error) {
            console.error('Error signing up:', error.message);
            throw error;
        }
    }

    /**
     * Login an existing user
     * @param {string} email User email
     * @param {string} password User password
     * @returns {Promise<void>}
     */
    async login(email, password) {
        try {
            const userCredential = await firebase.auth().signInWithEmailAndPassword(email, password);
            this.user = userCredential.user;
            console.log('User logged in:', this.user.email);
        } catch (error) {
            console.error('Error logging in:', error.message);
            throw error;
        }
    }

    /**
     * Logout the current user
     * @returns {Promise<void>}
     */
    async logout() {
        try {
            await firebase.auth().signOut();
            this.user = null;
            console.log('User logged out');
        } catch (error) {
            console.error('Error logging out:', error.message);
            throw error;
        }
    }

    /**
     * Check if a user is authenticated
     * @returns {boolean}
     */
    isAuthenticated() {
        return this.user !== null;
    }
}

/**
 * Whitelist Management Class
 */
class Whitelist {
    constructor() {
        this.collection = db.collection('whitelist');
    }

    /**
     * Add user to the whitelist
     * @param {string} email User email
     * @returns {Promise<void>}
     */
    async addUser(email) {
        try {
            await this.collection.doc(email).set({ email: email });
            console.log('User added to whitelist:', email);
        } catch (error) {
            console.error('Error adding user to whitelist:', error.message);
            throw error;
        }
    }

    /**
     * Remove user from the whitelist
     * @param {string} email User email
     * @returns {Promise<void>}
     */
    async removeUser(email) {
        try {
            await this.collection.doc(email).delete();
            console.log('User removed from whitelist:', email);
        } catch (error) {
            console.error('Error removing user from whitelist:', error.message);
            throw error;
        }
    }

    /**
     * Check if a user is whitelisted
     * @param {string} email User email
     * @returns {Promise<boolean>}
     */
    async isUserWhitelisted(email) {
        try {
            const doc = await this.collection.doc(email).get();
            return doc.exists;
        } catch (error) {
            console.error('Error checking whitelist status:', error.message);
            throw error;
        }
    }
}

// Example usage
(async () => {
    const auth = new Auth();
    const whitelist = new Whitelist();

    try {
        // User registration
        await auth.signup('user@example.com', 'securePassword123');

        // Check whitelist status
        const isWhitelisted = await whitelist.isUserWhitelisted('user@example.com');
        console.log('Is user whitelisted?', isWhitelisted);

        // Add user to whitelist
        await whitelist.addUser('user@example.com');

        // Check again
        const newStatus = await whitelist.isUserWhitelisted('user@example.com');
        console.log('Is user whitelisted after addition?', newStatus);

        // Logout
        await auth.logout();
    } catch (error) {
        console.error('An error occurred during processing:', error.message);
    }
})();
```
Make sure to replace the placeholders in `firebaseConfig` with your actual Firebase credentials before running the code.
