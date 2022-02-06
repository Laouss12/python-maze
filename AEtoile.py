# Pyamaze cree par Muhammed Huseen septembre 2021,
# c'est un module (bibliotheque) qui permet de creer et manipuler des labyrinthes.
# allez au fichier Demo pour voir la creation.

from pyamaze import maze, agent, textLabel
from queue import PriorityQueue  # PriorityQueue est un type avancé de structure de données


# Au lieu de retirer l'élément le plus a gauche, la Priority Queue
# trie et retire les éléments en fonction de leurs priorités.


def h(case1, case2):  # la fct d'heuristique return la distance entre la case en cours et la case but
    x1, y1 = case1
    x2, y2 = case2

    return abs(x1 - x2) + abs(y1 - y2)  # manhatten distance: distance verticale + distance horizontale
    # (somme des lignes) + (somme des colonnes)


def AEtoile(m):  # A*
    debut = (m.rows, m.cols)  # case debut recoit la derniere case
    explored = [debut]  # pour stocker tout les cases explorés
    g_score = {case: float('inf') for case in m.grid}  # fct g donne la distance entre le debut et la case en cours
    g_score[debut] = 0
    f_score = {case: float('inf') for case in m.grid}  # fct f est le cout de chemin,
    # la distance entre le debut et la case en cours
    # plus la distance entre la case en cours et la case but
    f_score[debut] = h(debut, (1, 1))  # f = g + h, pour l'instant g=0 donc f = h

    open = PriorityQueue()  # open est notre file d'attente
    open.put((h(debut, (1, 1)), h(debut, (1, 1)), debut))  # stocker les f dans la premiere case de open, les h dans la 2eme,
    # les cases dans la 3eme
    aPath = {}  # dictionnaire aPath prochainement utile pour l'affichage de la route directe

    while not open.empty():
        case = open.get()[2]  # 'case' recoit la 3eme case de open
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

                temp_g_score = g_score[case] + 1  # incrementer g car on est une case de plus loin du debut
                temp_f_score = temp_g_score + h(case, (1, 1))  # calculer f

                if temp_f_score < f_score[prochaineCase]:  # si la prochaine case est moins couteuse
                    explored.append(prochaineCase)  # ajouter au cases deja exploré
                    g_score[prochaineCase] = temp_g_score  # mettre a jour g
                    f_score[prochaineCase] = temp_f_score  # mettre a jour f
                    open.put((temp_f_score, h(prochaineCase, (1, 1)),
                              prochaineCase))  # enfiler cette prochaine case dans open
                    aPath[
                        prochaineCase] = case  # aPath de la prochaine case recoit la case avant elle (pour tracer la route directe vers le but)

    path = {}  # pour stocker les cases de la route directe
    pathCase = (1, 1)  # case de la route directe commence par la case de but
    while pathCase != debut:  # tq on est pas encore arrivé au debut
        path[aPath[pathCase]] = pathCase  # path[predecesseur de case] recoit case
        pathCase = aPath[pathCase]  # on avance, case recoit la case avant elle
    # comme ca path est rempli des cases de la route directe vers le but
    # si on veut voir le fonctionnement de l'algorithme au lieu de la route direct on return explored
    return explored


labyrinthe = maze(10,
                  10)  # Creation du labyrinthe, l'algo marche sur toute les tailles du matrice labyrinthe, ex: maze(20,30)
labyrinthe.CreateMaze()
path = AEtoile(labyrinthe)  # Itineraire a suivre dans la variable path
chercheur = agent(labyrinthe, footprints=True)  # agent en bleu
labyrinthe.tracePath({chercheur: path})  # pour que l'agent suit l'itineraire generé par la fct AEtoile
txt = textLabel(labyrinthe, 'BENBERKANE Oussama, AFIA Sihem groupe', 1)

labyrinthe.run()
