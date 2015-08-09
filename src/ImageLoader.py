import multiprocessing
# from collections import queue
from multiprocessing import Queue
from PIL import Image, ImageTk
import scipy.misc
import os
import time
import random
from glob import glob

def worker_main(image_paths, output_queue, image_output_size):
    print os.getpid(),"working"
    while True:
        path = random.choice(image_paths)
        image = Image.open(path)
        image.thumbnail(image_output_size, Image.ANTIALIAS);
        output_queue.put(image)

        print os.getpid(),"processed", path

class ImageLoader:

    OUTPUT_QUEUE_SIZE = 10
    WORKER_COUNT = 4

    def __init__(self, image_directory, output_size = (1920, 1080)):
        self.image_directory = image_directory
        self.output_size = output_size
        self.output_queue = Queue(self.OUTPUT_QUEUE_SIZE);


    def start(self):
        self.image_paths = self.get_image_paths(self.image_directory)
        self.pool = multiprocessing.Pool(self.WORKER_COUNT, worker_main, (self.image_paths, self.output_queue, self.output_size))

    def stop(self):
        self.pool.terminate()

    def get(self, *p, **kw):
        return self.output_queue.get(*p, **kw);

    def get_image_paths(self, image_directory):
        # [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.txt'))]
        image_paths = []
        for dirpath, dirnames, filenames in os.walk(image_directory):
            for file_name in filenames:
                if file_name.endswith(('.jpg', '.png', '.jpeg', '.gif')):
                    image_paths.append(os.path.join(dirpath, file_name))
        if not image_paths:
            print "There are no images in the source folder! Exiting"
            exit()
        return image_paths

def main():
    loader = ImageLoader("../testImages")
    loader.start()
    time.sleep(3);
    for x in range(2000):
        time.sleep(1);
        thing = loader.get(False);
        print "got a thing", thing


if __name__ == '__main__':
    main()
