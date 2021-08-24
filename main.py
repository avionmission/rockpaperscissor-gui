from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
import random


Window.size = (357, 667)

KV = '''
Screen:
    BoxLayout:
        MDLabel:
            text: 'SCORE'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            underline: 'true'
            bold: 'true'
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.9}
    BoxLayout:
        orientation : 'horizontal'
        MDLabel:
            id : your_points
            text: 'You: 0'
            font_name: "assets/JetBrainsMono.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.35, 'center_y' : 0.85}
        MDLabel:
            id : ai_points
            text: 'AI: 0'
            font_name: "assets/JetBrainsMono.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.65, 'center_y' : 0.85}
    BoxLayout:
        orientation : 'vertical'
        spacing : 10
        padding : 20
        MDRectangleFlatButton:
            text: 'R'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.3}
            on_release : app.play('r')
        MDRectangleFlatButton:
            text: 'P'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.2}
            on_release : app.play('p')
        MDRectangleFlatButton:
            text: 'S'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.1}
            on_release : app.play('s')
        MDFlatButton:
            text : 'Reset Score'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.84}
            font_name: "assets/JetBrainsMono-Medium.ttf"
            on_release : app.reset_score()
        MDFlatButton:
            id : ai_play
            text : 'Let AI play 1000 Times against itself'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.84}
            font_name: "assets/JetBrainsMono-Medium.ttf"
            on_release : 
                app.auto_play()
    BoxLayout:
        orientation : 'horizontal'
        Image:
            id : user_move
            allow_stretch : True
            keep_ratio : True
            source: "assets/rL.png"
        Image:
            id : ai_move
            allow_stretch : True
            keep_ratio : True
            source: "assets/rR.png"
        
            
        
'''


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)
        self.user_score = 0
        self.ai_score = 0

    def build(self):
        self.icon = 'assets/icon.png'
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        screen.add_widget(self.kvs)
        return screen

    def update_score(self, u, ai):
        if u == ai:
            self.ai_score += 0
        if u.isspace() or u not in ['r', 'p', 's']:
            quit()
        elif u == 'p' and ai == 'p':
            self.user_score += 0
        elif u == 'r' and ai == 'r':
            self.user_score += 0
        elif u == 's' and ai == 's':
            self.user_score += 0
        elif u == 'p' and ai == 'r':
            self.user_score += 1
        elif u == 'r' and ai == 's':
            self.user_score += 1
        elif u == 'p' and ai == 'r':
            self.user_score += 1
        elif u == 's' and ai == 'p':
            self.user_score += 1
        else:
            self.ai_score += 1
        self.kvs.ids.your_points.text = "You: " + str(self.user_score)
        self.kvs.ids.ai_points.text = "AI: " + str(self.ai_score)

    def play(self, char):
        x = char
        user_move_filename = "assets/" + char + "L.png"
        self.kvs.ids.user_move.source = user_move_filename

        y = random.choice(['r', 'p', 's'])
        ai_move_filename = "assets/" + y + "R.png"
        self.kvs.ids.ai_move.source = ai_move_filename
        self.update_score(x, y)

    def reset_score(self):
        self.user_score = 0
        self.ai_score = 0
        self.kvs.ids.your_points.text = "You: " + str(self.user_score)
        self.kvs.ids.ai_points.text = "AI: " + str(self.ai_score)

    def auto_play(self):
        for i in range(1000):
            x = random.choice(['r', 'p', 's'])
            user_move_filename = "assets/" + x + "L.png"
            self.kvs.ids.user_move.source = user_move_filename

            y = random.choice(['r', 'p', 's'])
            ai_move_filename = "assets/" + y + "R.png"
            self.kvs.ids.ai_move.source = ai_move_filename
            self.update_score(x, y)

ma = MainApp()
if __name__ == '__main__':
    ma.run()
