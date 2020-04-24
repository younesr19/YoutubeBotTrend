#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8
import fonction


class Video:

    def __init__(self,titre,chaine,vues,publication,lien):#Constructeur de vidéo

        self.titre = titre
        self.chaine = chaine
        self.vues = vues
        self.publication = publication
        self.lien = lien


    def __str__(self):
        return "[titre="+self.titre+",chaine="+self.chaine+",vues="+str(self.vues)+",publication="+self.publication+",lien="+self.lien+"]"

    def __unicode__(self):
        return u"[titre="+self.titre+",chaine="+self.chaine+",vues="+str(self.vues)+",publication="+self.publication+"]"

    def getRatioUpperTitre(self):
        return fonction.ratio_upper(self.titre)
