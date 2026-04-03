# A livrer le Lundi

## Rôle de chaque membre

`CHEF DE PROJET`
`main.py`: C'est le chef d'orchestre. Il contient la boucle principale qui tourne en permanence, lit le choix de l'utilisateur, et appelle les bonnes fonctions des autres fichiers.

`Fatim POUYE`
`gestion_taches.py`: C'est le cerveau. Il contient la logique : comment créer une tâche, comment en supprimer une, comment changer son statut. Il ne sait pas d'où viennent les données ni comment elles sont affichées.

`Aziz DIOP`
`stockage_json.py`:C'est la mémoire. Il s'occupe uniquement de lire et d'écrire dans le fichier `data.json`. Il gère les cas d'erreur (fichier manquant, corrompu, etc.) pour que le reste du programme ne plante pas.

`Mamadou SECK`
`interface.py`: C'est la vitrine. Il gère tout ce que l'utilisateur voit et tape dans le terminal : le menu, l'affichage des tâches, et la récupération des saisies.

## Ce que fait le projet
Ce projet est un **gestionnaire de tâches qui fonctionne dans le terminal**. Il permet à un utilisateur de créer, suivre et organiser ses tâches directement depuis la ligne de commande, sans interface graphique. Les tâches sont sauvegardées dans un fichier `data.json` sur l'ordinateur, ce qui signifie qu'elles sont **conservées même après avoir fermé le programme**.

## Fonctionnement concret

Quand l'utilisateur lance le programme avec `python main.py`, il voit apparaître un menu avec 4 options :

1. Ajouter une tâche ()
L'utilisateur tape un titre (ex: "Préparer la présentation"). Le programme crée automatiquement un ID unique et attribue le statut `à faire` par défaut. La tâche est immédiatement sauvegardée dans `data.json`.

2. Supprimer une tâche
L'utilisateur choisit l'ID de la tâche à effacer. Le programme la retire de la liste et met à jour le fichier JSON.

3. Afficher toutes les tâches
Le programme affiche dans le terminal la liste complète des tâches avec leur ID, leur titre et leur statut actuel.

0. Quitter
Ferme le programme proprement.

## Comment les données sont stockées

Toutes les tâches sont enregistrées dans un fichier `data.json` sous ce format :

```json
[
    {"id": 1, "titre": "Préparer la présentation", "statut": "en cours"},
    {"id": 2, "titre": "Rendre le rapport", "statut": "à faire"}
]
```

Ce fichier est créé automatiquement au premier lancement. Si le fichier est absent, vide ou corrompu, le programme démarre avec une liste vide sans planter.

## Nom des fonctions
# ajouter_tache, supprimer_tache, modifier_statut
# charger_taches, sauvegarder_taches
# afficher_menu, afficher_taches, demander_saisie