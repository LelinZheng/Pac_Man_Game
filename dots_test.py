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
    """Test for the eat method on 4 rows of dots"""
    ds = Dots(600, 600, 150, 450, 150, 450)
    length_of_BH = len(ds.bottom_row)
    test1_x = 74
    test1_y = 448
    ds.eat(test1_x, test1_y)
    # test if one dot is removed
    assert len(ds.bottom_row) == length_of_BH-1

    length_of_TH = len(ds.top_row)
    test2_x = 526
    test2_y = 150
    ds.eat(test2_x, test2_y)
    assert len(ds.top_row) == length_of_TH-1

    length_of_LV = len(ds.left_col)
    test3_x = 150
    test3_y = 223
    ds.eat(test3_x, test3_y)
    assert len(ds.left_col) == length_of_LV-1

    length_of_RV = len(ds.right_col)
    test4_x = 450
    test4_y = 598
    ds.eat(test4_x, test4_y)
    assert len(ds.right_col) == length_of_RV-1


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
