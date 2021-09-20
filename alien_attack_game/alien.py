import pygame
from pygame.sprite import Sprite

class Alien(Sprite):  # Klasa przedstawiająca pojedynczego obcego we flocie

    def __init__(self, ai_game):  # inicjalizacja obcego i zdefiniowanie jego położenia
        super().__init__()
        self.sceen = ai_game.screen

        # Wczytywanie obrazu obcego i zdefiniowanie jego położenia
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Umiesczenie nowego obcego w pobliżu lewego górnego rogi ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # przechowywanie dokładnego poziomego położenia obcego
        self.x = float(self.rect.x)

