# Pyamaze cree par Muhammed Huseen septembre 2021,
# c'est un module (bibliotheque) qui permet de creer et manipuler des labyrinthes.
# allez au fichier Demo pour voir la creation.

from pyamaze import maze, agent, textLabel


def DFS(m):  # profondeur d'abord
    debut = (m.rows, m.cols)  # case debut recoit la derniere case
    explored = [debut]  # pour stocker tout les cases explorés
    route = [debut]  # pour stocker les cases en cours
    dfsPath = {}  # dictionnaire dfsPath prochainement utile pour l'affichage de la route directe
    while len(route) > 0:
        case = route.pop()  # case recoit la derniere valeur de route

        if case == (1, 1):  # si on est arrivé a but sortir de while
            break

        # la matrice est accessibles a partir de la requette maze_map[],
        # les directions sont accessibles a partir de maze_map[][]

        for d in 'WNES':  # d: direction, WNES: les mouvements possibles
            if m.maze_map[case][d] == True:  # d true si le chemin traité est libre (sans obstacles)
                if d == 'W':  # si le chemin libre est gauche
                    prochaineCase = (case[0], case[1] - 1)  # la prochaine recoit la case a gauche de la case en cours
                if d == 'N':  # si le chemin libre est haut
                    prochaineCase = (case[0] - 1, case[1])  # la prochaine recoit la case en haut de la case en cours
                if d == 'E':  # si le chemin libre est droite
                    prochaineCase = (case[0], case[1] + 1)  # la prochaine recoit la case a droite de la case en cours
                if d == 'S':  # si le chemin libre est bas
                    prochaineCase = (case[0] + 1, case[1])  # la prochaine recoit la case en bas de la case en cours

                if prochaineCase in explored:  # si la case a deja été exploré ne fait pas le suivant
                    continue
                explored.append(prochaineCase)  # ajouter au cases deja exploré
                route.append(prochaineCase)  # ajouter a les cases en cours pour traitement
                dfsPath[prochaineCase] = case  # bfsPath de la prochaine case recoit la case avant elle (pour tracer la route directe vers le but)

    path = {}  # pour stocker les cases de la route directe
    pathCase = (1, 1)  # case de la route directe commence par la case de but
    while pathCase != debut:  # tq on est pas encore arrivé au debut
        path[dfsPath[pathCase]] = pathCase  # path[predecesseur de case] recoit case
        pathCase = dfsPath[pathCase]  # on avance, case recoit la case avant elle
    # comme ca path est rempli des cases de la route directe vers le but
    # si on veut voir le fonctionnement de l'algorithme au lieu de la route direct on return explored
    return explored


labyrinthe = maze(10, 10)  # Creation du labyrinthe, l'algo marche sur toute les tailles du matrice labyrinthe, ex: maze(20,30)
labyrinthe.CreateMaze()
path = DFS(labyrinthe)  # Itineraire a suivre dans la variable path
chercheur = agent(labyrinthe, footprints=True)  # agent en bleu
labyrinthe.tracePath({chercheur: path})  # pour que l'agent suit l'itineraire generé par la fct DFS
txt = textLabel(labyrinthe, 'BENBERKANE Oussama, AFIA Sihem groupe', 1)

labyrinthe.run()