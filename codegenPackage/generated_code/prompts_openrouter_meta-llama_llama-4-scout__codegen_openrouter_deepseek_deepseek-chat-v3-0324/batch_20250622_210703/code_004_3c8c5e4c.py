"""
Generated Code Metadata:
========================
Original URL: https://uaelegalfirm.com
Prompt: Generate a sample contract for a client in Germany seeking legal representation in the UAE, using a template in German.
Generated: DETERMINISTIC_3c8c5e4c4f12b2c0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Mandatsvertrag für Rechtsvertretung in den VAE
Erstellt am: {current_date}
"""

from datetime import datetime

class Mandatsvertrag:
    """
    Vertragstemplate für deutsche Klienten mit Rechtsvertretung in den VAE
    """
    
    def __init__(self, client_name, client_address, uae_lawyer_name, uae_lawyer_firm):
        """
        Initialisiert den Mandatsvertrag
        
        Args:
            client_name (str): Name des Klienten
            client_address (str): Adresse des Klienten
            uae_lawyer_name (str): Name des Anwalts in den VAE
            uae_lawyer_firm (str): Kanzleibezeichnung in den VAE
        """
        self.client_name = client_name
        self.client_address = client_address
        self.uae_lawyer_name = uae_lawyer_name
        self.uae_lawyer_firm = uae_lawyer_firm
        self.creation_date = datetime.now().strftime("%d.%m.%Y")
        self.vertragstext = self._generate_contract()
    
    def _generate_contract(self):
        """
        Generiert den Vertragstext auf Deutsch
        """
        return f"""
MANDATSVERTRAG

Zwischen

{self.client_name}
{self.client_address}
(im Folgenden "Mandant" genannt)

und

{self.uae_lawyer_name}
{self.uae_lawyer_firm}
(im Folgenden "Rechtsanwalt" genannt)

wird folgender Vertrag geschlossen:

§ 1 Mandat
Der Rechtsanwalt übernimmt die rechtliche Vertretung des Mandanten in den Vereinigten Arabischen Emiraten (VAE) in folgenden Angelegenheiten:
[Konkrete Beschreibung der Mandatsaufgaben einfügen]

§ 2 Vergütung
Die Vergütung des Rechtsanwalts erfolgt nach der Gebührenordnung für Rechtsanwälte der VAE. Pauschalen oder Stundensätze sind gesondert zu vereinbaren.

§ 3 Kosten
Der Mandant trägt alle Gerichts- und Verfahrenskosten sowie Auslagen des Rechtsanwalts.

§ 4 Vertragsdauer
Dieser Vertrag tritt mit Unterzeichnung in Kraft und endet mit Abschluss des Mandats oder durch schriftliche Kündigung einer Partei.

§ 5 Anwendbares Recht
Für diesen Vertrag gilt das Recht der VAE. Gerichtsstand ist [Gerichtsstand einfügen].

Ort, Datum: __________________    Ort, Datum: __________________
_____________________________    _____________________________
(Mandant)                         (Rechtsanwalt)
"""

    def save_contract(self, filepath):
        """
        Speichert den Vertrag als Textdatei
        
        Args:
            filepath (str): Pfad zur Speicherdatei
            
        Raises:
            IOError: Wenn Datei nicht geschrieben werden kann
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self.vertragstext)
        except IOError as e:
            raise IOError(f"Vertrag konnte nicht gespeichert werden: {str(e)}")

# Beispielnutzung
if __name__ == "__main__":
    try:
        vertrag = Mandatsvertrag(
            client_name="Max Mustermann",
            client_address="Musterstraße 1, 10115 Berlin",
            uae_lawyer_name="Dr. Ahmed Al-Mansoori",
            uae_lawyer_firm="Al-Mansoori & Partners Law Firm, Dubai"
        )
        vertrag.save_contract("mandatsvertrag_uae.txt")
        print("Vertrag erfolgreich generiert und gespeichert.")
    except Exception as e:
        print(f"Fehler beim Erstellen des Vertrags: {str(e)}")
```
