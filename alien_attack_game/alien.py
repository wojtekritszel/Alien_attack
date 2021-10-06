import pygame
from pygame.sprite import Sprite


class Alien(Sprite):  # Klasa przedstawiająca pojedynczego obcego we flocie

    def __init__(self, ai_game):  # inicjalizacja obcego i zdefiniowanie jego położenia
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Wczytywanie obrazu obcego i zdefiniowanie jego położenia
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Umiesczenie nowego obcego w pobliżu lewego górnego rogi ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # przechowywanie dokładnego poziomego położenia obcego
        self.x = float(self.rect.x)

    def check_edges(self):  # Zwraca wartość True jeśli obcy znajdzie się przy krawędzi
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)  # Przesunięcie obcego w prawo
        self.rect.x = self.x
