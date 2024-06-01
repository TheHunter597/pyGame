import pygame
from random import randint, uniform

# --------
running = True
game_over = False
start_time = 0
multiplier = 1
last_game_timer = 0
new_game_started = True
score = 50


# --------
def display_game_over_score():
    game_over_score = pygame.transform.scale_by(
        game_font.render(f"You scored: {score}", True, "black"), 0.6
    )
    game_over_score_rect = game_over_score.get_rect(
        midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.30)
    )
    screen.blit(game_over_score, game_over_score_rect)


def display_score():
    global start_time
    global score
    global multiplier
    global last_game_timer
    global end_time
    end_time = pygame.time.get_ticks()
    current = end_time - start_time
    multiplier = round(1 + ((end_time - last_game_timer) / MULTIPLIER_FACTOR), 2)
    if current >= 1000 / (1 * multiplier):
        score += 1
        start_time = end_time
    score_header = game_font.render(f"Score: {round(score)}", False, "black")
    score_header_rect = score_header.get_rect(
        midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.20)
    )
    screen.blit(score_header, score_header_rect)


def create_obstacles(current_obstacles):
    global current_obstacles_rects
    if current_obstacles:
        for obstacle in current_obstacles:
            if obstacle.left < -50:
                current_obstacles_rects = [x for x in current_obstacles if x.left > -50]
            if obstacle.bottom == SCREEN_HEIGHT * 0.48:
                screen.blit(current_fly_image, obstacle)
                obstacle.x -= FLY_SPEED * multiplier

            else:
                screen.blit(current_snail_image, obstacle)
                obstacle.x -= SNAIL_SPEED * multiplier


def detect_collissions(current_obstacles):
    global game_over
    for obstacle in current_obstacles:
        if obstacle.colliderect(player_surface):
            game_over = True


def create_player_animations():
    global current_player_image
    global current_player_index
    if player_surface.bottom < SCREEN_HEIGHT * 0.7:
        current_player_image = player_jump_image
    else:
        if current_player_index == 0:
            current_player_image = player_moving_1
            current_player_index = 1
        else:
            current_player_image = player_moving_2
            current_player_index = 0


def create_snail_animations():
    global current_snail_image
    global current_snail_index
    if current_snail_index == 0:
        current_snail_image = snail_moving_1
        current_snail_index = 1
    else:
        current_snail_image = snail_moving_2
        current_snail_index = 0


def create_fly_animations():
    global current_fly_image
    global current_fly_index
    if current_fly_index == 0:
        current_fly_image = fly_moving_1
        current_fly_index = 1
    else:
        current_fly_image = fly_moving_2
        current_fly_index = 0


# --------
GROUND_IMAGE = "graphics/ground.png"
SKY_IMAGE = "graphics/Sky.png"
SNAIL_IMAGE_1 = "graphics/snail/snail1.png"
SNAIL_IMAGE_2 = "graphics/snail/snail2.png"
FLY_IMAGE_1 = "graphics/Fly/Fly1.png"
FLY_IMAGE_2 = "graphics/Fly/Fly2.png"
PLAYER_MOVING_1_IMAGE = "graphics/Player/player_walk_1.png"
PLAYER_MOVING_2_IMAGE = "graphics/Player/player_walk_2.png"
PLAYER_JUMP_IMAGE = "graphics/Player/jump.png"
PLAYER_STAND = "graphics/Player/player_stand.png"
FONT = "font/Pixeltype.ttf"
# --------
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
# --------
OBJECT_WIDTH = round(SCREEN_WIDTH * 0.05)
OBJECT_HEIGHT = round(SCREEN_WIDTH * 0.05)
SNAIL_START_POS = (SCREEN_WIDTH + OBJECT_WIDTH, SCREEN_HEIGHT * 0.7)
FLY_START_POS = (SCREEN_WIDTH + OBJECT_WIDTH, SCREEN_HEIGHT * 0.5)
# --------
PLAYER_WIDTH = round(SCREEN_WIDTH * 0.056)
PLAYER_HEIGHT = round(SCREEN_WIDTH * 0.056)
PLAYER_START_POS = (PLAYER_WIDTH, SCREEN_HEIGHT * 0.7)
# --------
FRAMES_RATE = 60
JUMP_GRAVITY = -17
ACCELERATION = 0.7
SNAIL_SPEED = 2.8
FLY_SPEED = 3.45
MULTIPLIER_FACTOR = 20000
FONT_SIZE = round(SCREEN_WIDTH * 0.1)
# --------
pygame.init()
# --------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# --------
ground = pygame.image.load(GROUND_IMAGE).convert_alpha()
ground = pygame.transform.scale(ground, (SCREEN_WIDTH, SCREEN_HEIGHT * 0.3))
ground_rect = ground.get_rect(topleft=(0, SCREEN_HEIGHT * 0.7))
# --------
sky = pygame.image.load(SKY_IMAGE).convert_alpha()
sky = pygame.transform.scale(sky, (SCREEN_WIDTH, SCREEN_HEIGHT * 0.7))
sky_rect = sky.get_rect(topleft=(0, 0))
# --------
snail_moving_1 = pygame.transform.scale(
    pygame.image.load(SNAIL_IMAGE_1).convert_alpha(), (OBJECT_WIDTH, OBJECT_HEIGHT)
)
snail_moving_2 = pygame.transform.scale(
    pygame.image.load(SNAIL_IMAGE_2).convert_alpha(), (OBJECT_WIDTH, OBJECT_HEIGHT)
)
snail_images = [snail_moving_1, snail_moving_2]
current_snail_index = 0
current_snail_image = snail_images[current_snail_index]
# --------
fly_moving_1 = pygame.transform.scale(
    pygame.image.load(FLY_IMAGE_1).convert_alpha(), (OBJECT_WIDTH, OBJECT_HEIGHT)
)
fly_moving_2 = pygame.transform.scale(
    pygame.image.load(FLY_IMAGE_2).convert_alpha(), (OBJECT_WIDTH, OBJECT_HEIGHT)
)
fly_images = [fly_moving_1, fly_moving_2]
current_fly_index = 0
current_fly_image = fly_images[current_fly_index]

# --------
player_moving_1 = pygame.transform.scale(
    pygame.image.load(PLAYER_MOVING_1_IMAGE).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT),
)
player_moving_2 = pygame.transform.scale(
    pygame.image.load(PLAYER_MOVING_2_IMAGE).convert_alpha(),
    (PLAYER_WIDTH, PLAYER_HEIGHT),
)
player_jump_image = pygame.transform.scale(
    pygame.image.load(PLAYER_JUMP_IMAGE).convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)
)
player_images = [player_moving_1, player_moving_2]
current_player_index = 0
current_player_image = player_images[current_player_index]
player_surface = current_player_image.get_rect(midbottom=PLAYER_START_POS)
player_gravity = 0
# --------
player_standing = pygame.image.load(PLAYER_STAND)
player_standing = pygame.transform.rotozoom(player_standing, 0, 2)
player_standing_rect = player_standing.get_rect(
    midbottom=(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.65)
)
# --------
clock = pygame.time.Clock()
# --------
game_font = pygame.font.Font(FONT, FONT_SIZE)
game_over_text = game_font.render("Game Over", False, "black")
game_over_rect = game_over_text.get_rect(
    midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.20)
)
# --------
try_again_text = pygame.transform.scale_by(
    game_font.render(
        'To play again press "space" or click with the mouse', True, "black"
    ),
    0.5,
)
try_again_text_rect = try_again_text.get_rect(
    midbottom=(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.75)
)
instructions_text = pygame.transform.scale_by(
    game_font.render(
        "Up arrow to jump up and down arrow to accelerate going down", True, "black"
    ),
    0.5,
)
instructions_text_Rect = instructions_text.get_rect(
    midbottom=(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.85)
)

# --------
mouse = pygame.mouse
# --------
spawn_enemy_event = pygame.event.custom_type()
spawn_ememies_timer = pygame.time.set_timer(spawn_enemy_event, 1500)

player_movement_event = pygame.event.custom_type()
player_movement_timer = pygame.time.set_timer(player_movement_event, 150)

snail_movement_event = pygame.event.custom_type()
snail_movement_timer = pygame.time.set_timer(snail_movement_event, 400)

fly_movement_event = pygame.event.custom_type()
fly_movement_timer = pygame.time.set_timer(fly_movement_event, 200)
# --------
current_obstacles_rects = []
# --------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    game_over = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if player_surface.bottom >= SCREEN_HEIGHT * 0.7:
                    player_gravity = JUMP_GRAVITY
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if player_surface.bottom < SCREEN_HEIGHT * 0.7:
                    player_gravity = -JUMP_GRAVITY / 1.5
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                game_over = False
            if player_surface.collidepoint(event.pos):
                if player_surface.bottom >= SCREEN_HEIGHT * 0.7:
                    player_gravity = JUMP_GRAVITY
        if game_over == False:
            if event.type == spawn_enemy_event:
                ran_enemy = round(randint(0, 100), 2)
                if score > 60:
                    if ran_enemy in range(10, 20) and score > 250:
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=SNAIL_START_POS)
                        )
                        pos_list = list(SNAIL_START_POS)
                        pos_list[0] += 30
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=tuple(pos_list))
                        )
                        current_obstacles_rects.append(
                            current_fly_image.get_rect(midbottom=FLY_START_POS)
                        )

                    if ran_enemy in range(20, 30) and score > 200:
                        current_obstacles_rects.append(
                            current_fly_image.get_rect(midbottom=FLY_START_POS)
                        )
                        pos_list = list(FLY_START_POS)
                        pos_list[0] += 30
                        current_obstacles_rects.append(
                            current_fly_image.get_rect(midbottom=tuple(pos_list))
                        )
                    if ran_enemy in range(30, 40) and score > 160:
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=SNAIL_START_POS)
                        )
                        pos_list = list(SNAIL_START_POS)
                        pos_list[0] += 30
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=tuple(pos_list))
                        )
                        pos_list[0] += 30
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=tuple(pos_list))
                        )
                    if ran_enemy in range(40, 50) and score > 120:
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=SNAIL_START_POS)
                        )
                        pos_list = list(SNAIL_START_POS)
                        pos_list[0] += 30
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=tuple(pos_list))
                        )
                    if ran_enemy in range(50, 60):
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=SNAIL_START_POS)
                        )
                        current_obstacles_rects.append(
                            current_fly_image.get_rect(midbottom=FLY_START_POS)
                        )
                    elif ran_enemy <= 75:
                        current_obstacles_rects.append(
                            current_snail_image.get_rect(midbottom=SNAIL_START_POS)
                        )
                    else:
                        current_obstacles_rects.append(
                            current_fly_image.get_rect(midbottom=FLY_START_POS)
                        )
                else:
                    current_obstacles_rects.append(
                        current_snail_image.get_rect(midbottom=SNAIL_START_POS)
                    )
                pygame.time.set_timer(spawn_enemy_event, 0)
                base_time = 1400 - round(100 * multiplier)
                max_time = 1850 - round(100 * multiplier)
                if base_time < 150:
                    base_time = 150
                if max_time < 250:
                    max_time = 250
                spawn_ememies_timer = pygame.time.set_timer(
                    spawn_enemy_event, randint(base_time, max_time)
                )
            if event.type == player_movement_event:
                create_player_animations()
            if event.type == snail_movement_event:
                create_snail_animations()
            if event.type == fly_movement_event:
                create_fly_animations()
    # --------
    screen.blit(ground, ground_rect)
    screen.blit(sky, sky_rect)
    screen.blit(current_player_image, player_surface)
    if game_over:
        new_game_started = False
        screen.fill(color="#33ff99")
        screen.blit(game_over_text, game_over_rect)
        screen.blit(player_standing, player_standing_rect)
        screen.blit(try_again_text, try_again_text_rect)
        screen.blit(instructions_text, instructions_text_Rect)
        display_game_over_score()
        current_obstacles_rects = []
    else:
        display_score()
        detect_collissions(current_obstacles_rects)
        create_obstacles(current_obstacles_rects)

        if new_game_started == False:
            last_game_timer = end_time
            score = 0
            new_game_started = True
        player_gravity += ACCELERATION
        player_surface.bottom += player_gravity
        if player_surface.bottom > SCREEN_HEIGHT * 0.7:
            player_surface.bottom = SCREEN_HEIGHT * 0.7
    clock.tick(FRAMES_RATE)
    # --------
    pygame.display.update()
    # --------

pygame.quit()
