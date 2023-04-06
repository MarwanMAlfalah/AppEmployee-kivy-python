from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import mysql.connector as sql
#Prepared by Developer: Marwan M. Al-Falah
Window.clearcolor=(100/255.0,0,2,1)
Window.size=(400, 600)

class Emp(App):
    def build(self):
        self.title='Employee'
        layout = GridLayout(cols=1)
        self.imo = Image(source='E:\\WorkShop\\PY\\AppEmployee\\emp.png', size_hint=(0.1, 0.5), pos_hint={'x':0.0, 'y':1})
        self.L1 = Label(text='Employee', font_size=22, color=(.3,.6,2,1), size_hint=(0.1, 0.3))
        self.L2 = Label(text='Add a new employee', color=(.0,.9,2,1), size_hint=(0.1, 0.3))
        self.username = TextInput(hint_text='Username', size_hint=(0.1, 0.3))
        self.work = TextInput(hint_text='Job', size_hint=(0.1, 0.3))
        self.phone = TextInput(hint_text='Phone', size_hint=(0.1, 0.3))
        self.country = TextInput(hint_text='Contry', size_hint=(0.1, 0.3))
        self.gender = TextInput(hint_text="Gender: Enter 'M' to Male or 'F' to Female", size_hint=(0.1, 0.3))
        submit = Button(text='Add Employee', size_hint=(0.1, 0.5), color=(.0,.9,2,1), on_press=self.sub)
        layout.add_widget(self.imo)
        layout.add_widget(self.L1)
        layout.add_widget(self.L2)
        layout.add_widget(self.username)
        layout.add_widget(self.work)
        layout.add_widget(self.phone)
        layout.add_widget(self.country)
        layout.add_widget(self.gender)
        layout.add_widget(submit)
        return layout

    def sub(self, ob):
        un = self.username.text
        wk = self.work.text
        ph = self.phone.text
        co = self.country.text
        ge = self.gender.text
        con = sql.connect(host='localhost', user='root', password='', database='kivo')
        cur = con.cursor()
        query = 'insert into users(username, work, phone, country, gender) value(%s, %s, %s, %s, %s)'
        val = (un, wk, ph, co, ge)
        cur.execute(query, val)
        con.commit()
        con.close()

if __name__ == '__main__':
    Emp().run()