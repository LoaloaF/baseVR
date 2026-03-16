import platform
import os
import sys

def device_paths(raise_if_nas_missing=True):
    which_os = platform.system()
    user = os.getlogin()
    # print(f"OS: {which_os}, User: {user}")

    nas_dir, local_data_dir, project_dir = None, None, None
    if which_os == 'Linux' and user == 'houmanjava':
        nas_dir = "/mnt/SpatialSequenceLearning/"
        local_data_dir = "/home/houmanjava/local_data/"
        project_dir = "/home/houmanjava/VirtualReality"
    
    elif which_os == 'Linux' and user == 'vrmaster':
        nas_dir = "/mnt/SpatialSequenceLearning/"
        local_data_dir = "/home/vrmaster/local_data/"
        project_dir = "/home/vrmaster/Projects/VirtualReality/"
    
    elif which_os == 'Linux' and user == 'simon':
        nas_dir = "/BMI/VirtualReality/SpatialSequenceLearning/"
        local_data_dir = "/home/simon/local_data/"
        project_dir = "/home/simon/VirtualReality/"

    elif which_os == 'Linux' and user == 'samed':
        nas_dir = "/BMI/VirtualReality/SpatialSequenceLearning/"
        local_data_dir = "/home/samed/local_data/"
        project_dir = "/home/samed/VirtualReality/"

    
    elif which_os == "Darwin" and user == "root":
        nas_dir = "/Volumes/large/BMI/VirtualReality/SpatialSequenceLearning/"
        folders = [f for f in os.listdir("/Users") if os.path.isdir(os.path.join("/Users", f))]

        if "loaloa" in folders:
            local_data_dir = "/Users/loaloa/local_data/analysisVR_cache"
            project_dir = "/Users/loaloa/homedataAir/phd/ratvr/VirtualReality/"
        elif "yaohaotian" in folders:
            local_data_dir = "/Users/yaohaotian/Downloads/Study/BME/Research/MasterThesis/code/data/analysisVR_cache"
            project_dir = "/Users/yaohaotian/Downloads/Study/BME/Research/MasterThesis/code/"
        else:
            raise ValueError("Unknown MacOS user. Edit base_functionality.py in "
                             "baseVR repo to add user-specific paths.")
    
    else:
        raise ValueError("Unknown user. Edit base_functionality.py in "
                         "baseVR repo to add user-specific paths.")
    
    if not os.path.exists(nas_dir) or os.listdir(nas_dir) == []:
        msg = f"NAS directory not found: {nas_dir} - VPN connected?"
        print(msg)
        if raise_if_nas_missing:
            raise FileNotFoundError(msg)
    return nas_dir, local_data_dir, project_dir

def init_import_paths():
    _, _, project_dir = device_paths()
    paths = (project_dir,
             os.path.join(project_dir, 'ephysVR'),
             os.path.join(project_dir, 'baseVR'),
             os.path.join(project_dir, 'analysisVR'))
    
    for p in paths:
        if not os.path.exists(p):
            print(f"Warning: missing repository: {os.path.basename(p)}. Add to project root dir.")
        if p not in sys.path:
            sys.path.append(p)
            
