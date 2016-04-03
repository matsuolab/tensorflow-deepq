import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView

class Browser(QWebView):
    def __init__(self):
        QWebView.__init__(self)
    
    def keyPressEvent(self, e):
        print("hello")
        self.update()
        
    def update(self, svg=''):
        self.setHtml(svg)

def start_ui():
    app = QApplication(sys.argv)
    view = Browser()
    view.show()
    app.exec_()

if __name__ == '__main__':
    start_ui()
