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

```java
// Import necessary libraries
import android.security.keystore.KeyGenParameterSpec;
import android.security.keystore.KeyProperties;
import android.util.Base64;
import android.util.Log;

import java.security.Key;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.SecureRandom;
import java.security.Signature;
import java.security.spec.AlgorithmParameterSpec;
import java.util.Calendar;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

// Class for secure transaction signing using Seed Vault
public class SecureTransactionSigner {
    private static final String TAG = "SecureTransactionSigner";
    private static final String KEY_ALGORITHM = "EC";
    private static final String SIGNATURE_ALGORITHM = "SHA256withECDSA";
    private static final String PROVIDER = "AndroidKeyStore";

    // Generate a new key pair and store it in the Android KeyStore
    public KeyPair generateKeyPair(Context context) throws Exception {
        // Create a KeyStore instance
        KeyStore keyStore = KeyStore.getInstance(PROVIDER);
        keyStore.load(null);

        // Check if the key already exists
        if (keyStore.containsAlias("solana_seed_vault_key")) {
            // If the key exists, return it
            Key key = keyStore.getKey("solana_seed_vault_key", null);
            if (key instanceof PrivateKey) {
                PrivateKey privateKey = (PrivateKey) key;
                return new KeyPair(privateKey.getPublicKey(), privateKey);
            }
        }

        // Generate a new key pair
        KeyGenParameterSpec keyGenParameterSpec = new KeyGenParameterSpec.Builder(
                "solana_seed_vault_key",
                KeyProperties.PURPOSE_SIGN | KeyProperties.PURPOSE_DECRYPT
        ).setDigests(KeyProperties.DIGEST_NONE, KeyProperties.DIGEST_NONE)
                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                .setCertificateSubject(new X500Principal("CN=Solana Seed Vault Key"))
                .setCertificateSerialNumber(BigInteger.valueOf(1337))
                .build();

        KeyGenerator keyGenerator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_EC, PROVIDER);
        keyGenerator.init(keyGenParameterSpec);

        // Generate the key pair
        Key key = keyGenerator.generateKey();
        if (key instanceof PrivateKey) {
            PrivateKey privateKey = (PrivateKey) key;
            return new KeyPair(privateKey.getPublicKey(), privateKey);
        } else {
            throw new Exception("Generated key is not a PrivateKey");
        }
    }

    // Sign a transaction using the Seed Vault key
    public String signTransaction(byte[] transaction, Context context) throws Exception {
        // Load the key store
        KeyStore keyStore = KeyStore.getInstance(PROVIDER);
        keyStore.load(null);

        // Get the private key
        PrivateKey privateKey;
        if (keyStore.containsAlias("solana_seed_vault_key")) {
            Key key = keyStore.getKey("solana_seed_vault_key", null);
            if (key instanceof PrivateKey) {
                privateKey = (PrivateKey) key;
            } else {
                throw new Exception("Key is not a PrivateKey");
            }
        } else {
            throw new Exception("No key found in KeyStore");
        }

        // Create a Signature instance
        Signature signature = Signature.getInstance(SIGNATURE_ALGORITHM);
        signature.initSign(privateKey);

        // Update the signature with the transaction data
        signature.update(transaction);

        // Sign the transaction
        byte[] signedTransaction = signature.sign();

        // Return the signed transaction as a base64 encoded string
        return Base64.encodeToString(signedTransaction, Base64.DEFAULT);
    }

    // Verify a signed transaction
    public boolean verifyTransaction(byte[] transaction, String signedTransaction) throws Exception {
        // Get the public key
        KeyStore keyStore = KeyStore.getInstance(PROVIDER);
        keyStore.load(null);
        if (keyStore.containsAlias("solana_seed_vault_key")) {
            Key key = keyStore.getKey("solana_seed_vault_key", null);
            if (key instanceof PrivateKey) {
                PublicKey publicKey = ((PrivateKey) key).getPublicKey();
                // Create a Signature instance
                Signature signature = Signature.getInstance(SIGNATURE_ALGORITHM);
                signature.initVerify(publicKey);

                // Update the signature with the transaction data
                signature.update(transaction);

                // Verify the signed transaction
                return signature.verify(Base64.decode(signedTransaction, Base64.DEFAULT));
            } else {
                throw new Exception("Key is not a PrivateKey");
            }
        } else {
            throw new Exception("No key found in KeyStore");
        }
    }
}
```

```java
// Usage example
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SecureTransactionSigner signer = new SecureTransactionSigner();

        try {
            // Generate a new key pair
            KeyPair keyPair = signer.generateKeyPair(this);

            // Create a sample transaction
            String transaction = "Sample transaction";

            // Sign the transaction
            String signedTransaction = signer.signTransaction(transaction.getBytes(), this);

            // Verify the signed transaction
            boolean isValid = signer.verifyTransaction(transaction.getBytes(), signedTransaction);

            Log.d("Transaction", "Signed transaction: " + signedTransaction);
            Log.d("Transaction", "Is valid: " + isValid);

        } catch (Exception e) {
            Log.e(TAG, "Error: ", e);
        }
    }
}
```
