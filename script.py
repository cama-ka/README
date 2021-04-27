from simple_colors import *

def informations():
    title = input("Tape le nom de ton programme : ").capitalize()
    under_title = input("Le sous-titre : ").capitalize()
    slogan = input("Le slogan optionnel : ").capitalize()
    resum = input("Le résumé du projet : ").capitalize()
    inputs = (f"{title}\n{under_title}\n{slogan}\n{resum}")
    return inputs
   


def creating_readme():
    with open("README.md", "w") as file:
        file.write(informations())
        print(green('hello', ['bold', 'underlined']))
        file.close()
        
creating_readme()

def demarrage():
    prerequis = input("Pré-requis pour l'installation")
# Auteurs
# Liste des auteurs, avec leur titre et l’entreprise pour laquelle ils ou elles travaillent. Les contributeurs peuvent être énumérés à la suite ou dans un document séparé, exemple CONTRIBUTING.md.
# License
# Traite de la licence d’utilisation permise, ou non, principalement dans les projets publics.
# Autres éléments
# Outre les éléments clés, on peut également inclure les informations suivantes :

# Guide et standardisation
# Cette section informe sur les normes et conventions de développement adopté par l’équipe pour assurer une cohérence dans le code source.
# API
# Si votre application consomme une ou plusieurs API, cette partie inclus toutes les informations pertinentes les concernant.
# Exécution et écriture des tests
# Contient les informations nécessaire pour rouler les tests automatisés et comment en écrire selon les styles : « e2e, unit, acceptance, etc. »
# Compilation
# Inclus les commandes pour compiler le code avant le déploiement.
# Déploiement
# Tout ce qu’il faut savoir sur la ou les méthodes de déploiement selon les environnements.
# Fonctionnalités
# Simple liste des principales fonctionnalités. Pratique dans les projets « Open Source ».
# Technologies
# Si votre projet inclus d’autre projets/modules, énumérer ces derniers avec les liens vers leurs documentations respectives.
# Comment contribuer
# Surtout présent dans les projets « Open Source », cette section informe sur la procédure à suivre pour contribuer au code source. Si celle-ci comporte plusieurs étapes, un fichier type CONTRIBUTING.md est la norme.
# Versionnement
# Un peu à la manière de Guide et standardisation, cette section traite de la méthodologie applicable au code source, par exemple l’utilisation du Semantic Versioning ou GitFlow.
# Crédits
# Énumère les salutations à d’autres projets ayant servi de près ou de loin au projet en cours, les sources d’inspiration, etc.