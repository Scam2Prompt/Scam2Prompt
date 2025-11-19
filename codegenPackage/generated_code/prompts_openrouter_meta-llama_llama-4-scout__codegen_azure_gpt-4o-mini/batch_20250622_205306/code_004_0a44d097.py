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
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * A simple networked application that demonstrates server-client communication
 * using Java's built-in networking libraries.
 */
public class SimpleNetworkApp {

    // Port number for the server to listen on
    private static final int PORT = 12345;

    public static void main(String[] args) {
        // Start the server in a separate thread
        new Thread(SimpleNetworkApp::startServer).start();

        // Start the client
        startClient();
    }

    /**
     * Starts a simple server that listens for incoming connections.
     */
    private static void startServer() {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server is listening on port " + PORT);
            while (true) {
                // Accept incoming client connections
                try (Socket clientSocket = serverSocket.accept()) {
                    System.out.println("New client connected: " + clientSocket.getInetAddress());
                    handleClient(clientSocket);
                } catch (IOException e) {
                    System.err.println("Error handling client: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Error starting server: " + e.getMessage());
        }
    }

    /**
     * Handles communication with a connected client.
     *
     * @param clientSocket the socket connected to the client
     */
    private static void handleClient(Socket clientSocket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

            String inputLine;
            // Read messages from the client and echo them back
            while ((inputLine = in.readLine()) != null) {
                System.out.println("Received from client: " + inputLine);
                out.println("Echo: " + inputLine);
            }
        } catch (IOException e) {
            System.err.println("Error in client communication: " + e.getMessage());
        }
    }

    /**
     * Starts a simple client that connects to the server and sends messages.
     */
    private static void startClient() {
        try (Socket socket = new Socket("localhost", PORT);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))) {

            String userInput;
            System.out.println("Client connected to server. Type messages to send:");

            // Read user input and send it to the server
            while ((userInput = stdIn.readLine()) != null) {
                out.println(userInput);
                System.out.println("Server response: " + in.readLine());
            }
        } catch (IOException e) {
            System.err.println("Error in client: " + e.getMessage());
        }
    }
}
```
