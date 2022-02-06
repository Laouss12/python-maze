# Pyamaze cree par Muhammed Huseen septembre 2021,
# c'est un module (bibliotheque) qui permet de creer et manipuler des labyrinthes.
# allez au fichier Demo pour voir la creation.

from pyamaze import maze, agent, textLabel

labyrinthe = maze(10, 10)  # Creation du labyrinthe, l'algo marche sur toute les tailles du matrice labyrinthe, ex: maze(20,30)
labyrinthe.CreateMaze()

chercheur = agent(labyrinthe, footprints=True)  # agent en bleu

txt = textLabel(labyrinthe, 'BENBERKANE Oussama, AFIA Sihem groupe', 1)

labyrinthe.run()
