with open("test.txt","w") as file:
    file.write("essai")
    file.close()
        
def auteurs():
    auteur = input("Indiquez le prénom et nom de l'auteur : ").title()
    entreprise = input("Indiquez son entreprise : ").capitalize()
    # auteur_complet = str(f"{auteur}. {entreprise}")
    return f"{auteur}. {entreprise}"
    
def prerequis():
    pre_info = input("notez votre pré-requis : ")
    prerequis_infos = (f"- <h2>{pre_info}</h2></b><br>")
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

    
compte("auteurs", auteurs)
    