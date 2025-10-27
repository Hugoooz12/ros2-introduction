# ros2-introduction

Auteurs : Clément Durand et Hugo Bastien

Journée de prise en main de l'environnement ROS2

## Compilation

## Exercices et concepts

### Publisher/Subscriber basiques (exercices 1 à 3)

[lien du tuto de la doc (Humble)](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

Il est possible de faire communiquer un publisher et un subscriber autour d'un même sujet. Le publisher envoie le message et le subscriber le lis :)
On utlise les méthodes _create_publisher_ et _create_subscription_ de la classe Node :

    self.publisher = self.create_publisher(type, "topic", queue_len)
    self.subscription = self.create_subscription(type, "topic", callback_function, queue_len)

Dès que le subscriber détecte une entrée, la fonction _callback_ se joue.

#### Mise en place d'un timer

Il suffit d'utiliser la méthode _create_timer_ :

    self.timer = self.create_timer(timer_period, self.timer_callback)

le timer joue la fonction callback à chaque période.

### Message Custom (exercice 4)

[lien du tuto de la doc (Humble)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html#cmakelists-txt)

ROS autorise la définition de types de message personnalisés en spécifiant leur structure dans un fichier .msg. Une bonne pratique est de définir un package pour définir les messages qui sera en dépendances des autres packages qui consommeront les messages.

    ros2_ws/
    └── src/
        └── my_message_package/
            ├── package.xml
            ├── CMakeLists.txt
            ├── msg/
            │   └── Custom.msg
            └── ...
        └── my_package/
            ├── package.xml
            ├── setup.py
            ├── src/
            │   └── publisher.py
            │   └── subscriber.py
            └── ...

**/!\ttention :** la présence d'un CMakeLists.txt dans my_package rend la lecture du setup.py optionelle, il faut donc la spécifier sinon le build risque de ne pas fonctionner. Il faut ajouter l'instruction suivante :

    install(PROGRAMS
      src/publisher.py
      src/subscriber.py
      DESTINATION lib/${PROJECT_NAME}
    )

**/!\ttention #2 :** il faut ajouter une entête aux fichiers pour spécifier le language utiliser au moment du build : pour python _#!/usr/bin/env python3_

### Paramètres de Node (exercice 6)

En python, on utilise simplement la libraire sys pour récuperer la valeur de argv (voir la fonction main du node client).

### Client/Serveur (exercice 7)

[lien du tuto de la doc (Humble)](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)

la structure et l'architecture ressemble à celle du message custom, on remplace 'msg' par 'srv' :

    ros2_ws/
    └── src/
        └── my_server_package/
            ├── package.xml
            ├── CMakeLists.txt
            ├── srv/
            │   └── Custom.srv
            └── ...
        └── my_package/
            ├── package.xml
            ├── setup.py
            ├── src/
            │   └── client.py
            │   └── server.py
            └── ...

Nous avons fait le choix de placer les spécifications de notre serveur et de notre message dans le même package auxiliaire.

### Launch File (exercices 8 et 9)

[lien du tuto de la doc (Humble)](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html)
