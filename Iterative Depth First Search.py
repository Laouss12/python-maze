# Pyamaze cree par Muhammed Huseen septembre 2021,
# c'est un module (bibliotheque) qui permet de creer et manipuler des labyrinthes.
# allez au fichier Demo pour voir la creation.

from pyamaze import maze, agent, textLabel


def IDFS(m):  # profondeur d'abord iteratif

    debut = (m.rows, m.cols)  # case debut recoit la derniere case
    explored = [debut]  # pour stocker tout les cases explorés
    route = [debut]  # pour stocker les cases en cours
    idfsPath = {}  # dictionnaire bfsPath prochainement utile pour l'affichage de la route directe
    routeIDFS = route  # pour stocker la valeur de la case qu'on doit retrouver lorsque la limite de la profondeur est atteinte
    n = 4  # limite de la profondeur

    while len(route) > 0:
        if n > 0:
            case = route.pop()  # returner la dernière valeur de route pour passer par profondeur
        else:  # si la longeur maximale de profondeur est atteinte
            case = routeIDFS.pop(0)  # returner la première valeur de route pour passer par largeur
            n = 4  # réeinitialisation de la variable limite

        if case == (1, 1):  # si on est arrivé au but sortir de while
            break

        # la matrice est accessibles a partir de la requette maze_map[],
        # les directions sont accessibles a partir de maze_map[][]

        for d in 'WNES':  # d: direction, WNES: les mouvements possibles
            a = False
            b = False
            c = False  # a, b, et c pour controler l'incrementation de n
            if m.maze_map[case][d] == True:  # d true si le chemin traité est libre (sans obstacles)
                if d == 'W':  # si le chemin libre est gauche
                    prochaineCase = (case[0], case[1] - 1)  # la prochaine recoit la case a gauche de la case en cours
                    n = n - 1
                    a = True
                if d == 'N' and a is False:  # si le chemin libre est haut
                    prochaineCase = (case[0] - 1, case[1])  # la prochaine recoit la case en haut de la case en cours
                    n = n - 1
                    b = True
                if d == 'E' and a is False and b is False:  # si le chemin libre est droite
                    prochaineCase = (case[0], case[1] + 1)  # la prochaine recoit la case a droite de la case en cours
                    n = n - 1
                    c = True
                if d == 'S' and a is False and b is False and c is False:  # si le chemin libre est bas
                    prochaineCase = (case[0] + 1, case[1])  # la prochaine recoit la case en bas de la case en cours
                    n = n - 1


                if prochaineCase in explored:  # si la case a deja ete explore
                    continue
                routeIDFS.append(case)  # ajouter la case a routeIDFS pour traiter quand la limite de profondeur est atteinte
                explored.append(prochaineCase)  # ajouter au cases deja exploré
                route.append(prochaineCase)  # ajouter a les cases en cours pour traitement
                idfsPath[prochaineCase] = case  # bfsPath de la prochaine case recoit la case avant elle (pour tracer la route direct)

    path = {}  # pour stocker les cases de la route directe
    pathCase = (1, 1)  # case de la route directe commence par la case de but
    while pathCase != debut:  # tq on est pas encore arrivé au debut
        path[idfsPath[pathCase]] = pathCase  # path[predecesseur de case] recoit case
        pathCase = idfsPath[pathCase]  # on avance, case recoit la case avant elle
    # comme ca path est rempli des cases de la route directe vers le but
    # si on veut voir le fonctionnement de l'algorithme au lieu de la route direct on return explored
    return explored


labyrinthe = maze(15, 20)  # Creation du labyrinthe, l'algo marche sur toute les tailles du matrice labyrinthe, ex: maze(20,30)
labyrinthe.CreateMaze()
path = IDFS(labyrinthe)  # Itineraire a suivre dans la variable path
chercheur = agent(labyrinthe, footprints=True)  # agent en bleu
labyrinthe.tracePath({chercheur: path})  # pour que l'agent suit l'itineraire generé par la fct IDFS
txt = textLabel(labyrinthe, 'BENBERKANE Oussama, AFIA Sihem groupe', 1)

labyrinthe.run()
