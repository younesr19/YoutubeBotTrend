#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import fonction
from video import Video
class YoutubeBot():
    def __init__(self):
        print('Initialisation des options et du navigateur...\n')
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path=r'/home/etudiant/projet_youtube/geckodriver',options=options)

    def AllerTendance(self):
        print('Accès à la page tendance de Youtube...\n')
        self.driver.get('https://www.youtube.com/feed/trending')

    def TraitementTendance(self):
        print('Traitement des vidéos en tendances...\n')
        grid_container = self.driver.find_element_by_xpath('//*[@id="grid-container"]')
        liste_video_titre = grid_container.find_elements_by_id('video-title')
        liste_video_chaine = fonction.retirer_vide_tableau(grid_container.find_elements_by_id('channel-name'))
        liste_video_metadata = grid_container.find_elements_by_id('metadata-line')

        liste_video = []

        for i in range(0,len(liste_video_titre)):

            titre = liste_video_titre[i].text
            chaine = liste_video_chaine[i].text

            vue = fonction.traitement_vues(fonction.separateur_texte(liste_video_metadata[i].text,'\n')[0])
            publication = fonction.traitement_publication(fonction.separateur_texte(liste_video_metadata[i].text,'\n')[1])

            liste_video.append(Video(titre,chaine,vue,publication))

        for video in liste_video:
            print(video.__str__())

youtubebot = YoutubeBot()
youtubebot.AllerTendance()
youtubebot.TraitementTendance()
