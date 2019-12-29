import pygame , sys
from pygame.locals import *

pygame.init()

pencereYuzey = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Pygame ilk anlamlı deneme')

SIYAH = (0,0,0)
BEYAZ = (255,255,255)
MAVI = (0,0,255)
KIRMIZI = (255,0,0)

yaziKarakteri = pygame.font.SysFont(None,48)

yazi = yaziKarakteri.render('Merhaba Dünya', True, BEYAZ,KIRMIZI)
yaziRect = yazi.get_rect()
yaziRect.centerx = pencereYuzey.get_rect().centerx
yaziRect.centery = pencereYuzey.get_rect().centery


pencereYuzey.fill(BEYAZ)

pygame.draw.line(pencereYuzey, SIYAH, (90, 90), (150,90),5)

pygame.draw.circle(pencereYuzey, MAVI, (400,70),30,0)

pencereYuzey.blit(yazi, yaziRect)

pygame.display.update()

while True:
  for olay in pygame.event.get():
    if olay.type == QUIT:
      pygame.quit
      sys.exit()
