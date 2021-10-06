import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint


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
        self.stars = pygame.sprite.Group()

        self._create_fleet()
        # self._place_stars()

    def run_game(self):  # rozpoczęcie pętli głównej gry
        while True:  # oczekiwanie na naciśnięcie klawisza bądź przycisk myszy
            self._check_events()  # odświeżenie ekranu wtrakcie każdej iteracji pętli
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):  # reakcja na zdarzenia generowane przez mysz i klawiature
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

    def _fire_bullet(self):  # Utowrzenie nowego pocisku i dodanie go do grupy innych pocisków
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):  # Uaktualnia położenie pocisków i usuwa te niewodoczne na ekranie
        self.bullets.update()  # uakualnia położenie pocisków na ekranie
        for bullet in self.bullets.copy():  # pętla usuwa pocisku znajdujące się poza ekranem
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):  # Uaktualnienie położenia wszystkich obcych we flocie
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):  # Utworzenie floty obcych
        alien = Alien(self)  # Utowrzenie obcego
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #  ustalenie ilu obcych zmieści się na ekranie
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_hight - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # utowrzenie pełnej floty
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):  # Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):  # Przesunięcie całej floty w dół i zmiana kierunku, w którym się porusza
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction += -1

    # def _create_star(self, star_number, row_number):
    #     star = Star(self)
    #     star_width, star_height = star.rect.size
    #     star.x = star_width + 2 * star_width * star_number
    #     star.rect.x = star.x
    #     star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    #     self.stars.add(star)
    #
    # def _place_stars(self):
    #     star = Star(self)
    #     star_width, star_height = star.rect.size
    #     available_space_x = self.settings.screen_width - (2 * star_width)
    #     number_stars_x = available_space_x // (2 * star_width)
    #     ship_height = self.ship.rect.height
    #     available_space_y = (self.settings.screen_hight - (3 * star_height) - ship_height)
    #     number_rows = available_space_y // (2 * star_height)
    #
    #     for row_number in range(randint(0, 10)):
    #         for star_number in range(randint(0, 10)):
    #             self._create_star(star_number, row_number)

    def _update_screen(self): # uaktualnienie obrazów na ekranie i przejście do nowego ekranu
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # self.stars.draw(self.screen)

        pygame.display.flip()  # Wyświetlenie ostatniego modyfikowanego ekranu


if __name__ == '__main__':  # Utworzenie egzemplarza gry i jej uruchomienie
    aa = AlienAttack()
    aa.run_game()

