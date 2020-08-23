from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    ds = Dots(600, 600, 150, 450, 150, 450)

    ds.eat(56, 150)
    # pacman is able to eat the dot on (75, 150) and (0, 150)
    print(len(ds.top_row))
    for dot in ds.top_row:
        assert not (dot.x == 75 and dot.y == 150)
        assert not (dot.x == 0 and dot.y == 150)

    ds.eat(450, 500)
    # pacman is able to eat the dot on (450, 525) and (450, 450)
    for dot in ds.right_col:
        assert not (dot.x == 450 and dot.y == 525)
        assert not (dot.x == 450 and dot.y == 450)

    ds.eat(150, 570)
    # pacman is able to eat the dot on (150, 600)
    for dot in ds.left_col:
        assert not (dot.x == 150 and dot.y == 600)

    ds.eat(20, 450)
    # pacman is able to eat the dot on (0, 450)
    for dot in ds.bottom_row:
        assert not (dot.x == 0 and dot.y == 450)


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
