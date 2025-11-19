"""
Generated Code Metadata:
========================
Original URL: https://markin.github.io
Prompt: Explain how to set up Google Account sign-in for a mobile app using Firebase Authentication.
Generated: DETERMINISTIC_4541e8b1642fc9b8
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for setting up Google Sign-In with Firebase Authentication in an Android app:

```kotlin
// FirebaseAuthManager.kt
import android.app.Activity
import android.content.Intent
import android.util.Log
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInAccount
import com.google.android.gms.auth.api.signin.GoogleSignInClient
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.android.gms.common.api.ApiException
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.GoogleAuthProvider

class FirebaseAuthManager(private val activity: Activity) {
    private val auth: FirebaseAuth = FirebaseAuth.getInstance()
    private lateinit var googleSignInClient: GoogleSignInClient

    companion object {
        private const val TAG = "FirebaseAuthManager"
        private const val RC_SIGN_IN = 9001
    }

    // Initialize Google Sign-In
    fun initializeGoogleSignIn(webClientId: String) {
        val gso = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            .requestIdToken(webClientId)
            .requestEmail()
            .build()

        googleSignInClient = GoogleSignIn.getClient(activity, gso)
    }

    // Handle sign-in intent
    fun getGoogleSignInIntent(): Intent {
        return googleSignInClient.signInIntent
    }

    // Handle activity result
    fun handleSignInResult(data: Intent?, onSuccess: () -> Unit, onFailure: (Exception) -> Unit) {
        try {
            val task = GoogleSignIn.getSignedInAccountFromIntent(data)
            val account = task.getResult(ApiException::class.java)
            account?.let { firebaseAuthWithGoogle(it, onSuccess, onFailure) }
        } catch (e: ApiException) {
            Log.w(TAG, "Google sign in failed", e)
            onFailure(e)
        }
    }

    // Authenticate with Firebase
    private fun firebaseAuthWithGoogle(
        account: GoogleSignInAccount,
        onSuccess: () -> Unit,
        onFailure: (Exception) -> Unit
    ) {
        val credential = GoogleAuthProvider.getCredential(account.idToken, null)
        auth.signInWithCredential(credential)
            .addOnCompleteListener(activity) { task ->
                if (task.isSuccessful) {
                    Log.d(TAG, "signInWithCredential:success")
                    onSuccess()
                } else {
                    Log.w(TAG, "signInWithCredential:failure", task.exception)
                    task.exception?.let { onFailure(it) }
                }
            }
    }

    // Sign out
    fun signOut(onComplete: () -> Unit) {
        auth.signOut()
        googleSignInClient.signOut().addOnCompleteListener(activity) {
            onComplete()
        }
    }

    // Get current user
    fun getCurrentUser() = auth.currentUser
}
```

```xml
<!-- AndroidManifest.xml additions -->
<manifest ...>
    <application ...>
        <!-- Add internet permission -->
        <uses-permission android:name="android.permission.INTERNET" />
        
        <!-- Add meta-data for Firebase -->
        <meta-data
            android:name="com.google.firebase.messaging.default_notification_channel_id"
            android:value="@string/default_notification_channel_id" />
    </application>
</manifest>
```

```groovy
// app/build.gradle dependencies
dependencies {
    // Firebase
    implementation platform('com.google.firebase:firebase-bom:32.0.0')
    implementation 'com.google.firebase:firebase-auth-ktx'
    
    // Google Sign-In
    implementation 'com.google.android.gms:play-services-auth:20.5.0'
    
    // Firebase UI (optional)
    implementation 'com.firebaseui:firebase-ui-auth:8.0.2'
}
```

```kotlin
// MainActivity.kt usage example
class MainActivity : AppCompatActivity() {
    private lateinit var authManager: FirebaseAuthManager
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // Initialize with your web client ID from Firebase Console
        authManager = FirebaseAuthManager(this)
        authManager.initializeGoogleSignIn(getString(R.string.default_web_client_id))
        
        // Set up sign-in button click
        signInButton.setOnClickListener {
            startActivityForResult(
                authManager.getGoogleSignInIntent(),
                FirebaseAuthManager.RC_SIGN_IN
            )
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        
        if (requestCode == FirebaseAuthManager.RC_SIGN_IN) {
            authManager.handleSignInResult(
                data,
                onSuccess = {
                    // Handle successful sign-in
                    val user = authManager.getCurrentUser()
                    updateUI(user)
                },
                onFailure = { exception ->
                    // Handle sign-in failure
                    showError(exception.message ?: "Sign in failed")
                }
            )
        }
    }
    
    private fun updateUI(user: FirebaseUser?) {
        // Update UI based on authentication state
    }
    
    private fun showError(message: String) {
        // Show error to user
    }
}
```
