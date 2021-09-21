XDIM = 800; YDIM = 600

class Env:
    def __init__(self):
        self.x_range = (0, XDIM)
        self.y_range = (0, YDIM)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 5, YDIM],
            [0, YDIM, XDIM, 5],
            [5, 0, XDIM, 5],
            [XDIM, 5, 5, YDIM]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        obs_rectangle = [[500, 250, 300, 20],
                        [0, 150, 300, 20],
                        [180, 380, 300, 20],
                        [650, 50, 20, 100],
                        [650, 350, 20, 200],
                        [300, 150, 20, 120],
                        [180, 500, 120, 20],
                        [400, 500, 20, 100]]
        return obs_rectangle

    @staticmethod
    def obs_circle():
        obs_cir = [ [120, 240, 40],
                    [460, 160, 40],
                    [470, 520, 40]]

        return obs_cir
