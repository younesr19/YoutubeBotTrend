#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8


#Fonction permettant de retirer le texte vide des tableaux
#Retourne un nouveau tableau
def retirer_vide_tableau(tableau):
    nouveau_tableau = []
    for elem in tableau:
        if elem.text != "":
            nouveau_tableau.append(elem)

    return nouveau_tableau



#Fonction permettant de separer une chaine de caractère avec un délimiteur
#Retourne un tableau
def separateur_texte(texte,separateur):
    return texte.split(separateur)



#Fonction permettant de déterminer le nombre de vues en entier d'une chaine de caractère
#Retourne un entier
def traitement_vues(vues):
    kpresent = vues.find('k')
    vues_decouper = []
    vues_finale = ""
    #Si k est absent alors c'est M
    if kpresent == -1:
        vues_million= separateur_texte(vues,' ')[0]
        virgulepresent = vues_million.find(',')

        #Si la virgule e est présent
        if virgulepresent != -1:
            vues_million = separateur_texte(vues_million,',')
            vues_finale = vues_million[0]+vues_million[1]+"00000"
        else:
            vues_finale = vues_million+"000000"

    else:
        vues_mille = separateur_texte(vues,' ')[0]
        virgulepresent = vues_mille.find(',')

        if virgulepresent != -1:
            vues_mille = separateur_texte(vues_mille,',')
            vues_finale = vues_mille[0]+vues_mille[1]+"00"
        else:
            vues_finale=vues_mille+"000"
    return int(vues_finale)


def determiner_temps(texte):
    if texte == "jour" or texte == "jours":
        return "J"
    elif texte == "heure" or texte == "heures":
        return "H"
    elif texte == "semaine" or texte == "semaines":
        return "S"
    elif texte == "mois":
        return "M"
    return "Erreur"

#Fonction permettant de déterminer la date de publication d'une chaine de caractère
#Retourne une chaine de caractère
def traitement_publication(publication):
    diffuse = u'Diffusé'
    diffusionpresent = publication.find(diffuse)
    publication_finale = ""
    #Si c'était pas un stream alors c'était une video
    if diffusionpresent == -1:
        publication_video_entier = separateur_texte(publication,' ')[3]
        publication_video_temps = separateur_texte(publication,' ')[4]

        publication_finale = "video-"+publication_video_entier+"-"+determiner_temps(publication_video_temps)

    #Sinon c'était un stream
    else:
        publication_video_entier = separateur_texte(publication,' ')[4]
        publication_video_temps = separateur_texte(publication,' ')[5]
        publication_finale = "vodstream-"+publication_video_entier+"-"+determiner_temps(publication_video_temps)



    return publication_finale

#Fonction permettant de retirer les vidéos qui ne sont pas en tendances (notament les recommendations)
#Retourne une nouvelle liste webdriver
def retirer_videoNonTrend(container):
    liste_section = container.find_elements_by_tag_name('ytd-item-section-renderer')
    liste_finale = []
    for section in liste_section:
        crea = ""
        try:
            crea = section.find_element_by_tag_name('yt-horizontal-list-renderer')
        except Exception:
            liste_finale.append(section)
    return liste_finale


def ratio_upper(titre):
    upper = 0
    long_titre = len(titre)
    for char in titre:
        if char.isupper():
            upper+=1
    val = upper/float(long_titre)
    return val
