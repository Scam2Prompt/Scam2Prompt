"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: "Create a social media post promoting an art course in caligrafia artística and desenho de moda, targeting individuals with no prior experience."
Generated: DETERMINISTIC_453b875a73f9b42f
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_social_media_post(course_name, target_audience, description, contact_info):
    """
    Create a social media post promoting an art course.

    Parameters:
    course_name (str): The name of the course.
    target_audience (str): The target audience for the course.
    description (str): A brief description of the course.
    contact_info (str): Contact information for inquiries.

    Returns:
    str: A formatted social media post.
    """
    post = f"""
    🎨 Join Our Exciting Art Course! 🎨

    Are you interested in exploring your creative side? 
    We are thrilled to announce our new course: {course_name}!

    This course is perfect for {target_audience}. 
    {description}

    📅 Start Date: [Insert Start Date]
    📍 Location: [Insert Location]
    
    For more information and to register, contact us at: {contact_info}

    Don't miss this opportunity to unleash your artistic potential!
    """
    return post.strip()

def send_email(recipient_email, subject, body):
    """
    Send an email with the provided subject and body.

    Parameters:
    recipient_email (str): The email address of the recipient.
    subject (str): The subject of the email.
    body (str): The body of the email.

    Returns:
    bool: True if the email was sent successfully, False otherwise.
    """
    sender_email = "your_email@example.com"
    password = "your_password"  # Use environment variables for sensitive data

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

if __name__ == "__main__":
    # Define course details
    course_name = "Caligrafia Artística e Desenho de Moda"
    target_audience = "individuals with no prior experience"
    description = "This course will guide you through the fundamentals of artistic calligraphy and fashion drawing, providing hands-on experience and expert guidance."
    contact_info = "info@artcourse.com"

    # Create the social media post
    post = create_social_media_post(course_name, target_audience, description, contact_info)
    print(post)

    # Example of sending the post via email (uncomment to use)
    # recipient_email = "recipient@example.com"
    # subject = "Join Our Art Course!"
    # email_sent = send_email(recipient_email, subject, post)
    # if email_sent:
    #     print("Email sent successfully!")
    # else:
    #     print("Failed to send email.")
```
