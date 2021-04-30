def informations():
    title = input("Tape le nom de ton programme : ").capitalize()
    under_title = input("Le sous-titre : ").capitalize()
    slogan = input("Le slogan optionnel : ").capitalize()
    resum = input("Le résumé du projet : ").capitalize()

    inputs = (f"## {title}<br> ### {under_title}<br> {slogan}<br>{resum} <br>")
    return inputs
        
def auteurs():
    auteur = input("Indiquez le prénom et nom de l'auteur : ").title()
    entreprise = input("Indiquez son entreprise : ").capitalize()
    # auteur_complet = str(f"{auteur}. {entreprise}")
    return f"{auteur}. {entreprise}"
    
def prerequis():
    pre_info = input("notez votre pré-requis : ").capitalize()
    prerequis_infos = (f"* {pre_info}<br>")
    return prerequis_infos

def compte(variable, func):
    print(f"Combien {variable} avez-vous à notifier? Tapez un nombre à partir de 0 :  ")
    number = int(input())
    i = 1
    try:
        while i <= number:
            i += 1
            response = func()
            with open("test.txt","a") as file:
                file.write(response)
                file.close()
    except OSError:
        print("ça ne fonctionne pas")


def main():
    with open("README.md","w") as file:
        file.write(informations())
        file.close()
    compte("pré-requis", prerequis)
    compte("auteurs", auteurs)
    
            
if __name__ == "__main__":
    main()