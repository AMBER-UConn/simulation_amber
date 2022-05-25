import os, sys

def main():
    args = sys.argv

    if len(args) != 3: #args should only have 3 arguments: file name, input xacro path, output urdf path
        raise Exception("Expected 2 arguments, got {}".format(len(args) - 1))
    
    xacro(args[1], args[2])



def xacro(xac_path: str, urdf_path: str = os.getcwd() + r"/file.urdf"):
    os.system("xacro {} > {}".format(xac_path, urdf_path))



if __name__ == "__main__":
    main()
