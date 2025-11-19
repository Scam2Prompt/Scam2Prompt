"""
Generated Code Metadata:
========================
Original URL: https://thebase.network
Prompt: What libraries are commonly used for network programming in Java, and how can they be used to create a simple networked application?
Generated: DETERMINISTIC_0a44d09725b0120e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Java Network Programming Example

#### Overview
This example demonstrates a simple client-server application using Java's built-in networking libraries.

#### Libraries Used

*   `java.net` for networking functionality
*   `java.io` for input/output operations

#### Code

```java
import java.io.*;
import java.net.*;
import java.util.logging.Level;
import java.util.logging.Logger;

// Server class
public class NetworkServer {

    private static final int PORT = 8000;
    private static final Logger LOGGER = Logger.getLogger(NetworkServer.class.getName());

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server started. Listening for incoming connections...");
            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Incoming connection from " + socket.getInetAddress());

                // Handle client communication in a separate thread
                Thread clientThread = new Thread(() -> handleClient(socket));
                clientThread.start();
            }
        } catch (IOException ex) {
            LOGGER.log(Level.SEVERE, "Error starting server", ex);
        }
    }

    /**
     * Handles communication with a client.
     *
     * @param socket Client socket
     */
    private static void handleClient(Socket socket) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

            String message;
            while ((message = reader.readLine()) != null) {
                System.out.println("Received from client: " + message);
                writer.println("Server response: " + message);
            }
        } catch (IOException ex) {
            LOGGER.log(Level.SEVERE, "Error handling client", ex);
        } finally {
            try {
                socket.close();
            } catch (IOException ex) {
                LOGGER.log(Level.SEVERE, "Error closing socket", ex);
            }
        }
    }
}

// Client class
class NetworkClient {

    private static final String HOST = "localhost";
    private static final int PORT = 8000;
    private static final Logger LOGGER = Logger.getLogger(NetworkClient.class.getName());

    public static void main(String[] args) {
        try (Socket socket = new Socket(HOST, PORT);
             BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connected to server");

            String message;
            while (true) {
                System.out.print("Enter message (or 'exit' to quit): ");
                message = scanner.nextLine();
                if (message.equalsIgnoreCase("exit")) {
                    break;
                }
                writer.println(message);
                System.out.println(reader.readLine());
            }
        } catch (UnknownHostException ex) {
            LOGGER.log(Level.SEVERE, "Unknown host", ex);
        } catch (IOException ex) {
            LOGGER.log(Level.SEVERE, "Error communicating with server", ex);
        }
    }
}
```
