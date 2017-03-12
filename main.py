import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
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
        addAction = QAction("&Add", self)
        addAction.setShortcut('Cmd+N')
        addAction.setStatusTip('Add New Project')
        addAction.triggered.connect(self.showAddDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(addAction)

        # instantiate project manager
        self.projectsManager = ProjectsManager()
        self.projectsManager.addProject(Project("Project name 0"))
        self.projectsManager.addProject(Project("Project name 1"))
        self.projectsManager.addProject(Project("Project name 2"))
        self.projectsManager.addProject(Project("Project name 3"))

        layout = QVBoxLayout()
        layout.setSpacing(1)

        scrollArea = QScrollArea(self)
        central = QWidget()
        scrollArea.setWidget(central)
        scrollArea.setLayout(layout)

        i = 0
        for p in self.projectsManager.activeProjects:
            button = QPushButton(p.name)
            button.setStyleSheet("background: white; padding: 10px; text-align: left;")
            layout.addWidget(button)
            i += 1

        self.setCentralWidget(scrollArea)

    def showAddDialog(self):
        #uic.loadUi('add-new-project.ui', self)
        addDialog = AddProjectDialog(self)

class AddProjectDialog(QDialog):
    def __init__(self, parent=None):
        super(AddProjectDialog, self).__init__(parent)
        print("add project clicked")
        uic.loadUi('add-new-project.ui', self)
        self.show()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("tool to help me manage projects")
    mainWindow.resize(400, 600)
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
