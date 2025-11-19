"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Develop a function to convert text encoding and charset for email messages, supporting multiple charsets like UTF-8, ISO-10646-UCS-2, and Windows-1256.
Generated: DETERMINISTIC_79844a4c5e18cdf1
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import chardet
from email import charset as email_charset
from email.header import Header
from email.message import Message
from email.mime.text import MIMEText
from typing import Optional, Union

# Register additional charsets not covered by email.charset by default
email_charset.add_charset('utf-8', email_charset.SHORTEST, None, 'utf-8')
email_charset.add_charset('iso-10646-ucs-2', email_charset.SHORTEST, None, 'utf-16')
email_charset.add_charset('windows-1256', email_charset.SHORTEST, None, 'windows-1256')

def convert_email_encoding(
    message: Union[str, Message],
    target_charset: str = 'utf-8',
    source_charset: Optional[str] = None
) -> Message:
    """
    Convert the encoding and charset of an email message or text to the specified charset.
    
    Args:
        message: The email message or text to convert. Can be either a string or email.Message object.
        target_charset: The target charset to convert to (default: 'utf-8').
        source_charset: The source charset of the message. If None, attempts to detect automatically.
    
    Returns:
        A new email.message.Message object with the converted content.
    
    Raises:
        ValueError: If the source charset cannot be detected or is invalid.
        UnicodeError: If the conversion fails.
    """
    # Create a new MIME message if input is a string
    if isinstance(message, str):
        if source_charset is None:
            detected = chardet.detect(message.encode('ascii', errors='replace'))
            source_charset = detected['encoding'] or 'ascii'
        
        try:
            msg = MIMEText(message, _charset=source_charset)
        except (UnicodeError, LookupError) as e:
            raise ValueError(f"Invalid source charset '{source_charset}': {str(e)}") from e
    else:
        msg = message
    
    # Convert the message to the target charset
    if target_charset.lower() != msg.get_charset():
        try:
            payload = msg.get_payload(decode=True)
            
            if payload is None:
                payload = msg.get_payload()
            
            if isinstance(payload, str):
                payload = payload.encode(msg.get_charset() or 'ascii')
            
            decoded_payload = payload.decode(msg.get_charset() or 'ascii')
            
            # Create new message with target charset
            new_msg = MIMEText(decoded_payload, _charset=target_charset)
            
            # Copy headers (except content-type which is set by MIMEText)
            for header, value in msg.items():
                if header.lower() not in ('content-type', 'content-transfer-encoding'):
                    if isinstance(value, str):
                        try:
                            # Try to decode header if it's encoded
                            decoded_header = Header(value).encode('utf-8')
                            new_msg[header] = decoded_header
                        except UnicodeError:
                            new_msg[header] = value
                    else:
                        new_msg[header] = value
            
            return new_msg
        
        except (UnicodeError, LookupError) as e:
            raise UnicodeError(f"Failed to convert from {msg.get_charset()} to {target_charset}: {str(e)}") from e
    
    return msg
```
