"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Create a visitor tracking system for a company using DemirSoft's Ziyaretçi Takip Programı, including features for recording visitor information and tracking entry/exit times.
Generated: DETERMINISTIC_5b52873c2434b3cc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
import sys

class VisitorTrackingSystem:
    """
    A visitor tracking system for recording visitor information and tracking entry/exit times.
    """
    
    def __init__(self, db_name='visitor_tracking.db'):
        """
        Initialize the system with a SQLite database connection.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        """
        Create necessary tables if they don't exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                company TEXT,
                phone TEXT,
                email TEXT,
                purpose TEXT,
                host_employee TEXT,
                entry_time DATETIME NOT NULL,
                exit_time DATETIME,
                notes TEXT
            )
        ''')
        self.conn.commit()
    
    def add_visitor(self, full_name, company=None, phone=None, email=None, 
                   purpose=None, host_employee=None, notes=None):
        """
        Record a new visitor entry.
        """
        if not full_name:
            raise ValueError("Full name is required")
        
        entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            self.cursor.execute('''
                INSERT INTO visitors 
                (full_name, company, phone, email, purpose, host_employee, entry_time, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (full_name, company, phone, email, purpose, host_employee, entry_time, notes))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
    
    def record_exit(self, visitor_id):
        """
        Record visitor exit time.
        """
        exit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            self.cursor.execute('''
                UPDATE visitors 
                SET exit_time = ?
                WHERE id = ? AND exit_time IS NULL
            ''', (exit_time, visitor_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def get_active_visitors(self):
        """
        Retrieve all visitors who haven't exited yet.
        """
        try:
            self.cursor.execute('''
                SELECT * FROM visitors 
                WHERE exit_time IS NULL
                ORDER BY entry_time DESC
            ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def get_visitor_history(self, days=30):
        """
        Retrieve visitor history for the last N days.
        """
        cutoff_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        try:
            self.cursor.execute('''
                SELECT * FROM visitors 
                WHERE entry_time >= ?
                ORDER BY entry_time DESC
            ''', (cutoff_date,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def search_visitors(self, search_term):
        """
        Search visitors by name, company, or host employee.
        """
        search_term = f"%{search_term}%"
        
        try:
            self.cursor.execute('''
                SELECT * FROM visitors 
                WHERE full_name LIKE ? OR 
                      company LIKE ? OR 
                      host_employee LIKE ?
                ORDER BY entry_time DESC
            ''', (search_term, search_term, search_term))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()

def main_menu():
    """
    Display the main menu and handle user input.
    """
    vts = VisitorTrackingSystem()
    
    while True:
        print("\nDemirSoft Ziyaretçi Takip Programı")
        print("1. Yeni Ziyaretçi Kaydı")
        print("2. Ziyaretçi Çıkışı Kaydet")
        print("3. Aktif Ziyaretçileri Listele")
        print("4. Ziyaretçi Geçmişini Görüntüle")
        print("5. Ziyaretçi Ara")
        print("6. Çıkış")
        
        choice = input("Seçiminiz: ")
        
        if choice == '1':
            register_new_visitor(vts)
        elif choice == '2':
            record_visitor_exit(vts)
        elif choice == '3':
            list_active_visitors(vts)
        elif choice == '4':
            view_visitor_history(vts)
        elif choice == '5':
            search_visitors(vts)
        elif choice == '6':
            vts.close()
            print("Programdan çıkılıyor...")
            sys.exit()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

def register_new_visitor(vts):
    """
    Register a new visitor.
    """
    print("\nYeni Ziyaretçi Kaydı")
    full_name = input("Ad Soyad: ").strip()
    company = input("Firma (varsa): ").strip() or None
    phone = input("Telefon (varsa): ").strip() or None
    email = input("E-posta (varsa): ").strip() or None
    purpose = input("Ziyaret Amacı (varsa): ").strip() or None
    host_employee = input("Görüşülecek Personel (varsa): ").strip() or None
    notes = input("Notlar (varsa): ").strip() or None
    
    visitor_id = vts.add_visitor(full_name, company, phone, email, purpose, host_employee, notes)
    if visitor_id:
        print(f"Ziyaretçi başarıyla kaydedildi. ID: {visitor_id}")
    else:
        print("Ziyaretçi kaydedilirken bir hata oluştu.")

def record_visitor_exit(vts):
    """
    Record visitor exit.
    """
    print("\nZiyaretçi Çıkışı Kaydet")
    visitor_id = input("Ziyaretçi ID: ").strip()
    
    try:
        visitor_id = int(visitor_id)
    except ValueError:
        print("Geçersiz ID formatı.")
        return
    
    if vts.record_exit(visitor_id):
        print("Çıkış başarıyla kaydedildi.")
    else:
        print("Çıkış kaydedilemedi. Geçersiz ID veya ziyaretçi zaten çıkış yapmış.")

def list_active_visitors(vts):
    """
    List all active visitors.
    """
    print("\nAktif Ziyaretçiler:")
    visitors = vts.get_active_visitors()
    
    if not visitors:
        print("Aktif ziyaretçi bulunmamaktadır.")
        return
    
    for visitor in visitors:
        print(f"ID: {visitor[0]}, Ad: {visitor[1]}, Firma: {visitor[2] or 'N/A'}, "
              f"Giriş: {visitor[7]}, Görüşülecek: {visitor[6] or 'N/A'}")

def view_visitor_history(vts):
    """
    View visitor history.
    """
    days = input("\nSon kaç günün kaydını görüntülemek istersiniz? (Varsayılan: 30): ").strip()
    days = int(days) if days.isdigit() else 30
    
    print(f"\nSon {days} Günün Ziyaretçi Geçmişi:")
    visitors = vts.get_visitor_history(days)
    
    if not visitors:
        print("Kayıt bulunamadı.")
        return
    
    for visitor in visitors:
        exit_time = visitor[8] if visitor[8] else "Hala içeride"
        print(f"ID: {visitor[0]}, Ad: {visitor[1]}, Firma: {visitor[2] or 'N/A'}, "
              f"Giriş: {visitor[7]}, Çıkış: {exit_time}")

def search_visitors(vts):
    """
    Search visitors.
    """
    search_term = input("\nArama terimi girin (ad, firma veya personel): ").strip()
    
    if not search_term:
        print("Arama terimi g
