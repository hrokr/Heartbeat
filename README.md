# Heartbeat
## Alex Rook

## Background and Motivation

Former paramedic and this seemed likes something that hadn't been done before.



... well, yes and no


... but mostly no.

## Better answer the why



## A Bit on How the Hearts Works

EKG https://www.sciencedirect.com/topics/medicine-and-dentistry/phonocardiography
PCG
PPG ppg.png (source: paulvangent.com)

Four locations are most often used to listen to the heart sounds, which are named according to the positions where the valves can be best heard:

    Aortic area - centered at the second right intercostal space.
    Pulmonic area - in the second intercostal space along the left sternal border.
    Tricuspid area - in the fourth intercostal space along the left sternal edge.
    Mitral area - at the cardiac apex, in the fifth intercostal space on the midclavicular line.






## Prior Work
Artificial neural networks (ANNs) have been the most widely used machine learning-based approach for heart sound classification. Typical relevant studies grouped by the signal features as the input to the ANN classifier include: using wavelet features [12], time, frequency and complexity-based features [13], and time-frequency features [14]. A number of researchers have also applied support vector machines (SVM) for heart sound classification in recent years. The studies can also be divided according to the feature extraction methods, including wavelet [15], time, frequency and time-frequency feature-based classifiers [16]. Hidden Markov models (HMM) have also been employed for pathology classification in PCG recordings [17,18]. Clustering-based classifiers, typically the k-nearest neighbors (kNN) algorithm [19,20], have also been employed to classify pathology in PGCs. In addition, many other techniques have been applied, including threshold-based methods, decision trees [21], discriminant function analysis [22,23] and logistic regression.














Heart sound recordings were sourced from several contributors around the world, collected at either a clinical or nonclinical environment, from both healthy subjects and pathological patients. The Challenge training set consists of five databases (A through E) containing a total of 3,126 heart sound recordings, lasting from 5 seconds to just over 120 seconds. You can browse these files, or download the entire training set as a zip archive (169 MB).

In each of the databases, each record begins with the same letter followed by a sequential, but random number. Files from the same patient are unlikely to be numerically adjacent. The training and test sets have each been divided so that they are two sets of mutually exclusive populations (i.e., no recordings from the same subject/patient were are in both training and test sets). Moreover, there are two data sets that have been placed exclusively in either the training or test databases (to ensure there are ‘novel’ recording types and to reduce overfitting on the recording methods). Both the training set and the test set may be enriched after the close of the unofficial phase. The test set is unavailable to the public and will remain private for the purpose of scoring.

The heart sound recordings were collected from different locations on the body. The typical four locations are aortic area, pulmonic area, tricuspid area and mitral area, but could be one of nine different locations. In both training and test sets, heart sound recordings were divided into two types: normal and abnormal heart sound recordings. The normal recordings were from healthy subjects and the abnormal ones were from patients with a confirmed cardiac diagnosis.


Heart valve defects include mitral valve prolapse, mitral regurgitation, aortic stenosis and valvular surgery. All the recordings from the patients were generally labeled as abnormal. We do not provide more specific classification for these abnormal recordings. 

Four locations are most often used to listen to the heart sounds, which are named according to the positions where the valves can be best heard:

    Aortic area - centered at the second right intercostal space.
    Pulmonic area - in the second intercostal space along the left sternal border.
    Tricuspid area - in the fourth intercostal space along the left sternal edge.
    Mitral area - at the cardiac apex, in the fifth intercostal space on the midclavicular line.


## Resources
http://www.paulvangent.com -- work was with a PPG but well written and interesting