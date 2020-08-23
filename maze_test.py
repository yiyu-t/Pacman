from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450, 100, 300, g)

    m.eat_dots(56, 150)
    # pacman is able to eat the dot on (75, 150) and (0, 150)
    for dot in m.dots.top_row:
        assert not (dot.x == 75 and dot.y == 150)
        assert not (dot.x == 0 and dot.y == 150)

    m.eat_dots(20, 300)
    # pacman is able to eat the dot on (20, 300)
    for dot in m.dots.bottom_row:
        assert not (dot.x == 0 and dot.y == 300)

    m.eat_dots(150, 370)
    # pacman is able to eat the dot on (150, 400)
    for dot in m.dots.left_col:
        assert not (dot.x == 150 and dot.y == 400)

    m.eat_dots(450, 270)
    # pacman is able to eat the dot on (450, 225) and (450, 300)
    for dot in m.dots.right_col:
        assert not (dot.x == 450 and dot.y == 225)
        assert not (dot.x == 450 and dot.y == 300)
