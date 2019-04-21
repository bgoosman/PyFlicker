from App import App

class AppContainer:
    def __init__(self, app):
        self.app = app

    def start(self):
        while True:
            self.app.update()

    def cleanup(self):
        self.app.cleanup()

def main():
    appContainer = AppContainer(App())
    try:
        appContainer.start()
    except (BrokenPipeError, ConnectionResetError):
        pass
    finally:
        appContainer.cleanup()

if __name__=='__main__':
    main()
