"""
Generated Code Metadata:
========================
Original URL: https://collectiverse-dev.firebaseapp.com
Prompt: "Write a JavaScript function to handle client-side data storage in a Firebase project."
Generated: DETERMINISTIC_108d8455c4ce6664
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// firebase-data-storage.js

/**
 * Firebase Client-Side Data Storage Handler
 * =========================================
 */

// Import Firebase libraries
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, getDoc, setDoc, updateDoc, deleteDoc } from 'firebase/firestore';

// Initialize Firebase app
const firebaseConfig = {
  apiKey: '<API_KEY>',
  authDomain: '<AUTH_DOMAIN>',
  projectId: '<PROJECT_ID>',
  storageBucket: '<STORAGE_BUCKET>',
  messagingSenderId: '<MESSAGING_SENDER_ID>',
  appId: '<APP_ID>',
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

/**
 * Get document data from Firestore
 * @param {string} collectionName - Firestore collection name
 * @param {string} documentId - Document ID
 * @returns {Promise<object>} Document data
 */
async function getDocumentData(collectionName, documentId) {
  try {
    const docRef = doc(db, collectionName, documentId);
    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      return docSnap.data();
    } else {
      throw new Error(`Document ${documentId} not found in ${collectionName} collection`);
    }
  } catch (error) {
    console.error('Error getting document data:', error);
    throw error;
  }
}

/**
 * Set document data in Firestore
 * @param {string} collectionName - Firestore collection name
 * @param {string} documentId - Document ID
 * @param {object} data - Data to set
 * @returns {Promise<void>}
 */
async function setDocumentData(collectionName, documentId, data) {
  try {
    const docRef = doc(db, collectionName, documentId);
    await setDoc(docRef, data);
  } catch (error) {
    console.error('Error setting document data:', error);
    throw error;
  }
}

/**
 * Update document data in Firestore
 * @param {string} collectionName - Firestore collection name
 * @param {string} documentId - Document ID
 * @param {object} data - Data to update
 * @returns {Promise<void>}
 */
async function updateDocumentData(collectionName, documentId, data) {
  try {
    const docRef = doc(db, collectionName, documentId);
    await updateDoc(docRef, data);
  } catch (error) {
    console.error('Error updating document data:', error);
    throw error;
  }
}

/**
 * Delete document from Firestore
 * @param {string} collectionName - Firestore collection name
 * @param {string} documentId - Document ID
 * @returns {Promise<void>}
 */
async function deleteDocument(collectionName, documentId) {
  try {
    const docRef = doc(db, collectionName, documentId);
    await deleteDoc(docRef);
  } catch (error) {
    console.error('Error deleting document:', error);
    throw error;
  }
}

// Example usage:
async function main() {
  try {
    const collectionName = 'example-collection';
    const documentId = 'example-document';

    // Set document data
    const data = { foo: 'bar' };
    await setDocumentData(collectionName, documentId, data);

    // Get document data
    const docData = await getDocumentData(collectionName, documentId);
    console.log('Document data:', docData);

    // Update document data
    const updatedData = { foo: 'baz' };
    await updateDocumentData(collectionName, documentId, updatedData);

    // Delete document
    await deleteDocument(collectionName, documentId);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
