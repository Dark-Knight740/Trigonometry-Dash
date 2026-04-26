class Player:
    JUMPING = 'jumping'
    FALLING = 'falling'
    GROUNDED = 'grounded'
    SINE_MODE = 'sine_mode'

    def __init__(self):
        self.state = Player.GROUNDED
        self.height = 0
        self.active_mode = None

    def jump(self):
        if self.state == Player.GROUNDED:
            self.state = Player.JUMPING
            self.height += 10  # jump height
            print("Jumping!")

    def fall(self):
        if self.state == Player.JUMPING:
            self.state = Player.FALLING
            print("Falling!")
            self.height -= 10  # fall height
            if self.height <= 0:
                self.state = Player.GROUNDED
                self.height = 0
                print("Grounded!")

    def activate_sine_mode(self):
        self.active_mode = Player.SINE_MODE
        print("Sine Mode Activated!")

    def collision_handling(self, obstacle):
        if self.state == Player.FALLING and obstacle:
            self.state = Player.GROUNDED
            print("Collision detected! Grounded.")

        elif self.state == Player.SINE_MODE and obstacle:
            print("Sine mode collision with obstacle!")  # Handle collision in sine mode

    def update(self):
        # Simulate the player's actions over time
        if self.state == Player.JUMPING:
            self.fall()  # Automatically fall after jumping
        elif self.state == Player.FALLING:
            if self.height <= 0:
                self.fall()
        
# Example usage:
player = Player()
player.jump()
player.update()  # Simulate an update cycle
