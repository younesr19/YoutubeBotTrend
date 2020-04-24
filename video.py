#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8


class Video:

    def __init__(self,titre,chaine,vues,publication):#Constructeur de vidéo

        self.titre = titre
        self.chaine = chaine
        self.vues = vues
        self.publication = publication


    def __str__(self):
        return "[titre="+self.titre+",chaine="+self.chaine+",vues="+str(self.vues)+",publication="+self.publication+"]"

    def __unicode__(self):
        return u"[titre="+self.titre+",chaine="+self.chaine+",vues="+str(self.vues)+",publication="+self.publication+"]"
