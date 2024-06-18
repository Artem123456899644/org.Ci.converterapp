from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Задаем цвета для стилизации
primary_color =(0.2, 0.2, 0.2, 1)  # Голубой цвет для основного фона
secondary_color = (0.2, 0.2, 0.2, 1)  # Светло-голубой цвет для кнопки и текстового поля

mass = {
    "Б": "1", "Ф": "2", "Р": "3", "А": "4", "П": "5",
    "С": "6", "Ж": "7", "Н": "8", "Е": "9", "Х": "0",
    "1": "Б", "2": "Ф", "3": "Р", "4": "А", "5": "П",
    "6": "С", "7": "Ж", "8": "Н", "9": "Е", "0": "Х",
    " ": " ", "б": "1", "ф": "2", "р": "3", "а": "4",
    "п": "5", "с": "6", "ж": "7", "н": "8", "е": "9",
    "х": "0",
}

def convert_message(text):
    result = ""
    for char in text:
        result += mass.get(char, char)
    return result

class ConverterApp(App):
    def build(self):
        Window.clearcolor = primary_color
        self.title = 'Converter'
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text='Converter', font_size=34, color=(0, 0, 0, 1))  # Черный цвет для текста
        layout.add_widget(self.label)
        
        self.input_text = TextInput(hint_text='Enter text here', font_size=24, size_hint_y=None, height=40, background_color=secondary_color)
        layout.add_widget(self.input_text)
        
        self.convert_button = Button(text='Convert', font_size=24, size_hint_y=None, height=50, background_color=secondary_color)
        self.convert_button.bind(on_press=self.convert_text)
        layout.add_widget(self.convert_button)
        
        return layout

    def convert_text(self, instance):
        text = self.input_text.text
        converted_text = convert_message(text)
        self.input_text.text = converted_text

if __name__ == '__main__':
    ConverterApp().run()
