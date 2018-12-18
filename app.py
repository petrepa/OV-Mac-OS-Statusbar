import rumps
import datetime
from door import door_status

class OV_StatusBarApp(rumps.App):
    def __init__(self):
        super(OV_StatusBarApp, self).__init__("OV Door Status")
        self.icon = 'images/help-circle-outline.png'
        self.menu.add(rumps.MenuItem(title='Status'))
        self.menu.add(rumps.separator)
        

    @rumps.timer(60*60)
    def _get_door_status(self, sender):
        if door_status() == True:
            self.menu['Status'].title = "OV er ope"
            self.icon = 'images/door-open.png'
        else:
            self.menu['Status'].title = "OV er stengt"
            self.icon = 'images/door-closed.png'
    
if __name__ == "__main__":
    OV_StatusBarApp().run()