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
    """Test the eat_dots() method"""
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)

    # testing if there is any dot being eaten after the method
    # I cannot test x and y because they are local variables
    dots_bottom_list_length = len(m.dots.bottom_row)
    # x and y within the boundaries
    test1_x = 75
    test1_y = 300
    m.eat_dots(test1_x, test1_y)
    assert len(m.dots.bottom_row) != dots_bottom_list_length

    dots_top_list_length = len(m.dots.top_row)
    # x and y bigger than width and height
    test2_x = 675
    test2_y = 500
    m.eat_dots(test2_x, test2_y)
    assert len(m.dots.top_row) != dots_top_list_length

    dots_top_list_length = len(m.dots.top_row)
    # x and y smaller than 0
    test3_x = -75
    test3_y = -300
    m.eat_dots(test3_x, test3_y)
    assert len(m.dots.top_row) != dots_top_list_length
