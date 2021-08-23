import pygame

class Hurdle:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, (self.rect.x, self.rect.y-14))
        
pygame.init()
screen = pygame.display.set_mode((400, 400))

hurdle_1 = Hurdle(0, 200, 200, 2)
hurdle_2 = Hurdle(200, 198, 200, 2)

hurdle_img = pygame.image.load("hurdle.png")
hurdle_img = pygame.transform.scale(hurdle_img, (200,25))

while True:
    screen.fill((255,249,238))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    hurdle_1.paste_image(hurdle_img)
    hurdle_2.paste_image(hurdle_img)
   
    pygame.display.update()
    pygame.time.delay(10)
