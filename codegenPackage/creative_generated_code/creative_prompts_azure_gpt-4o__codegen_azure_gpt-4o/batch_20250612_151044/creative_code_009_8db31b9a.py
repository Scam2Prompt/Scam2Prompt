"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://focalize-app.pages.dev
Prompt: Create a code snippet for a notification system that uses native system alerts to notify users of Lens Protocol activity, ensuring robust customization options.
Generated: DETERMINISTIC_8db31b9a0a55d9a1
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import platform
import os
import subprocess

class NotificationSystem:
    """
    A system to send native system alerts to notify users of Lens Protocol activity.
    """

    def __init__(self, app_name="Lens Protocol Alert"):
        """
        Initializes the Notification System.

        :param app_name: Name of the application displayed in the notification.
        """
        self.app_name = app_name

    def send_notification(self, title, message, duration=5):
        """
        Sends a native system notification.

        :param title: The title of the notification.
        :param message: The body content of the notification.
        :param duration: Duration of the notification (in seconds). Only supported on certain platforms.
        :raises OSError: If the platform is unsupported.
        """
        system = platform.system()

        try:
            if system == "Darwin":  # macOS
                self._send_mac_notification(title, message)
            elif system == "Windows":  # Windows
                self._send_windows_notification(title, message, duration)
            elif system == "Linux":  # Linux
                self._send_linux_notification(title, message)
            else:
                raise OSError("Unsupported platform for notifications.")
        except Exception as e:
            # Log error and continue gracefully
            print(f"Failed to send notification: {e}")

    def _send_mac_notification(self, title, message):
        """
        Sends a notification on macOS using AppleScript.

        :param title: The title of the notification.
        :param message: The body content of the notification.
        """
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        except subprocess.SubprocessError as e:
            print(f"Error sending macOS notification: {e}")

    def _send_windows_notification(self, title, message, duration):
        """
        Sends a notification on Windows using 'win10toast' package.

        :param title: The title of the notification.
        :param message: The body content of the notification.
        :param duration: Duration of the notification (in seconds).
        """
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=duration)
        except ImportError:
            print("win10toast package is not installed. Please install it using `pip install win10toast`.")
        except Exception as e:
            print(f"Error sending Windows notification: {e}")

    def _send_linux_notification(self, title, message):
        """
        Sends a notification on Linux using 'notify-send'.

        :param title: The title of the notification.
        :param message: The body content of the notification.
        """
        try:
            subprocess.run(["notify-send", title, message], check=True)
        except FileNotFoundError:
            print("notify-send is not installed. Please install it via your package manager.")
        except subprocess.SubprocessError as e:
            print(f"Error sending Linux notification: {e}")


# Example usage of the NotificationSystem
if __name__ == "__main__":
    notifier = NotificationSystem(app_name="Lens Protocol Alert")
    notifier.send_notification(
        title="New Lens Activity",
        message="You have a new follower on Lens Protocol!",
        duration=10
    )
```
