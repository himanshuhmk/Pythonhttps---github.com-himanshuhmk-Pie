
import kivy
from kivy.app import App
from kivy.uix.label import Label



class Ignition(App):
   
    def build(self):
      return Label(text="Bhalu")
        
      
if __name__=="__main__":
    Ignition().run()
