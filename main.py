from gl import Render

r = Render()

r.glCreateWindow(1000, 1000)

r.glClearColor(0.2, 0.4, 0.6)

r.glClear()

r.glLine(100, 300, 300, 100)

r.glLine(300, 500, 100, 100)

r.glFinish("casa.bmp")