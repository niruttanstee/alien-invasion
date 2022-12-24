# Settings class.
# Instead of adding settings throughout the code, let's write a module called
# settings that contains a class called Settings to store all these values in
# one place.

# This approach allows us work with just one settings object any time we need
# to access an individual setting. This also makes it easier to modify the
# game's appeareance and behaviour as our project grows.

# To modify the game, we'll simply change some values in settings.py.
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3