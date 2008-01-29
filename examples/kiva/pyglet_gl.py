

from numpy import array

import pyglet
from pyglet.window import key, Window
try:
    import OpenGL
except ImportError:
    raise Exception('OpenGL pacakge needs to be isntalled to run this example')

from enthought.kiva.backend_gl import GraphicsContext
from enthought.kiva.constants import FILL, STROKE, FILL_STROKE

class TestWindow(Window):
    def __init__(self, *args, **kw):
        Window.__init__(self, *args, **kw)
        self.init_window()

    def init_window(self):
        self.gc = GraphicsContext(size=(self.width, self.height))
        self.gc.init_gl_viewport()

    def on_key_press(self, symbol, modifiers):
        if symbol in (key.ESCAPE, key.Q):
            self.has_exit = True
    
    def draw(self):
        gc = self.gc
        gc.save_state()
        gc.clear(0, 1, 0, 1)
        gc.set_stroke_color((1,1,1,1))
        gc.set_line_width(2)
        pts = array([[50, 50], [50,100], [100,100], [100,50]])
        gc.begin_path()
        gc.lines(pts)
        gc.close_path()
        gc.draw_path(STROKE)
        gc.flush()
        gc.restore_state()


def main():
    win = TestWindow(width = 640, height=480)
    exit = False
    while not exit:
        win.switch_to()
        win.dispatch_events()
        win.clear()
        win.draw()
        win.flip()
        exit = win.has_exit


if __name__ == "__main__":
    main()

