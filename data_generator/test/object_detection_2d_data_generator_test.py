import unittest, os, shutil
from data_generator.object_detection_2d_data_generator import DataGenerator

class ObjectDetection2dDataGeneratorTest(unittest.TestCase):
    

    def setUp(self):
        return None


    def test_stats(self):
        subject = DataGenerator(
            filenames=[ 'f1', 'f2', 'f3' ],
            image_ids=[ 1, 2, 3 ],
            labels=[
                [[ 11,0,0,100,100 ], [11,0,0,100,100], [12,0,0,100,100]],
                [[ 11,0,0,100,100 ], [11,0,0,100,100], [12,0,0,100,100]],
                [[ 11,0,0,100,100 ], [11,0,0,100,100], [12,0,0,100,100]]
            ],
        )

        self.assertEqual(subject.stats(), {
            11: {
                'images': 3,
                'objects': 6
            },
            12: {
                'images': 3,
                'objects': 3
            }
        })
