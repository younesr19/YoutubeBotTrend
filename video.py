#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8
import fonction


class Video:

    def __init__(self,classement,titre,chaine,vues,temps,publication,lien):#Constructeur de vidéo
        self.classement = classement
        self.titre = titre
        self.chaine = chaine
        self.vues = vues
        self.temps = temps
        self.publication = publication
        self.lien = lien


    def __str__(self):
        return "[titre="+self.titre+",chaine="+self.chaine+",vues="+str(self.vues)+",temps="+str(self.temps)+",publication="+self.publication+",lien="+self.lien+"]"

    def __unicode__(self):
        return u"[titre="+self.titre+",chaine="+self.chaine+",vues="+str(self.vues)+",publication="+self.publication+"]"

    def getRatioUpperTitre(self):
        return fonction.ratio_upper(self.titre)

    def aUnTirer(self):
        if self.titre.find(' - ') == -1:
            return False
        else:
            return True

    def estDureeMoyenne(self):
        return self.temps<240
