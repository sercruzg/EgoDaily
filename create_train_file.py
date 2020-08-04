import mmcv
import numpy as np

name_dataset = 'EgoDaily'

f = open('train' + name_dataset + '.txt', "r")

n = int(f.readline())
annotations = []
for _ in range(n):
    path = f.readline()[:-1]
    line = f.readline().split()
    width = int(line[0])
    height = int(line[1])

    anno = int(f.readline())
    bboxes = []
    labels = []
    for __ in range(anno):
        line = f.readline().split()
        bboxes.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
        labels.append(int(line[4]))

    bboxes_ignore = []
    labels_ignore = []

    bboxes = np.array(bboxes)
    labels = np.array(labels)

#    print(bboxes)
    bboxes_ignore = np.zeros((0, 4))
    labels_ignore = np.zeros((0, ))

    #print('{} {}'.format(width, height))

    annotation = {
        'filename': path,
        'width': width,
        'height': height,
        'ann': {
            'bboxes': bboxes.astype(np.float32),
            'labels': labels.astype(np.int64),
            'bboxes_ignore': bboxes_ignore.astype(np.float32),
            'labels_ignore': labels_ignore.astype(np.int64)
        }
    }
    annotations.append(annotation)
f.close()
mmcv.dump(annotations, 'train' + name_dataset + '.pkl')

