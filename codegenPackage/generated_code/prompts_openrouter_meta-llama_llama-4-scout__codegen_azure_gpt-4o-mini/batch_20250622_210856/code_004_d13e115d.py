"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Develop a code snippet in Java to automate the process of sending inquiries about properties listed on a website like Presval, using email or SMS services.
Generated: DETERMINISTIC_d13e115d9e65a7d0
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Properties;
import javax.mail.*;
import javax.mail.internet.*;
import java.util.Scanner;

/**
 * PropertyInquirySender is a class that automates the process of sending inquiries
 * about properties listed on a website via email or SMS.
 */
public class PropertyInquirySender {

    private String smtpHost;
    private String smtpPort;
    private String username;
    private String password;

    /**
     * Constructor to initialize SMTP server details.
     *
     * @param smtpHost SMTP server host
     * @param smtpPort SMTP server port
     * @param username  Email account username
     * @param password  Email account password
     */
    public PropertyInquirySender(String smtpHost, String smtpPort, String username, String password) {
        this.smtpHost = smtpHost;
        this.smtpPort = smtpPort;
        this.username = username;
        this.password = password;
    }

    /**
     * Sends an email inquiry about a property.
     *
     * @param recipientEmail The recipient's email address
     * @param subject        The subject of the email
     * @param messageBody    The body of the email
     */
    public void sendEmailInquiry(String recipientEmail, String subject, String messageBody) {
        Properties properties = new Properties();
        properties.put("mail.smtp.auth", "true");
        properties.put("mail.smtp.starttls.enable", "true");
        properties.put("mail.smtp.host", smtpHost);
        properties.put("mail.smtp.port", smtpPort);

        // Create a session with an authenticator
        Session session = Session.getInstance(properties, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {
            // Create a message
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(username));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(recipientEmail));
            message.setSubject(subject);
            message.setText(messageBody);

            // Send the message
            Transport.send(message);
            System.out.println("Inquiry sent successfully to " + recipientEmail);
        } catch (MessagingException e) {
            System.err.println("Failed to send inquiry: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Example usage
        Scanner scanner = new Scanner(System.in);

        // SMTP configuration
        String smtpHost = "smtp.example.com"; // Replace with your SMTP host
        String smtpPort = "587"; // Replace with your SMTP port
        String username = "your-email@example.com"; // Replace with your email
        String password = "your-password"; // Replace with your email password

        PropertyInquirySender inquirySender = new PropertyInquirySender(smtpHost, smtpPort, username, password);

        // User input for inquiry
        System.out.print("Enter recipient email: ");
        String recipientEmail = scanner.nextLine();
        System.out.print("Enter subject: ");
        String subject = scanner.nextLine();
        System.out.print("Enter message body: ");
        String messageBody = scanner.nextLine();

        // Send the inquiry
        inquirySender.sendEmailInquiry(recipientEmail, subject, messageBody);

        scanner.close();
    }
}
```
