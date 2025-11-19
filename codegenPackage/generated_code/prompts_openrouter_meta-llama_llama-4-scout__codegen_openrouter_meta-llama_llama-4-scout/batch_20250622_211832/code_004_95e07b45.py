"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Develop a chatbot that provides information about SMKN 1 Kadipaten's programs, such as Pembentukan Karakter dan Integritas, and facilities like Fasilitas dan Infrastruktur.
Generated: DETERMINISTIC_95e07b45d8cc7079
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

# Define a class for the chatbot
class SMKN1KadipatenChatbot:
    def __init__(self):
        # Initialize programs and facilities data
        self.programs = {
            "Pembentukan Karakter dan Integritas": "Program Pembentukan Karakter dan Integritas SMKN1 Kadipaten bertujuan untuk membentuk karakter siswa yang berintegritas dan berakhlak mulia.",
            "Program Lainnya": "Informasi program lainnya dapat dilihat di situs web resmi SMKN1 Kadipaten."
        }

        self.facilities = {
            "Fasilitas dan Infrastruktur": "SMKN1 Kadipaten memiliki fasilitas dan infrastruktur yang memadai untuk mendukung proses belajar mengajar, seperti laboratorium, perpustakaan, dan ruang kelas.",
            "Fasilitas Lainnya": "Informasi fasilitas lainnya dapat dilihat di situs web resmi SMKN1 Kadipaten."
        }

    # Method to get program information
    def get_program_info(self, program_name):
        try:
            return self.programs[program_name]
        except KeyError:
            return "Mohon maaf, program tersebut tidak tersedia."

    # Method to get facility information
    def get_facility_info(self, facility_name):
        try:
            return self.facilities[facility_name]
        except KeyError:
            return "Mohon maaf, fasilitas tersebut tidak tersedia."

    # Method to handle user query
    def handle_query(self, query):
        query = query.lower()
        if "program" in query:
            program_name = query.replace("program ", "")
            return self.get_program_info(program_name.capitalize())
        elif "fasilitas" in query or "fasilitas dan infrastruktur" in query:
            facility_name = query.replace("fasilitas ", "").replace("fasilitas dan infrastruktur", "Fasilitas dan Infrastruktur")
            return self.get_facility_info(facility_name.capitalize())
        else:
            return "Mohon maaf, saya tidak mengerti pertanyaan Anda."

def main():
    chatbot = SMKN1KadipatenChatbot()
    print("Selamat datang di chatbot SMKN1 Kadipaten!")
    
    while True:
        user_query = input("Anda: ")
        if user_query.lower() == "exit":
            print("Chatbot: Sampai jumpa lagi!")
            break
        else:
            print("Chatbot: ", chatbot.handle_query(user_query))

if __name__ == "__main__":
    main()
```
