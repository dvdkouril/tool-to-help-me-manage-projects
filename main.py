import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from project import Project

class ProjectsManager:
    def __init__(self):
        self.activeProjects = []
        self.waitingProjects = []
        self.finishedProjects = []

    def addProject(self, project, active=True):
        if (active):
            self.activeProjects.append(project)
        else:
            self.waitingProjects.append(project)

    def listProjects(self, onlyActive=True):
        for project in self.activeProjects:
            print(project.name)

        if (not onlyActive):
            for project in self.waitingProjects:
                print(project.name)

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #ui
        self.statusBar().showMessage('Ready')
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.listLabel = QLabel(self)
        self.listLabel.setText("label")
        self.projectsList = QListView(self)
        self.projectsManager = ProjectsManager()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("tool to help me manage projects")
    mainWindow.resize(400, 600)
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
