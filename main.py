from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class RaqebApp(App):
    def build(self):
        self.layout = BoxLayout(orientation= 'vertical' , padding=20, spacing=20)
        
        # عنوان التطبيق
        self.title_label = Label(
            text="نظام راقب - تخمين الكروت",
            font_size= '28sp' ,
            color=(0, 0.7, 1, 1)  # لون أزرق جذاب
        )
        
        # مكان عرض الرقم المولد
        self.result_label = Label(
            text="اضغط للبدء",
            font_size= '40sp' ,
            bold=True
        )
        
        # زر التوليد
        self.btn = Button(
            text="توليد كرت عشوائي 🚀",
            size_hint=(1, 0.3),
            background_color=(0, 0.5, 0.8, 1),
            font_size= '24sp' 
        )
        self.btn.bind(on_press=self.generate_card)
        
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def generate_card(self, instance):
        # توليد رقم عشوائي من 6 خانات
        card_number = "".join([str(random.randint(0, 9)) for _ in range(6)])
        self.result_label.text = card_number

if __name__ ==  '__main__' :
    RaqebApp().run()
