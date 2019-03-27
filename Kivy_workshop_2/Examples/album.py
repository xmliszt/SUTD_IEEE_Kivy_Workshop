from kivy.app import App
from kivy.uix.gridlayout import GridLayout # put the parent object you want your window to inherit when the app starts here


class mainWindow(GridLayout):  # create your window object which initialise with the object you imported from kivy library
    pass # don't do anything here, all the structures are defined in .kv file



# create your Application object which inherits the App feature in kivy library
class albumApp(App):  # the cla
    # ss name "<kivy_file_name>App" must be kivy file name

    # construct your build function which will build your window for later to run
    def build(self):
        return mainWindow()


if __name__ == "__main__":
    display = albumApp() # instantiate builder object, which is your built app
    display.run() # run the application
