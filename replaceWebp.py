import os
from pathlib import Path
import matplotlib.pyplot as plt

def replaceWebp(dir_path: str, output_format: str):
    
    """
    Find and replace .webp format images with desired image format.
    
    """
    
    
    def runConvert(filepath: str):
        
        print(filepath)
        #Check if .webp file
        if os.path.basename(filepath).split('.')[-1] != 'webp':
            return
        
        img = plt.imread(filepath)
        
        if img.shape is None:
            return
        
        savepath = os.path.dirname(filepath) + '/' + Path(filepath).stem + output_format
        
        plt.imsave(savepath, img)
        
        if os.path.exists(savepath) == True:
            os.remove(filepath)

        return

    
    for root, dirs, files in os.walk(dir_path, topdown=True):
        for name in files:
            filepath = os.path.join(root, name)
            print(filepath)
            runConvert(filepath)

        for name in dirs:
            filepath = os.path.join(root, name)
            print(filepath)
            runConvert(filepath)
            
    return
    
