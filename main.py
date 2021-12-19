from random import randint


def getinput(texte):
    invalide = True
    print(texte)
    while invalide:
        invalide = False
        inputtext = input('Entrez un nombre de 1 à 3 : ')
        if len(inputtext) != 1:
            invalide = True
        elif inputtext[0] < '1' or inputtext[0] > '3':
            invalide = True
        if invalide:
            print("Valeur invalide, veuillez réessayer")
        else:
            return inputtext


def gennums(amount):
    nums = [0] * amount
    for x in range(amount):
        nums[x] = randint(0, 9)
    return nums


def genans(nums, usernums):
    returnvalue = ""
    for x in range(len(nums)):
        if nums[x] == int(usernums[x]):
            returnvalue += "="
        elif nums[x] < int(usernums[x]):
            returnvalue += "<"
        else:
            returnvalue += ">"
    return returnvalue


def getanshard(nums, usernums):
    returnvaluetab = [None] * len(nums)
    returnvalue = ""
    inputcopy = [None] * len(nums)
    numscopy = [None] * len(usernums)

    for x in range(len(inputcopy)):
        inputcopy[x] = int(usernums[x])
        numscopy[x] = int(nums[x])
    for x in range(len(returnvaluetab)):
        if inputcopy[x] == numscopy[x]:
            numscopy[x] = None
            inputcopy[x] = None
            returnvaluetab[x] = "="
    for x in range(len(returnvaluetab)):
        if inputcopy[x] is not None:
            for y in range(len(inputcopy)):
                if inputcopy[x] == numscopy[y] and inputcopy[x] is not None:
                    numscopy[y] = None
                    inputcopy[x] = None
                    returnvaluetab[x] = "#"
    for x in range(len(returnvaluetab)):
        if returnvaluetab[x] is None:
            returnvaluetab[x] = "!"
        returnvalue += returnvaluetab[x]
    return returnvalue


def getnumbers():
    invalide = True
    while invalide:
        pasafficher = False
        invalide = False
        numberinputs = input()
        if len(numberinputs) != 4 and len(numberinputs) != 0:
            invalide = True
        elif len(numberinputs) == 0:
            pasafficher = False
            invalide2 = True
            while invalide2:
                invalide2 = False
                userans = input("Voulez vous quitter? y (oui) / n (non)")
                match userans:
                    case "y" | "Y":
                        return "quit"
                    case "n" | "N":
                        invalide = True
                        pasafficher = True
                        print("Entrez 4 chiffres sous le format XXXX")
                    case _:
                        invalide2 = True
                if invalide2:
                    print("Réponse invalide, veuillez réessayer.")
        else:
            for x in numberinputs:
                if x < '0' or x > '9':
                    invalide = True

        if invalide:
            if not pasafficher:
                print("Valeur invalide, veuillez réessayer")
        else:
            return numberinputs


def partiedifficile(regles):
    print(regles)
    nums = gennums(4)
    historique = ""
    for x in range(10):
        print("\nEssai #" + str(x + 1))
        print("Entrez 4 chiffres sous le format XXXX")
        usernum = getnumbers()
        if usernum == "quit":
            return False
        ans = getanshard(nums, usernum)
        if ans == "====":
            print("Bravo, vous avez gagné!")
            return True
        else:
            historique += "\n"
            historique += "Essai #" + str(x + 1) + "\t"
            for x in range(len(usernum)):
                historique += usernum[x]
            historique += "\t"
            for x in range(len(ans)):
                historique += ans[x]
            print(historique)
    numsstring = ""
    for x in nums:
        numsstring += str(x)
    print("Malheureusement, la réponse était " + numsstring)

    return False


def afficherwl(w, l):
    print("Nombre de parties gagnées : " + str(w))
    print("Nombre de parties perdues : " + str(l))


def partiefacile(regles):
    print(regles)
    nums = gennums(4)
    historique = ""
    for x in range(5):
        print("\nEssai #" + str(x + 1))
        print("Entrez 4 chiffres sous le format XXXX")
        usernum = getnumbers()
        if usernum == "quit":
            return False
        ans = genans(nums, usernum)
        if ans == "====":
            print("Bravo, vous avez gagné!")
            return True
        else:
            historique += "\n"
            historique += "Essai #" + str(x + 1) + "\t"
            for x in range(len(usernum)):
                historique += usernum[x]
            historique += "\t"
            for x in range(len(ans)):
                historique += ans[x]
            print(historique)
    numsstring = ""
    for x in nums:
        numsstring += str(x)
    print("Malheureusement, la réponse était " + numsstring)
    return False


menutext = "Bienvenue au jeu \"le maître des chiffres\" \n\t" \
           "1. Commencer une nouvelle partie facile\n\t2. " \
           "Commencer une nouvelle partie avancée\n\t3. " \
           "Quitter\n\t"
reglesfaciles = "Vous avez 5 essais pour trouver le nombre. Pour chaque position," \
                "\n\tun \"=\" indique que vous avez trouvé le bon chiffre." \
                "\n\tun \"<\" indique que le chiffre recherché est plus petit que votre nombre" \
                "\n\tun \">\" indique que le chiffre recherché est plus grand que votre nombre"
reglesdifficiles = "Vous avez 10 essais pour trouver le nombre. Pour chaque position," \
              "\n\tun \"=\" indique que vous avez trouvé le bon chiffre à la bonne position" \
              "\n\tun \"#\" indique que le chiffre est bon mais il n'est pas à la bonne position" \
              "\n\tun \"!\" indique que le chiffre ne fait pas partie de la liste\n"


W = 0
L = 0
userInput = 0
while userInput != 3:
    if W != 0 or L != 0:
        afficherwl(W, L)
    won = False
    userInput = int(getinput(menutext))
    match userInput:
        case 1:
            won = partiefacile(reglesfaciles)
        case 2:
            won = partiedifficile(reglesdifficiles)
    if won:
        W += 1
    else:
        L += 1
