def ecrire(func):
    with open("README.md","a") as file:
                    file.write(func)
                    file.close()

def informations():
    title = input("Tape le nom de ton programme : ").capitalize()
    under_title = input("Le sous-titre : ").capitalize()
    slogan = input("Le slogan optionnel : ").capitalize()
    resum = input("Le résumé du projet : ").capitalize()

    inputs = (f"## {title}\n### {under_title}\n {slogan}\n {resum}\n\n")
    return inputs
        
def auteurs():
    auteur = input("Indiquez le prénom et nom de l'auteur : ").title()
    entreprise = input("Indiquez son entreprise : ").capitalize()
    return f"{auteur}. {entreprise}"
    
def prerequis():
    pre_info = input("Notez votre pré-requis : ").capitalize()
    prerequis_infos = (f"* {pre_info}\n\n")
    return prerequis_infos

def compte(titre,variable, func):
    print(f"Combien {variable} avez-vous à notifier ?")
    while True:
        try:
            number = int(input())
            i = 1
            while i <= number:
                i += 1
                response = func()
                with open("README.md","a") as file:
                    file.write(titre)
                    file.write(response)
                    file.close()
            break
        except ValueError:
            print(f"Vous n'avez pas {variable}.")
            break
            
            
def telecharger_prog():
    prog = input("Comment télécharger le programme : ").capitalize()
    prog_f = (f"### Programme\n {prog}\n\n")
    return prog_f

def environnement_virtuel():
    env = input("Comment créer un environnement virtuel : ").capitalize()
    prog_f = (f"###Créer l'environnement virtuel \n - {env}\n")
    return prog_f

def lancement():
    lancer = input("Comment lancer le programme : ").capitalize()
    lancer_f = (f"####Télécharger le programme\n {lancer}\n\n")
    return lancer_f


def main():
    with open("README.md","w") as file:
        file.write(informations())
        file.close()
    compte(f"### Pré-requis \n","de pré-requis", prerequis)
    ecrire(telecharger_prog())
    ecrire(environnement_virtuel())
    ecrire(lancement())
    compte(f"### Auteurs \n","d' auteurs", auteurs)
    print("Le fichier est terminé.")
            
if __name__ == "__main__":
    main()