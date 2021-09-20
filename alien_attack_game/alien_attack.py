import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienAttack:  # Ogólna klasa przeznaczona do zarzadzania zasobami i sposobem działania gry
    def __init__(self):  # inicjalizacja gry i tworzenie jej zasobów
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Attack")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):  # rozpoczęcie pętli głównej gry
        while True:  # oczekiwanie na naciśnięcie klawisza bądź przycisk myszy
            self._check_events() # odświeżenie ekranu wtrakcie każdej iteracji pętli
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self): # reakcja na zdarzenia generowane przez mysz i klawiature
            for event in pygame.event.get():  # pętla zdarzeń
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self): # Utowrzenie nowego pocisku i dodanie go do grupy innych pocisków
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self): # Uaktualnia położenie pocisków i usuwa te niewodoczne na ekranie
        self.bullets.update() # uakualnia położenie pocisków na ekranie
        for bullet in self.bullets.copy():  # pętla usuwa pocisku znajdujące się poza ekranem
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self): # Utworzenie floty obcych
        alien = Alien(self) # Utowrzenie obcego
        self.aliens.add(alien)

    def _update_screen(self): # uaktualnienie obrazów na ekranie i przejście do nowego ekranu
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()  # Wyświetlenie ostatniego modyfikowanego ekranu


if __name__ == '__main__':  # Utworzenie egzemplarza gry i jej uruchomienie
    aa = AlienAttack()
    aa.run_game()

