"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgceden.web.app
Prompt: What features should I consider when building a web app with Firebase Hosting?
Generated: DETERMINISTIC_7fd2ce128012a0ec
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Firebase libraries
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';
import 'firebase/storage';

// Firebase configuration object
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Function to handle user registration
async function registerUser(email, password) {
    try {
        const userCredential = await firebase.auth().createUserWithEmailAndPassword(email, password);
        console.log('User registered:', userCredential.user);
    } catch (error) {
        console.error('Error registering user:', error.message);
    }
}

// Function to handle user login
async function loginUser(email, password) {
    try {
        const userCredential = await firebase.auth().signInWithEmailAndPassword(email, password);
        console.log('User logged in:', userCredential.user);
    } catch (error) {
        console.error('Error logging in:', error.message);
    }
}

// Function to log out the user
async function logoutUser() {
    try {
        await firebase.auth().signOut();
        console.log('User logged out');
    } catch (error) {
        console.error('Error logging out:', error.message);
    }
}

// Function to upload files to Firebase Storage
async function uploadFile(file) {
    const storageRef = firebase.storage().ref();
    const fileRef = storageRef.child(file.name);
    
    try {
        const snapshot = await fileRef.put(file);
        console.log('File uploaded successfully:', snapshot);
    } catch (error) {
        console.error('Error uploading file:', error.message);
    }
}

// Function to add data to Firestore
async function addDataToFirestore(collection, data) {
    const db = firebase.firestore();

    try {
        const docRef = await db.collection(collection).add(data);
        console.log('Document written with ID:', docRef.id);
    } catch (error) {
        console.error('Error adding document:', error.message);
    }
}

// Example usage
document.getElementById('registerBtn').addEventListener('click', () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    registerUser(email, password);
});

document.getElementById('loginBtn').addEventListener('click', () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    loginUser(email, password);
});

document.getElementById('logoutBtn').addEventListener('click', logoutUser);
document.getElementById('uploadBtn').addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        uploadFile(file);
    }
});

// To add data to Firestore
// addDataToFirestore('users', { name: 'John Doe', email: 'john@example.com' });
```

Make sure to replace the `firebaseConfig` values with your actual Firebase project configuration.
