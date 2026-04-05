import json

FICHIER = "data.json"

def charger_taches():
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def sauvegarder_taches(taches):
    try:
        with open(FICHIER, "w", encoding="utf-8") as f:
            json.dump(taches, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        