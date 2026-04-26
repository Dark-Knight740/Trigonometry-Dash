# Physics Engine Code

class PhysicsEngine:
    def __init__(self):
        self.gravity = -9.81  # gravity acceleration
        self.jump_power = 10  # initial jump power
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True

    def update(self, delta_time):
        # Apply gravity
        self.velocity_y += self.gravity * delta_time
        position_y += self.velocity_y * delta_time

        # Collision detection
        if position_y <= 0:
            position_y = 0
            self.is_jumping = False
            self.velocity_y = 0

    def sine_wave_movement(self, time, amplitude, frequency):
        return amplitude * sin(2 * pi * frequency * time)
