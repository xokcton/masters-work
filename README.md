<h1 align="center">MASTER'S QUALIFICATION WORK</h1>

<b>Topic</b>: Localization of the Image Objects Based on the Python Programming Language

## Prerequisites:

Make sure you have [git](https://git-scm.com/downloads), [python 3](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/#files) installed on your machine.

## To run the project follow this steps:

1. `git clone https://github.com/xokcton/masters-work.git`
1. `cd ./masters-work`
1. Windows: `python -m venv venv` | Linux: `python3 -m venv venv`
1. Windows: `venv\Scripts\activate` | Linux: `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `mkdir model/weights` in the root folder
1. Download the pre-trained yolov3.weights [file](https://pjreddie.com/media/files/yolov3.weights) or any other from the official [site](https://pjreddie.com/darknet/yolo/) to the "model/weights" folder
1. `mkdir images` in the root folder and fill it up
1. Windows: `python main.py` | Linux: `python3 main.py`

## To try Yolov8 by ultralitics:

Follow the link to [google colab](https://colab.research.google.com/drive/1k4784TtkH11k4w6mgKh_YKSrldYUE7HY?usp=sharing), create a folder `images` in the root directory and fill it with content. Next, run the script. The desired result will be waiting for you in the `output` folder.
