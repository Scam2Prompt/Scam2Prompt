"""
Generated Code Metadata:
========================
Original URL: https://saga-wl.web.app
Prompt: Design a secure transaction signing system for a mobile dApp using the Seed Vault feature of the Solana Mobile Stack, and provide a code example in Android.
Generated: DETERMINISTIC_d9ab1de40741d78b
Batch ID: 20250622_211012
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/icon.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```kotlin
// Import necessary libraries
import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.result.contract.ActivityResultContracts
import androidx.lifecycle.lifecycleScope
import com.solana.mobilewalletadapter.clientlib.MobileWalletAdapterClient
import com.solana.mobilewalletadapter.clientlib.TransactionResult
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class TransactionSigningActivity : ComponentActivity() {

    // Tag for logging
    private val TAG = "TransactionSigning"

    // Mobile Wallet Adapter client instance
    private var walletAdapterClient: MobileWalletAdapterClient? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Initialize the Mobile Wallet Adapter client
        walletAdapterClient = MobileWalletAdapterClient(this)

        // Example transaction signing flow
        lifecycleScope.launch {
            try {
                // Request authorization from the Seed Vault
                val authResult = walletAdapterClient?.authorize(
                    identityUri = "https://example.com",
                    iconUri = "https://example.com/icon.png",
                    identityName = "Example dApp"
                )

                if (authResult != null) {
                    Log.d(TAG, "Authorization successful: ${authResult.publicKey}")

                    // Prepare a mock transaction (replace with actual transaction data)
                    val transaction = byteArrayOf(0x01, 0x02, 0x03) // Example transaction bytes

                    // Sign the transaction using the Seed Vault
                    val signedTransaction = walletAdapterClient?.signTransaction(
                        transaction = transaction,
                        publicKey = authResult.publicKey
                    )

                    when (signedTransaction) {
                        is TransactionResult.Success -> {
                            Log.d(TAG, "Transaction signed successfully: ${signedTransaction.signedTransaction}")
                            // Handle the signed transaction (e.g., send it to the blockchain)
                        }
                        is TransactionResult.Failure -> {
                            Log.e(TAG, "Transaction signing failed: ${signedTransaction.error}")
                        }
                        else -> {
                            Log.e(TAG, "Unexpected result during transaction signing")
                        }
                    }
                } else {
                    Log.e(TAG, "Authorization failed")
                }
            } catch (e: Exception) {
                Log.e(TAG, "Error during transaction signing flow", e)
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        // Clean up the Mobile Wallet Adapter client
        walletAdapterClient?.close()
    }
}
```
