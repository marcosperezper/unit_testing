import unittest
from model.Geometria import Geometria as g


class TestGeometria(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass() -> OK")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() -> OK")

    def setUp(self):
        print("setUp() -> OK")

    def test_AreaCuadrado(self):
        r = g.areaCuadrado(self, 4)
        self.assertEqual(r, 16)
        print("test_AreaCuadrado -> Passed")

    def test_AreaCirculo(self):
        r = g.areaCirculo(self, 5)
        self.assertEqual(round(r, 2), 78.54)
        print("test_AreaCirculo -> Passed")

    def test_AreaTriangulo(self):
        r = g.areaTiangulo(self, 4, 8)
        self.assertEqual(r, 16)
        print("test_AreaTriangulo -> Passed")

    def test_AreaRectangulo(self):
        r = g.areaRectangulo(self, 10, 3)
        self.assertEqual(r, 30)
        print("test_AreaRectangulo -> Passed")

    def test_AreaPentagono(self):
        r = g.areaPentagono(self, 12, 15)
        self.assertEqual(r, 90)
        print("test_AreaPentagono -> Passed")

    def test_AreaRombo(self):
        r = g.areaRombo(self, 12, 21)
        self.assertEqual(r, 126)
        print("test_AreaRombo -> Passed")

    def test_AreaRomboide(self):
        r = g.areaRomboide(self, 25, 7)
        self.assertEqual(r, 175)
        print("test_AreaRomboide -> Passed")

    def test_AreaTrapecio(self):
        r = g.areaTrapecio(self, 10, 4, 21)
        print(r)
        self.assertEqual(r, 147)
        print("test_AreaTrapecio -> Passed")

    def test_SetFiguraName(self):
        figure = g(5, 2, 3)
        figure_name = ["Cuadrado", "Circulo", "Tiangulo", "Rectangulo", "Pentagono", "Rombo", "Romboide", "Trapecio"]
        for i, name in enumerate(figure_name, start=1):
            figure.set_figuraName(i)
            self.assertEqual(figure.figuraName, name)
        print("test_SetFiguraName -> Passed")

    def test_Switch(self):
        figure = g(5, 2, 3)
        areas = [25, 78.54, 5, 10, 5, 5, 10, 10.5]
        for i, area in enumerate(areas, start=1):
            a = figure.switch(i)
            self.assertEqual(round(a, 2), area)
        print("test_Switch -> Passed")

    def tearDown(self):
        print("tearDown() -> OK")


if __name__ == "__main__":
    unittest.main()
