def ajouter_tache(taches, titre):
    if not titre:
        return taches, False, "le titre est vide"
    for tache in taches:
        if tache['titre'].lower() == titre.lower:
            return taches, False, f"la taches '{titre}' existe"
    nouvel_tache = {
        "id"    : len(taches) + 1,
        "titre" : titre,
        "statut": "à faire"
    }
    taches.append(nouvel_tache)
    return taches, True, f"la tache '{titre} est ajoutéé"


def supprimer_tache(taches, id_tache):
    for tache in taches:
        if tache["id"] == id_tache:
            taches.remove(tache)
            return taches, True, f"tache '{tache['titre']}' supprimée"
    return taches, False, f"Aucune tache avec l'id {id_tache}"
               

def modifier_statut(taches, id_tache, nouveau_statut):
    STATUT_VALIDER = ["à faire", "en cours", "terminée"]
    if nouveau_statut not in STATUT_VALIDER:
        return taches, False, "Statut invalide"
    
    for tache in taches:
        if tache["id"] == id_tache:
            tache["statut"] = nouveau_statut
            return taches, True, f"statut modifié : '{nouveau_statut}'"    
          
    return taches, False, f"Aucune tâche avec l'id {id_tache}."