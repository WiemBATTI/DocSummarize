from extraction import *
from preprocess import *
from BART_model import *
import sys
import time
start_time = time.time()


try:
    if len(sys.argv) < 2:
        print("Usage: python main.py <chemin_du_fichier>")
        sys.exit(1)
    file_path = sys.argv[1]
    process_file(file_path)
except FileNotFoundError as e:
    print(e)
    print("Arrêt du programme.")


text=extract_text(file_path)
txt=clean_text(text)
txt=supp_debut(txt)
txt=supp_fin(txt)

txt=supp_phrases(txt)

x=generate_summary(txt)

print("  ", x.encode('utf-8').decode(sys.stdout.encoding))


end_time = time.time()

# Calcul de la durée
duration = end_time - start_time
#print("Temps d'exécution :", duration, "secondes")



