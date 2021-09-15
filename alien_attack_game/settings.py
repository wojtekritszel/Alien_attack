class Settings:  # Klasa przeznaczona do przechowywania wszystkich ustawień gry

    def __init__(self):  # Inicjalizacja ustawień gry
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5