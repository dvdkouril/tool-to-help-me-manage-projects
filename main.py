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

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)


        self.activeProjectsLabel = QLabel(self)
        self.activeProjectsLabel.setText("ACTIVE PROJECTS")

        # instantiate project manager
        self.projectsManager = ProjectsManager()
        self.projectsManager.addProject(Project("Project name 0"))
        self.projectsManager.addProject(Project("Project name 1"))
        self.projectsManager.addProject(Project("Project name 2"))
        self.projectsManager.addProject(Project("Project name 3"))

        layout = QVBoxLayout()
        layout.addWidget(self.activeProjectsLabel)

        i = 0
        for p in self.projectsManager.activeProjects:
            button = QPushButton(p.name, self)
            button.move(0, 100 * i)
            button.setStyleSheet("background: white")
            layout.addWidget(button)
            i += 1

        window = QWidget(self)
        window.setLayout(layout)

        self.setCentralWidget(window)

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("tool to help me manage projects")
    mainWindow.resize(400, 600)
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
