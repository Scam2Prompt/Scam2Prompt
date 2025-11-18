"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write a script to generate a notice board system for announcements like holidays or portal maintenance, as seen on the RSP Bharat website.
Generated: DETERMINISTIC_5db2e4d22fcf57ae
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Notice Board System for Announcements
This script implements a simple notice board system for displaying announcements
such as holidays or portal maintenance notifications. It supports adding, viewing,
editing, and deleting notices.

Requirements:
- Python 3.x
"""

import datetime

class NoticeBoard:
    def __init__(self):
        """Initialize the notice board with an empty list of notices."""
        self.notices = []

    def add_notice(self, title, content, expiration_date):
        """
        Add a new notice to the notice board.
        
        Parameters:
        title (str): Title of the notice.
        content (str): Content/details of the notice.
        expiration_date (datetime.date): Expiration date of the notice.
        
        Raises:
        ValueError: If the expiration date is in the past.
        """
        if expiration_date < datetime.date.today():
            raise ValueError("Expiration date cannot be in the past.")
        self.notices.append({
            "title": title,
            "content": content,
            "expiration_date": expiration_date,
            "created_at": datetime.datetime.now()
        })
        print(f"Notice '{title}' added successfully!")

    def view_notices(self):
        """
        View all active notices on the notice board.
        Notices that have expired will not be displayed.
        """
        print("---- Active Notices ----")
        active_notices = [notice for notice in self.notices
                          if notice["expiration_date"] >= datetime.date.today()]
        if not active_notices:
            print("No active notices available.")
        else:
            for i, notice in enumerate(active_notices):
                print(f"{i + 1}. {notice['title']} (Expires: {notice['expiration_date']})")
                print(f"   {notice['content']}")
                print(f"   Created on: {notice['created_at']}")
                print()

    def edit_notice(self, index, title=None, content=None, expiration_date=None):
        """
        Edit an existing notice by index.
        
        Parameters:
        index (int): Index of the notice to edit (1-based index).
        title (str): New title for the notice (optional).
        content (str): New content for the notice (optional).
        expiration_date (datetime.date): New expiration date (optional).
        
        Raises:
        IndexError: If the index is invalid.
        ValueError: If the expiration date is in the past.
        """
        try:
            notice = self.notices[index - 1]
        except IndexError:
            raise IndexError("Invalid notice index.")
        
        if expiration_date and expiration_date < datetime.date.today():
            raise ValueError("Expiration date cannot be in the past.")
        
        if title:
            notice["title"] = title
        if content:
            notice["content"] = content
        if expiration_date:
            notice["expiration_date"] = expiration_date
        
        print(f"Notice at index {index} updated successfully!")

    def delete_notice(self, index):
        """
        Delete a notice by index.
        
        Parameters:
        index (int): Index of the notice to delete (1-based index).
        
        Raises:
        IndexError: If the index is invalid.
        """
        try:
            deleted_notice = self.notices.pop(index - 1)
            print(f"Notice '{deleted_notice['title']}' deleted successfully!")
        except IndexError:
            raise IndexError("Invalid notice index.")


# --- Example Usage ---
if __name__ == "__main__":
    notice_board = NoticeBoard()

    try:
        # Add notices
        notice_board.add_notice(
            "Holiday Announcement",
            "Office will be closed on 25th December due to Christmas.",
            datetime.date(2023, 12, 25)
        )
        notice_board.add_notice(
            "Portal Maintenance",
            "The portal will be down for maintenance on 5th January from 10 PM to 2 AM.",
            datetime.date(2024, 1, 5)
        )

        # View notices
        notice_board.view_notices()

        # Edit a notice
        notice_board.edit_notice(
            index=1,
            content="Office will be closed on 25th December for Christmas celebrations.",
            expiration_date=datetime.date(2023, 12, 26)
        )

        # View notices after editing
        notice_board.view_notices()

        # Delete a notice
        notice_board.delete_notice(index=2)

        # View notices after deletion
        notice_board.view_notices()

    except Exception as e:
        print(f"Error: {e}")
```
