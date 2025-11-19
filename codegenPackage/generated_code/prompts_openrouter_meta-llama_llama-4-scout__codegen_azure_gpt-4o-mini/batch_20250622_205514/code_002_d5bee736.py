"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: "Generate a code snippet in Java to create a simple database for storing information about recyclable materials, inspired by the services provided by SCR Reciclados."
Generated: DETERMINISTIC_d5bee7362d5f0bb0
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * This class manages a simple SQLite database for storing information about recyclable materials.
 */
public class RecyclableMaterialsDatabase {

    private static final String DATABASE_URL = "jdbc:sqlite:recyclable_materials.db";

    /**
     * Initializes the database by creating the necessary table if it does not exist.
     */
    public void initializeDatabase() {
        String createTableSQL = "CREATE TABLE IF NOT EXISTS materials (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "name TEXT NOT NULL," +
                "type TEXT NOT NULL," +
                "recyclable BOOLEAN NOT NULL" +
                ");";

        try (Connection conn = DriverManager.getConnection(DATABASE_URL);
             PreparedStatement pstmt = conn.prepareStatement(createTableSQL)) {
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error initializing database: " + e.getMessage());
        }
    }

    /**
     * Adds a new recyclable material to the database.
     *
     * @param name        The name of the material.
     * @param type        The type of the material (e.g., plastic, paper).
     * @param recyclable   Indicates whether the material is recyclable.
     */
    public void addMaterial(String name, String type, boolean recyclable) {
        String insertSQL = "INSERT INTO materials (name, type, recyclable) VALUES (?, ?, ?);";

        try (Connection conn = DriverManager.getConnection(DATABASE_URL);
             PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
            pstmt.setString(1, name);
            pstmt.setString(2, type);
            pstmt.setBoolean(3, recyclable);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error adding material: " + e.getMessage());
        }
    }

    /**
     * Retrieves all recyclable materials from the database.
     */
    public void listMaterials() {
        String selectSQL = "SELECT * FROM materials;";

        try (Connection conn = DriverManager.getConnection(DATABASE_URL);
             PreparedStatement pstmt = conn.prepareStatement(selectSQL);
             ResultSet rs = pstmt.executeQuery()) {

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        ", Name: " + rs.getString("name") +
                        ", Type: " + rs.getString("type") +
                        ", Recyclable: " + rs.getBoolean("recyclable"));
            }
        } catch (SQLException e) {
            System.err.println("Error retrieving materials: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        RecyclableMaterialsDatabase db = new RecyclableMaterialsDatabase();
        db.initializeDatabase();

        // Example usage
        db.addMaterial("PET Bottle", "Plastic", true);
        db.addMaterial("Aluminum Can", "Metal", true);
        db.addMaterial("Cardboard Box", "Paper", true);

        System.out.println("List of recyclable materials:");
        db.listMaterials();
    }
}
```
