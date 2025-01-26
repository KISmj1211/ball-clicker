import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800,600
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,0,0)

ball_radius = 30
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_color = BLUE

ball_speed_x = 3
ball_speed_y = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Clicker")
clock= pygame.time.Clock()

font = pygame.font.Font(None,36)


score = 0
time_limit=30
start_ticks = pygame.time.get_ticks()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((ball_x -mouse_x)**2+(ball_y-mouse_y)**2)**0.5
            if distance < ball_radius:
                score +=1
                ball_x = random.randint(ball_radius, WIDTH -ball_radius)
                ball_y = random.randint(ball_radius, HEIGHT -ball_radius)
                ball_speed_x+=random.choice([-1,1])*0.5
                ball_speed_y+=random.choice([-1,1])*0.5
                print("Score:",score)
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius <0 or ball_x+ball_radius>WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_x - ball_radius<0 or ball_y +ball_radius>HEIGHT:
        ball_speed_y = -ball_speed_y

    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    if elapsed_time>time_limit:
        running = False
    
    screen.fill(WHITE)
    pygame.draw.circle(screen,ball_color,(ball_x,ball_y), ball_radius)

    score_text = font.render("Score:"+str(score), True, BLACK)
    screen.blit(score_text,(10,10))

    time_text = font.render(f"Time: {max(0,int(time_limit-elapsed_time))}s",True,BLACK)
    screen.blit(time_text,(WIDTH-150,10))
    pygame.display.flip()
    clock.tick(60)

game_over=True
while game_over:
    screen.fill(WHITE)
    font = pygame.font.Font(None,72)
    game_over_text = font.render("Game Over", True,RED)
    final_score_text = font.render(f"Final score: {score}", True, BLACK)
    screen.blit(game_over_text,(WIDTH//2-150,HEIGHT//2-50))
    screen.blit(final_score_text,(WIDTH//2-150,HEIGHT//2+50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=False
            pygame.quit()
            sys.exit()
