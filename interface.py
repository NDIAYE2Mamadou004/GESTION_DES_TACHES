def menu():
    print("\n=========Gestion des taches ========")
    print("\t1.Ajouter une tache")
    print("\t2.Supprimer une tache")
    print("\t3.Modifier le statut d'une tâche")  
    print("\t4.Afficher les taches")
    print("\t0.Quitter l application")


def demander_saisie(choix):
    return input(f"{choix} : ").strip()


def afficher_taches(taches):
    if not taches : 
        print("Aucun tache pour le moment !!")
    else :
        for tache in taches : 
            print(f"id :[{tache['id']}] - Titre :[{tache['titre']}] - Statut :[{tache['statut']}]")
            

    
            
        