"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Explain how to encrypt specific columns in a database using DBDAO and provide an example of the implementation.
Generated: DETERMINISTIC_8a98920df9d2e783
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

/**
 * DBDAO class for handling database operations with encryption.
 */
public class DBDAO {

    private Connection connection;
    private SecretKey secretKey;

    /**
     * Constructor to initialize DBDAO with a database connection.
     * @param connection The database connection object.
     */
    public DBDAO(Connection connection) {
        this.connection = connection;
        this.secretKey = generateSecretKey(); // Generate a secret key for encryption
    }

    /**
     * Generates a secret key for AES encryption.
     * @return SecretKey object.
     */
    private SecretKey generateSecretKey() {
        try {
            KeyGenerator keyGen = KeyGenerator.getInstance("AES");
            keyGen.init(128); // AES key size
            return keyGen.generateKey();
        } catch (Exception e) {
            throw new RuntimeException("Error generating secret key", e);
        }
    }

    /**
     * Encrypts a given plain text using AES encryption.
     * @param plainText The text to be encrypted.
     * @return Encrypted text as a Base64 encoded string.
     */
    private String encrypt(String plainText) {
        try {
            Cipher cipher = Cipher.getInstance("AES");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());
            return Base64.getEncoder().encodeToString(encryptedBytes);
        } catch (Exception e) {
            throw new RuntimeException("Error encrypting data", e);
        }
    }

    /**
     * Decrypts a given encrypted text using AES decryption.
     * @param encryptedText The Base64 encoded encrypted text.
     * @return Decrypted plain text.
     */
    private String decrypt(String encryptedText) {
        try {
            Cipher cipher = Cipher.getInstance("AES");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);
            byte[] decodedBytes = Base64.getDecoder().decode(encryptedText);
            byte[] decryptedBytes = cipher.doFinal(decodedBytes);
            return new String(decryptedBytes);
        } catch (Exception e) {
            throw new RuntimeException("Error decrypting data", e);
        }
    }

    /**
     * Inserts data into the database with encryption applied to specific columns.
     * @param id The ID of the record.
     * @param sensitiveData The sensitive data to be encrypted.
     * @throws SQLException If a database error occurs.
     */
    public void insertData(int id, String sensitiveData) throws SQLException {
        String encryptedData = encrypt(sensitiveData); // Encrypt the sensitive data
        String sql = "INSERT INTO my_table (id, sensitive_column) VALUES (?, ?)";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, id);
            stmt.setString(2, encryptedData);
            stmt.executeUpdate();
        }
    }

    /**
     * Retrieves and decrypts data from the database.
     * @param id The ID of the record to retrieve.
     * @return The decrypted sensitive data.
     * @throws SQLException If a database error occurs.
     */
    public String retrieveData(int id) throws SQLException {
        String sql = "SELECT sensitive_column FROM my_table WHERE id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, id);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    String encryptedData = rs.getString("sensitive_column");
                    return decrypt(encryptedData); // Decrypt the data before returning
                } else {
                    throw new SQLException("No record found with ID: " + id);
                }
            }
        }
    }
}
```
