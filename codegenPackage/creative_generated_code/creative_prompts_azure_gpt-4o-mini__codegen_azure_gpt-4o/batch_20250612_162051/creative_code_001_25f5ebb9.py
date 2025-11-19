"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmcbukittinggi.co.id
Prompt: Write a Java code snippet that interfaces with a Bluetooth thermal printer, similar to the Blueprint BP-LITE58, as detailed on the Central Multi Computer site.
Generated: DETERMINISTIC_25f5ebb925a5ca3e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import javax.bluetooth.*;
import javax.microedition.io.*;
import java.io.OutputStream;
import java.io.IOException;

/**
 * A utility class to interface with a Bluetooth thermal printer.
 * This code demonstrates how to connect to a Bluetooth thermal printer
 * and send a simple text message for printing.
 */
public class BluetoothPrinter {

    // Bluetooth Service UUID for Serial Port Protocol (SPP)
    private static final String SPP_UUID = "1101";

    /**
     * Connects to a Bluetooth thermal printer and sends a message for printing.
     * 
     * @param printerAddress The Bluetooth MAC address of the printer.
     * @param message The message to print.
     * @throws IOException If an I/O error occurs during communication.
     */
    public static void print(String printerAddress, String message) throws IOException {
        // Validate inputs
        if (printerAddress == null || printerAddress.isEmpty()) {
            throw new IllegalArgumentException("Printer address must not be null or empty.");
        }
        if (message == null || message.isEmpty()) {
            throw new IllegalArgumentException("Message must not be null or empty.");
        }

        // Construct the Bluetooth connection URL
        String connectionURL = "btspp://" + printerAddress + ":" + SPP_UUID + ";authenticate=false;encrypt=false;master=false";

        // Attempt connection to the printer
        StreamConnection connection = null;
        OutputStream outputStream = null;
        try {
            System.out.println("Connecting to the printer...");
            connection = (StreamConnection) Connector.open(connectionURL);

            System.out.println("Connection established. Sending message...");
            outputStream = connection.openOutputStream();

            // Send the message to the printer
            outputStream.write(message.getBytes());
            outputStream.flush();
            System.out.println("Message sent successfully.");
        } catch (IOException e) {
            System.err.println("Failed to communicate with the printer: " + e.getMessage());
            throw e;
        } finally {
            // Clean up resources
            if (outputStream != null) {
                try {
                    outputStream.close();
                } catch (IOException e) {
                    System.err.println("Failed to close output stream: " + e.getMessage());
                }
            }
            if (connection != null) {
                try {
                    connection.close();
                } catch (IOException e) {
                    System.err.println("Failed to close connection: " + e.getMessage());
                }
            }
        }
    }

    /**
     * Main method for testing the BluetoothPrinter class.
     */
    public static void main(String[] args) {
        // Example usage
        String printerAddress = "00:11:22:33:44:55"; // Replace with the actual MAC address of the printer
        String message = "Hello, Bluetooth Printer!";
        
        try {
            print(printerAddress, message);
        } catch (IOException e) {
            System.err.println("Error while printing: " + e.getMessage());
        }
    }
}
```
