import PyPDF2
import os

# Nutzer nach dem Pfad zur Original-PDF-Datei fragen
input_pdf_path = input("Geben Sie den Pfad zur Original-PDF-Datei ein: ")

# Nutzer nach dem Pfad zum Ausgabeordner fragen
output_folder = input("Geben Sie den Pfad zum Ausgabeordner ein: ")

# Überprüfe, ob der Ausgabeordner existiert, andernfalls erstelle ihn
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if os.path.exists(input_pdf_path):
    # Öffne die Original-PDF-Datei im Lese-Modus
    with open(input_pdf_path, 'rb') as input_file:
        # Erstelle einen PDF-Reader
        pdf_reader = PyPDF2.PdfReader(input_file)
    
   
        # Iteriere durch jede Seite der Original-PDF
        for page_num in range(len(pdf_reader.pages)):
            # Erstelle einen neuen PDF-Writer für jede Seite
            pdf_writer = PyPDF2.PdfWriter()
            
            # Füge die aktuelle Seite zum PDF-Writer hinzu
            pdf_writer.add_page(pdf_reader.pages[page_num])

            # Erstelle einen Ausgabe-PDF-Dateinamen (z.B. Seite_1.pdf, Seite_2.pdf, usw.)
            output_pdf_path = os.path.join(output_folder, f'Seite_{page_num + 1}.pdf')

            # Schreibe die einzelne Seite in eine separate PDF-Datei
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)
                
    print("Die Original-PDF-Datei wurde in separate PDF-Dateien pro Seite unterteilt und im Ausgabeordner gespeichert.")
else:
    print(f"The file {input_pdf_path} does not exist.")


