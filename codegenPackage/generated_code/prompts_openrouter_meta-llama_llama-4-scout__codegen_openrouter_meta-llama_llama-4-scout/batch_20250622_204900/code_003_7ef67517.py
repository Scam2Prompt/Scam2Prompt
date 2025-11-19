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
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * A simple echo server that listens on a specified port and responds with the received message.
 */
public class EchoServer {

    private static final int BUFFER_SIZE = 1024;
    private static final String DOMAIN = "echodex.live";
    private static final int PORT = 8000;

    /**
     * Starts the echo server on the specified port.
     * 
     * @param port the port to listen on
     * @throws IOException if an I/O error occurs
     */
    public static void startServer(int port) throws IOException {
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("Echo server started on port " + port);

        ExecutorService executor = Executors.newCachedThreadPool();
        while (true) {
            Socket socket = serverSocket.accept();
            System.out.println("New connection from " + socket.getInetAddress());

            // Handle client in separate thread
            executor.execute(new ClientHandler(socket));
        }
    }

    /**
     * Handles a client connection.
     */
    private static class ClientHandler implements Runnable {

        private final Socket socket;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println("Received: " + line);
                    writer.println(line); // Echo back to client
                }
            } catch (IOException e) {
                System.err.println("Error handling client: " + e.getMessage());
            } finally {
                try {
                    socket.close();
                } catch (IOException e) {
                    System.err.println("Error closing socket: " + e.getMessage());
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            startServer(PORT);
        } catch (IOException e) {
            System.err.println("Error starting server: " + e.getMessage());
            System.exit(1);
        }
    }
}
```
