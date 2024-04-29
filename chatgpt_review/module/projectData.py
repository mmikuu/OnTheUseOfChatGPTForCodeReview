class projectData:

    def __init__(self,Allproject,FilteredProject,AllPR,FilteredPR,AllLink,FilteredLink):
        self.Allproject = Allproject
        self.FilteredProject = FilteredProject
        self.AllPR = AllPR
        self.FilteredPR = FilteredPR
        self.AllLink = AllLink
        self.FilteredLink = FilteredLink


    def printString(self):
        print(self.get_string())

    def get_string(self):
        return "AllProject:" +str(self.Allproject) +"\nFilteredProject:" +str(self.FilteredProject) + "\nAllPR:" + str(self.AllPR) + "\nFilteredPR:" + str(self.FilteredPR) + "\nAllLink:" +  str(self.AllLink) +  "\nFilteredLink" + str(self.FilteredLink)
