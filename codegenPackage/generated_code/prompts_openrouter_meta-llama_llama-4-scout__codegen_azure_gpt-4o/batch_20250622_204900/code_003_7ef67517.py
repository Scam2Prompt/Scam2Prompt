"""
Generated Code Metadata:
========================
Original URL: https://echodex.live
Prompt: Given the name echodex and its .live domain, how might one design a simple echo server in Java that could be part of a larger live data processing service?
Generated: DETERMINISTIC_7ef6751765f6f3cf
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.*;
import java.net.*;

/**
 * EchoServer - A simple echo server implementation in Java.
 * This server listens for incoming client connections and echoes back any data received.
 * Designed to be part of a larger live data processing service.
 */
public class EchoServer {

    // Port number for the server to listen on
    private static final int PORT = 8080;

    public static void main(String[] args) {
        // Start the echo server
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("EchoServer is running on port " + PORT);

            // Continuously accept client connections
            while (true) {
                try {
                    // Accept a client connection
                    Socket clientSocket = serverSocket.accept();
                    System.out.println("Client connected: " + clientSocket.getInetAddress());

                    // Handle the client connection in a separate thread
                    new Thread(new ClientHandler(clientSocket)).start();
                } catch (IOException e) {
                    System.err.println("Error accepting client connection: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Error starting server: " + e.getMessage());
        }
    }

    /**
     * ClientHandler - Handles communication with a single client.
     */
    private static class ClientHandler implements Runnable {
        private final Socket clientSocket;

        public ClientHandler(Socket clientSocket) {
            this.clientSocket = clientSocket;
        }

        @Override
        public void run() {
            try (
                // Set up input and output streams for the client
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)
            ) {
                String inputLine;
                // Read data from the client and echo it back
                while ((inputLine = in.readLine()) != null) {
                    System.out.println("Received: " + inputLine);
                    out.println(inputLine); // Echo the data back to the client
                }
            } catch (IOException e) {
                System.err.println("Error handling client: " + e.getMessage());
            } finally {
                try {
                    // Close the client socket
                    clientSocket.close();
                    System.out.println("Client disconnected: " + clientSocket.getInetAddress());
                } catch (IOException e) {
                    System.err.println("Error closing client socket: " + e.getMessage());
                }
            }
        }
    }
}
```
