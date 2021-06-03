from model.Geometria import Geometria
from view.View import View

if __name__ == '__main__':
    g = Geometria(2.00, 3.00, 4.00)
    v = View()
    v.select(g)
