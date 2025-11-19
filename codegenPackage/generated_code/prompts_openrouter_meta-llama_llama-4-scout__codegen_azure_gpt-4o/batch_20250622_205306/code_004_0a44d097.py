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

```java
// Import necessary libraries for network programming in Java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

// A simple networked application demonstrating a server-client communication
public class SimpleNetworkApp {

    // Main method to run the application
    public static void main(String[] args) {
        // Start the server in a separate thread
        new Thread(() -> startServer(8080)).start();

        // Start the client in a separate thread
        new Thread(() -> startClient("localhost", 8080)).start();
    }

    /**
     * Starts a simple server that listens for incoming connections and responds to client messages.
     *
     * @param port The port number to bind the server to.
     */
    public static void startServer(int port) {
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server started on port " + port);

            // Accept incoming client connections
            try (Socket clientSocket = serverSocket.accept();
                 BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                 PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                System.out.println("Client connected.");

                // Read and respond to client messages
                String message;
                while ((message = in.readLine()) != null) {
                    System.out.println("Received from client: " + message);
                    out.println("Server received: " + message);
                }
            }
        } catch (Exception e) {
            // Handle exceptions gracefully
            System.err.println("Server error: " + e.getMessage());
        }
    }

    /**
     * Starts a simple client that connects to the server and sends messages.
     *
     * @param host The server's hostname or IP address.
     * @param port The server's port number.
     */
    public static void startClient(String host, int port) {
        try (Socket socket = new Socket(host, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {

            System.out.println("Connected to server.");

            // Send messages to the server
            out.println("Hello, Server!");
            out.println("How are you?");
            out.println("Goodbye!");

            // Read responses from the server
            String response;
            while ((response = in.readLine()) != null) {
                System.out.println("Received from server: " + response);
            }
        } catch (Exception e) {
            // Handle exceptions gracefully
            System.err.println("Client error: " + e.getMessage());
        }
    }
}
```
