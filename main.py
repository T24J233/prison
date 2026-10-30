# -*- coding: utf-8 -*-
"""
@author: Ozaki
"""

import pygame
import sys
from living import Living
from corridor import Corridor


def main():
    pygame.init()
    screen = pygame.display.set_mode((880,600))
    clock = pygame.time.Clock()
    
    lock_flag = [False, False, False, False, False, False, False, False, False, False, False, False]
    
    room_state = 0
    room_ctrl = [Living(screen, lock_flag),
                 Corridor(screen, lock_flag)]
    
    while True:

        """ マウスカーソル位置 """
        x, y = pygame.mouse.get_pos()
        room_ctrl[room_state].pos_event(x, y)
        
        """ クリックイベント，キーイベント """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                room_ctrl[room_state].click_event(x, y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    room_state = (room_state - 1) % 2
                elif event.key == pygame.K_RIGHT:
                    room_state = (room_state + 1) % 2
                elif event.key == pygame.K_a:
                    lock_flag[0] = not lock_flag[0]
                elif event.key == pygame.K_b:
                    lock_flag[1] = not lock_flag[1]
                elif event.key == pygame.K_c:
                    lock_flag[2] = not lock_flag[2]
                elif event.key == pygame.K_d:
                    lock_flag[3] = not lock_flag[3]
                elif event.key == pygame.K_e:
                    lock_flag[4] = not lock_flag[4]
                elif event.key == pygame.K_f:
                    lock_flag[5] = not lock_flag[5]
                elif event.key == pygame.K_g:
                    lock_flag[6] = not lock_flag[6]
                elif event.key == pygame.K_h:
                    lock_flag[7] = not lock_flag[7]
                elif event.key == pygame.K_i:
                    lock_flag[8] = not lock_flag[8]
                elif event.key == pygame.K_j:
                    lock_flag[9] = not lock_flag[9]
                elif event.key == pygame.K_k:
                    lock_flag[10] = not lock_flag[10]
                elif event.key == pygame.K_l:
                    lock_flag[11] = not lock_flag[11]                                    

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        """ 処理 """
        room_ctrl[room_state].do()
        
        """ 描画 """
        room_ctrl[room_state].draw()
        pygame.display.update()
        
        clock.tick(30)
        
        
if __name__ == '__main__':
    main()
