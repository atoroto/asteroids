import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(*self.position, new_radius)
        new_velocity_1 = self.velocity.rotate(new_angle)
        new_asteroid_1.velocity = new_velocity_1 * 2.2

        new_asteroid_2 = Asteroid(*self.position, new_radius)
        new_velocity_2 = self.velocity.rotate(-new_angle)
        new_asteroid_2.velocity = new_velocity_2 * 1.2
