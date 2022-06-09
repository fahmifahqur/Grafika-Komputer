import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

def draw_diamond():
    glBegin(GL_TRIANGLES)

    glColor(0,0,1)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(0.0,0.5,0.0)

    glVertex3f(-0.5,-0.5,0.5)
    glVertex3f(0.5,-0.5,0.5)
    glVertex3f(0.0,0.5,0.0)

    glColor(1,0,0)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5,0.5)
    glVertex3f(0.0,0.5,0.0)

    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,0.5)
    glVertex3f(0.0,0.5,0.0)
   

    glEnd()

#instalasi
pygame.init()
#resolusi display layar
display=(600,600)
#mode layar double buffering
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Gambar Limas 3D Segi Empat")

gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
#memindahkan objek sesuai dengan matrix translate
glTranslate(0,0,0-5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            glTranslatef(0.5,0,0)
        if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)

        if event.key == pygame.K_UP:
                glTranslatef(0,1,0)
        if event.key == pygame.K_DOWN:
                glTranslatef(0,-1,0)

    glRotate(1,1,1,1)
    #menghapus semua kanvas/display
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_diamond()
    pygame.display.flip()
    #menunggu 20ms sebelum looping lagi
    pygame.time.wait(20)
