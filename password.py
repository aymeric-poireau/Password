import hashlib

l, u, p, d = 0, 0, 0, 0

majuscule="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscule="abcdefghijklmnopqrstuvwxyz"
charactere_speciaux="$£@_§%&#µ*¤?!^%"
digits="0123456789"

while (l!=1 and u!=1 and p!=1 and d!=1):
    
    s = input("Entrer un mot de passe valide: ")
    if (len(s) >= 8):
        for i in s:
        
            # verifier si il y a une lettre minuscule de l'alphabet
            if (i in minuscule):
                l+=1           
 
            # verifier si il y a une lettre majuscule de l'alphabet
            if (i in majuscule):
                u+=1           

        
            # vérification si il y a un ou des nombres
            if (i in digits):
                d+=1           
 
            # vérification si il y a un ou des charactères spéciaux
            if(i in charactere_speciaux):
                p+=1       
    
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
        print("Votre mot de passe à été pris en compte")
        # cryptage du mot de passe
        hashed_ouput = hashlib.sha256(i.encode('ascii')).hexdigest()
        print(hashed_ouput)
    else:
        print("Votre mot de passe ne respecte pas les charactères requis")




