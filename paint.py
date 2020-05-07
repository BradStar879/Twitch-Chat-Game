from PIL import Image, ImageColor
import pygame


def write_pixel(xy, rgb):
    # im = Image.new('RGB', (100, 100)) # create the Image of size 1 pixel
    im = Image.open('simplePixel.png')
    im.putpixel(xy, rgb)  # or whatever color you wish
    im.save('simplePixel.png')  # or any image format


def main():
    image = pygame.image.load('simplePixel.png')
    running = True
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Paint Game")
    while running:
        # Clear screen to white before drawing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
        screen.fill(0)
        # screen.blit(image, (0, 0))
        pygame.display.flip()


# if __name__ == "__main__":
#     main()
