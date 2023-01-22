import main
import pandas as pd

def test_funcUI_Selector(choice_id):
    assert choice_id > 0 | choice_id < 4

def test_getData(num):
    test_funcUI_Selector(num)
    for i in range(1,num):
        assert type(main.getData(i)) == type(pd.DataFrame())


