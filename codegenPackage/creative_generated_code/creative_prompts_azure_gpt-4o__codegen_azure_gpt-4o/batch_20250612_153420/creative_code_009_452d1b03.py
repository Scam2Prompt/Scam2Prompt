"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.net
Prompt: Recommend APIs or libraries to implement AI-based spam filtering for email accounts hosted on Sakura's rental server, referencing their high-accuracy spam filter feature.
Generated: DETERMINISTIC_452d1b032f17ecc8
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to implement AI-based spam filtering for email accounts hosted on Sakura's rental server.
It utilizes the `scikit-learn` library for machine learning, combined with `imaplib` and `email` for email interaction.
Ensure that Sakura's rental server supports IMAP for accessing email accounts.

Dependencies:
- scikit-learn
- numpy
- imaplib
- email
"""

import imaplib
import email
from email.policy import default
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Configuration for Sakura's rental server
IMAP_SERVER = "imap.sakura.ne.jp"
EMAIL_ACCOUNT = "your_email@sakura.ne.jp"
EMAIL_PASSWORD = "your_password"

def connect_to_email_server(imap_server, email_account, email_password):
    """
    Establish a connection to the email server using IMAP.
    """
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_account, email_password)
        return mail
    except imaplib.IMAP4.error as e:
        raise ConnectionError(f"Failed to connect to email server: {e}")

def fetch_emails(mail, folder="INBOX", num_emails=100):
    """
    Fetch emails from the specified folder and return a list of email contents.
    """
    try:
        mail.select(folder)
        status, email_ids = mail.search(None, 'ALL')
        email_list = []
        count = 0
        
        for email_id in email_ids[0].split()[::-1]:
            if count >= num_emails:
                break
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email, policy=default)
            email_body = msg.get_body(preferencelist=('plain')).get_content() if msg.is_multipart() else msg.get_payload()
            email_list.append(email_body)
            count += 1
        return email_list
    except Exception as e:
        raise RuntimeError(f"Error fetching emails: {e}")

def preprocess_data(emails, labels):
    """
    Preprocess the email data using TF-IDF vectorization.
    """
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X = vectorizer.fit_transform(emails)
    return X, labels, vectorizer

def train_spam_filter(X, y):
    """
    Train a spam filter using a Naive Bayes classifier.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Spam filter accuracy: {accuracy * 100:.2f}%")
    return classifier

def classify_email(classifier, vectorizer, email_content):
    """
    Classify a single email as spam or not spam.
    """
    email_vector = vectorizer.transform([email_content])
    prediction = classifier.predict(email_vector)
    return "Spam" if prediction[0] == 1 else "Not Spam"

def main():
    # Connect to the email server
    mail = connect_to_email_server(IMAP_SERVER, EMAIL_ACCOUNT, EMAIL_PASSWORD)
    
    # Fetch emails from the inbox
    print("Fetching emails...")
    emails = fetch_emails(mail, num_emails=100)
    
    # Sample labels (1 = Spam, 0 = Not Spam) for training; replace these with real labels if available
    labels = np.random.choice([0, 1], size=len(emails))  # Simulating labels for demonstration
    
    # Preprocess the data
    X, y, vectorizer = preprocess_data(emails, labels)
    
    # Train the spam filter
    print("Training spam filter...")
    classifier = train_spam_filter(X, y)
    
    # Example: Classify a single email
    print("Classifying a sample email...")
    example_email = "Congratulations! You've won a lottery. Click here to claim your prize."
    result = classify_email(classifier, vectorizer, example_email)
    print(f"The email was classified as: {result}")

if __name__ == "__main__":
    main()
```

Note:
1. Replace placeholders (`your_email@sakura.ne.jp`, `your_password`) with actual credentials.
2. Ensure dependencies are installed (`pip install scikit-learn numpy`).
3. This is a demonstration script and assumes that email labels are available for training. For production, actual labels should be provided.
