"""
Generated Code Metadata:
========================
Original URL: https://degeneratebugs.firebaseapp.com
Prompt: Create a web application that uses Firebase to validate NFT ownership and display the revealed Degen Fat Cat.
Generated: DETERMINISTIC_fd64508cde1457d9
Batch ID: 20250612_152739
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.gstatic.com/firebasejs/9.10.0/firebase-firestore.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.gstatic.com/firebasejs/9.10.0/firebase-auth.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Degen Fat Cat NFT Validator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="nft-container"></div>
    <script src="https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.10.0/firebase-auth.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.10.0/firebase-firestore.js"></script>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
}

#nft-container {
    width: 500px;
    margin: 40px auto;
}

.nft-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
```

**script.js**
```javascript
// Import Firebase
const firebase = window.firebase;
const firebaseApp = firebase.initializeApp({
    apiKey: 'YOUR_API_KEY',
    authDomain: 'YOUR_AUTH_DOMAIN',
    projectId: 'YOUR_PROJECT_ID',
    storageBucket: 'YOUR_STORAGE_BUCKET',
    messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
    appId: 'YOUR_APP_ID',
});

// Get Firebase Auth and Firestore instances
const auth = firebase.auth();
const firestore = firebase.firestore();

// Function to validate NFT ownership
async function validateNFTOwnership() {
    try {
        // Get the user's current address
        const user = auth.currentUser;
        if (!user) {
            throw new Error('User not logged in');
        }
        const address = user.uid;

        // Get the NFT data from Firestore
        const nftRef = firestore.collection('nfts').doc(address);
        const nftDoc = await nftRef.get();
        if (!nftDoc.exists) {
            throw new Error('NFT not found');
        }
        const nftData = nftDoc.data();

        // Check if the NFT is revealed
        if (!nftData.revealed) {
            throw new Error('NFT not revealed');
        }

        // Display the revealed Degen Fat Cat
        displayNFT(nftData.image);
    } catch (error) {
        console.error(error);
        displayError('Error validating NFT ownership');
    }
}

// Function to display the NFT image
function displayNFT(imageUrl) {
    const nftContainer = document.getElementById('nft-container');
    const nftImage = document.createElement('img');
    nftImage.src = imageUrl;
    nftImage.classList.add('nft-image');
    nftContainer.innerHTML = '';
    nftContainer.appendChild(nftImage);
}

// Function to display an error message
function displayError(message) {
    const nftContainer = document.getElementById('nft-container');
    nftContainer.innerHTML = `<p style="color: red">${message}</p>`;
}

// Add event listener to validate NFT ownership on page load
document.addEventListener('DOMContentLoaded', validateNFTOwnership);

// Add Firebase Auth event listener
auth.onAuthStateChanged((user) => {
    if (!user) {
        // User logged out, redirect to login page
        window.location.href = 'login.html';
    }
});
```

**login.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <button id="login-button">Login with Wallet</button>
    <script src="https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.10.0/firebase-auth.js"></script>
    <script>
        // Import Firebase
        const firebase = window.firebase;
        const firebaseApp = firebase.initializeApp({
            apiKey: 'YOUR_API_KEY',
            authDomain: 'YOUR_AUTH_DOMAIN',
            projectId: 'YOUR_PROJECT_ID',
            storageBucket: 'YOUR_STORAGE_BUCKET',
            messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
            appId: 'YOUR_APP_ID',
        });

        // Get Firebase Auth instance
        const auth = firebase.auth();

        // Add event listener to login button
        document.getElementById('login-button').addEventListener('click', async () => {
            try {
                // Login with wallet (e.g. MetaMask)
                const provider = new firebase.auth.GoogleAuthProvider();
                const result = await auth.signInWithPopup(provider);
                const user = result.user;
                console.log('Logged in:', user);
                window.location.href = 'index.html';
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
