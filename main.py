from gestion_taches import ajouter_tache, supprimer_tache, modifier_statut
from stockage_json import charger_taches, sauvegarder_taches
from interface import menu, afficher_taches, demander_saisie

def main():
    taches = charger_taches()

    while True:
        menu()
        choix = demander_saisie("Votre choix")

        if choix == "1":
            titre = demander_saisie("Titre de la tâche")
            taches, succes, message = ajouter_tache(taches, titre)
            print(message)
            if succes:
                sauvegarder_taches(taches)

        elif choix == "2":
            afficher_taches(taches)
            id_tache = int(demander_saisie("ID à supprimer"))
            taches, succes, message = supprimer_tache(taches, id_tache)
            print(message)
            if succes:
                sauvegarder_taches(taches)

        elif choix == "3":
            afficher_taches(taches)
            id_tache = int(demander_saisie("ID à modifier"))
            statut = demander_saisie("Nouveau statut (à faire / en cours / terminée)")
            taches, succes, message = modifier_statut(taches, id_tache, statut)
            print(message)
            if succes:
                sauvegarder_taches(taches)

        elif choix == "4":
            afficher_taches(taches)

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

main()