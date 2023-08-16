class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        # 设置屏幕
        self.screen_width = 720
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # self.bg_color = (135, 206, 250)

        # 飞船设置
        self.ship_speed = 0.3

        # 设置子弹
        self.bullet_speed = 0.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 5

