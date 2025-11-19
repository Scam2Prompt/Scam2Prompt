"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Create a Java program to monitor and manage a set of IP phones for a small business in Bogotá, integrating with existing telephone systems."
Generated: DETERMINISTIC_d38d97e5cb4f549a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.List;

/**
 * IP Phone Monitor and Manager for small businesses.
 * 
 * This program monitors and manages a set of IP phones, integrating with existing telephone systems.
 * 
 * @author [Your Name]
 */
public class IpPhoneMonitor {

    // Configuration
    private static final String TELEPHONE_SYSTEM_IP = "192.168.1.100";
    private static final int TELEPHONE_SYSTEM_PORT = 5060;
    private static final int BUFFER_SIZE = 1024;

    // IP Phone class to represent individual phones
    static class IpPhone {
        private String ipAddress;
        private int extension;

        public IpPhone(String ipAddress, int extension) {
            this.ipAddress = ipAddress;
            this.extension = extension;
        }

        public String getIpAddress() {
            return ipAddress;
        }

        public int getExtension() {
            return extension;
        }
    }

    public static void main(String[] args) {
        // Initialize IP phone list
        List<IpPhone> ipPhones = new ArrayList<>();

        // Add IP phones to the list (example)
        ipPhones.add(new IpPhone("192.168.1.10", 101));
        ipPhones.add(new IpPhone("192.168.1.11", 102));

        // Create a UDP socket to communicate with IP phones
        try (DatagramSocket socket = new DatagramSocket()) {
            // Monitor and manage IP phones
            monitorIpPhones(socket, ipPhones);
        } catch (IOException e) {
            System.err.println("Error creating socket: " + e.getMessage());
        }
    }

    /**
     * Monitor and manage IP phones by sending and receiving UDP messages.
     * 
     * @param socket    UDP socket to use for communication
     * @param ipPhones  List of IP phones to monitor and manage
     * @throws IOException if an I/O error occurs
     */
    private static void monitorIpPhones(DatagramSocket socket, List<IpPhone> ipPhones) throws IOException {
        // Send registration request to each IP phone
        for (IpPhone ipPhone : ipPhones) {
            sendRegistrationRequest(socket, ipPhone);
        }

        // Continuously listen for incoming UDP messages from IP phones
        while (true) {
            byte[] buffer = new byte[BUFFER_SIZE];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            socket.receive(packet);

            // Handle incoming message
            handleIncomingMessage(packet);
        }
    }

    /**
     * Send a registration request to an IP phone.
     * 
     * @param socket    UDP socket to use for communication
     * @param ipPhone   IP phone to send the registration request to
     * @throws IOException if an I/O error occurs
     */
    private static void sendRegistrationRequest(DatagramSocket socket, IpPhone ipPhone) throws IOException {
        // Create registration request message
        String message = "REGISTER sip:" + TELEPHONE_SYSTEM_IP + ":" + TELEPHONE_SYSTEM_PORT + " SIP/2.0\r\n";
        message += "Via: SIP/2.0/UDP " + ipPhone.getIpAddress() + ":5060\r\n";
        message += "From: <sip:" + ipPhone.getExtension() + "@" + TELEPHONE_SYSTEM_IP + ">\r\n";
        message += "To: <sip:" + ipPhone.getExtension() + "@" + TELEPHONE_SYSTEM_IP + ">\r\n";
        message += "Call-ID: " + System.currentTimeMillis() + "\r\n";
        message += "CSeq: 1 REGISTER\r\n";
        message += "Expires: 3600\r\n";
        message += "\r\n";

        // Send registration request to IP phone
        byte[] data = message.getBytes();
        DatagramPacket packet = new DatagramPacket(data, data.length, InetAddress.getByName(ipPhone.getIpAddress()), 5060);
        socket.send(packet);
    }

    /**
     * Handle an incoming UDP message from an IP phone.
     * 
     * @param packet  Incoming UDP packet
     */
    private static void handleIncomingMessage(DatagramPacket packet) {
        // Get the message from the packet
        String message = new String(packet.getData(), 0, packet.getLength());

        // Log the incoming message
        System.out.println("Received message from " + packet.getAddress().getHostAddress() + ":");
        System.out.println(message);

        // Handle the message based on its type (e.g., registration response, call setup request, etc.)
        if (message.startsWith("SIP/2.0 200")) {
            // Handle registration response
            handleRegistrationResponse(message);
        } else if (message.startsWith("INVITE")) {
            // Handle call setup request
            handleCallSetupRequest(message);
        }
    }

    /**
     * Handle a registration response from an IP phone.
     * 
     * @param message  Registration response message
     */
    private static void handleRegistrationResponse(String message) {
        // Log the registration response
        System.out.println("Registration response:");
        System.out.println(message);
    }

    /**
     * Handle a call setup request from an IP phone.
     * 
     * @param message  Call setup request message
     */
    private static void handleCallSetupRequest(String message) {
        // Log the call setup request
        System.out.println("Call setup request:");
        System.out.println(message);

        // Process the call setup request (e.g., route the call to the destination)
        processCallSetupRequest(message);
    }

    /**
     * Process a call setup request.
     * 
     * @param message  Call setup request message
     */
    private static void processCallSetupRequest(String message) {
        // Extract the destination extension from the message
        String[] lines = message.split("\r\n");
        String toHeader = null;
        for (String line : lines) {
            if (line.startsWith("To:")) {
                toHeader = line;
                break;
            }
        }

        if (toHeader != null) {
            String destinationExtension = toHeader.split("<sip:")[1].split("@")[0];

            // Route the call to the destination
            routeCall(destinationExtension);
        }
    }

    /**
     * Route a call to a destination extension.
     * 
     * @param destinationExtension  Destination extension
     */
    private static void routeCall(String destinationExtension) {
        // Log the call routing
        System.out.println("Routing call to extension " + destinationExtension);

        // Implement call routing logic here (e.g., use a database to find the destination IP phone)
        // For demonstration purposes, assume the destination IP phone is 192.168.1.20
        String destinationIpAddress = "192.168.1.20";

        // Send the call setup request to the destination IP phone
        sendCallSetupRequest(destinationIpAddress, destinationExtension);
    }

    /**
     * Send a call setup request to a destination IP phone.
     * 
     * @param destinationIpAddress  Destination IP address
     * @param destinationExtension  Destination extension
     */
    private static void sendCallSetupRequest(String destinationIpAddress, String destinationExtension) {
        // Create call setup request message
        String message = "INVITE sip:" + destinationExtension + "@" + TELEPHONE_SYSTEM_IP + " SIP/2.0\r\n";
        message += "Via: SIP/2.0/UDP " + TELEPHONE_SYSTEM_IP + ":" + TELEPHONE_SYSTEM_PORT + "\r\n";
        message += "From: <sip:caller@" + TELEPHONE_SYSTEM_IP + ">\r\n";
        message += "To: <sip:" + destinationExtension + "@" + TELEPHONE_SYSTEM_IP + ">\r\n";
        message += "Call-ID: " + System.currentTimeMillis() + "\r\n";
        message += "CSeq: 1 INVITE\r\n";
        message += "\r\n";

        // Send call setup request to destination IP phone
        try (DatagramSocket socket = new DatagramSocket()) {
            byte[] data = message.getBytes();
            DatagramPacket packet = new DatagramPacket(data, data.length, InetAddress.getByName(destinationIpAddress), 5060);
            socket.send(packet);
        } catch (IOException e) {
            System.err.println("Error sending call setup request: " + e.getMessage());
        }
    }
}
```
