import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize
from extraction import *
import re

#preprocess
def clean_text(text):
    pattern = r'\bM{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b' # supprimer les numéros roman
    cleaned_text = re.sub(pattern, '', text)
    cleaned_text = re.sub(r"[^a-zA-Z\s'’`àâäéèêëîïôöùûüœçÀÂÄÇÈÉÊËÎÏÔÖÙÛÜ.,]", '', cleaned_text)  # Supprime les caractères spéciaux
    cleaned_text = re.sub(r'\.{2,}', ' ', cleaned_text)  # Remplace les séquences de points par un seul espace
    cleaned_text = cleaned_text.lower()  # Convertit en minuscules
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text


def supp_debut(text):
    if detect_lang(text) == "fr":
        # String to search for
        chaine_a_chercher = " introduction générale "
    elif detect_lang(text) == "en":
        # String to search for
        chaine_a_chercher = " general introduction "
    else:
        print("ERROR")
        return text  # Return the original text if language is not supported

    i = text.find(chaine_a_chercher)

    if i != -1:
        # Calculate the number of occurrences of the string in the text
        nombre_occurrences = text.count(chaine_a_chercher)
        if nombre_occurrences >= 2:
            nombre_occurrences = 2
        for i in range(nombre_occurrences):
            start_index = 0
            if start_index != -1:
                end_index = text.find(chaine_a_chercher, start_index + 1)
                if end_index != -1:
                    cleaned_text = text[:start_index] + text[end_index:]
                    text = cleaned_text
                else:
                    cleaned_text = text  # If the end index is not found, remove only the introduction
            else:
                cleaned_text = text  # If the start index is not found, keep the original text
    else:
        cleaned_text = text

    return cleaned_text



def supp_fin(text):
   if detect_lang(text)== "fr":
       # Chaîne de caractères à rechercher
       chaine_a_chercher1 = " références "
       chaine_a_chercher2 = " bibliographie " 
       chaine_a_chercher3 = " nethographie "
       chaine_a_chercher4 = " webographie "
       
   elif detect_lang(text)== "en":
       # Chaîne de caractères à rechercher
       chaine_a_chercher1 = " references "
       chaine_a_chercher2 = " bibliography "
       chaine_a_chercher3 = " nethography "
       chaine_a_chercher4 = " webographie "
   else:
       print("ERROR")
   # Trouver l'indice où commence la table des matières

   ind1=text.find(chaine_a_chercher1)
   nombre_occurrences1 = text.count(chaine_a_chercher1)
   ind2=text.find(chaine_a_chercher2)
   nombre_occurrences2 = text.count(chaine_a_chercher2)
   ind3=text.find(chaine_a_chercher3)
   nombre_occurrences3 = text.count(chaine_a_chercher3)
   ind4=text.find(chaine_a_chercher4)
   nombre_occurrences4 = text.count(chaine_a_chercher4)
   start_index=[ind1,ind2,ind3,ind4]
 
   nb_occ=[ nombre_occurrences1, nombre_occurrences2, nombre_occurrences3, nombre_occurrences4]

   # Filtrer les indices différents de -1
   filtered_indices = [index for index in start_index if index != -1]


   if filtered_indices: # la liste n est pas vide
        i=start_index.index(min(filtered_indices))
     
        n = nb_occ[i]
       
        if n==1:
            cleaned_text = text[:min(filtered_indices)]
        else:
            cleaned_text = text

   else:
       cleaned_text = text  # Si l'indice de début n'est pas trouvé, conserver le texte d'origine

   return cleaned_text


#supprimer les phrase qui n'ont pas de sens
def has_few_words(sentence, max_words=5):
        words = nltk.word_tokenize(sentence)
        return len(words) <= max_words

def supp_phrases(text):
    sentences = sent_tokenize(text)
    

    filtered_sentences = [sentence for sentence in sentences if not has_few_words(sentence)]
    filtered_text = ' '.join(filtered_sentences)
    #removed_sentences = [sentence for sentence in sentences if has_few_words(sentence)]
    #print(removed_sentences)

    return filtered_text

