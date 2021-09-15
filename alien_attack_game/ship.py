import pygame

class Ship:  # Klasa przeznaczona do zarządzania statkiem kosmicznym

    def __init__(self, ai_game):  # inicjalizacja statku kosmicznego i jego położenie początkowe
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # wczytywanie statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        # położenie statku jest przechowywane w postaci liczby zmienno przeczcinkowej
        self.x = float(self.rect.x)

        # opcja wskazująca na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self): # uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):  # Wyświetlanie statku kosmicznego w jego aktualnym położeniu
        self.screen.blit(self.image, self.rect)
