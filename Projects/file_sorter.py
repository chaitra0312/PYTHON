import os
import shutil
FILE_CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}
folder_path = input("Enter the full path of the folder you want to sort:").strip()
for category in FILE_CATEGORIES:
    category_path = os.path.join(folder_path,category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path,filename)
    if os.path.isfile(file_path):
        moved =  False
        for category , extensions in FILE_CATEGORIES.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path,os.path.join(folder_path,category,filename))
                moved = True
                break
        if not moved:
            shutil.move(file_path,os.path.join(folder_path,"Others",filename))
print("File Sorted succesfully!")
