"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markin.github.io
Prompt: Explain how to set up Google Account sign-in for a mobile app using Firebase Authentication.
Generated: DETERMINISTIC_4541e8b1642fc9b8
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for setting up Google Account sign-in for a mobile app using Firebase Authentication in Android (Java):

```java
// Import necessary packages
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.auth.api.signin.GoogleSignIn;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.android.gms.auth.api.signin.GoogleSignInClient;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.common.api.ApiException;
import com.google.firebase.auth.AuthCredential;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.auth.GoogleAuthProvider;

public class GoogleSignInActivity extends AppCompatActivity {

    private static final String TAG = "GoogleSignInActivity";
    private static final int RC_SIGN_IN = 9001; // Request code for Google Sign-in

    private GoogleSignInClient mGoogleSignInClient; // Google Sign-in client
    private FirebaseAuth mAuth; // Firebase Authentication instance

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_google_sign_in);

        // Initialize Firebase Auth
        mAuth = FirebaseAuth.getInstance();

        // Configure Google Sign-in options
        GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
                .requestIdToken(getString(R.string.default_web_client_id)) // Use your web client ID from Firebase Console
                .requestEmail() // Request email from the user
                .build();

        // Build the GoogleSignInClient using the options
        mGoogleSignInClient = GoogleSignIn.getClient(this, gso);

        // Set up a button listener to start the Google Sign-in flow
        findViewById(R.id.sign_in_button).setOnClickListener(v -> signIn());
    }

    // Start the Google Sign-in flow
    private void signIn() {
        Intent signInIntent = mGoogleSignInClient.getSignInIntent();
        startActivityForResult(signInIntent, RC_SIGN_IN);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        // Check if the result is from the Google Sign-in flow
        if (requestCode == RC_SIGN_IN) {
            try {
                // Get signed-in account from the result
                GoogleSignInAccount account = GoogleSignIn.getSignedInAccountFromIntent(data).getResult(ApiException.class);

                // Log success and authenticate with Firebase
                Log.d(TAG, "Google sign-in successful.");
                firebaseAuthWithGoogle(account);
            } catch (ApiException e) {
                // Handle sign-in failure
                Log.w(TAG, "Google sign-in failed: " + e.getStatusCode());
                Toast.makeText(this, "Google sign-in failed.", Toast.LENGTH_SHORT).show();
            }
        }
    }

    // Authenticate with Firebase using the Google account
    private void firebaseAuthWithGoogle(GoogleSignInAccount acct) {
        Log.d(TAG, "firebaseAuthWithGoogle:" + acct.getId());

        // Get credentials from the Google account
        AuthCredential credential = GoogleAuthProvider.getCredential(acct.getIdToken(), null);

        // Sign in to Firebase with the credentials
        mAuth.signInWithCredential(credential)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        // Sign-in success, update UI with Firebase user information
                        Log.d(TAG, "signInWithCredential:success");
                        FirebaseUser user = mAuth.getCurrentUser();
                        Toast.makeText(this, "Welcome, " + user.getDisplayName(), Toast.LENGTH_SHORT).show();
                    } else {
                        // Sign-in failure, log the exception and show an error message
                        Log.w(TAG, "signInWithCredential:failure", task.getException());
                        Toast.makeText(this, "Authentication failed.", Toast.LENGTH_SHORT).show();
                    }
                });
    }

    @Override
    protected void onStart() {
        super.onStart();

        // Check if the user is already signed in
        FirebaseUser currentUser = mAuth.getCurrentUser();
        if (currentUser != null) {
            // User is signed in, you can update the UI
            Log.d(TAG, "User already signed in: " + currentUser.getDisplayName());
            Toast.makeText(this, "Welcome back, " + currentUser.getDisplayName(), Toast.LENGTH_SHORT).show();
        }
    }
}
```

### Notes:
1. Ensure you add the necessary dependencies to your `build.gradle`:
   ```gradle
   implementation 'com.google.firebase:firebase-auth:version'
   implementation 'com.google.android.gms:play-services-auth:version'
   ```

2. Replace `R.string.default_web_client_id` with your actual Web Client ID from the Firebase Console (`google-services.json` file).

3. Add the appropriate UI elements like a button with ID `sign_in_button` in your layout (`activity_google_sign_in.xml`).

4. Enable Google Sign-in in your Firebase Console under Authentication > Sign-in method.
