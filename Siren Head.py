from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

app = Ursina()

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000000))

class Enemy(Entity):
    def __init__(self, player):
        super().__init__(
            model = "Siren Head.fbx",
            texture = 'siren_head_body_d',
            position = (0,0,6000)
        )
        self.add_script(SmoothFollow(target=player, offset=[0, 1, 0], speed=0.2))

class Ground(Entity):
    def __init__(self):
        super().__init__(
            model = 'plane',
            collider = 'box',
            scale = (100000,0,100000),
            texture = 'grass'
        )

player = FirstPersonController(
    position = (0,15,-200),
    speed = 500,
    jump_height = 500
    )

Sky()
window.fullscreen = True

Enemy(player)
Ground()

app.run()
