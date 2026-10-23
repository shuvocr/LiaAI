from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 16
    spacing: 10

    Label:
        text: "[b]Lia AI[/b] — তোমার AI বন্ধু"
        markup: True
        font_size: "25sp"
        size_hint_y: None
        height: "55dp"

    Label:
        id: reply
        text: "হ্যালো! আমি Lia AI। আমাকে কিছু জিজ্ঞেস করো।"
        halign: "left"
        valign: "top"
        text_size: self.width, None

    TextInput:
        id: message
        hint_text: "এখানে বাংলা বা ইংরেজিতে লেখো..."
        multiline: True
        size_hint_y: None
        height: "100dp"

    Button:
        text: "পাঠাও"
        size_hint_y: None
        height: "50dp"
        on_release: app.send_message()
"""

class LiaAI(App):
    def build(self):
        self.title = "Lia AI"
        Window.clearcolor = (0.08, 0.09, 0.13, 1)
        return Builder.load_string(KV)

    def send_message(self):
        text = self.root.ids.message.text.strip()
        if not text:
            self.root.ids.reply.text = "আগে একটি মেসেজ লেখো।"
            return

        self.root.ids.reply.text = (
            "তুমি লিখেছ: " + text +
            "\\n\\nএটি Lia AI-এর প্রাথমিক সংস্করণ। "
            "পরের ধাপে আসল AI সংযোগ করব।"
        )
        self.root.ids.message.text = ""

if __name__ == "__main__":
    LiaAI().run()
