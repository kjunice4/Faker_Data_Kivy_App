from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

import pandas as pd
from faker import Faker
import random

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Data_Science"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Data_Science"
                root.manager.transition.direction = "left"        

        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Data Science"
            on_release:
                app.root.current = "Data_Science"
                root.manager.transition.direction = "left" 
                          
        
""")

# Menu
Builder.load_string("""
<Data_Science>
    id:Data_Science
    name:"Data_Science"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Data Science Menu"
            
            Button:
                text: "Generate New Fake Data"   
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "DisplayData"
                    root.manager.transition.direction = "left" 
                    
""")

#Updates
Builder.load_string("""
<details>
    id:details
    name:"details"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Data Science App Details"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Data_Science"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "All data shown is randomly generated and fake"
                
            
                
""")

#EXPONENTS STEPS
Builder.load_string("""
<DisplayData>
    id:DisplayData
    name:"DisplayData"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Data Science Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Data_Science"
                        root.manager.transition.direction = "right" 
            
            Button:
                text: "Generate New Fake Data"   
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                background_color: 0, 1 , 0 , 1
                on_release:
                    DisplayData.display()
            
            GridLayout:
                id: display
                cols: 4
                size_hint: 1, None
                height: self.minimum_height   

""")

class DisplayData(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(DisplayData, self).__init__(**kwargs)
            
    def display(self):
        print()
        
        try:
            fake = Faker("en_GB")

            # how many customers to fake
            N = 10

            # get first names, last names and postcodes
            first_name = [fake.first_name() for i in range(N)]
            last_name = [fake.last_name() for i in range(N)]
            sales_teams = ["Sales Team A","Sales Team B","Sales Team C"]
            team = [random.choice(sales_teams) for i in range(N)]
            sales = [ "$" + str('{:2,.2f}'.format(random.choice(range(1000,1000000)))) for i in range(N)]

            df_fake = pd.DataFrame({
                "first_name": first_name,
                "last_name": last_name,
                "team": team,
                "Sales": sales,
                })
            
            print(df_fake)
            
            
            self.ids.display.add_widget(Label(text= "" ,font_size = '15sp',size_hint_x = 0.2, size_hint_y= None, height=100))
            self.ids.display.add_widget(Label(text= "Sales person" ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.display.add_widget(Label(text= "Team" ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.display.add_widget(Label(text= "Monthly Sales" ,font_size = '15sp', size_hint_y= None, height=100))
            
            i = 0 
            while i < N:
                print("while loop starting")
                num_cell = Label(text= str(i+1),font_size = '15sp',size_hint_x = 0.2, size_hint_y= None, height=50)
                name_cell = Label(text= first_name[i] + " " + last_name[i],font_size = '15sp', size_hint_y= None, height=50)
                team_cell = Label(text= team[i],font_size = '15sp', size_hint_y= None, height=50)
                sales_cell = Label(text= sales[i],font_size = '15sp', size_hint_y= None, height=50)
                print("while loop, variables set")
                self.ids.display.add_widget(num_cell)
                self.ids.display.add_widget(name_cell)
                self.ids.display.add_widget(team_cell)
                self.ids.display.add_widget(sales_cell)
                print("while loop compelted, looping")
                i = i + 1
            
        except Exception:
            self.ids.display.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))
                
class Homepage(Screen):
    pass            

class Data_Science(Screen):
    pass

class details(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Data_Science(name="Data_Science"))     
sm.add_widget(DisplayData(name="DisplayData"))     
sm.add_widget(details(name="details"))
sm.current = "DisplayData"   

class DataScienceApp(App):
    def __init__(self, **kwargs):
        super(DataScienceApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    DataScienceApp().run()
    
