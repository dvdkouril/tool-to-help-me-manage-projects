class Project:
    def __init__(self, name="Default Name", description="Default Project Description",
        tags=[], workingDirectory=""):
        self.projectId = 0 #TODO: make new ID for each project
        self.name = name
        self.description = description
        self.tags = tags
        self.workingDirectory = workingDirectory
        self.startTime = None
        self.endTime = None

    def rename(self, newName):
        self.name = newName

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getTags(self):
        return self.tags

#project = Project("Master thesis")
#print(project.name)
