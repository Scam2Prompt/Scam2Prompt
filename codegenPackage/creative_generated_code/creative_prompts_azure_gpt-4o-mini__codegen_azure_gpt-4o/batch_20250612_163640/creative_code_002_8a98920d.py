"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Explain how to encrypt specific columns in a database using DBDAO and provide an example of the implementation.
Generated: DETERMINISTIC_8a98920df9d2e783
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Base64;

/**
 * Utility class for encrypting and decrypting database columns using AES encryption.
 */
public class ColumnEncryptor {

    private static final String AES_ALGORITHM = "AES";
    private static final int AES_KEY_SIZE = 128;

    /**
     * Generates a new AES key.
     * 
     * @return SecretKey - AES encryption key
     * @throws Exception if key generation fails
     */
    public static SecretKey generateAESKey() throws Exception {
        KeyGenerator keyGen = KeyGenerator.getInstance(AES_ALGORITHM);
        keyGen.init(AES_KEY_SIZE);
        return keyGen.generateKey();
    }

    /**
     * Encrypts a plaintext string using the provided AES key.
     * 
     * @param plaintext The text to encrypt
     * @param key       The AES key
     * @return Encrypted string (Base64 encoded)
     * @throws Exception if encryption fails
     */
    public static String encrypt(String plaintext, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encryptedBytes = cipher.doFinal(plaintext.getBytes("UTF-8"));
        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    /**
     * Decrypts an encrypted string using the provided AES key.
     * 
     * @param encryptedText The encrypted text (Base64 encoded)
     * @param key           The AES key
     * @return Decrypted plaintext
     * @throws Exception if decryption fails
     */
    public static String decrypt(String encryptedText, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decodedBytes = Base64.getDecoder().decode(encryptedText);
        byte[] decryptedBytes = cipher.doFinal(decodedBytes);
        return new String(decryptedBytes, "UTF-8");
    }

    /**
     * Encrypts a specific column in the database.
     * 
     * @param columnName     The name of the column to encrypt
     * @param tableName      The name of the table containing the column
     * @param connection     Database connection
     * @param encryptionKey  AES encryption key
     * @throws Exception if encryption or database operations fail
     */
    public static void encryptColumn(String columnName, String tableName, Connection connection, SecretKey encryptionKey) throws Exception {
        String selectQuery = String.format("SELECT id, %s FROM %s", columnName, tableName);
        String updateQuery = String.format("UPDATE %s SET %s = ? WHERE id = ?", tableName, columnName);

        try (PreparedStatement selectStmt = connection.prepareStatement(selectQuery);
             PreparedStatement updateStmt = connection.prepareStatement(updateQuery)) {

            ResultSet resultSet = selectStmt.executeQuery();

            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String originalValue = resultSet.getString(columnName);

                // Encrypt the column value
                String encryptedValue = encrypt(originalValue, encryptionKey);

                // Update the encrypted value back in the database
                updateStmt.setString(1, encryptedValue);
                updateStmt.setInt(2, id);
                updateStmt.executeUpdate();
            }
        } catch (Exception e) {
            throw new Exception("Error encrypting column: " + columnName, e);
        }
    }

    /**
     * Example usage of the ColumnEncryptor utility.
     */
    public static void main(String[] args) {
        // Replace with your database connection setup
        try (Connection connection = DBDAO.getConnection()) {
            // Generate AES encryption key
            SecretKey encryptionKey = generateAESKey();

            // Encrypt a specific column in the database
            encryptColumn("sensitive_data", "users", connection, encryptionKey);

            // Print the key for later use (store securely in production)
            String encodedKey = Base64.getEncoder().encodeToString(encryptionKey.getEncoded());
            System.out.println("Encryption Key (Base64): " + encodedKey);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

/**
 * Mock DBDAO class for obtaining database connections.
 * Replace with your actual database connection logic.
 */
class DBDAO {

    /**
     * Returns a database connection.
     * 
     * @return Connection - Database connection object
     * @throws Exception if connection fails
     */
    public static Connection getConnection() throws Exception {
        // Replace with actual database connection logic
        // Example:
        // return DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");
        throw new UnsupportedOperationException("Database connection logic not implemented.");
    }
}
```
