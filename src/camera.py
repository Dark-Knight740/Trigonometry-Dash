class Camera:
    def __init__(self, player):
        self.player = player
        self.offset_x = 0
        self.offset_y = 0

    def update(self):
        # Update the camera's position to follow the player
        self.offset_x = self.player.x - (screen_width / 2)
        self.offset_y = self.player.y - (screen_height / 2)

    def apply(self, entity):
        # Transform the entity's position based on the camera's offset
        entity.x -= self.offset_x
        entity.y -= self.offset_y

    def get_viewport(self):
        # Calculate the boundaries of the viewport
        return (self.offset_x, self.offset_y, screen_width, screen_height)