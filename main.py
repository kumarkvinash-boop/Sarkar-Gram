from kivy.app import App
from kivy.uix.button import Button

class SarkarApp(App):
    def build(self):
        return Button(text='Sarkar Empire Live!', background_color=(0, 0.5, 1, 1))

if __name__ == "__main__":
    SarkarApp().run()
