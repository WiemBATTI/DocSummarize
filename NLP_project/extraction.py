import os
import fitz  # Cette bibliothèque est appelée "fitz" dans PyMuPDF
from docx import Document
from langdetect import detect

def check_file_type(file_path):
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == '.pdf':
        return 'pdf'
    elif file_extension.lower() == '.docx':
        return 'docx'
    elif file_extension.lower() == '.txt':
        return 'txt'
    else:
        raise ValueError("Unsupported file type. : {}".format(file_extension))

def process_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("file does not exist : {}".format(file_path))

    try:
        file_type = check_file_type(file_path)
        # Continuer avec le traitement du fichier ici
    except ValueError as e:
        print(e)
        print("Arrêt du programme.")




def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_document = fitz.open(pdf_file)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_document.close()
    return text








def extract_text_from_word(word_file):

  # Ouvrir le document Word
  doc = Document(word_file)

  # Extraire le texte du document
  text = ""

  for paragraph in doc.paragraphs:
      text += paragraph.text + "\n"
  return text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
        return text


def extract_text(file_path):
     file_type = check_file_type(file_path)
     print(file_type)

     if file_type == 'pdf':
         #print("C'est un fichier PDF.")
         text = extract_text_from_pdf(file_path)
         return text
     elif file_type == 'docx':
          #print("C'est un fichier DOCX.")
          text = extract_text_from_word(file_path)
          return text

     elif file_type == 'txt':
          #print("C'est un fichier TXT.")
          text = extract_text_from_txt(file_path)
          return text

     else:
          return "Ce n'est ni un fichier PDF ni un fichier DOCX."


#detecter la langue du texte

def detect_lang(text):
    detected_language = detect(text)
    return detected_language



