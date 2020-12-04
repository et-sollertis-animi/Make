import sys
import os

ARGUMENTS = sys.argv
PROJECTDIRECTORY = r"C:\Users\rngup\OneDrive\Documents\Programming"
del ARGUMENTS[0]

def createFile(filename):
    with open(filename, "a+") as file:
        pass

try:
    if len(ARGUMENTS) == 2:
        projectName = ARGUMENTS[0]
        projectType = ARGUMENTS[1]
        init = input(f"Initializing project with name: {projectName} and type: {projectType} (Press any key to continue...) ")
        projectPath = os.path.join(PROJECTDIRECTORY, projectName)
        try:
            os.mkdir(projectPath)
        except FileExistsError:
            print(f"Project already initialized at {projectPath}")
            sys.exit(1)
        print(f"Created empty project at {projectPath}")
        createFile(os.path.join(projectPath, "README.md"))
        projectMain = projectName + f".{projectType}"
        createFile(os.path.join(projectPath, projectMain))
        os.chdir(projectPath)
        os.system(f"git init")
        with open(os.path.join(projectPath, "README.md"), "w") as readme:
            default = f"""# {projectName}
### Credits
Project initialized by Make. For more information, please visit https://github.com/et-sollertis-animi/Make"""
            readme.write(default)
        os.system("code .")
        print(f"""----- Created files -----
    - README.md
    - {projectMain}
----- Other Actions -----
    - Added default text to README.md
    - Initialized Git""")
        print("Thank you for using Make")
    else:
        print("Please enter your request in the format: 'make <project name> <project type>'")
        sys.exit(1)
except KeyboardInterrupt:
    print("\nReturning to the terminal...")
    sys.exit(1)