import pygame
import pygame.camera
def capture():
    pygame.camera.init()
    cam=pygame.camera.Camera("/dev/video0",(1366,768))
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,"image.jpg")
    return("image.jpg")

