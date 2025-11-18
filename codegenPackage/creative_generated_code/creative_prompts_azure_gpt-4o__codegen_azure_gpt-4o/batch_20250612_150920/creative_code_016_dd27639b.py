"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Develop a Java program for database connectivity using Oracle 11g, referencing the training content available on edukacija.net.
Generated: DETERMINISTIC_dd27639b289d468c
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class OracleDBConnectivity {

    // JDBC URL, username, and password for Oracle Database
    private static final String DB_URL = "jdbc:oracle:thin:@localhost:1521:xe"; // Replace with your DB details
    private static final String DB_USER = "your_username";                     // Replace with your DB username
    private static final String DB_PASSWORD = "your_password";                 // Replace with your DB password

    /**
     * Main method to test database connectivity and query execution.
     */
    public static void main(String[] args) {
        Connection connection = null;

        try {
            // Load Oracle JDBC Driver
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // Establish connection to the database
            connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            System.out.println("Connected to Oracle Database successfully!");

            // Execute a sample query
            String query = "SELECT * FROM your_table"; // Replace with your table name
            executeQuery(connection, query);

        } catch (ClassNotFoundException e) {
            System.err.println("Oracle JDBC Driver not found!");
            e.printStackTrace();
        } catch (SQLException e) {
            System.err.println("Database connection or query execution failed!");
            e.printStackTrace();
        } finally {
            // Close the connection
            closeConnection(connection);
        }
    }

    /**
     * Executes a provided SQL query and prints the result set.
     *
     * @param connection Active database connection
     * @param query      SQL query string to execute
     */
    private static void executeQuery(Connection connection, String query) {
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;

        try {
            // Prepare and execute the query
            preparedStatement = connection.prepareStatement(query);
            resultSet = preparedStatement.executeQuery();

            // Print the query results
            System.out.println("Query Results:");
            while (resultSet.next()) {
                int id = resultSet.getInt("id"); // Replace "id" with your column name
                String name = resultSet.getString("name"); // Replace "name" with your column name
                System.out.println("ID: " + id + ", Name: " + name);
            }
        } catch (SQLException e) {
            System.err.println("Error executing query!");
            e.printStackTrace();
        } finally {
            // Close resources
            closeResultSet(resultSet);
            closeStatement(preparedStatement);
        }
    }

    /**
     * Closes the database connection.
     *
     * @param connection Connection to be closed
     */
    private static void closeConnection(Connection connection) {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("Database connection closed.");
            } catch (SQLException e) {
                System.err.println("Error closing connection!");
                e.printStackTrace();
            }
        }
    }

    /**
     * Closes the PreparedStatement.
     *
     * @param preparedStatement PreparedStatement to be closed
     */
    private static void closeStatement(PreparedStatement preparedStatement) {
        if (preparedStatement != null) {
            try {
                preparedStatement.close();
            } catch (SQLException e) {
                System.err.println("Error closing PreparedStatement!");
                e.printStackTrace();
            }
        }
    }

    /**
     * Closes the ResultSet.
     *
     * @param resultSet ResultSet to be closed
     */
    private static void closeResultSet(ResultSet resultSet) {
        if (resultSet != null) {
            try {
                resultSet.close();
            } catch (SQLException e) {
                System.err.println("Error closing ResultSet!");
                e.printStackTrace();
            }
        }
    }
}
```
