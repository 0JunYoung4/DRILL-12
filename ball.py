from pathlib import Path

from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    SIZE = 21
    SPEED = 10

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image(str(Path(__file__).with_name('ball21x21.png')))
        self.x, self.y = x, y
        self.direction = direction

    def update(self):
        self.x += self.direction * self.SPEED
        if self.x < -self.SIZE / 2 or self.x > get_canvas_width() + self.SIZE / 2:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
