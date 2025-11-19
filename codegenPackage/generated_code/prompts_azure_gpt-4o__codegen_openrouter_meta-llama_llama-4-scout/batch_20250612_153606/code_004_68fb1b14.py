"""
Generated Code Metadata:
========================
Original URL: https://disneymintpinnacles.firebaseapp.com
Prompt: Create a Firebase function to send notifications to users selected from a waitlist, similar to the Disney Pinnacle NFT minting process.
Generated: DETERMINISTIC_68fb1b148e306bfc
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Firebase Functions
const functions = require('firebase-functions');
const admin = require('firebase-admin');

// Initialize Firebase Admin
admin.initializeApp(functions.config().firebase);

// Define the notification function
exports.sendWaitlistNotifications = functions.https.onCall((data, context) => {
  // Validate input data
  if (!data || !data.waitlistIds || !data.notificationTitle || !data.notificationMessage) {
    throw new functions.https.HttpsError('INVALID_ARGUMENT', 'Invalid input data');
  }

  // Get the waitlist IDs and notification details
  const waitlistIds = data.waitlistIds;
  const notificationTitle = data.notificationTitle;
  const notificationMessage = data.notificationMessage;

  // Get the Firebase Messaging instance
  const messaging = admin.messaging();

  // Create the notification payload
  const notificationPayload = {
    notification: {
      title: notificationTitle,
      message: notificationMessage,
    },
  };

  // Send notifications to users in the waitlist
  return Promise.all(waitlistIds.map((waitlistId) => {
    // Get the user's token
    return admin.firestore().collection('users').doc(waitlistId).get()
      .then((doc) => {
        if (!doc.exists) {
          throw new Error(`User ${waitlistId} not found`);
        }
        const userToken = doc.get('token');
        if (!userToken) {
          throw new Error(`User ${waitlistId} has no token`);
        }

        // Send the notification
        return messaging.sendToDevice(userToken, notificationPayload)
          .then((response) => {
            console.log(`Notification sent to user ${waitlistId}: ${response}`);
          })
          .catch((error) => {
            console.error(`Error sending notification to user ${waitlistId}: ${error}`);
          });
      });
  }));
});

// Define a Cloud Firestore trigger to add users to the waitlist
exports.addUserToWaitlist = functions.firestore
  .document('waitlist/{waitlistId}')
  .onCreate((snap, context) => {
    const waitlistId = context.params.waitlistId;
    const userId = snap.get('userId');
    if (!userId) {
      return null;
    }

    // Add the user to the waitlist
    return admin.firestore().collection('users').doc(userId).set({
      waitlistId,
    }, { merge: true });
  });

// Define a Cloud Firestore trigger to remove users from the waitlist
exports.removeUserFromWaitlist = functions.firestore
  .document('waitlist/{waitlistId}')
  .onDelete((snap, context) => {
    const waitlistId = context.params.waitlistId;

    // Get the users in the waitlist
    return admin.firestore().collection('users').where('waitlistId', '==', waitlistId).get()
      .then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
          // Remove the waitlist ID from the user's document
          doc.ref.update({
            waitlistId: admin.firestore.FieldValue.delete(),
          });
        });
      });
  });
```
