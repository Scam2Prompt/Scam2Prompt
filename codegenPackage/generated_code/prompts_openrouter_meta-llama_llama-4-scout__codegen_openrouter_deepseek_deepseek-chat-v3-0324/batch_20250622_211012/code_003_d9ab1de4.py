"""
Generated Code Metadata:
========================
Original URL: https://saga-wl.web.app
Prompt: Design a secure transaction signing system for a mobile dApp using the Seed Vault feature of the Solana Mobile Stack, and provide a code example in Android.
Generated: DETERMINISTIC_d9ab1de40741d78b
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
// TransactionSigner.kt
package com.example.solanadapp

import android.content.Context
import com.solanamobile.seedvault.WalletContractV1
import com.solanamobile.seedvault.WalletContractV1.AUTHORITY
import com.solanamobile.seedvault.WalletContractV1.Method
import com.solanamobile.seedvault.WalletContractV1.SIGN_TRANSACTION
import com.solanamobile.seedvault.WalletContractV1.SIGN_TRANSACTION_RESULT
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.solana.core.Transaction
import org.solana.core.TransactionSerializer
import java.io.ByteArrayOutputStream

class TransactionSigner(private val context: Context) {

    /**
     * Signs a Solana transaction using Seed Vault
     * @param transaction The unsigned transaction to sign
     * @param authToken The authorization token from Seed Vault
     * @param publicKey The public key of the account to sign with
     * @return Signed transaction bytes
     * @throws SecurityException if signing fails
     */
    suspend fun signTransaction(
        transaction: Transaction,
        authToken: String,
        publicKey: ByteArray
    ): ByteArray = withContext(Dispatchers.IO) {
        try {
            // Serialize the transaction
            val txBytes = TransactionSerializer.serialize(transaction)
            
            // Prepare the signing request
            val request = WalletContractV1.SignTransactionRequest(
                authToken = authToken,
                publicKey = publicKey,
                transaction = txBytes,
                cluster = WalletContractV1.CLUSTER_MAINNET // or DEVNET/TESTNET
            )

            // Execute the signing request via Seed Vault
            val result = context.contentResolver.call(
                AUTHORITY,
                SIGN_TRANSACTION,
                null,
                Method.signTransaction(request).toBundle()
            )

            // Verify and return the signed transaction
            result ?: throw SecurityException("No response from Seed Vault")
            val signedTx = result.getByteArray(SIGN_TRANSACTION_RESULT)
                ?: throw SecurityException("Invalid signing response")
            
            signedTx
        } catch (e: Exception) {
            throw SecurityException("Transaction signing failed", e)
        }
    }
}

// TransactionSigningViewModel.kt
package com.example.solanadapp

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import org.solana.core.Transaction

sealed class SigningState {
    object Idle : SigningState()
    object Signing : SigningState()
    data class Success(val signedTx: ByteArray) : SigningState()
    data class Error(val message: String) : SigningState()
}

class TransactionSigningViewModel(application: Application) : AndroidViewModel(application) {
    private val transactionSigner = TransactionSigner(application)
    private val _signingState = MutableStateFlow<SigningState>(SigningState.Idle)
    val signingState: StateFlow<SigningState> = _signingState

    fun signTransaction(transaction: Transaction, authToken: String, publicKey: ByteArray) {
        _signingState.value = SigningState.Signing
        viewModelScope.launch {
            try {
                val signedTx = transactionSigner.signTransaction(transaction, authToken, publicKey)
                _signingState.value = SigningState.Success(signedTx)
            } catch (e: SecurityException) {
                _signingState.value = SigningState.Error(e.message ?: "Signing failed")
            }
        }
    }
}

// AndroidManifest.xml (partial)
<queries>
    <package android:name="com.solanamobile" />
    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="https" android:host="solana.com" />
    </intent>
</queries>
```
