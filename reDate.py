from datetime import datetime
import piexif
import os
# Example of whatsapp image
# filename = 'C:\\Users\\yf\\Desktop\\IMG-20210125-WA0079.jpg'


def reDate(img_location):
    dict = img_location.split("-")[1]
    year = int(dict[0:4])
    month = int(dict[4:6])
    day = int(dict[6:8])

    print(year, "-", month, "-", day)
    exif_dict = piexif.load(img_location)
    new_date = datetime(int(year), int(month), int(day), 0,
                        0, 0).strftime("%Y:%m:%d %H:%M:%S")
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, img_location)


myFolder = "C:\\Users\\yf\\Desktop\\do"
fileSet = []

for root, dirs, files in os.walk(myFolder):
    for fileName in files:
        fileSet.append(os.path.join(root, fileName))

for file in fileSet:
    if (file.find(".png") != -1):
        reDate(file)
