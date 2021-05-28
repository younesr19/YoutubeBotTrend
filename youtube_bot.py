#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import fonction
import threading
from video import Video
class YoutubeBot():
    def __init__(self):
        print('Initialisation des options et du navigateur...\n')
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver',options=options)

    def AllerTendance(self):
        print('Accès à la page tendance de Youtube...\n')
        self.driver.get('https://www.youtube.com/feed/trending')

    def AllerTendanceSpeciale(self,type_tendance):
        print('Accès à la page tendance de '+type_tendance+' de Youtube... \n')
        tendance = self.driver.find_elements_by_class_name('ytd-channel-list-sub-menu-avatar-renderer')
        tendance = fonction.recuperer_tendance_speciale(tendance,type_tendance)
        self.driver.get(tendance.get_attribute('href'))

    def TraitementTendance(self):
        print('Traitement des vidéos en tendances...\n')
        grid_container = self.driver.find_element_by_id('primary')

        grid_container = fonction.retirer_videoNonTrend(grid_container)

        liste_video_titre = []
        liste_video_chaine = []
        liste_video_duree = []
        liste_video_metadata = []

        for container in grid_container:
            liste_video_titre += container.find_elements_by_id('video-title')
            liste_video_chaine += fonction.retirer_vide_tableau(container.find_elements_by_id('channel-name'))
            liste_video_duree += container.find_elements_by_class_name('ytd-thumbnail-overlay-time-status-renderer')
            liste_video_metadata += container.find_elements_by_id('metadata-line')
        liste_video = []
        cmp = 1
        for i in range(0,len(liste_video_titre)):

            titre = liste_video_titre[i].text
            chaine = liste_video_chaine[i].text
            temps = fonction.traitement_temps(liste_video_duree[i+cmp].get_attribute('aria-label'))
            cmp+=1
            lien=fonction.separateur_texte(liste_video_titre[i].get_attribute('href'),'=')[1]

            vue = fonction.traitement_vues(fonction.separateur_texte(liste_video_metadata[i].text,'\n')[0])
            publication = fonction.traitement_publication(fonction.separateur_texte(liste_video_metadata[i].text,'\n')[1])

            liste_video.append(Video(i+1,titre,chaine,vue,temps,publication,lien))

        for i in range(0,len(liste_video)):
            print(liste_video[i].__str__())


youtubebot = YoutubeBot()
youtubebot.AllerTendance()
#youtubebot.AllerTendanceSpeciale("Musique")
youtubebot.TraitementTendance()
