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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SMKN1KadipatenChatbot:
    def __init__(self):
        # Initialize chatbot data
        self.data = {
            "programs": {
                "Pembentukan Karakter dan Integritas": "Program ini bertujuan untuk membentuk karakter siswa yang berintegritas, disiplin, dan bertanggung jawab.",
            },
            "facilities": {
                "Fasilitas dan Infrastruktur": "SMKN 1 Kadipaten memiliki fasilitas lengkap seperti laboratorium komputer, perpustakaan, ruang kelas yang nyaman, dan lapangan olahraga."
            }
        }

    def get_information(self, category, topic):
        """
        Fetch information based on category and topic.

        :param category: The category of information (e.g., 'programs', 'facilities').
        :param topic: The specific topic within the category.
        :return: Information string or error message if not found.
        """
        try:
            # Validate category
            if category not in self.data:
                return f"Maaf, kategori '{category}' tidak ditemukan. Silakan pilih 'programs' atau 'facilities'."

            # Validate topic
            if topic not in self.data[category]:
                return f"Maaf, topik '{topic}' tidak ditemukan dalam kategori '{category}'."

            # Return the requested information
            return self.data[category][topic]
        except Exception as e:
            logging.error(f"Error fetching information: {e}")
            return "Terjadi kesalahan saat memproses permintaan Anda. Silakan coba lagi."

    def chat(self):
        """
        Start the chatbot interaction with the user.
        """
        print("Selamat datang di Chatbot SMKN 1 Kadipaten!")
        print("Anda dapat bertanya tentang program atau fasilitas sekolah.")
        print("Ketik 'exit' untuk keluar.\n")

        while True:
            try:
                # Get user input
                category = input("Masukkan kategori (programs/facilities): ").strip().lower()
                if category == 'exit':
                    print("Terima kasih telah menggunakan Chatbot SMKN 1 Kadipaten. Sampai jumpa!")
                    break

                topic = input("Masukkan topik: ").strip()
                if topic == 'exit':
                    print("Terima kasih telah menggunakan Chatbot SMKN 1 Kadipaten. Sampai jumpa!")
                    break

                # Fetch and display information
                response = self.get_information(category, topic)
                print(f"\n{response}\n")
            except KeyboardInterrupt:
                print("\nChatbot dihentikan. Sampai jumpa!")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print("Terjadi kesalahan. Silakan coba lagi.\n")


# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = SMKN1KadipatenChatbot()
    chatbot.chat()
```
