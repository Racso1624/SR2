from gl import Render

r = Render()

r.glCreateWindow(1000, 1000)

r.glClearColor(0.2, 0.4, 0.6)

r.glClear()

r.glLine(100, 300, 300, 100)

r.glLine(300, 500, 100, 100)

r.glLine(300, 300, 100, 350)

r.glLine(300, 600, 350, 500)

r.glLine(500, 500, 100, 300)

r.glLine(500, 700, 300, 300)

r.glLine(700, 700, 300, 100)

r.glLine(700, 900, 100, 100)

r.glLine(900, 900, 100, 350)

r.glLine(600, 900, 500, 350)

r.glLine(300, 100, 350, 525)

r.glLine(100, 100, 525, 300)

r.glLine(600, 350, 500, 650)

r.glLine(100, 350, 525, 650)

r.glLine(900, 600, 350, 550)

r.glLine(350, 600, 650, 550)

r.glFinish("casa.bmp")