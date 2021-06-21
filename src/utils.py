#                 Pygame VFX                #
#             MIT - Kadir Aksoy             #
#   https://github.com/kadir014/pygame-vfx  #


from PIL import Image, ImageFilter
import pygame


# Optimized blurring algorithm by The New St. Paul aka MintFan
def blur(canvas, pos, size, radius=10, alpha=255, resolution=40):
    resolution = resolution #percentage of pixels to use for blur
    s = pygame.Surface(size)
    s.blit(canvas, (0, 0), (pos[0], pos[1], size[0], size[1]))
    s = pygame.transform.rotozoom(s, 0, (resolution / 100.0) * 1)
    size2 = s.get_size()
    rad = radius
    b = pygame.image.tostring(s, "RGBA", False)
    b = Image.frombytes("RGBA", size2, b)
    b = b.filter(ImageFilter.GaussianBlur(radius=int(rad)))
    b = pygame.image.frombuffer(b.tobytes(), b.size, b.mode).convert()
    b.set_alpha(alpha)
    b = pygame.transform.rotozoom(b, 0, (100.0 / resolution) * 1)
    canvas.blit(b, pos)
